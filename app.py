from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Simulating an error (divide by zero)
    result = 1 / 0  # This will cause a ZeroDivisionError
    return f"Result: {result}"

if __name__ == "__main__":
    app.run(debug=True)
