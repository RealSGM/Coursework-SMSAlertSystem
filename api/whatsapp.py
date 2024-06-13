from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import re
import uuid
import api.translater as translater
from datetime import datetime
eventloop = []

#opens chrome on whatsapp
#------------
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
#------------

def connected():
    try:
        check = driver.execute_script('document.querySelector(\'[class="landing-title _aj-8"]\').innerHTML')
        return False
    except:
        return True
    
def checkSent(time): #time written as 00:00
    try:
        check = driver.execute_script('for(i=0;i<spans.length;i++){if(spans[i].innerHTML=="'+time+'"){console.log(spans[i])}}')
        return True
    except:
        return False

# a coroutine that continues the caller function when it is the next in the event loop
# Once the function is complete it can call the coroutine again to remove it from the loop
# allowing the next event to run
# ------------
def queueEvent():
    id = uuid.uuid4()
    global eventloop
    eventloop.append(id)
    while eventloop[0] != id: pass #wait while not the next in the loop
    yield #let the function run until called again
    eventloop.remove(id) #the coroutine is called again when the function is done, so we can remove it from the event loop
    yield #done
# ------------

def send(number, msg, language="en"):
    #print("Sending message to", number)
    ticket = queueEvent() # get a ticket and wait in line of the event loop
    next(ticket) # wait until cotoutine passes back control

    #searches for number
    #------------
    (driver.find_element(By.CSS_SELECTOR, 'span[data-icon="new-chat-outline"]')).click()
    search = driver.find_element(By.CSS_SELECTOR, 'p[class="selectable-text copyable-text x15bjb6t x1n2onr6"]')
    search.send_keys(number[1:])
    time.sleep(0.5)
    #------------

    #If number doesn't exist
    #------------
    try:
        error = driver.execute_script('return document.querySelector(\'span[class="_ao3e"]\').innerHTML')
        
        if error == "No results found for '"+number[1:]+"'":
            next(ticket) # function finished, remove from eventloop
            return False
        else:
            raise Exception
    except:
        #select phone number and send message
        #------------
        search.send_keys(Keys.RETURN)
        time.sleep(0.5)
        message = driver.find_elements(By.CSS_SELECTOR, 'p[class="selectable-text copyable-text x15bjb6t x1n2onr6"]')
        message=message[len(message)-1]
        for line in msg.split("\n"):
            translated_line = translater.translate(language, line)
            message.send_keys(translated_line)
            message.send_keys(Keys.SHIFT, Keys.RETURN)
        message.send_keys(Keys.RETURN)
        #------------
        next(ticket)# function finished, remove from eventloop
        return True#checkSent(datetime.now().strftime("%H:%M"))
        #------------

def get_messages():
    if connected():
        ticket = queueEvent()# get a ticket and wait in line of the event loop
        next(ticket)# wait until cotoutine passes back control
        #JS code for getting all the listed messages
        #------------
        findMessages = """messages = document.querySelectorAll('._ak8k');
        found = [];
        for (const message of messages) {
            try{found.push(message.childNodes[0].childNodes[1].innerHTML);}
            catch{}
            try{found.push(message.childNodes[0].childNodes[2].innerHTML);}
            catch{}
        }
        return found;"""
        #------------

        #Run JS to fetch the messages and filter out the html garbage
        #------------
        messages = driver.execute_script(findMessages)
        messages = [message for message in messages if message != ":&nbsp;"]


        messages = [re.sub(r'<.+?>', '', message) for message in messages if message is not None] #just added if not none
        next(ticket)# function finished, remove from eventloop
        return messages
    return []
    #------------

#Usage
#Make sure you login to whatsapp before use!
#Also once logged in feel free to minimise the tab as it works in the background
#------------
#import Whatsapp
#whatsapp.send("07912286631","Hello World!")
#whatsapp.getMessages()
#------------