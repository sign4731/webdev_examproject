from bottle import delete, error, get, default_app,response, post, put, redirect, request, route, run, static_file, view
import uuid
import time
from time import ctime
import imghdr
import os
import sqlite3
import json
import g
import re
import jwt

##############################
# DELETE
import tweet_delete_delete
import tweet_likes_delete
import user_unfollow_delete

# GET
import admin_get
import logout_get
import main_get
import user_profile_get

# POST
import login_post 
import signup_post 
import tweet_create_post
import tweet_likes_post
import user_follow_post

# PUT
import tweet_update_put

##############################
@get("/")
@view("index")
def _():
    return

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
@route('/profile_images/<picture>')
def _(picture):
    return static_file(picture, root='./profile_images')

##############################
@route('/tweet_images/<picture>')
def _(picture):
    return static_file(picture, root='./tweet_images')

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
  run(host="127.0.0.1", port=3000, debug=True, reloader=True, server="paste")
