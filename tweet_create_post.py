from bottle import post, response, request
import g
import imghdr
import jwt
import os
import sqlite3
import time
import uuid

##############################
@post("/create-tweet")
def _():
    try:
        print("you are trying to tweet")
        
        tweet_id = str(uuid.uuid4())

        # Validate
        tweet_text = request.forms.get("tweet_text")
        if not tweet_text:
            response.status = 500
            return "You need text!"
        if len(tweet_text) > 500:
            response.status = 500
            return "Max 500 characters"
        tweet_text = g._is_text(tweet_text)

        # Get image if any
        tweet_image = ""
        if request.files.get("tweet_image"):
            tweet_image = request.files.get("tweet_image")
            print(dir(tweet_image))
            image_name = tweet_image.file
            # get image extension fx .png or .jpeg
            print(tweet_image.filename)
            file_name, file_extension = os.path.splitext(tweet_image.filename)
            print(file_name)
            print(file_extension)
            # Validate extention
            if file_extension not in (".png", ".jpeg", ".jpg"): 
                response.status = 400
            # Overwrite jpg to jpeg to pass imghdr validation
            if file_extension == ".jpg": file_extension = ".jpeg"

            image_id = str(uuid.uuid4())
            image_name = f"{image_id}{file_extension}"
            print(image_name)
            # Save the image
            tweet_image.save(f"tweet_images/{image_name}") 
            tweet_image = f"{image_name}"

            # Make sure that image is actually a valid image
            # by reading its mime type
            imghdr_extention = imghdr.what(f"tweet_images/{image_name}")
            if file_extension != f".{imghdr_extention}":
                print(file_extension)
                # remove the invalid image from the folder
                os.remove(f"tweet_images/{image_name}")
                tweet_image = ""
                response.status = 400

        # Get owner of tweet
        db = sqlite3.connect("database.sqlite")
        db.row_factory = g.dict_factory

        user_jwt = request.get_cookie("user_jwt") 
        decoded_jwt = jwt.decode(user_jwt, "my secret key", algorithms="HS256")
        user_email = decoded_jwt["user_email"]
        print(user_email)

        tweet_created_by = db.execute("SELECT user_id FROM users WHERE user_email = ?", (user_email,)).fetchone()
        print(tweet_created_by["user_id"])

        
        tweet_iat = int(time.time())
        tweet_iat_date = time.ctime()
        print(tweet_iat)
        print(tweet_iat_date)
        tweet_updated_at = ""

        tweet = {
            "tweet_id" : tweet_id,
            "tweet_text" : tweet_text,
            "tweet_image" : tweet_image,
            "tweet_created_by": tweet_created_by["user_id"],
            "tweet_iat" : tweet_iat,
            "tweet_iat_date" : tweet_iat_date,
            "tweet_updated_at" : tweet_updated_at
        }
        print(tweet)

    except Exception as ex:
        print(ex)
        response.status = 500
    
    try:

        # Add to database
        db.execute("INSERT INTO tweets VALUES(:tweet_id, :tweet_text, :tweet_image, :tweet_created_by, :tweet_iat, :tweet_iat_date, :tweet_updated_at)", tweet)
        db.commit()
        print("you tweeted")

        # Get tweet and user to output
        tweet_and_user = db.execute("SELECT * FROM tweets JOIN users WHERE tweets.tweet_id = ? AND users.user_email = ?", (tweet_id, user_email,)).fetchone()
        print(tweet_and_user)


        return dict(tweet_and_user = tweet_and_user)
    except Exception as ex:
        print(ex)
        response.status = 500
    finally:
        db.close()