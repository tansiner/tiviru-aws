from flask import Flask, render_template, escape, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.secret_key = "Secret Key"

#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tiviru.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)




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



    


@app.route('/')
@app.route('/home')
def home():

    
    # main_slider = Media
    # ms_slides = []
    # for slide in main_slider.query.filter_by().all():
    #     ms_slides.append(slide)

  
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

    return "hello world"


if __name__ == '__main__':


    app.run()
