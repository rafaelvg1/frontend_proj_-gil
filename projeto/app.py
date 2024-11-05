from flask import Flask, render_template
import os
from flask import Flask, render_template
from flask_pymongo import PyMongo
import os



app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://admin:admin@progeficaz.e4oxl.mongodb.net/insper_pay"


mongo = PyMongo(app)


@app.route('/', methods=["GET"])
def teste():
    filtro={}
    projecao={"id":0}
    item=mongo.db.comidas.find(filtro,projecao)
    return render_template("inicial.html",item=item)








# Rota para a página inicial
@app.route('/')
def home():
    return render_template('inicial.html')

# Rota para a página de bebidas
@app.route('/bebidas')
def bebidas():
    return render_template('bebidas.html')

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000, host='0.0.0.0')



