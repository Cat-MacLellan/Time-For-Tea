{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":22,"position":22,"stack":[[{"start":{"row":0,"column":0},"end":{"row":14,"column":23},"action":"insert","lines":["import os","from flask import Flask","","app = Flask(__name__)","","","@app.route('/')","def hello():","    return 'Hello World ...again'","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":14,"column":23},"action":"remove","lines":["import os","from flask import Flask","","app = Flask(__name__)","","","@app.route('/')","def hello():","    return 'Hello World ...again'","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":2},{"start":{"row":0,"column":0},"end":{"row":21,"column":23},"action":"insert","lines":["import os","from flask import Flask, render_template, redirect, request, url_for","from flask_pymongo import PyMongo","from bson.objectid import ObjectId ","","app = Flask(__name__)","app.config[\"MONGO_DBNAME\"] = 'task_manager'","app.config[\"MONGO_URI\"] = os.getenv('MONGO_URI', 'mongodb://localhost')","","mongo = PyMongo(app)","","","@app.route('/')","@app.route('/get_tasks')","def get_tasks():","    return render_template(\"tasks.html\", tasks=mongo.db.tasks.find())","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"]}],[{"start":{"row":6,"column":30},"end":{"row":6,"column":42},"action":"remove","lines":["task_manager"],"id":3},{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"insert","lines":["t"]},{"start":{"row":6,"column":31},"end":{"row":6,"column":32},"action":"insert","lines":["e"]},{"start":{"row":6,"column":32},"end":{"row":6,"column":33},"action":"insert","lines":["a"]}],[{"start":{"row":13,"column":17},"end":{"row":13,"column":22},"action":"remove","lines":["tasks"],"id":4},{"start":{"row":13,"column":17},"end":{"row":13,"column":18},"action":"insert","lines":["c"]},{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"insert","lines":["a"]},{"start":{"row":13,"column":19},"end":{"row":13,"column":20},"action":"insert","lines":["t"]},{"start":{"row":13,"column":20},"end":{"row":13,"column":21},"action":"insert","lines":["e"]},{"start":{"row":13,"column":21},"end":{"row":13,"column":22},"action":"insert","lines":["g"]},{"start":{"row":13,"column":22},"end":{"row":13,"column":23},"action":"insert","lines":["o"]},{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"insert","lines":["r"]},{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"insert","lines":["i"]},{"start":{"row":13,"column":25},"end":{"row":13,"column":26},"action":"insert","lines":["e"]},{"start":{"row":13,"column":26},"end":{"row":13,"column":27},"action":"insert","lines":["s"]}],[{"start":{"row":15,"column":28},"end":{"row":15,"column":33},"action":"remove","lines":["tasks"],"id":5}],[{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"insert","lines":["c"],"id":6},{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"insert","lines":["a"]},{"start":{"row":15,"column":30},"end":{"row":15,"column":31},"action":"insert","lines":["t"]},{"start":{"row":15,"column":31},"end":{"row":15,"column":32},"action":"insert","lines":["e"]},{"start":{"row":15,"column":32},"end":{"row":15,"column":33},"action":"insert","lines":["g"]},{"start":{"row":15,"column":33},"end":{"row":15,"column":34},"action":"insert","lines":["o"]},{"start":{"row":15,"column":34},"end":{"row":15,"column":35},"action":"insert","lines":["r"]},{"start":{"row":15,"column":35},"end":{"row":15,"column":36},"action":"insert","lines":["y"]}],[{"start":{"row":15,"column":44},"end":{"row":15,"column":49},"action":"remove","lines":["tasks"],"id":7},{"start":{"row":15,"column":44},"end":{"row":15,"column":45},"action":"insert","lines":["c"]},{"start":{"row":15,"column":45},"end":{"row":15,"column":46},"action":"insert","lines":["a"]},{"start":{"row":15,"column":46},"end":{"row":15,"column":47},"action":"insert","lines":["t"]},{"start":{"row":15,"column":47},"end":{"row":15,"column":48},"action":"insert","lines":["e"]},{"start":{"row":15,"column":48},"end":{"row":15,"column":49},"action":"insert","lines":["g"]},{"start":{"row":15,"column":49},"end":{"row":15,"column":50},"action":"insert","lines":["o"]},{"start":{"row":15,"column":50},"end":{"row":15,"column":51},"action":"insert","lines":["r"]},{"start":{"row":15,"column":51},"end":{"row":15,"column":52},"action":"insert","lines":["y"]}],[{"start":{"row":15,"column":66},"end":{"row":15,"column":67},"action":"remove","lines":["s"],"id":8},{"start":{"row":15,"column":65},"end":{"row":15,"column":66},"action":"remove","lines":["k"]},{"start":{"row":15,"column":64},"end":{"row":15,"column":65},"action":"remove","lines":["s"]},{"start":{"row":15,"column":63},"end":{"row":15,"column":64},"action":"remove","lines":["a"]},{"start":{"row":15,"column":62},"end":{"row":15,"column":63},"action":"remove","lines":["t"]}],[{"start":{"row":15,"column":62},"end":{"row":15,"column":63},"action":"insert","lines":["c"],"id":9},{"start":{"row":15,"column":63},"end":{"row":15,"column":64},"action":"insert","lines":["a"]}],[{"start":{"row":15,"column":62},"end":{"row":15,"column":64},"action":"remove","lines":["ca"],"id":10},{"start":{"row":15,"column":62},"end":{"row":15,"column":70},"action":"insert","lines":["category"]}],[{"start":{"row":7,"column":26},"end":{"row":7,"column":71},"action":"remove","lines":["os.getenv('MONGO_URI', 'mongodb://localhost')"],"id":11}],[{"start":{"row":7,"column":26},"end":{"row":7,"column":28},"action":"insert","lines":["''"],"id":12}],[{"start":{"row":7,"column":27},"end":{"row":7,"column":121},"action":"insert","lines":["mongodb+srv://cat:<password>@myfirstcluster-lypt3.mongodb.net/test?retryWrites=true&w=majority"],"id":13}],[{"start":{"row":7,"column":45},"end":{"row":7,"column":55},"action":"remove","lines":["<password>"],"id":14}],[{"start":{"row":7,"column":45},"end":{"row":7,"column":46},"action":"insert","lines":["c"],"id":15},{"start":{"row":7,"column":46},"end":{"row":7,"column":47},"action":"insert","lines":["a"]},{"start":{"row":7,"column":47},"end":{"row":7,"column":48},"action":"insert","lines":["t"]},{"start":{"row":7,"column":48},"end":{"row":7,"column":49},"action":"insert","lines":["U"]},{"start":{"row":7,"column":49},"end":{"row":7,"column":50},"action":"insert","lines":["s"]},{"start":{"row":7,"column":50},"end":{"row":7,"column":51},"action":"insert","lines":["e"]},{"start":{"row":7,"column":51},"end":{"row":7,"column":52},"action":"insert","lines":["r"]}],[{"start":{"row":13,"column":26},"end":{"row":13,"column":27},"action":"remove","lines":["s"],"id":16},{"start":{"row":13,"column":25},"end":{"row":13,"column":26},"action":"remove","lines":["e"]},{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"remove","lines":["i"]}],[{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"insert","lines":["y"],"id":17}],[{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"remove","lines":["s"],"id":18}],[{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"remove","lines":["k"],"id":19},{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"remove","lines":["s"]},{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"remove","lines":["a"]},{"start":{"row":14,"column":8},"end":{"row":14,"column":9},"action":"remove","lines":["t"]}],[{"start":{"row":14,"column":8},"end":{"row":14,"column":9},"action":"insert","lines":["c"],"id":20},{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"insert","lines":["a"]},{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"insert","lines":["t"]},{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"insert","lines":["e"]},{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"insert","lines":["g"]},{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"insert","lines":["o"]},{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"insert","lines":["r"]},{"start":{"row":14,"column":15},"end":{"row":14,"column":16},"action":"insert","lines":["y"]}],[{"start":{"row":7,"column":89},"end":{"row":7,"column":90},"action":"remove","lines":["t"],"id":21},{"start":{"row":7,"column":88},"end":{"row":7,"column":89},"action":"remove","lines":["s"]}],[{"start":{"row":7,"column":88},"end":{"row":7,"column":89},"action":"insert","lines":["a"],"id":22}],[{"start":{"row":5,"column":21},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":23}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":6,"column":0},"end":{"row":6,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1564177680903,"hash":"17954a0cfd4a143697463146fb7005c9b21f3938"}