from flask import Flask, jsonify, request
import get_latest_news as news


app = Flask(__name__)


@app.route('/')
def home():
    data = news.getNews()
    return jsonify({"data":data})

if __name__ == '__main__':
    app.run(debug=True)