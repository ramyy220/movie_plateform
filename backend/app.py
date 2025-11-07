from flask import Flask, jsonify
from flask_cors import CORS  # type: ignore

app= Flask(__name__)
CORS(app) 

@app.route('/')
def home():
    return jsonify({"message": "Welcome to backend API"})

if __name__ == '__main__':
    app.run(debug=True)