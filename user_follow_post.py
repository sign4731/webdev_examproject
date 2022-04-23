from bottle import post, response, request
import g
import jwt
import sqlite3

##############################
@post("/follows/<user_id>")
def _ (user_id):
    try:
        # Get user to follow
        db = sqlite3.connect(f"{g.PATH}database.sqlite")
        db.row_factory = g.dict_factory
        user_to_be_followed = db.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()
        print(user_to_be_followed)

        # Validate user to follow
        if not user_to_be_followed:
                response.status = 400
                return "User doesn't exist"

        # Who followed? Get id of the user that is logged in
        user_jwt = request.get_cookie("user_jwt") 
        decoded_jwt = jwt.decode(user_jwt, "my secret key", algorithms="HS256")
        user_email = decoded_jwt["user_email"]
        print(user_email)

        user_followed_by = db.execute("SELECT user_id FROM users WHERE user_email = ?", (user_email,)).fetchone()
        print(user_followed_by["user_id"])

        # Insert follow in follows table
        user_followed = {
            "user_who_followed_id_fk": user_followed_by["user_id"],
            "user_who_got_followed_id_fk": user_to_be_followed["user_id"],
        }

        print("USER FOLLOWED")
        print(user_followed)
        
        db.execute("INSERT INTO follows VALUES(:user_who_followed_id_fk, :user_who_got_followed_id_fk)", user_followed)
        db.commit()

        return f"You followed {user_to_be_followed}"
    except Exception as ex:
        print(ex)
        response.status = 500
        return