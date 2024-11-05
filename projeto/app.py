from flask import Flask, render_template
import os

app = Flask(__name__)



# Rota para a página inicial
@app.route('/')
def home():
    return render_template('inicial.html')

# Rota para a página de bebidas
@app.route('/bebidas')
def bebidas():
    return render_template('bebidas.html')


if __name__ == '__main__':
    app.run(debug=True)
