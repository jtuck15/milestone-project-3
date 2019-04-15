import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# connecting to the database

app.config['MONGO_DBNAME'] ='cooking_recipes'
app.config['MONGO_URI'] = 'mongodb+srv://jtuck15:jt511526@jimmyt-2rj89.mongodb.net/cooking_recipes?retryWrites=true'

mongo = PyMongo(app)

# meals rendered from database to the home page

@app.route('/')
@app.route('/get_meals')
def get_meals():
    return render_template('meals.html', course=mongo.db.course.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
            port=int(os.environ.get('PORT')), 
            debug=True)