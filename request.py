#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 09:44:14 2019

@author: hala
"""



from flask import Flask, render_template
import sqlite3 as sql
DATABASE="q12.db"

app = Flask(__name__)




@app.route('/result')
def result():
     with sql.connect(DATABASE) as con :
        cur=con.cursor()
     res=cur.execute("select * from user")  
     return render_template('result.html', users=res)

if __name__ == '__main__':
    app.run()

