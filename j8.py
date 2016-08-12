import string
from itertools import chain
from random import choice, sample

from flask import Flask
from flask import request
from flask import render_template
from flask_mail import Mail
from flask_mail import Message

#mailserver info
MAIL_SERVER='smtp.gmail.com'
MAIL_PORT=465
MAIL_USE_TLS = False
MAIL_USE_SSL= True
MAIL_USERNAME = '*Your email*'
MAIL_PASSWORD = '*Your passwowrd*'


app = Flask(__name__)
app.config.from_object(__name__)

mail = Mail(app)

#makes the website
@app.route('/')
def my_form():
    return render_template("form-mini.html")


#takes the input from the form and creates the password, emails it and saves it to the database
@app.route('/', methods=['POST'])

def my_form_post():
    #These 4 variables get the input from the form 
    digits=int(request.form['digits'])
    upper=int(request.form['uppercase'])
    lower=int(request.form['lowercase'])
    spchars=int(request.form['spcars'])
   
   
    #These 3 variables set the letters sizes
    lowercase = string.ascii_lowercase.translate(None, "o")
    uppercase = string.ascii_uppercase.translate(None, "O")
    letters = "{0:s}{1:s}".format(lowercase, uppercase)

    #This chooses from the characters from the password randomly based on the variables above
    password = list(
        chain(
            (choice(uppercase) for _ in range(upper)),
            (choice(lowercase) for _ in range(lower)),
            (choice(string.digits) for _ in range(digits)),
            (choice(string.punctuation) for _ in range(spchars)),
            (choice(letters) for _ in range((digits - upper - lower - spchars)))
        )
    )
    # These 3 variables help produce the outputs and messages later int he file
    damail = str(request.form['email'])

    dapass = "".join(sample(password, len(password)))

    lstoutput = (' Hello ') + damail + ('  your password is   ') + dapass
    #Creates the email
    msg = Message(
       'Hello',
       sender='passcreator',
       recipients= [str(damail)])
    msg.body = "Hello thanks" + (' your password is  ') + dapass
    mail.send(msg)
    # opens the database file and saves the password email and employee id (as stid)
    with open('/home/zryder/mysite/static/database.txt','a') as fo:
        fo.write(str(request.form['email']) + (' ') + str(request.form['stid']) + (' ') + dapass)

    #prints the output from the variable above on the next webpage
    return render_template("index.html", lstoutput=lstoutput)


if __name__ == '__main__':
    app.run()
