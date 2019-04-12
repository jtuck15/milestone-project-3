import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# app.config['MONGO_DBNAME'] ='cooking recipes'
# MONGODB_URI = os.getenv("MONGO_URI")
# mongo = PyMongo(app)




if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'), 
            port=int(os.environ.get('PORT', '5000')), 
            debug=True)