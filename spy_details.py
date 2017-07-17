from datetime import datetime               # this statement impot the date time  library

class Spy:                                      # here,spy is a class name

    def __init__(self, name, salutation, age, rating):          # here 'self' is also a another variable like others ,it is used for accessing the values from class variables...
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None




class ChatMessage:                            # here 'ChatMessage' is also a class name.....

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me




spy = Spy('shivansh', 'Mr.', 42, 3.7)           #default values....



#default friends info.....
f1 = Spy('arnav', 'Mr.',  40,2)            # friend one info.....
f2 = Spy('parry', 'Ms.',  25,2.5)               # friend two info.....
f3 = Spy('mridul', 'Dr.', 35,4.2)              # friend three info.....




friends = [f1, f2, f3]            # list of friends....
messages=['help me','save me','sos','help']
