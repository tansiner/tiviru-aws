from flask import Flask, render_template, escape, json, jsonify, make_response, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "Secret Key"

#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tiviru.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://vrkarqgzzzkmtn:0e32017efa344188261e0ca0fa2fe78a0c7f986a6604ce207a4921ca072f4b4e@ec2-34-246-155-237.eu-west-1.compute.amazonaws.com:5432/de51kvccijsfj2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/')
@app.route('/home')
def home():
    main_slider = Media
    
    main_slider = Media
    ms_slides = []
    for slide in main_slider.query.filter_by().all():
        ms_slides.append(slide)



    # users = Users
    # my_users = []
    # for slide in users.query.filter_by().all():
    #     my_users.append(slide)





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

    
    return render_template("home.html", ms_slides = ms_slides)


if __name__ == '__main__':


    app.run()
