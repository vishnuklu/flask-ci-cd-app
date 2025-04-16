from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask from PyCharm!"

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))  # Get port from environment
    app.run(host='0.0.0.0', port=port, debug=True)  # Bind to 0.0.0.0
