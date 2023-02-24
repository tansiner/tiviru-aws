from flask import Flask, render_template, escape, json, jsonify, make_response, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.secret_key = "Secret Key"


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


    # users = Users
    # my_users = []
    # for slide in users.query.filter_by().all():
    #     my_users.append(slide)

    # print(my_users)



    return "privet"


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


    app.run()
