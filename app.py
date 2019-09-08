import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
import bcrypt

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'tea'
app.config["MONGO_URI"] = 'mongodb+srv://cat:catUser@myfirstcluster-lypt3.mongodb.net/tea?retryWrites=true&w=majority'

mongo = PyMongo(app)
app.secret_key = os.urandom(24)

@app.route('/')
@app.route('/get_category')
def get_category():
    return render_template("home.html", category=mongo.db.category.find())
    
    
@app.route('/register', methods=['POST', 'GET'])
def register():
    
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username' : request.form['username']})

        if existing_user is None:
            pw_hash = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
    
            db_password = pw_hash.decode("utf-8")
           
            users.insert({'username' : request.form['username'], 'password' : db_password})
          
            session['username'] = request.form['username']
            return redirect(url_for('login'))
        
    return render_template('register.html')
    
@app.route('/login', methods=['POST', 'GET'])
def login():

    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'username' : request.form['username']})
    
        if login_user:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
                session['username'] = request.form['username']
                return redirect(url_for('get_category'))
    
        
    return render_template('login.html')


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('get_category'))    

@app.route('/get_tea/<category_name>', methods=['GET', 'POST'])
def get_tea(category_name):
    get_tea = mongo.db.teatype.find({'category_name': category_name})
    return render_template('tea_types.html', teatypes=get_tea, category=mongo.db.category.find({'category_name': category_name}))


@app.route('/get_tea_specific/<tea_name>', methods=['GET', 'POST'])
def get_tea_specific(tea_name):
    tea_specific = mongo.db.teatype.find({'tea_name': tea_name})
    return render_template('tea_specific.html', teatypes=tea_specific)
   
@app.route('/show_lists')
def show_lists():
    return render_template('lists.html', lists=mongo.db.lists.find(), teatype = mongo.db.teatype.find())

@app.route('/add_list')
def add_list():
    return render_template('add_list.html', teatypes = mongo.db.teatype.find())
    
@app.route('/insert_list', methods=['POST'])
def insert_list():
    lists =  mongo.db.lists
    lists.insert_one(request.form.to_dict())
    return redirect(url_for("show_lists"))
    
#@edit_list
#@delete list
#@delete tea from list
#@addnew tea to list (in edit? )


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
 