import string
from time import time
from itertools import chain
from random import seed, choice, sample


def mkpasswd (length=int(input("how many  chars in the password?")),digits=int(input("how many numbers in the password?")), upper=int(input("how many upper case")), lower=int(input("how many lower case")), spchars=int(input("how many special characters"))):
    """Create a random password with
specific length and characters based on size
prints password when done

    
    """

    seed(time())

    lowercase = string.ascii_lowercase.translate(None, "o")
    uppercase = string.ascii_uppercase.translate(None, "O")
    letters = "{0:s}{1:s}".format(lowercase, uppercase)
    

    password = list(
        chain(
            (choice(uppercase) for _ in range(upper)),
            (choice(lowercase) for _ in range(lower)),
            (choice(string.digits) for _ in range(digits)),
            (choice(string.punctuation) for _ in range(spchars)),
            (choice(letters) for _ in range((length - digits - upper - lower - spchars)))
        )
    )

    return "".join(sample(password, len(password)))


print mkpasswd()

