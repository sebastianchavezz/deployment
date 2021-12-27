from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import session, sessionmaker
from sqlalchemy import create_engine




app = Flask(__name__)
db_name = 'sqlite:///database2.db'
engine = create_engine(db_name, echo = True)


app.config['SQLALCHEMY_DATABASE_URI'] = db_name
app.config['SQLALCHEMY_TRACK_NODIFICATIONS'] = True 


db = SQLAlchemy(app)

Session = sessionmaker(bind = engine)
session = Session()


class Game(db.Model):

    __tablename__ = 'games'

    index = db.Column(db.String)
    name = db.Column(db.String)
    steam_id = db.Column(db.Integer,primary_key=True)
    developers = db.Column(db.String)
    genre = db.Column(db.String)
    reviews = db.Column(db.Integer)
    positives = db.Column(db.Integer)
    is_free = db.Column(db.Boolean)
    prices_eu = db.Column(db.Float)
    units_sold = db.Column(db.Integer)
    final_revenue = db.Column(db.Integer)
    

    def __init__(self,index,name,steam_appid,developers,genre,reviews,positives,is_free,price,units_sold,revenue,) -> None:
        self.index= index
        self.name=name
        self.steam_id = steam_appid
        self.developers = developers
        self.genre = genre
        self.reviews = reviews
        self.positives = positives
        self.is_free = is_free
        self.prices_eu = price 
        self.units_sold = units_sold
        self.revenue = revenue

     
    




@app.route('/')
def home():
    return render_template('home.html')


@app.route('/dataset')
def get_name():
    

    spel = Game.query.all()
   

    return render_template('dataset.html',spel=spel) 

@app.route('/stats')
def visuals():
    return render_template("stats.html")


if __name__ == '__main__':
    
    app.run(debug=True)
