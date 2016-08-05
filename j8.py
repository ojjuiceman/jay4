import string
from itertools import chain
from random import choice, sample

from flask import Flask
from flask import request
from flask import render_template
from flask_mail import Mail
from flask_mail import Message


MAIL_SERVER='smtp.gmail.com'
MAIL_PORT=465
MAIL_USE_TLS = False
MAIL_USE_SSL= True
MAIL_USERNAME = 'name@gmail.com'
MAIL_PASSWORD = '**'



app = Flask(__name__)
mail = Mail(app)
app.config.from_object(__name__)

mail = Mail(app)

@app.route('/')
def my_form():
    return render_template("index.html")



@app.route('/', methods=['POST'])

def my_form_post():

    digits=int(request.form['digits'])
    upper=int(request.form['uppercase'])
    lower=int(request.form['lowercase'])
    spchars=int(request.form['spcars'])
    """ The 4 values above take the input from the forms on the website
        The 3 values below setup the lower case letter and upeprcase letters
    """


    lowercase = string.ascii_lowercase.translate(None, "o")
    uppercase = string.ascii_uppercase.translate(None, "O")
    letters = "{0:s}{1:s}".format(lowercase, uppercase)
    
    #This creates the password based off all of the inputs from the user
    password = list(
        chain(
            (choice(uppercase) for _ in range(upper)),
            (choice(lowercase) for _ in range(lower)),
            (choice(string.digits) for _ in range(digits)),
            (choice(string.punctuation) for _ in range(spchars)),
            (choice(letters) for _ in range((digits - upper - lower - spchars)))
        )
    )
    # creates a variable for the users email
    damail = str(request.form['email'])
    # creates a variable for the password
    dapass = "".join(sample(password, len(password)))
    # creates and sends the email to the user
    msg = Message(
       'Hello',
       sender='namen@gmail.com',
       recipients= [str(damail)])
    msg.body = "Hello thanks" + (' your password is  ') + dapass
    mail.send(msg)
    # opens and writes to the text database file
    with open('*yourappsdirectory*\database.txt','a') as fo:
        fo.write(str(request.form['email']) + (' ') + str(request.form['stid']) + (' ') + dapass)
    
    # returns a message with the users password
    return str(request.form['email']) + ('  your password is   ') + dapass

# Runs the webapp      
if __name__ == '__main__':
    app.run()
