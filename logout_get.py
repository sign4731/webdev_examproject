from bottle import get, redirect, response, request
import g
import jwt
import sqlite3

##############################
@get("/logout")
def _():
    try:
        # Connect to db
        db = sqlite3.connect(f"{g.PATH}database.sqlite")

        # Get the user session id
        user_jwt = request.get_cookie("user_jwt") 
        decoded_jwt = jwt.decode(user_jwt, "my secret key", algorithms="HS256")
        print(decoded_jwt)

        user_session_id = decoded_jwt['user_session_id']
        print(user_session_id)

        # Remove user session from database
        db.execute("DELETE FROM sessions WHERE user_session_id = ?", (user_session_id,))
        db.commit()
        print(user_session_id + " has logged out")

        # Remove cookie
        response.delete_cookie("user_jwt")

    except Exception as ex:
        print(ex)
        response.status = 500
    finally:
        db.close()
        return redirect("/")