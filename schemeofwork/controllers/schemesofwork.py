# -*- coding: utf-8 -*-
# try something like
from gluon.shell import exec_environment
schemeofworkModel = exec_environment('applications/schemeofwork/models/schemeofworkModel.py', request=request)
examboardModel = exec_environment('applications/schemeofwork/models/examboardModel.py')
keystageModel = exec_environment('applications/schemeofwork/models/keystageModel.py')

import datetime


def index():
    content = {
        "main_heading":"Schemes of work",
        "sub_heading":"Our shared schemes of work by key stage",
        "strap_line":"",
        "background_img":"home-bg.jpg"
              }

    # get the schemes of work
    data = schemeofworkModel.get_all()

    return dict(content = content, model = data)


def view():
    id_ = int(request.vars.id)
    model = schemeofworkModel.get_model(id_=id_)

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
    id_ = int(request.vars.id if request.vars.id is not None else 0)
    model = schemeofworkModel.get_model(id_)
    if(model == None):
        redirect(URL('index', vars=dict(message="item deleted")))

    examboard_options = examboardModel.get_options()
    keystage_options = keystageModel.get_options()

    content = {
        "main_heading":model.name if model.name == "" else "New Scheme of work",
        "sub_heading":model.exam_board_name + " " + model.key_stage_name,
        "strap_line": "" if model.name == "" else "Create a new scheme of work. Fill out the form below then click next to select or create learning episode."
              }
    return dict(content = content, model = model, examboard_options = examboard_options, keystage_options = keystage_options)


@auth.requires_login()
def save_item():
    model = schemeofworkModel.save(
        auth_user_id=auth.user.id,
        id_=request.vars.id,
        name=request.vars.name,
        description=request.vars.description,
        exam_board_id=request.vars.exam_board_id,
        key_stage_id=request.vars.key_stage_id,)

    return redirect(URL('learningepisode', 'index', vars=dict(scheme_of_work_id = model.id)))


@auth.requires_login()
def delete_item():
    id_ = int(request.vars.id)
    schemeofworkModel.delete(auth_user_id=auth.user.id, id_ = id_)
    return redirect(URL('index'))
