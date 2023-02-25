from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "Secret Key"

#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:admin12345@database-1.cl7j5j2rhsoe.us-west-2.rds.amazonaws.com/flaskaws'
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

    main_slider = Media
    ms_slides = []
    for slide in main_slider.query.filter_by(main_slider="1").all():
        ms_slides.append(slide)

    return render_template("home.html", ms_slides = ms_slides, series_slides = series_slides)


if __name__ == '__main__':
    app.run()
