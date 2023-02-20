from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from tkinter import *
from tkcalendar import Calendar
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet
# from rasa_sdk.forms import FormValidationAction 

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_calendar"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # creating an object of tkinter
        tkobj = Tk()
        # setting up the geomentry
        tkobj.geometry("400x400")
        tkobj.title("Calendar picker")
        #creating a calender object
        tkc = Calendar(tkobj,selectmode = "day",year=2022,month=1,date=1)
        #display on main window
        tkc.pack(pady=40)
        # getting date from the calendar 
        def fetch_date():
            date.config(text = "Selected Date is: " + tkc.get_date())
        #add button to load the date clicked on calendar
        but = Button(tkobj,text="Select Date",command=fetch_date, bg="black", fg='white')
        #displaying button on the main display
        but.pack()
        #Label for showing date on main display
        date = Label(tkobj,text="",bg='black',fg='white')
        date.pack(pady=20)
        #starting the object
        tkobj.mainloop()
        dat= tkc.get_date()
        dispatcher.utter_message("Date is:"+ dat)
        return []


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_ports"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

  
        # Create object
        root = Tk()
        
        # Adjust size
        root.geometry( "200x200" )
        
        # Change the label text
        def show():
            label.config( text = clicked.get() )
        
        # Dropdown menu options
        options = [
            "Netaji Subhash Chandra Bose International Airport, Kolkata",
            "Chennai International Airport, Chennai",
            "Thiruvananthapuram International Airport",
            "Sardar Vallabh Bhai Patel International Airport, Ahmedabad",
            "Guru Ram Dass Jee International Airport, Amritsar",
            "Lokpriya Gopinath Bordoloi International Airport, Guwahati",
            "Goa International Airport (Civil Enclave)",
            "Srinagar International Airport, Srinagar (Civil Enclave)",
            "Jaipur International Airport",
            "Kozhikode Airport, Calicut",
            "Veer Savarkar International Airport (Civil Enclave), Port Blair, A&N Islands (UT)",
            "Indira Gandhi International Airport, Delhi",
            "Chattrapati Shivaji International Airport, Mumbai",
            "GMR Hyderabad International Airport, Hyderabad",
            "Bangalore International Airport Limited, Bengaluru",
            "Cochin International Airport, Kochi (Private) ",
            "Bharat Ratna Babasaheb Dr. B.R. Ambedkar International Airport, Nagpur (Maharashtra)"
        ]
        
        # datatype of menu text
        clicked = StringVar()
        
        # initial menu text
        clicked.set( "Netaji Subhash Chandra Bose International Airport, Kolkata" )
        
        # Create Dropdown menu
        drop = OptionMenu( root , clicked , *options )
        drop.pack()
        
        # Create button, it will change label text
        button = Button( root , text = "Choose" , command = show ).pack()
        
        # Create Label
        label = Label( root , text = " " )
        label.pack()
        
        # Execute tkinter
        root.mainloop()

        dispatcher.utter_message("Done",button)
        return []

class ActionCarousel(Action):

    def name(self) -> Text:
        return "action_greetcarousel"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        message= {
            "type": "template",
            "payload":{
                "template_type":"generic",
                "elements":[
                    {
                        "title":"Hello there",
                        "image_url": "https://img.freepik.com/premium-vector/robot-icon-bot-sign-design-chatbot-symbol-concept-voice-support-service-bot-online-support-bot-vector-stock-illustration_100456-34.jpg",
                        "buttons": [
                        #     {
                        #         "title": "Buy Property",
                        #         "payload": "Buy Property",
                        #         "type": "postback"
                        # }                   
                        ]
                    }
                ]
            }
        }
        dispatcher.utter_message(attachment=message)
        return 

import sqlite3
def DataUpdate(name,bor,dest,bordate,mail,phone):
    try:
        sqliteConnection = sqlite3.connect('travel_sqlite.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO travel_tables
                          ('name','bor','dest','bordate','mail','phone') 
                          VALUES (?, ?, ?, ?, ?, ?);"""

        data_tuple = (name,bor,dest,bordate,mail,phone)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Python Variables inserted successfully into travel_tables table")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

class ActionSubmit(Action):
        def name(self) -> Text:
            return "action_add_data"
        async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            name=tracker.get_slot('name'),
            bor=tracker.get_slot('bor'),
            dest=tracker.get_slot('dest'),
            bordate=tracker.get_slot('bordate'),
            mail=tracker.get_slot('mail'),
            phone=tracker.get_slot('phone')
            DataUpdate(name,bor,dest,bordate,mail,phone)
            dispatcher.utter_message("Thanks for the valuable information.")
            return()

from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client     

### custom action for sending message through twilio
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_send"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        phone=tracker.get_slot('phone')
        account_sid = 'AC3aac0cad358f7b722f0e53f98b0a8134'
        auth_token = '4e316902f614742f5e184655137d2d75'
        client = Client(account_sid, auth_token)

###working sending otp verification
        verification = client.verify \
                     .v2 \
                     .services('VA7464e064d23ff87ada62bb0f04e5a267') \
                     .verifications \
                     .create(to=phone, channel='sms')

        print(verification.status)  
        return []


### checking otp status
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_verify"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        phone=tracker.get_slot('phone')
        codey=tracker.get_slot('code')
        account_sid = 'AC3aac0cad358f7b722f0e53f98b0a8134'
        auth_token = '4e316902f614742f5e184655137d2d75'
        client = Client(account_sid, auth_token)
        verification_check = client.verify \
                                .v2 \
                                .services('VA7464e064d23ff87ada62bb0f04e5a267') \
                                .verification_checks \
                                .create(to=phone, code=codey)
        # print(verification_check.status)
        temp=verification_check.status
        print(temp)
        if (temp== 'approved'):
                return dispatcher.utter_message(response="utter_approve")
        else:
                return dispatcher.utter_message(response="utter_changeph")  
       


class ValidateRestaurantForm(Action):
    def name(self) -> Text:
        return "travel_info"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        required_slots = ['bor','dest','bordate']

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]

        # All slots are filled.
        return [SlotSet("requested_slot", None)]

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_info",
                                 bor=tracker.get_slot("bor"),
                                 dest=tracker.get_slot("dest"),
                                 bordate=tracker.get_slot("bordate"))
