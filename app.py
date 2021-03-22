from flask import Flask, jsonify, request, render_template, redirect, url_for
import get_latest_news as news


app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/apidata')
def json_data(page=1):
    data = news.getNews()
    return jsonify({"data":data})

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)