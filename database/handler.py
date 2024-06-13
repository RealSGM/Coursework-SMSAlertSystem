import sqlite3

## Number Functions
def fetch_numbers():
    connection = sqlite3.connect("database/database.db")
    db = connection.cursor()
    db.execute("SELECT * FROM OptedNumbers")
    rows = db.fetchall()
    connection.close()
    return rows
    
def add_number(number, language):
    connection = sqlite3.connect("database/database.db")
    db = connection.cursor()
    db.execute(f"INSERT INTO OptedNumbers VALUES ('{number}', '{language}')")
    connection.commit()
    connection.close()

def clear_numbers():
    connection = sqlite3.connect("database/database.db")
    db = connection.cursor()
    db.execute("DELETE FROM OptedNumbers")
    connection.commit()
    connection.close()
    

## Email Functions
def add_email(email, language):
    connection = sqlite3.connect("database/database.db")
    db = connection.cursor()
    db.execute(f"INSERT INTO OptedEmails VALUES ('{email}', '{language}')")
    connection.commit()
    connection.close()

def fetch_emails():
    ## Fetch email and language
    connection = sqlite3.connect("database/database.db")
    db = connection.cursor()
    db.execute("SELECT * FROM OptedEmails")
    rows = db.fetchall()
    connection.close()
    return rows

def clear_emails():
    connection = sqlite3.connect("database/database.db")
    db = connection.cursor()
    db.execute("DELETE FROM OptedEmails")
    connection.commit()
    connection.close()

def delete_email(email):
    connection = sqlite3.connect("database/database.db")
    db = connection.cursor()
    db.execute(f"DELETE FROM OptedEmails WHERE Email='{email}'")
    connection.commit()
    connection.close()

def delete_number(number):
    connection = sqlite3.connect("database/database.db")
    db = connection.cursor()
    db.execute(f"DELETE FROM OptedNumbers WHERE PhoneNumber='{number}'")
    connection.commit()
    connection.close()

def delete_email(email):
    connection = sqlite3.connect("database/database.db")
    db = connection.cursor()
    db.execute(f"DELETE FROM OptedEmails WHERE Email='{email}'")
    connection.commit()
    connection.close()