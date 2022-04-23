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
    return static_file("/styles/app.css", root=g.PATH)

##############################
@get("/scripts/createTweet.js")
def _():
    return static_file("/scripts/createTweet.js", root=g.PATH)

##############################
@get("/scripts/deleteTweet.js")
def _():
    return static_file("/scripts/deleteTweet.js", root=g.PATH)
    
##############################
@get("/scripts/handleFileInput.js")
def _():
    return static_file("/scripts/handleFileInput.js", root=g.PATH)

##############################
@get("/scripts/handleFollow.js")
def _():
    return static_file("/scripts/handleFollow.js", root=g.PATH)

##############################
@get("/scripts/handleLikeTweet.js")
def _():
    return static_file("/scripts/handleLikeTweet.js", root=g.PATH)

##############################
@get("/scripts/index.js")
def _():
    return static_file("/scripts/index.js", root=g.PATH)

##############################
@get("/scripts/logIn.js")
def _():
    return static_file("/scripts/logIn.js", root=g.PATH)

##############################
@get("/scripts/removeImage.js")
def _():
    return static_file("/scripts/removeImage.js", root=g.PATH)

##############################
@get("/scripts/signUp.js")
def _():
    return static_file("/scripts/signUp.js", root=g.PATH)

##############################
@get("/scripts/toggleModal.js")
def _():
    return static_file("/scripts/toggleModal.js", root=g.PATH)

##############################
@get("/scripts/updateTweet.js")
def _():
    return static_file("/scripts/updateTweet.js", root=g.PATH)

##############################
@get("/scripts/validator.js")
def _():
    return static_file("/scripts/validator.js", root=g.PATH)

##############################
@route('/profile_images/<picture>')
def _(picture):
    return static_file(picture, root=f"{g.PATH}profile_images")

##############################
@route('/tweet_images/<picture>')
def _(picture):
    return static_file(picture, root=f"{g.PATH}tweet_images")

##############################
   


##############################
try:
  import production
  application = default_app()
except Exception as ex:
  run(host="127.0.0.1", port=3000, debug=True, reloader=True, server="paste")
