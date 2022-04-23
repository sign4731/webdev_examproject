from bottle import get, response, view
import g
import sqlite3

##############################
@get("/admin")
@view("admin")
def _():
    try:
        db = sqlite3.connect(f"{g.PATH}database.sqlite")
        db.row_factory = g.dict_factory

        # Get and show all tweets 
        tweets = db.execute("SELECT * FROM tweets JOIN users WHERE tweets.tweet_created_by = users.user_id ORDER BY tweet_iat DESC").fetchall()
        print("TWEETS")
        print(tweets)

        # See how much all tweets are liked
        all_likes = db.execute("SELECT * FROM tweets_liked_by").fetchall()
        print("ALL LIKES", all_likes)

        return dict(tweets = tweets, all_likes = all_likes, path = g.PATH)
    except Exception as ex:
        print(ex)
        response.status = 500
    finally:
        db.close()