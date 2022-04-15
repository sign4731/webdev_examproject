from bottle import post, response, request 
import g
import imghdr
import json
import os
import sqlite3
import time
import uuid

# Email imports
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

##############################
@post("/signup")
def _():
    try:
        user_id = str(uuid.uuid4())

        # Tag validation
        user_tag = request.forms.get("user_tag")
        if not user_tag:
            response.status = 500
            return "You need a tag name!"
        user_tag = g._is_text(user_tag)

        # First name validation
        user_first_name = request.forms.get("user_first_name")
        if not user_first_name:
            response.status = 500
            return "You need a first name!"
        
        user_first_name = g._is_text(user_first_name)
        user_first_name = user_first_name.capitalize()
        
        # Last name validation
        user_last_name = request.forms.get("user_last_name")
        if not user_last_name:
            response.status = 500
            return "You need a last name!"
        user_last_name = g._is_text(user_last_name)
        user_last_name = user_last_name.capitalize()
        
        # Email validation
        user_email = request.forms.get("user_email")
        if not user_email:
            response.status = 500
            return "You need an email!"

        # Password validation
        user_password = request.forms.get("user_password")
        if not user_password:
            response.status = 500
            return "You need a password!"
        if len(user_password) < 6:
            response.status = 500
            return "Password should be at least 6 characters!"
        if len(user_password) > 20:
            response.status = 500
            return "Password should be max 20 characters!"

        # Image validation
        user_image = request.files.get("user_image")
        if not user_image:
            response.status = 500
            return "You need an image!"
        
        print(dir(user_image))
        image_name = user_image.file
        # get image extension fx .png or .jpeg
        print(user_image.filename)
        file_name, file_extension = os.path.splitext(user_image.filename)
        print(file_name)
        print(file_extension)
        # Validate extention
        if file_extension not in (".png", ".jpeg", ".jpg"): 
            response.status = 400
            return "Wrong file type"
        # Overwrite jpg to jpeg to pass imghdr validation
        if file_extension == ".jpg": file_extension = ".jpeg"

        image_id = str(uuid.uuid4())
        image_name = f"{image_id}{file_extension}"
        print(image_name)
        # Save the image
        user_image.save(f"profile_images/{image_name}") 
        user_image = f"{image_name}"

        # Make sure that image is actually a valid image
        # by reading its mime type
        imghdr_extention = imghdr.what(f"profile_images/{image_name}")
        if file_extension != f".{imghdr_extention}":
            print(file_extension)
            # remove the invalid image from the folder
            os.remove(f"profile_images/{image_name}")
            response.status = 400
            return "Wrong file extension"

        user = {
            "user_id":user_id, 
            "user_tag":f"@{user_tag}",
            "user_first_name":user_first_name, 
            "user_last_name":user_last_name, 
            "user_email":user_email, 
            "user_password":user_password, 
            "user_image":user_image,
            "user_iat":time.ctime(),
            }
        print(user)

    except Exception as ex:
        print(ex)
        response.status = 500
        return "Something went wrong"
    

    try:
        db = sqlite3.connect("database.sqlite")
        db.execute("INSERT INTO users VALUES(:user_id, :user_tag, :user_first_name, :user_last_name, :user_email, :user_password, :user_image, :user_iat)", user)
        db.commit()
        db.row_factory = g.dict_factory
        users = json.dumps(db.execute("SELECT * FROM users").fetchall())
        print("HERE IS ALL USERS")
        print(users)

    except Exception as ex:
        print(ex)
        response.status = 500
        return "Something went wrong"
    
    finally:
        db.close()

    ######## SEND EMAIL ########
    print("EMAIL")
    print(user_first_name)
    print(user_email)

    sender_email = "web2022school@gmail.com"
    receiver_email = user_email
    password = g.GMAIL_PASSWORD

    message = MIMEMultipart("alternative")
    message["Subject"] = "Welcome to Twitter!"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Welcome to Twitter
    """

    html = """\
    <html>
    <body>
        <p>
        Hi, %s<br>
        <b>Thank you for joining Twitter!</b><br>
        </p>
    </body>
    </html>
    """ % user_first_name

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        try:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            return f"email sent to {user}"
        except Exception as ex:
            print(ex)
            response.status = 500
            return "uppps... could not send the email"