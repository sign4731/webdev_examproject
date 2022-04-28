from bottle import delete, response
import g
import sqlite3

##############################
@delete("/main/<tweet_id>")
def _(tweet_id):
    try: 
        # Get tweet from database 
        db = sqlite3.connect(f"{g.PATH}database.sqlite")
        db.row_factory = g.dict_factory
        tweet = db.execute("SELECT * FROM tweets WHERE tweet_id = ?", (tweet_id,)).fetchone()
        print(tweet)
        print(tweet["tweet_created_by"])

        # Validate tweet
        if not tweet:
            response.status = 400
            return "Tweet doesn't exist"

        # Delete tweet from db
        db.execute("DELETE FROM tweets WHERE tweet_id= ?", (tweet_id,))
        db.execute("DELETE FROM tweets_liked_by WHERE tweet_id_fk= ?", (tweet_id,))
        db.commit()
        return f"you deleted {tweet}"

    except Exception as ex:
        print(ex)
        response.status = 500
        return 
    finally:
        db.close()
        