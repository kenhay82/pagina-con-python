from flask import Flask,render_template

app  = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def index():    
    return render_template('index.html')

@app.route('/productos')
def productos():
    return render_template('productos.html')

if __name__ == '__main__':
    app.run()