from bottle import post, response, request
import g
import json
import jwt
import re
import sqlite3
import uuid

##############################
@post("/login")
def _():
    try:
        # Validate
        user_email = request.forms.get("user_email")
        if not user_email:
            response.status = 500
            return "You need to insert an email"
        if not re.match(g.REGEX_EMAIL, user_email):
            response.status = 500
            return "You need to insert a valid email"

        user_password = request.forms.get("user_password")
        if not user_password:
            return "You need to insert a password"
        if len(user_password) < 6:
            response.status = 500
            return "Password should be at least 6 characters!"
        if len(user_password) > 20:
            response.status = 500
            return "Password should be max 20 characters!"

        user = {
            "user_email":user_email,
            "user_password":user_password
        }
    except Exception as ex:
        print(ex)
        response.status = 500
    
    try:
        db = sqlite3.connect(f"{g.PATH}database.sqlite")
        user = db.execute("SELECT * FROM users WHERE user_email = ? AND user_password = ?", (user_email, user_password,)).fetchone()
        if not user:
            response.status = 500
            return "There is no user matching this information"
        print("THIS IS YOU")
        print(json.dumps(user))

        # Create session
        user_session_id = str(uuid.uuid4())
        user_session = {
            "user_session_id": user_session_id,
            "user_email":user_email
        }
        db.execute("INSERT INTO sessions VALUES(:user_session_id, :user_email)", user_session)
        sessions = db.execute("SELECT * FROM sessions").fetchall()
        db.commit()
        print(user_session)
        print(json.dumps(sessions))

        # Set cookie with jwt
        user_jwt = jwt.encode( user_session, "my secret key", algorithm="HS256")
        response.set_cookie("user_jwt", user_jwt)

        return user
    except Exception as ex:
        print(ex)
        response.status = 500
    finally:
        db.close()
     
