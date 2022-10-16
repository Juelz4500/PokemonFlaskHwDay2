from flask import Flask, redirect, render_template, url_for, request
from config import Config
import requests
import json
import findpokemon

app = Flask(__name__, template_folder='templates', static_folder='static')



@app.route("/")
def index():
    return render_template('home.html')


@app.route(f"/pokemon", methods=["POST", "GET"])
def pokemon():
    pokeName = request.form.get('pokemon')
    pokeName = pokeName.capitalize()
    try:
        pokemon = findpokemon.findPokeByName(pokeName)
    except:
        return render_template('error.html')

    return render_template('pokemon.html', 
        pokemon=pokemon
        )

@app.route("/error")
def error():
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)