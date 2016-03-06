import time
from twilio.rest import TwilioRestClient
 
# Find these values at https://twilio.com/user/account
account_sid = "AC62628353d0183ec53beae8c4201e9818"
auth_token = "d9c0efa555367cd2f34df0afe9e3e56f"
client = TwilioRestClient(account_sid, auth_token)


import Tkinter
from Tkinter import *

top = Tk()
top.title("Healthy Hackaton")
L0 = Label(top, text="Name")
L0.pack()

E0 = Entry(top, bd =5)
E0.pack()
L1 = Label(top, text="Phone number (+44...)")
L1.pack()

E1 = Entry(top, bd =5)
E1.pack()
L2 = Label(top, text="Hours you have been up tonight")
L2.pack()
E2 = Entry(top, bd =5)
E2.pack()
L3 = Label(top, text="Age")
L3.pack()
E3 = Entry(top, bd =5)
E3.pack()


def sendIt():
  
  message = client.messages.create(to=E1.get(), 
            from_="+441406455023", body="\n Hello, " + E0.get() + "! You have been up " + E2.get() + " hours. As you are " + E3.get() + " years old, you should have consumed " + str((int(E2.get()) * int(E3.get())*6)) + " kcalories, which is " + str(((int(E2.get()) * int(E3.get())*6))/45) + " redbulls or " + str(((int(E2.get()) * int(E3.get())*6))/285) + " slices of pizza.")
  
  time.sleep(30)
  message = client.messages.create(to=E1.get(), 
            from_="+441406455023", body="Every extra slice of pizza would require you to write code for 6 more hours (you burn 46 calories per hour when you write code).")
  time.sleep(30)
  message = client.messages.create(to=E1.get(), 
            from_="+441406455023", body="Send an Sms with the text: \n 1) Health - more advice from us \n 2) Link - entertaining video about health and coding \n 3) Challenge - a little challenge for you. \n 4) Gym - best gyms in Manchester \n 5) Leave - end the conversation")
  #time.sleep(300)
  #message = client.messages.create(to=E1.get(), 
   #         from_="+441406455023", body="Based on the average that the hackaton has around 200 people aged aproximately 19-25 and most of them have been up between 7 and 10 hours, we should have around " + str(int(200 * (8 * 22 * 6))/(285 * 8)) + " pizzas here!")
  
B = Tkinter.Button(top, text ="Start", command = sendIt)
B.pack()

top.mainloop()



