from random import randint

from flask import Flask

app = Flask(__name__)

def highest_random(limit):
    highest = 0
    for i in range(5):
        r = randint(0, limit)
        if r > highest:
            highest = r
    msg = f'Hello {highest:d}'
    return msg


