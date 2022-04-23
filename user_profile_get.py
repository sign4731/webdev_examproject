from bottle import get, redirect, response, request, view
import g
import jwt
import sqlite3

##############################
@get("/profile/<user_id>")
@view("profile")
def _(user_id):

    try:
        db = sqlite3.connect(f"{g.PATH}database.sqlite")
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

        # Get logged in user
        user_jwt = request.get_cookie("user_jwt") 
        decoded_jwt = jwt.decode(user_jwt, "my secret key", algorithms="HS256")
        
        user_email = decoded_jwt["user_email"]
        print(user_email)

        logged_in_user = db.execute("SELECT * FROM users WHERE user_email = ?", (user_email,)).fetchone()
        print(logged_in_user)

        # Get user whose profile is visiting
        user = db.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()
        print(user)

        # Get and show all tweets belonging to user
        tweets = db.execute("SELECT * FROM tweets JOIN users WHERE tweets.tweet_created_by = users.user_id ORDER BY tweet_iat DESC").fetchall()
        tweets_amount = db.execute("SELECT COUNT(*) FROM tweets WHERE tweet_created_by = ?", (user_id,)).fetchone()
        print("TWEETS")
        print(tweets)
        print("TWEETS COUNT")
        print(tweets_amount['COUNT(*)'])
        tweets_amount = tweets_amount['COUNT(*)']

        # Get and show all users
        users = db.execute("SELECT * FROM users").fetchall()
        print(users)

        # Get how many followers the user have
        followers_amount = db.execute("SELECT COUNT(*) FROM follows WHERE user_who_got_followed_id_fk = ?", (user['user_id'],)).fetchone()
        print("AMOUNT OF FOLLOWERS")
        print(followers_amount['COUNT(*)'])
        followers_amount = followers_amount['COUNT(*)']

        # Get how many the user is following
        following_amount = db.execute("SELECT COUNT(*) FROM follows WHERE user_who_followed_id_fk = ?", (user['user_id'],)).fetchone()
        print("AMOUNT OF FOLLOWING")
        print(following_amount['COUNT(*)'])
        following_amount = following_amount['COUNT(*)']

        # See how much all tweets are liked
        all_likes = db.execute("SELECT * FROM tweets_liked_by").fetchall()
        print("ALL LIKES", all_likes)

        # See what tweets are liked by logged in user
        user_id = logged_in_user["user_id"]
        user_likes = db.execute("SELECT * FROM tweets_liked_by WHERE user_id_fk = ?", (user_id,)).fetchall()
        print("THIS USER LIKES", user_likes)

        # Get who logged in user follows
        follows = db.execute("SELECT * FROM follows WHERE user_who_followed_id_fk = ?", (user_id,)).fetchall()
        print("FOLLOWS")
        print(follows)


        return dict(
            logged_in_user=logged_in_user, 
            user = user, tweets = tweets, 
            users = users, 
            all_likes = all_likes, 
            followers_amount = followers_amount, 
            following_amount = following_amount, 
            user_likes = user_likes, 
            follows = follows, 
            path = g.PATH, 
            tweets_amount = tweets_amount)

    except Exception as ex:
        print(ex)
        response.status = 500
    finally:
        db.close()