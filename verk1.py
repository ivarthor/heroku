from sys import argv
import bottle
from bottle import *

@route('/')
def index():
    return """
    <h2> Verkefni 1 </h2>
    <p><a href=" /about"> um okkur </a></p>
    <p><a href=" /bio"> ferilskra</a></p>
    <p><a href=" /pics"> Myndir</a></p>
    """

@route('/about')
def jobbi():
    return "hér eru upplýsingar um Jonna vinnumann"

@route('/bio')
def jobbi():
    return "hér er ferilskrá Jonna vinnumanns"

@route('/pics')
def jobbi():
    return "hér eru myndir af Jonna vinnumann"



bottle.run(host='0.0.0.0', port=argv[1])
