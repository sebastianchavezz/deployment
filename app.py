from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db_name = 'sqlite:///database2.db'



app.config['SQLALCHEMY_DATABASE_URI'] = db_name
app.config['SQLALCHEMY_TRACK_NODIFICATIONS'] = True 


db = SQLAlchemy(app)


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
def get_name():
    

    spel = Game.query.all()
   

    return render_template('home.html',spel=spel) 

if __name__ == '__main__':
    
    app.run(debug=True)
