from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from CI/CD Demo!"

@app.route("/about")
def about():
    return "Learning CI/CD step by step."


if __name__ == "__main__":
     port = int(os.environ.get("PORT", 5000))
     app.run(host="0.0.0.0", port=port)
