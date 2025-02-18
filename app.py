
from flask import Flask, request, jsonify
from flask_cors import CORS
from database import Database
from models import NewsPost

app = Flask(__name__)
CORS(app)

# API Routes
@app.route('/api/news', methods=['GET'])
def get_news():
    # Return all news posts
    pass

@app.route('/api/news', methods=['POST'])
def add_news():
    # Add new news post
    pass

@app.route('/api/news/<id>', methods=['GET'])
def get_single_news(id):
    # Return specific news post
    pass

if __name__ == '__main__':
    app.run(debug=True)