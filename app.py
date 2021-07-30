from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/classify')
def classify():
    try:
        url = request.args.get('Link to news')
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
