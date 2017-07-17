from spy_details import spy, Spy, ChatMessage, friends ,messages                 #this statement import the spy chatmessage and friend from spy detail...
from steganography.steganography import Steganography                      #impot stegano-graphy library....
from datetime import datetime                                            #impot datetime....




STATUS_MESSAGES = ['VERY BUSY..', 'SWIMMING...', 'HEY,I M USING SPY CHAT']          #default status message.....





print "Hello! Let\'s get started"

question = "Do You Want to Continue As " + spy.salutation + " " + spy.name + " (Y/N)? : "

existing = raw_input(question)                  # take input from user for continue with default values or not...






def add_a_status():         #here ,  add_a_status is a function name...for update a status...

    print"\nSTATUS UPDATE :\n"
    updated_status_message = None

    if spy.current_status_message != None:

        print '\tYour current status message is %s \n' % (spy.current_status_message)

    else:
        print '\tYou don\'t have any status message currently... '
    question = raw_input("\tDo you want to update your message.please enter either 'Y' or 'N'.. : ")
    question=str(question)
    if question.upper() == 'Y':

        default = raw_input("\t\tDo you want to select from the older status (y/n)? : ")

        if default.upper() == 'N':
            new_status_message = raw_input("\t\t\tWhat status message do you want to set? : ")


            if len(new_status_message) > 0:
                STATUS_MESSAGES.append(new_status_message)              # this statement add the 'new_status_message' add the end of 'STATUS_MESSAGES'.....
                updated_status_message = new_status_message

        elif default.upper() == 'Y':   #

            item_position = 1

            for message in STATUS_MESSAGES:
                print '\t\t\t%d. %s' % (item_position, message)
                item_position = item_position + 1

            message_selection = int(raw_input("\t\tChoose from the above messages : "))


            if len(STATUS_MESSAGES) >= message_selection:                # if length of 'STATUS_MESSAGES' is  greater than 'message_selection' than execute otherwise not...
                updated_status_message = STATUS_MESSAGES[message_selection - 1]

        else:
            print '\t\tThe option you chose is not valid! Press either y or n.\n'

    if updated_status_message:
        print '\n\tYour updated status message is: %s\n' % (updated_status_message)
    else:
        print '\n\tYou current don\'t have a status update!!!\n'

    return updated_status_message    # this statement return the value of  updated_status_message...





def add_friend():             # here  'add_a_friend()' is also a func. name... for add a new friend..

    print"\nADD FRIEND :"
    new_friend = Spy('','',0,0.0)

    new_friend.name = raw_input("\tPlease add your friend's name : ")
    if new_friend.name.isalpha() == True:
        new_friend.salutation = raw_input("\tAre they Mr. or Ms.? : ")
        new_friend.salutation=str( new_friend.salutation)

        new_friend.age = raw_input("\tAge? : ")
        new_friend.age = int(new_friend.age)                    #this statement convert the data to int type..

        new_friend.rating = raw_input("\tSpy rating? : ")
        new_friend.rating = float(new_friend.rating)            #this statement convert the data to float type..

        if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= 0:
            friends.append(new_friend)          #this state ment add a new friend at the end of the friends list...
            print '\n\tYour Friend is Added!\n'
        else:
            print '\n\tSorry!!! Invalid entry. We can\'t add spy with the details you provided\n'
    else:
        print"\tPlease Enter a valid Name...!!"
    return len(friends)         # this statement return the length of a friends(list)...






def select_a_friend():           # here  'select_a_friend()' is also a func. name... for select a friend..
    item_number = 0
    print"\n\tYour friend list is give as below :\n"

    for friend in friends:
        print '\t\t%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,  # this statement print all 'friends' in your 'friend list'....
                                                   friend.age,
                                                   friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input(" \n\tPlease Choose from your friends : ")

    friend_choice_position = int(friend_choice) - 1   # this statement subtract the entered choice of user by one, for index value....

    return friend_choice_position                   # this statement return the value of 'friend_choice_position' ......






def send_a_message():                  # here  'send_a_message()' is also a func. name...
    print"SEND MESSAGE :"
    friend_choice = select_a_friend()   # this state ment call the 'select_a_friend()' and returned value is assigned to   'friend_choice'....

    original_image = raw_input("\tWhat is the name of the image? : ")
    output_path = "output.jpg"
    text = raw_input("\tWhat do you want to say? : ")
    if len(text)>0:
        Steganography.encode(original_image, output_path, text) #this statement encode the 'original image' with 'text'.....

        new_chat = ChatMessage(text,True)
        friends[friend_choice].chats.append(new_chat)

        print "\n\tYour secret message image is ready..."
    else:
        print"WARNING ,you can not send image without any text!!!"





def read_a_message():                   # here, 'read_a_message()' is also a func. name...                  #

    print"\nREAD MESSAGE : "
    sender = select_a_friend()               # this state ment call the 'select_a_friend()' and returned value is assigned to   'sender'......

    output_path = raw_input("\tWhat is the name of the file?")

    secret_text = Steganography.decode(output_path)             # this statement decode the text from a image whice is send by ur friend to you.....
    for each in messages:
        if  secret_text == each:
            print "\tyour friend is in danger"
    new_chat = ChatMessage(secret_text,False)          # here, false means the message is send by your friend.....

    friends[sender].chats.append(new_chat)

    print "\tYour secret message has been saved!"







def read_a_chat_history():                  # function for read a chat history...

    print "\nREAD CHAT HISTORY : "
    read_for = select_a_friend()

    print '\n'

    for chat in friends[read_for].chats:            #here we using 'for' loop..
        if chat.sent_by_me:
            print '\t[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), '\n\t\tYou said:', chat.message)
        else:
            print '\t[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)







def start_chat(spy):        # here 'start_chat()' is a function name or 'spy' is a parameter......

    spy.name = spy.salutation + " " + spy.name


    if spy.age > 12 and spy.age < 50:                   # if spy age > 12 and spy age < 50 ,than equation under this is execute ,otherwise not...


        print "Authentication Complete. Welcome " + spy.name + " age: " + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you Onboard"

        show_menu = True

        while show_menu:
            print"\nMENU:"                   #  it is the 'menu' of spy chat
            menu_choices ="\n  What do you want to do? \n     1. Add a status update \n     2. Add a friend \n     3. Send a secret message \n     4. Read a secret message \n     5. Read Chats from a user \n     6. Close Application \n  Please enter your choice : "

            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0 and len(menu_choice)<8:        #  if len(menu_choice) > 0 and len(menu_choice)<8, tan execute other wise not.....
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = add_a_status()                 # call the 'add_a_status() ' and returend in to a  ' spy.current_status_message '..

                elif menu_choice == 2:
                    number_of_friends = add_friend()                                   # call the ' add_a_friend() '   and returend in to a 'number_of_friends'..
                    print "You have '%d' friends" % (number_of_friends)

                elif menu_choice == 3:
                    send_a_message()                                                 # call the  'send_a_message()' function...

                elif menu_choice == 4:
                    read_a_message()                                                 # call the 'read_a_message() ' function...

                elif menu_choice == 5:
                    read_a_chat_history()                                        # call the 'read_a_chat_history()' function...

                else:
                    show_menu = False

            else:
                print"Your choice don't match with 'MENU'.Please enter your correct choice!!!"
    else:
        print 'Sorry you are not of the correct age to be a spy'





if existing.upper() == "Y":
    start_chat(spy)             # call the 'start_chat()' function and pass a 'spy' as a parameter...


elif existing.upper() == "N":

    spy = Spy('','',0,0.0)
    spy.name = raw_input("'WELCOME' to Spy Chat, Please,Enter Your Spy Name : ")
    if spy.name.isalpha()== True :
        if len(spy.name) > 0:                               # if length of spy name is > 0 than statement under this 'if' staement is execute otherwise not...
            spy.salutation = raw_input("Should I Call You Mr. or Ms.? : ")

            spy.age = raw_input("What is Your Age? : ")
            spy.age = int(spy.age)             #this statement convert spy age into a integer type.....
            if spy.age > 12 and spy.age <= 50:             #if spy age > 12 and spy age < 50 ,than equation under this is execute ,otherwise not...

                spy.rating = raw_input("What is Your Spy Rating? Please rated from '0' to '5' : ")
                spy.rating = float(spy.rating)      #this statement convert spy rating into a float type......

                if spy.rating <= 5 and spy.rating >= 4:
                    print "Your spy rating is 'Excelent'."

                elif spy.rating <= 4 and spy.rating > 2.5:
                    print "Your spy rating is 'Very Good'."

                elif spy.rating <=2.5  and spy.rating > 1.5:
                    print "Your spy rating is 'Good'."

                elif spy.rating <=1.5 and spy.rating > 1:
                    print "Your spy rating is 'Fair'."

                elif spy.rating <= 1 and spy.rating >= .5:
                    print "Your spy rating is 'Poor'."

                elif spy.rating < .5 and spy.rating >= 0:
                    print "Your spy rating is 'Poor'."


                start_chat(spy)                    #this statement call the 'start_chat()' function and pass 'spy' as a parameter.....

            else:
                print"minimum age must be '18' for uses this App !  "

        else:
            print "Please Add a Valid Spy-Name !"

    else:
        print"Please enter valid name !"
else:
      print "Please enter a correcnt choice either 'Y' or 'N'!!!"














