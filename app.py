from databases import *
from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('finalproject.html', coupons=query_all_coupons())



if __name__ == '__main__':
    app.run(debug=True)