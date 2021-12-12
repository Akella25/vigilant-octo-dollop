from flask import Flask
from lol import Person

app = Flask(__name__)


@app.route('/')
def index():
    name = [i.first_name for i in Person.persons]
    last = [i.last_name for i in Person.persons]
    ful_name = zip(name, last)
    return ';'.join(map('-'.join, ful_name))


@app.route('/person/<int:person_id>')
def person(person_id):
    for id in Person.persons:
        if id.id == person_id:
            return str(id)
