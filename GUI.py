def LogIn():
    name=input("Please enter your name: ")
    file = open(name.lower() + " profile.txt", "r")
#+=========GUI===========GUI============GUI===========+

    #mport modules
import Tkinter
import time

from twilio.rest import TwilioRestClient
 
# Find these values at https://twilio.com/user/account
account_sid = "AC62628353d0183ec53beae8c4201e9818"
auth_token = "d9c0efa555367cd2f34df0afe9e3e56f"
client = TwilioRestClient(account_sid, auth_token)

    #---Window---#
    #make window
window = Tkinter.Tk()
#change title
window.title("Python Games Login")
#change size
window.geometry("320x320")
    #change window icon
    #change window colour
window.configure(bg="#39d972")

    #---Commands---#
    #go
def sendIt():
  
  message = client.messages.create(to=E1.get(), 
            from_="+441406455023", body="You have been up " + E2.get() + " hours. As you are " + E3.get() + " years old, you should have consumed " + str((int(E2.get()) * int(E3.get())*16) - 300) + " kcalories, which is " + str(((int(E2.get()) * int(E3.get())*16) - 300)/45) + " redbulls or " + str(((int(E2.get()) * int(E3.get())*16) - 300)/285) + " slices of pizza.")
  time.sleep(50)
  message = client.messages.create(to=E1.get(), 
            from_="+441406455023", body="You have all the reasons to smile today!")
  time.sleep(30)
  message = client.messages.create(to=E1.get(), 
            from_="+441406455023", body="Your day was good because you made it this way! Find more motivation tomorrow, by checking our app!")

def callback():
        line = file.readlines()
        username = user.get()
        password = passw.get()
        if username == line[1].strip() and password == line[2].strip():
            message.configure(text = "Logged in.")
        else:
            message.configure(text = "Username and password don't match the account \n under the name;\n \'" + name + "\'. \nPlease try again.")
    #---Widgets---#
    #labels
title1 = Tkinter.Label(window, text="-Let's be fit in the hackaton-\n", bg="#39d972")
usertitle = Tkinter.Label(window, text="---Name---", bg="#39d972")
passtitle = Tkinter.Label(window, text="---Phone---", bg="#39d972")
agetitle = Tkinter.Label(window, text="---Age---", bg="#39d972")
hourstitle = Tkinter.Label(window, text="---Hours you have been up---", bg="#39d972")
message = Tkinter.Label(window, bg="#39d972")

    #text entry windows
E0 = Tkinter.Entry(window)
E1 = Tkinter.Entry(window)
E2 = Tkinter.Entry(window)
E3 = Tkinter.Entry(window)

    #buttons
go = Tkinter.Button(window, text="GET RESULTS!", command = send, bg="#93ff00")

    #pack widgets
title1.pack()
usertitle.pack()
E0.pack()
passtitle.pack()
E1.pack()

agetitle.pack()
E2.pack()
hourstitle.pack()
E3.pack()


go.pack()
message.pack()

    #start window
window.mainloop()
