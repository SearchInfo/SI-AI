# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import codecs
import bfilter
import test
import web_crawler_fin
app = Flask (__name__)

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        url = request.form['url']
        web_crawler_fin.webcrawler(url)
        
        result = bfilter.runFilter()
    return render_template('index.html', result = result)

if __name__ == '__main__':
    app.run()

