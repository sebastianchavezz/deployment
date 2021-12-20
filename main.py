from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db_name = 'sqlite:///game.db'



app.config['SQLALCHEMY_DATABASE_URI'] = db_name
app.config['SQLALCHEMY_TRACK_NODIFICATIONS'] = True 


db = SQLAlchemy(app)


class Game(db.Model):

    __tablename__ = 'game'

    type = db.Column(db.String)
    name = db.Column(db.String)
    steam_appid = db.Column(db.Integer,primary_key=True)
    
spel2 = Game.query.all()


@app.route('/')
def get_name():
    

    spel = Game.query.all()
   

    return render_template('home.html',spel=spel) 

if __name__ == '__main__':
    
    app.run(debug=True)
