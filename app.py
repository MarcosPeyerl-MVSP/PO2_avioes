from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/fotos') 
def fotos():
    return render_template('Fotos.html')

@app.route('/videos') 
def videos():
    return render_template('Videos.html')

@app.route('/sobre') 
def sobre():
    return render_template('Sobre.html')

if __name__ == '__main__':
    app.run(debug=True)