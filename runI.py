from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])



def hello_monkey():
    """Respond to incoming calls with a simple text message."""
    variable = True
    resp = twilio.twiml.Response()
    if request.values.get('Body') == "Health":
      resp.message("You have chosen to get more info about a healthier life during hackatons. What we recomend: \n 1) Stand straight on your chair. \n 2) Make sure you move from time to time \n 3) Eat a fruit once in a while \n 4) Drink water regularly \n 5) Enjoy the Hackaton- laughing burns 40 calories per 10 minutes. \n --Go back to the Menu by writing Menu or Quit by writing Leave")
    elif request.values.get('Body') == "Link":
      resp.message("https://www.youtube.com/watch?v=fviFNrWKzZ8 \n --Go back to the Menu by writing Menu or Quit by writing Leave")
    elif request.values.get('Body') == "Challenge":
      resp.message("How many calories do you think a snickers has? \n 1) 300 \n 2) 488 \n 3) 255 \n Answer with 1, 2 or 3")
    elif request.values.get('Body') == "2":
      resp.message("Correct! A snickers has 488 calories! Want more? --Go back to the Menu by writing Menu or Quit by writing Leave")
    elif request.values.get('Body') == "1":
      resp.message("Wrong! Keep trying by entering 2 or 3. --Go back to the Menu by writing Menu or Quit by writing Leave")
    elif request.values.get('Body') == "3":
      resp.message("Wrong! Keep trying by entering 1 or 2 --Go back to the Menu by writing Menu or Quit by writing Leave")
    elif request.values.get('Body') == "Menu":
      resp.message("Send an Sms with the text: \n 1) Health - more advice from us \n 2) Link - entertaining video about health and coding \n 3) Challenge - a little challenge for you. \n 4) Gym - best gyms in Manchester \n 5) Leave - end the conversation")
    elif request.values.get('Body') == "Gym":
      resp.message("http://www.manchesterconfidential.co.uk/health-and-beauty/fitness/cheapest-and-dearest-gyms-in-manchester \n --Go back to the Menu by writing Menu or Quit by writing Quit.")
    else:
      resp.message("Key not recognised! Go back to the menu by writing Menu or Quit by writing Leave")

  
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
