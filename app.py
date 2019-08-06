import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'tea'
app.config["MONGO_URI"] = 'mongodb+srv://cat:catUser@myfirstcluster-lypt3.mongodb.net/tea?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_category')
def get_category():
    return render_template("home.html", category=mongo.db.category.find())
   
@app.route('/get_tea_types/<category_id>', methods=['GET', 'POST'])
def get_tea_types(category_id):
    tea= mongo.db.teatype.find_one({'_id': ObjectId(category_id)})
    return render_template('tea_types.html', teatype=tea) 
   
   
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)