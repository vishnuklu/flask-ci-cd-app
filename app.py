from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/new_route')
def new_route():
    return 'This is a new route.'

if __name__ == '__main__':
    app.run(debug=True)
