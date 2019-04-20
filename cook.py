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
    return render_template('meals.html', 
                            course=mongo.db.course.find(), 
                            starters=mongo.db.starters.find(), 
                            main_courses=mongo.db.main_courses.find(),
                            desserts=mongo.db.desserts.find(),
                            side_dishes=mongo.db.side_dishes.find())
    

@app.route('/add_meal')
def add_meal():
    return render_template('add_meal.html',
                            course=mongo.db.course.find(),
                            starters = mongo.db.starters.find(),
                            main_courses = mongo.db.main_courses.find(),
                            desserts = mongo.db.desserts.find(),
                            side_dishes = mongo.db.side_dishes.find())
                            

@app.route('/insert_meal', methods=['POST'])
def insert_meal():
    starters = mongo.db.starters
    main_courses = mongo.db.main_courses
    desserts = mongo.db.desserts
    side_dishes = mongo.db.side_dishes
    
    if request.form.get('course_name') == 'Starters':
        starters.insert_one(request.form.to_dict())
        
    elif request.form.get('course_name') == 'Main Courses':
        main_courses.insert_one(request.form.to_dict())
        
    elif request.form.get('course_name') == 'Desserts':
        desserts.insert_one(request.form.to_dict())
        
    elif request.form.get('course_name') == 'Side Dishes':
        side_dishes.insert_one(request.form.to_dict())
    
    return redirect(url_for('get_meals'))
    


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
            port=int(os.environ.get('PORT')), 
            debug=True)