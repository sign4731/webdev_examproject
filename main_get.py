from bottle import get, redirect, response, request,  view
import g
import jwt
import sqlite3
from time import time, ctime

##############################
@get("/main")
@view("main")
def _():
    
    try:
        db = sqlite3.connect("database.sqlite")
        db.row_factory = g.dict_factory

        # Check if user is logged in, otherwise redirect to start
        response.set_header("Cache-Control", "no-cache, no-store, must-revalidate")
        user_jwt = request.get_cookie("user_jwt") 
        print(user_jwt)
        if not user_jwt:
            raise

    except Exception as ex:
        print(ex)
        print("REDIRECTING")
        return redirect("/")
        

    try:
        
        # Get and show image belonging to logged in user
        user_jwt = request.get_cookie("user_jwt") 
        decoded_jwt = jwt.decode(user_jwt, "my secret key", algorithms="HS256")
        
        user_email = decoded_jwt["user_email"]
        print(user_email)

        logged_in_user = db.execute("SELECT * FROM users WHERE user_email = ?", (user_email,)).fetchone()
        print(logged_in_user) 

        # Get and show all tweets 
        tweets = db.execute("SELECT * FROM tweets JOIN users WHERE tweets.tweet_created_by = users.user_id ORDER BY tweet_iat DESC").fetchall()
        print("TWEETS")
        print(tweets)

        # See what tweets are liked by logged in user
        user_id = logged_in_user["user_id"]
        # likes = db.execute("SELECT * FROM tweets_liked_by WHERE user_id_fk = ?", user_id).fetchall()
        user_likes = db.execute("SELECT * FROM tweets_liked_by WHERE user_id_fk = ?", (user_id,)).fetchall()
        # likes_counter = db.execute("SELECT COUNT(*) FROM tweets_liked_by WHERE user_id_fk = ?", (user_id,)).fetchall()
        print("THIS USER LIKES", user_likes)
        # print(likes_counter)

        # See how much all tweets are liked
        all_likes = db.execute("SELECT * FROM tweets_liked_by").fetchall()
        print("ALL LIKES", all_likes)
            
        # Get and show all users
        users = db.execute("SELECT * FROM users").fetchall()
        print(users)

        # Get who logged in user follows
        follows = db.execute("SELECT * FROM follows WHERE user_who_followed_id_fk = ?", (user_id,)).fetchall()
        print("FOLLOWS")
        print(follows)

        # return dict with logged in user, tweets and all users
        return dict(
            logged_in_user = logged_in_user, 
            users = users, 
            tweets = tweets, 
            user_likes = user_likes, 
            all_likes = all_likes, 
            follows=follows)

    except Exception as ex:
        print(ex)
        response.status = 500
    finally:
        db.close()