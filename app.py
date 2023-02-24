from flask import Flask, render_template, escape, request, json, jsonify, make_response, redirect, url_for, session, flash
from flask import json
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from xml.dom import minidom
from datetime import datetime
import requests
from threading import Timer
from flask import request
import time
from itertools import zip_longest
from datetime import datetime
import sqlite3
import os
import os.path
import random
import urllib.request
from urllib.parse import urlparse,urljoin
from bs4 import BeautifulSoup
import requests,uuid,pathlib,os


app = Flask(__name__)
app.secret_key = "Secret Key"

#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tiviru.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://vrkarqgzzzkmtn:0e32017efa344188261e0ca0fa2fe78a0c7f986a6604ce207a4921ca072f4b4e@ec2-34-246-155-237.eu-west-1.compute.amazonaws.com:5432/de51kvccijsfj2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

print(db)

#Creating model table for our CRUD database
class Slider(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    img = db.Column(db.String(100))
    summary = db.Column(db.String(100))
    genre = db.Column(db.String(100))
    state = db.Column(db.String(100))
    date = db.Column(db.String(100))
    country = db.Column(db.String(100))
    link = db.Column(db.String(100))
    header_font = db.Column(db.String(100))
    content_font = db.Column(db.String(100))
    header_img = db.Column(db.String(100))


    def __init__(self, id, title, img, summary, genre, state, date, country, link, header_font, content_font, header_img):

        self.id = id
        self.title = title
        self.img = img
        self.summary = summary
        self.genre = genre
        self.state = state
        self.date = date
        self.country = country
        self.link = link
        self.header_font = header_font
        self.content_font = content_font
        self.header_img = header_img



#Creating model table for Media
class Media(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    category = db.Column(db.String(100))
    genres = db.Column(db.String(100))
    summary = db.Column(db.String(100))
    cast = db.Column(db.String(100))
    img = db.Column(db.String(100))
    source = db.Column(db.String(100))
    country = db.Column(db.String(100))
    status = db.Column(db.String(100))
    year = db.Column(db.String(100))
    main_slider = db.Column(db.String(100))
    carousel = db.Column(db.String(100))
   


    def __init__(self, id, title, category, genres, summary, cast, img, source, country, status, year, main_slider, carousel):

        self.id = id
        self.title = title
        self.category = category
        self.genres = genres
        self.summary = summary
        self.cast = cast
        self.img = img
        self.source = source
        self.country = country
        self.status = status
        self.year = year
        self.main_slider = main_slider
        self.carousel = carousel


#Creating model table for Media
class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    registration_date = db.Column(db.String(100))

   


    def __init__(self, id, firstname, lastname, email, username, password, registration_date):

        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.registration_date = registration_date
    
    


@app.route('/')
@app.route('/home')
def home():
    # main_slider = Media
    # print(main_slider)
    
    # main_slider = Media
    # ms_slides = []
    # for slide in main_slider.query.filter_by().all():
    #     ms_slides.append(slide)

    # print(ms_slides)


    users = Users
    my_users = []
    for slide in users.query.filter_by().all():
        my_users.append(slide)

    print(my_users)



    return "hello"


        # series = Media
        # series_slides = []
        # for slide in series.query.filter_by(category="series", carousel="1").all():
        
        #     series_slides.append(slide)


        # documentaries = Media
        # documentaries_slides = []
        # for slide in documentaries.query.filter_by(category="documentary", carousel="1").all():
        
        #     documentaries_slides.append(slide)


        # movies = Media
        # movies_slides = []
        # for slide in movies.query.filter_by(category="movie", carousel="1").all():
        
        #     movies_slides.append(slide)


        # tvshows = Media
        # tvshows_slides = []
        # for slide in tvshows.query.filter_by(category="tvshow", carousel="1").all():
        
        #     tvshows_slides.append(slide)

    
        # return render_template("home.html", ms_slides = ms_slides,
        #                                     series_slides = series_slides,
        #                                     documentaries_slides = documentaries_slides, 
        #                                     movies_slides = movies_slides,
        #                                     tvshows_slides = tvshows_slides)


if __name__ == '__main__':

    app.config['ENV'] = 'development'
    app.config['DEBUG'] = True
    app.config['TESTING'] = False

    app.run(port=5001)
