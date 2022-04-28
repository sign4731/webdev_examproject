from bottle import error, get, default_app,response, route, run, static_file, view
import g


##############################
# DELETE
import tweet_delete_delete
import tweet_likes_delete
import user_unfollow_delete

# GET
import admin_get
import logout_get
import main_get
import user_profile_get

# POST
import login_post 
import signup_post 
import tweet_create_post
import tweet_likes_post
import user_follow_post

# PUT
import tweet_update_put

##############################
@get("/")
@view("index")
def _():
    return

##############################
@error(404)
@view("error")
def _(error):
    print(error)
    response.status = 404
    return 

##############################




# STATIC FILES
##############################
@get("/styles/app.css")
def _():
    return static_file("/styles/app.css", root=".")

##############################
@get("/scripts/createTweet.js")
def _():
    return static_file("/scripts/createTweet.js", root=".")

##############################
@get("/scripts/deleteTweet.js")
def _():
    return static_file("/scripts/deleteTweet.js", root=".")
    
##############################
@get("/scripts/handleFileInput.js")
def _():
    return static_file("/scripts/handleFileInput.js", root=".")

##############################
@get("/scripts/handleFollow.js")
def _():
    return static_file("/scripts/handleFollow.js", root=".")

##############################
@get("/scripts/handleLikeTweet.js")
def _():
    return static_file("/scripts/handleLikeTweet.js", root=".")

##############################
@get("/scripts/index.js")
def _():
    return static_file("/scripts/index.js", root=".")

##############################
@get("/scripts/logIn.js")
def _():
    return static_file("/scripts/logIn.js", root=".")

##############################
@get("/scripts/removeImage.js")
def _():
    return static_file("/scripts/removeImage.js", root=".")

##############################
@get("/scripts/signUp.js")
def _():
    return static_file("/scripts/signUp.js", root=".")

##############################
@get("/scripts/toggleModal.js")
def _():
    return static_file("/scripts/toggleModal.js", root=".")

##############################
@get("/scripts/updateTweet.js")
def _():
    return static_file("/scripts/updateTweet.js", root=".")

##############################
@get("/scripts/validator.js")
def _():
    return static_file("/scripts/validator.js", root=".")

##############################
@route('/profile_images/<picture>')
def _(picture):
    return static_file(picture, root="profile_images")

##############################
@route('/tweet_images/<picture>')
def _(picture):
    return static_file(picture, root="tweet_images")

##############################
   


##############################
try:
  import production
  application = default_app()
except Exception as ex:
  run(host="127.0.0.1", port=3000, debug=True, reloader=True, server="paste")
