# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import filter
app = Flask (__name__)
@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        url = float(request.form['url'])
    
    result = 0
    result = filter.filters("asdasda")
    return render_template('index.html', result = result)

if __name__ == '__main__':
    app.run(debug=True)
    
