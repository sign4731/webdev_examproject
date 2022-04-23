from bottle import post, response, request
import g
import jwt
import sqlite3

##############################
@post("/likes/<tweet_id>")
def _(tweet_id):
    try:
        # Get tweet from database 
        db = sqlite3.connect(f"{g.PATH}database.sqlite")
        db.row_factory = g.dict_factory
        tweet = db.execute("SELECT * FROM tweets WHERE tweet_id = ?", (tweet_id,)).fetchone()
        print(tweet)

        # Validate tweet
        if not tweet:
            response.status = 400
            return "Tweet doesn't exist"

        # Who likes it? The user who is logged in aka get the logged in user's id
        user_jwt = request.get_cookie("user_jwt") 
        decoded_jwt = jwt.decode(user_jwt, "my secret key", algorithms="HS256")
        user_email = decoded_jwt["user_email"]
        print(user_email)

        tweet_liked_by = db.execute("SELECT user_id FROM users WHERE user_email = ?", (user_email,)).fetchone()
        print(tweet_liked_by["user_id"])

        # update/insert the liked tweet
        tweet_liked = {
            "tweet_id_fk": tweet_id,
            "user_id_fk": tweet_liked_by["user_id"],
        }

        print("TWEET LIKED BY")
        print(tweet_liked)
        
        db.execute("INSERT INTO tweets_liked_by VALUES(:tweet_id_fk, :user_id_fk)", tweet_liked)
        db.commit()
    except Exception as ex:
        print(ex)
        response.status = 500
        return 
    finally:
        db.close()
        return f"you liked {tweet}"
