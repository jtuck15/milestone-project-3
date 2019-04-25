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
                            side_dishes=mongo.db.side_dishes.find(),
                            all_recipes = mongo.db.all_recipes.find())
    

@app.route('/add_meal')
def add_meal():
    return render_template('add_meal.html',
                            course=mongo.db.course.find(),
                            starters = mongo.db.starters.find(),
                            main_courses = mongo.db.main_courses.find(),
                            desserts = mongo.db.desserts.find(),
                            side_dishes = mongo.db.side_dishes.find(),
                            all_recipes = mongo.db.all_recipes.find())
                            

@app.route('/insert_meal', methods=['POST'])
def insert_meal():
    all_recipes = mongo.db.all_recipes
    
    all_recipes.insert_one(request.form.to_dict())
    
    return redirect(url_for('get_meals'))
    

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    _recipe = mongo.db.all_recipes.find_one({'_id': ObjectId(recipe_id)})
    _course = mongo.db.course.find()
    course_list = [course for course in _course]
    return render_template('edit_recipe.html', recipe= _recipe, course= course_list)
    

@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    all_recipes = mongo.db.all_recipes
    all_recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'meal_name': request.form.get('meal_name'),
        'course_name': request.form.get('course_name'),
        'description': request.form.get('description'),
        'cooking_time': request.form.get('cooking_time'),
        'author': request.form.get('author'),
        'ingredients': request.form.get('ingredients'),
        'method': request.form.get('method'),
        'picture': request.form.get('picture')
    })
    
    return redirect(url_for('get_meals'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
            port=int(os.environ.get('PORT')), 
            debug=True)