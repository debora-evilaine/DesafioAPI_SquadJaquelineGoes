from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)


@app.route("/")
def get_home_page():
    return render_template("home.html")

@app.route("/locations")
def get_locations():
    url = "https://rickandmortyapi.com/api/location"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("locations.html", locations = dict["results"])

@app.route("/episodes")
def get_episodes():
    url = "https://rickandmortyapi.com/api/episode"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("episodes.html", episodes = dict["results"])

@app.route("/location/<id>")
def get_single_location(id):
    url = "https://rickandmortyapi.com/api/location/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    single_location = json.loads(data)

    return render_template("location.html",  location = single_location)

@app.route("/episode/<id>")
def get_single_episode(id):
    url = "https://rickandmortyapi.com/api/episode/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    single_episode = json.loads(data)

    return render_template("episode.html", episode = single_episode)

@app.route("/character/<id>")
def get_single_character(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    single_character = json.loads(data)

    return render_template("character.html", character = single_character)