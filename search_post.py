from bottle import post, response, request
import g
import sqlite3

##############################
@post("/search")
def _():
    try:
        # Get user input
        search_query = request.forms.get("search_query")
        print(search_query)
        if not search_query:
            return dict(search_output = {})
        
    except Exception as ex:
        print(ex)
        response.status = 500

    try:
        db = sqlite3.connect("database.sqlite")
        db.row_factory = g.dict_factory

        # Get like from db
        search_output = db.execute("SELECT * FROM users WHERE user_first_name LIKE ? OR user_last_name LIKE ? OR user_tag LIKE ?", ('%'+search_query+'%', '%'+search_query+'%', '%'+search_query+'%',)).fetchall()
        print(search_output)

        # Output result
        return dict(search_output = search_output)
        
    except Exception as ex:
        print(ex)
        response.status = 500
        return f"{ex}"
    finally:
        db.close()