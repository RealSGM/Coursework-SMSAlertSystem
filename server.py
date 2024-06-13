## Imports
import socket, threading, json, time
from api import emailer, translater, weather, whatsapp
from database import handler as db

## Global Variables
weather_data = []
clients = []

# Commands that can be called by the client
def get_weather(params):
    if weather_data == []: ## Ensure that weather data is available
        return json.dumps({"success": False})
    weather_data[-1]["success"] = True
    return json.dumps(weather_data[-1])

def send_message(params):
    formatted_message = params.replace('~~~','\n')
    
    for row in db.fetch_emails():
        translated_message =  translater.translate(row[1], formatted_message) ## Translate message to user's language
        emailer.send_email(row[0], "Weather Alert", translated_message)
        
    if not whatsapp.connected(): ## Check if whatsapp is connected
        print("- WhatsApp not yet connected!")
    else:
        for row in db.fetch_numbers():
            if not whatsapp.send(row[0], formatted_message, row[1]): 
                print(f"- Failed to send message to {row[0]}")

    return f'+ Alert Sent! "{params}"'

def ping(params):
    return "All Good!" 

# Weather API ---------------------------------------------
def run_weather_api():
    update_weather_data(False)
    while True:
        time.sleep(3600) ## Wait 1 hour
        update_weather_data()

# Fetches weather data every hour from API and stores it in weather_data
def update_weather_data(sending=True):
    latest_weather = weather.get_weather()
    weather_data.append(latest_weather)

    message = f"Location: {latest_weather['location']['country']}~~~"
    message += f"Temperature: {latest_weather['current']['temp_c']}°C~~~"
    message += f"Condition: {latest_weather['current']['condition']['text']}~~~"
    message += f"Wind Speed: {latest_weather['current']['wind_kph']} km/h~~~"
    message += f"Humidity: {latest_weather['current']['humidity']}%"
    
    if sending:
        send_message(message)

# WhatsApp API --------------------------------------------
# Checks messages to see if it has recieved an OPTIN
def check_messages():
    while True:
        for msg in whatsapp.get_messages():
            if "OPTIN" in msg: # Text message saying 'OPTIN 07********9'
                user = msg.split(" ")[1]
                if "@" in user:
                    if user not in [email[0] for email in db.fetch_emails()]:
                        add_email(user)
                else:
                    if user not in [num[0] for num in db.fetch_numbers()]:
                        add_number(user)

            elif "OPTOUT" in msg: # Text message saying 'OPTOUT 07********9'
                user = msg.split(" ")[1]
                if "@" in user:
                    if user in [email[0] for email in db.fetch_emails()]:
                        remove_email(user)
                else:
                    if user in [num[0] for num in db.fetch_numbers()]:
                        remove_number(user)
        time.sleep(3)

# Database ------------------------------------------------
def add_number(number, language="km"):
    print(f"+ Added {number} to database")
    en_msg = "Welcome to the Weather Alert System! You will now receive weather updates every hour and alerts for certain weather conditions."
    translated_msg = translater.translate(language, en_msg)
    db.add_number(number, language)
    whatsapp.send(number, translated_msg)
    
def add_email(email, language="km"):
    print(f"+ Added {email} to database")
    db.add_email(email, language)
    en_msg = "Welcome to the Weather Alert System! You will now receive weather updates every hour and alerts for certain weather conditions."
    translated_msg = translater.translate(language, en_msg)
    emailer.send_email(email, "Welcome!", translated_msg)

def remove_number(number):
    print(f"- Removed {number} from database")
    db.delete_number(number)
    whatsapp.send(number, "Goodbye!")

def remove_email(email):
    print(f"- Removed {email} from database")
    db.delete_email(email)
    emailer.send_email(email, "Removed from System!", "Goodbye!")

# Server --------------------------------------------------
# Receives command and runs function. Each client_handler has its own thread
def client_handler(con, addr):
    commands = ["get_weather", "send_message","ping"]
    try:
        while True:
            data = con.recv(1024).decode()
            data_arr = data.split(" ", 1)
            if len(data_arr) == 2:
                command, params = data_arr
                if command in commands:
                    response = eval(f"{command}('{params}')")
                    con.sendall(response.encode())
            else:
                con.sendall("Invalid Command".encode())
                
    except ConnectionResetError:
        clients.remove(addr)
        print(f"- Connection with {addr} closed.")
    finally:
        con.close()

# Terminal Commands
def terminal():
    # print("> Type `help` for commands -----------------")
    while True:
        command = input()
        if command =="list":
            print("\nPhone Numbers\n----------")
            for num in db.fetch_numbers(): print(num[0])
                
            print("----------\nEmails\n----------")
            for email in db.fetch_emails(): print(email[0])

        elif command == "clients":
            print("----------\nClients\n----------")
            [print(client) for client in clients]

        elif command == "clear numbers":
            db.clear_numbers()
            print("Numbers Cleared!")
            
        elif command == "clear emails":
            db.clear_emails()
            print("Emails Cleared!")

        elif "add" in command: #add 07********1
            param = command.split(" ")[1]
            if "@" in param:
                db.add_email(param, "km")
                print(f"+ Added {param} to database")
            else:
                db.add_number(param, "km")
                print(f"+ Added {param} to database")
        
        elif "delete" in command:
            param = command.split(" ")[1]
            if "@" in param:
                db.delete_email(param)
                print(f"Deleted {param} from the database")
            else:
                db.delete_number(param)
                print(f"Deleted {param} from the database")
        
        elif command == "force weather":
            update_weather_data()
            print("Sent weather update!")

        elif command == "help":
            print("----------\nCommands\n----------")
            print("list - lists phone numbers & emails")
            print("clients - lists connected clients")
            print("clear numbers - clears numbers db")
            print("clear emails - clears emails db")
            print("add *number* or *email* - adds given number/email to db")
            print("delete *number* or *email* - deletes given number/email from db")
            print("force weather - Force sends out weather update")

def run_server(host='127.0.0.1', port=12345):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    
    threading.Thread(target=run_weather_api).start()
    threading.Thread(target=check_messages).start()
    threading.Thread(target=terminal).start()
    
    while True:
        conn, addr = server.accept()
        clients.append(addr)
        print("+ New client connected!")
        threading.Thread(target=client_handler, args=(conn, addr)).start()

if __name__ == "__main__":
    run_server()