from src import create_app, api_key, mail_username, mail_password
import requests
from flask import render_template, request, Response, redirect, url_for, flash, jsonify
from flask_mail import Mail, Message

import random
import string

# It calls the function in the __init__.py file.
app = create_app()


# MAIL CONFIGURATION
# Configuration for the SMTP server (Simple Mail Transfer Protocol) on Gmail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] =   mail_username
app.config['MAIL_PASSWORD'] =  mail_password 
# Remitente del correo
app.config['MAIL_DEFAULT_SENDER'] = ("Cinema Paradiso", mail_username)

mail = Mail(app)

# Hacer la solicitud a la API
@app.route('/')
def index():

    #URL for API requests
    BASE_URL = "https://api.themoviedb.org/3"
    IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"
    findNewMovies = f"{BASE_URL}/movie/now_playing"
    findTopFive = f"{BASE_URL}/discover/movie"
    findOldies = f"{BASE_URL}/discover/movie"

    releaseYears = ""

    for i in range(1950, 1990):
        releaseYears += str(i) + "|"
    
    releaseYears += "1990" 

    randomMovie = random.randint(0,11)

    #Parameters for the requests
    #New Movies
    paramsNM = {
        "api_key": api_key,
        "language": "en-US",
        "page": 1
    }

    #Best movies of last year
    paramsFive = {
        "api_key": api_key,
        "language": "en-US",
        "page": 1,
        "primary_release_year": 2024,
        "sort_by": "popularity.desc",
    }

    #Old movies with good ratings
    paramsOldies = {
        "api_key": api_key,
        "language": "en-US",
        "primary_release_year": releaseYears,
        "sort_by": "popularity.desc"
    }

    #API Request for new movies
    response = requests.get(findNewMovies, params=paramsNM)

    if response.status_code == 200:
        # Get the JSON response and movies list
        data = response.json()
        newMovies = data.get("results", [])[randomMovie:(randomMovie+5)]  # Limit to 5 movies in the page
        # Add full image URL to each movie
        for newMovie in newMovies:
            if newMovie.get("poster_path"):
                newMovie["poster_path"] = f"{IMAGE_BASE_URL}{newMovie['poster_path']}"
    else:
        newMovies = []

    
    #API request for best 5 movies of last year
    response = requests.get(findTopFive, params=paramsFive)

    if response.status_code == 200:
        # Get the JSON response and movies list
        data = response.json()
        topFives = data.get("results", [])[randomMovie:(randomMovie+5)]  # Limit to 5 movies in the page
        # Add full image URL to each movie
        for topFive in topFives:
            if topFive.get("poster_path"):
                topFive["poster_path"] = f"{IMAGE_BASE_URL}{topFive['poster_path']}"
    else:
        topFives = []

    
    #API request for 8 old movies with good rating
    response = requests.get(findOldies, params=paramsOldies)

    if response.status_code == 200:
        # Get the JSON response and movies list
        data = response.json()
        oldies = data.get("results", [])[randomMovie:(randomMovie+8)]  # Limit to 8 movies in the page
        # Add full image URL to each movie
        for oldie in oldies:
            if oldie.get("poster_path"):
                oldie["poster_path"] =f"{IMAGE_BASE_URL}{oldie['poster_path']}"
    else:
        oldies = []

    return render_template("index.html", newMovies=newMovies, topFives=topFives, oldies=oldies)


@app.route('/sendApplication', methods=['POST'])
def send_application():

    name = request.form['name']
    surname = request.form['surname']
    email = request.form['mail']
    message = request.form['message']


    msg = Message(
        subject="Request to Join The Final Cut Club",
        sender=app.config['MAIL_DEFAULT_SENDER'],
        recipients=[mail_username]  
    )
    msg.body = f"""
    Name: {name}
    Surname: {surname}
    Mail: {email}

    Message:
    {message}
    """

    try:

        mail.send(msg)
        print("The message was sent successfully!")
    except Exception as e:
        print(e)  
        print("The message could not be sent.")

    return redirect('/')

@app.route('/sendMessage', methods=['POST'])
def send_message():

    name = request.form['name']
    surname = request.form['surname']
    email = request.form['mail']
    message = request.form['message']


    msg = Message(
        subject="Someone saw your blog and wants to contact you!",
        sender=app.config['MAIL_DEFAULT_SENDER'],
        recipients=[mail_username]  
    )
    msg.body = f"""
    Name: {name}
    Surname: {surname}
    Mail: {email}

    Message:
    {message}
    """

    try:
        mail.send(msg)
        print("The message was sent successfully!")
    except Exception as e:
        print(e)  
        print("The message could not be sent.")

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)