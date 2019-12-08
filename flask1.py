#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 09:22:28 2019

@author: hala
"""
# =============================================================================
# Q1
# =============================================================================
from flask import Flask,render_template
app=Flask(__name__)


@app.route('/')
def index():
    return 'This is the Index page'
@app.route('/hello')
def hello():
    return "Hello World!"
@app.route('/members')
def member():
    return "Members page"

# =============================================================================
# Q2
# =============================================================================
@app.route('/index/<int:marks>')
def mark(marks):
    return render_template('Index.html',marks=marks)

# =============================================================================
# Q3
# =============================================================================
@app.route('/index')
def Q3():
    return render_template('app.html')


if __name__=='__main__':
    app.run()