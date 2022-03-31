from bottle import error, get, default_app,response, post, redirect, request, route, run, static_file, view
import uuid
import time 
import imghdr
import os
import sqlite3
import json
import g
import re

##############################
# POST
import signup_post 
import login_post

##############################
@get("/")
@view("index")
def _():
    return

##############################
@get("/main")
def _():
    return "main" 

##############################
@get("/styles/app.css")
def _():
    return static_file("/styles/app.css", root=".")

##############################
@get("/scripts/validator.js")
def _():
    return static_file("/scripts/validator.js", root=".")

##############################
@get("/scripts/scripts.js")
def _():
    return static_file("/scripts/scripts.js", root=".")

##############################
@route('/media/<picture>')
def _(picture):
    return static_file(picture, root='./media')

##############################
@error(404)
@view("error")
def _(error):
    print(error)
    response.status = 404
    return    

##############################
try:
  import production
  application = default_app()
except Exception as ex:
  run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")
