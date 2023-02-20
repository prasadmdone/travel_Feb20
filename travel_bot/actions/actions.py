# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from tkinter import *
from tkcalendar import Calendar

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

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        data=[{"label":"option1","value":"/inform{'slot_name':'option1'}"},
        {"label":"option2","value":"/inform{'slot_name':'option2'}"},
        {"label":"option3","value":"/inform{'slot_name':'option3'}"}]
        message={"payload":"dropDown","data":data}
        dispatcher.utter_message(text="Hello World!",json_message=message)

        return []

# class ActionListGames(Action):
#     def name(self) -> Text:
#         return "action_list_games"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         response_games = requests.get("https://www.gamexn.com/api/v2/games")
#         processed_output = json.load(io.BytesIO(response_games.content))['data']['games']

#         games = [
#             {
#                 "label": row['gameName'],
#                 "value": "/game_option{\"game_name\": \"" + row['gameCode'] + "\"}"
#             } for row in processed_output
#         ]
#         message = {"payload": "dropDown", "data": games}

#         dispatcher.utter_message(text="Please select a game option:", json_message=message)
#         return []