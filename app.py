from flask import Flask


app = Flask(__name__)


@app.route('/')

if __name__ == '__main__':
    app.run(debug=True)