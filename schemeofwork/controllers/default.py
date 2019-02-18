# -*- coding: utf-8 -*
import db_schemeofwork
import db_keyword
import db_topic

def index():

    # get the schemes of work
    latest_schemes_of_work = db_schemeofwork.get_latest_schemes_of_work(db, top = 5, auth_user = auth.user_id)

    content = {
        "main_heading":T("Teach Computer Science"),
        "sub_heading":T("Computing Schemes of Work across all key stages")
              }

    return dict(content = content, latest_schemes_of_work = latest_schemes_of_work)


def about():
    content = {
        "main_heading":T("About us"),
        "sub_heading":T("Computing Schemes of Work across all key stages")
              }
    return dict(content = content)

# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)

def get_key_words():
    """ returns keywords as json """
    ' get the topic_id from the url'

    key_words = db_keyword.get_options(db)

    import gluon.contrib.simplejson
    return gluon.contrib.simplejson.dumps(key_words)


def get_related_topics():
    """ returns topics as json """
    ' get the topic_id from the url'
    topic_id = int(request.args(0))

    topics = db_topic.get_options(db, topic_id=topic_id, lvl=2)
    serializable_list = []
    for item in topics:
        serializable_list.append({"id":item.id, "name":item.name})

    import gluon.contrib.simplejson
    return gluon.contrib.simplejson.dumps(serializable_list)
