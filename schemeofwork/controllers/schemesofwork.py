# -*- coding: utf-8 -*-
import cls_schemeofwork
import cls_examboard as db_examboard
import cls_keystage as db_keystage
from datetime import datetime
from cls_schemeofwork import SchemeOfWorkModel
from pager import Pager
from validation_helper import html_validation_message

def index():
    """ index action """

    filtered_key_stage_id =  int(request.args(0) if request.args(0) is not None else 0)

    page_to_display = int(request.vars.page if request.vars.page is not None else 1)

    # get the schemes of work
    data = cls_schemeofwork.get_all(db, key_stage_id=filtered_key_stage_id, auth_user=auth.user_id)
    # get the key stages to show
    key_stage_options = db_keystage.get_options(db)

    # get the key stage name to display
    filtered_key_stage_name = ""
    for ks in key_stage_options:
        if ks.id == filtered_key_stage_id:
            filtered_key_stage_name = ks.name

    # page the data
    pager = Pager(page = page_to_display, page_size = 10, data = data)

    pager_html = pager.render_html(URL('schemesofwork', 'index', vars=dict(key_stage_id=filtered_key_stage_id)))

    data = pager.data_to_display()


    content = {
        "main_heading":T("Schemes of Work"),
        "sub_heading":T("Our shared schemes of work by key stage"),
        "strap_line":None,
        "background_img":"home-bg.jpg"
              }

    return dict(content = content,
                model = data,
                key_stage_id = filtered_key_stage_id,
                key_stage_name = filtered_key_stage_name,
                key_stage_options = key_stage_options,
                page = page_to_display,
                pager_html = pager_html)


def view():
    """ view action (NOT USED) """

    id_ = int(request.vars.id)
    model = cls_schemeofwork.get_model(db, id_=id_, auth_user=auth.user_id)

    # check results and redirect if necessary

    if(model == None):
        ' TODO: SEND MESSAGE'
        redirect(URL('index'))

    content = {
        "main_heading":model.name,
        "sub_heading":model.exam_board_name + " " + model.key_stage_name
              }
    return dict(content = content, model = model)


@auth.requires_login()
def edit():
    """ edit action """

    id_ = int(request.vars.id if request.vars.id is not None else 0)
    model = cls_schemeofwork.get_model(db, id_, auth.user_id)
    if(model == None):
        redirect(URL('index', vars=dict(message="item deleted")))

    examboard_options = db_examboard.get_options(db)
    keystage_options = db_keystage.get_options(db)

    content = {
        "main_heading":T("Scheme of Work") if model.name == "" else model.name,
        "sub_heading":T("Create a new scheme of work") if model.name == "" else T("{} {}".format(model.key_stage_name, model.exam_board_name)),
        "strap_line":T("Fill out the form below then click save")
              }
    return dict(content = content, model = model, examboard_options = examboard_options, keystage_options = keystage_options)


@auth.requires_login()
def save_item():
    """ save_item non-view action """
    published = int(request.vars.published if request.vars.published is not None else 1)

    # create instance of model from request.vars

    model = SchemeOfWorkModel(
        id_=request.vars.id,
        name=request.vars.name,
        description=request.vars.description,
        exam_board_id=request.vars.exam_board_id,
        key_stage_id=request.vars.key_stage_id,
        created=datetime.now(),
        created_by_id=auth.user_id)

    # validate the model and save if valid otherwise redirect to default invalid

    model.validate()
    if model.is_valid == True:
        model = cls_schemeofwork.save(db, model, published)
    else:
        """ redirect back to page and show message """
        session.alert_message = html_validation_message(model.validation_errors) #model.validation_errors
        if request.env.http_referer:
            redirect(request.env.http_referer)

    ' redirect if necessary '
    redirect_to_url = ""

    if request.vars._next != "None" and request.vars._next != "":
        redirect_to_url = request.vars._next
    else:
        redirect_to_url = URL('learningepisode', 'index', args=[model.id])
    return redirect(redirect_to_url)


@auth.requires_login()
def delete_item():
    """ delete_item non-view action """

    id_ = int(request.vars.id)
    cls_schemeofwork.delete(db, auth_user_id=auth.user.id, id_ = id_)
    return redirect(URL('index'))


@auth.requires_login()
def publish_item():
    """ delete_item non-view action """

    id_ = int(request.vars.id)
    cls_schemeofwork.publish(db, auth_user_id=auth.user.id, id_ = id_)
    return redirect(URL('index'))
