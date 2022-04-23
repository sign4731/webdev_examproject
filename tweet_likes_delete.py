from bottle import delete, response, request
import g
import jwt
import sqlite3

##############################
@delete("/likes/<tweet_id>")
def _(tweet_id):
    try: 
        print(" YOU ARE TRYING TO UNLIKE A TWEET")
        # connect to database
        db = sqlite3.connect(f"{g.PATH}database.sqlite")
        db.row_factory = g.dict_factory
        tweet = db.execute("SELECT * FROM tweets WHERE tweet_id = ?", (tweet_id,)).fetchone()
        print(tweet)

        # Validate tweet
        if not tweet:
            response.status = 400
            return "Tweet doesn't exist"

        # Who unlikes it? The user who is logged in aka get the logged in user's id
        user_jwt = request.get_cookie("user_jwt") 
        decoded_jwt = jwt.decode(user_jwt, "my secret key", algorithms="HS256")
        user_email = decoded_jwt["user_email"]
        print(user_email)

        tweet_unliked_by = db.execute("SELECT user_id FROM users WHERE user_email = ?", (user_email,)).fetchone()
        print(tweet_unliked_by["user_id"])
        tweet_unliked_by = tweet_unliked_by["user_id"]

        # update/delete the unliked tweet
        db.execute("DELETE FROM tweets_liked_by WHERE tweet_id_fk = ? AND user_id_fk = ?", (tweet_id, tweet_unliked_by,))
        db.commit()
    except Exception as ex:
        print(ex)
        response.status = 500
        return 
    finally:
        db.close()
        return f"you unliked {tweet}"