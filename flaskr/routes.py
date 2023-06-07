from flaskr import app

@app.route('/')
@app.route('/index')
def index():
    return '<p>Hello World</p>'