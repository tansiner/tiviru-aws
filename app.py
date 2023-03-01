from flask import Flask, render_template, escape, request, json, jsonify, make_response, redirect, url_for, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
from xml.dom import minidom
from datetime import datetime

app = Flask(__name__)
app.secret_key = "Secret Key"

#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/flaskaws'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)




#Creating model table for our CRUD database
class Channels(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    channel_name = db.Column(db.String(100))
    channel_logo = db.Column(db.String(100))
    iptv = db.Column(db.String(100))
    country = db.Column(db.String(100))
    webstream = db.Column(db.String(100))
    status = db.Column(db.String(100))


    def __init__(self, id, channel_name, channel_logo, channel_src, status, country):

        self.id = id
        self.channel_name = channel_name
        self.channel_logo = channel_logo
        self.iptv = iptv
        self.webstream = webstream
        self.country = country
        self.status = webstream



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

    
    series = Media
    series_slides = []
    for slide in series.query.filter_by(category="series", carousel="1").all():
        series_slides.append(slide)


    documentaries = Media
    documentaries_slides = []
    for slide in documentaries.query.filter_by(category="documentary", carousel="1").all():
    
        documentaries_slides.append(slide)

    movies = Media
    movies_slides = []
    for slide in movies.query.filter_by(category="movies", carousel="1").all():
    
        movies_slides.append(slide)
    

    return render_template("home.html", ms_slides = ms_slides, series_slides = series_slides, documentaries_slides = documentaries_slides, movies_slides = movies_slides)











guide=minidom.parse("static/guide.xml")
full_date = datetime.date(datetime.now())
today = full_date.strftime("%Y%m%d")
current = datetime.now() # current date and time
now = current.strftime("%H%M%S")

@app.route('/tv')
def tv():

    i = 0
    index = 0

    total_len = len(Channels.query.all())
    current_epg = [[] for x in range(0,total_len)]
    full_epg = [[] for x in range(0,total_len)]

    programme = guide.getElementsByTagName("programme")


    guide_channels = []
    for prg in programme:

        if prg.getAttribute("channel") not in guide_channels:
            guide_channels.append(prg.getAttribute("channel"))


    from datetime import datetime

    now = datetime.now()
    

    current_time = now.strftime("%H%M%S")
    print("Current Time =", current_time)



    for channel in Channels.query:
        
        print(channel.status)
        
        
        if channel.status == 1:
        
            if channel.channel_name in guide_channels:


                for program in programme:

                    start_time = program.getAttribute("start")[8:15]
                    finish_time = program.getAttribute("stop")[8:15]
                    index += 1


                    if channel.channel_name == program.getAttribute("channel"):

                        if (finish_time > current_time) or (finish_time[0:2] == "00") or (finish_time[0:2] == "01" or (finish_time[0:2] == "02") or (finish_time[0:2] == "03") or (finish_time[0:2] == "04") or (finish_time[0:2] == "05")):

                            current_epg[i].append({'start_time':start_time,'finish_time':finish_time,'program':program.childNodes[1].childNodes[0].data})
                        full_epg[i].append({'start_time':start_time,'finish_time':finish_time,'program':program.childNodes[1].childNodes[0].data})


                    index = 0


            else:
                for program in programme:

                    index += 1
                    current_epg[i].append({'start_time':"",'finish_time':"",'program':"no epg"})
                    full_epg[i].append({'start_time':"",'finish_time':"",'program':"no epg"})
                    index = 0
            i += 1


    x = 0
    channel_list_for_current_epg = []
    channel_list_for_full_epg = []
    
    stream_option = "webstream"
    
    if stream_option == "iptv":
        
        
    
        for channel in Channels.query:

            channel_list_for_current_epg.append(
            {
            'channel_name': channel.channel_name,
            'channel_logo': channel.channel_logo,
            'iptv': channel.iptv,
            'country': channel.country,
            'current_epg':current_epg[x]
            },)

            x += 1



        
    
    
    else:
        
        for channel in Channels.query:
            
            if channel.status == 1:

                channel_list_for_current_epg.append(
                {
                'channel_name': channel.channel_name,
                'channel_logo': channel.channel_logo,
                'webstream': channel.webstream,
                'country': channel.country,
                'current_epg':current_epg[x]
                },)
                
                
                channel_list_for_full_epg.append(
                {
                'channel_name': channel.channel_name,
                'channel_logo': channel.channel_logo,
                'webstream': channel.webstream,
                'country': channel.country,
                'full_epg':full_epg[x]
                },)

                x += 1

    return render_template("tv.html", data=channel_list_for_current_epg, data2=channel_list_for_full_epg ,stream_option=stream_option)
    # return render_template("tv.html")



@app.route('/update_schedule', methods = ['POST', 'GET'])
def update_schedule():
    
    
    if request.method == 'POST':
        q = request.form['q']
        current_date = request.form['current_date']
        
           
    i = 0
    index = 0

    total_len = len(Channels.query.all())
    epg = [[] for x in range(0,total_len)]

    programme = guide.getElementsByTagName("programme")


    guide_channels = []
    for prg in programme:

        if prg.getAttribute("channel") not in guide_channels:
            guide_channels.append(prg.getAttribute("channel"))



    current_time = current_date
    print("Current Time =", current_time)

    for channel in Channels.query:
        if channel.status == 1:
        
            if channel.channel_name in guide_channels:


                for program in programme:

                    start_time = program.getAttribute("start")[8:15]
                    finish_time = program.getAttribute("stop")[8:15]
                    index += 1


                    if channel.channel_name == program.getAttribute("channel"):

                        if (finish_time > current_time) or (finish_time[0:2] == "00") or (finish_time[0:2] == "01" or (finish_time[0:2] == "02") or (finish_time[0:2] == "03") or (finish_time[0:2] == "04") or (finish_time[0:2] == "05")):

                            epg[i].append({'start_time':start_time,'finish_time':finish_time,'program':program.childNodes[1].childNodes[0].data})


                    index = 0


            else:
                for program in programme:

                    index += 1
                    epg[i].append({'start_time':"",'finish_time':"",'program':"no epg"})
                    index = 0
            i += 1


    x = 0
    channels_lst = []
    
    stream_option = "webstream"
    
    if stream_option == "iptv":
        
        
    
        for channel in Channels.query:

            channels_lst.append(
            {
            'channel_name': channel.channel_name,
            'channel_logo': channel.channel_logo,
            'iptv': channel.iptv,
            'epg':epg[x]
            },)

            x += 1



        
    
    
    else:
        
        for channel in Channels.query:
            
            if channel.status == 1:

                channels_lst.append(
                {
                'channel_name': channel.channel_name,
                'channel_logo': channel.channel_logo,
                'webstream': channel.webstream,
                'epg':epg[x]
                },)

                x += 1




    return jsonify(channels_lst)





if __name__ == '__main__':

    app.config['ENV'] = 'development'
    app.config['DEBUG'] = True
    app.config['TESTING'] = False
    app.run()
