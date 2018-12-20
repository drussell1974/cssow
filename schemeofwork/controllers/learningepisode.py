# -*- coding: utf-8 -*-
from gluon.shell import exec_environment
learningepisodeModel = exec_environment('applications/schemeofwork/models/learningepisodeModel.py', request=request)
schemeofworkModel = exec_environment('applications/schemeofwork/models/schemeofworkModel.py', request=request)

def index():
    scheme_of_work_id = int(request.vars.scheme_of_work_id)
    scheme_of_work_name = schemeofworkModel.get_schemeofwork_name_only()

    data = learningepisodeModel.get_all()
    schemeofwork_options = schemeofworkModel.get_options()

    content = {
        "main_heading":"Learning episodes",
        "sub_heading": "for {}".format(scheme_of_work_name),
        "background_img":"home-bg.jpg"
              }

    return dict(content = content, model = data, scheme_of_work_id = scheme_of_work_id, schemeofwork_options = schemeofwork_options)


@auth.requires_login()
def edit():
    model = learningepisodeModel.get_model()
    if request.vars.scheme_of_work_id is not None:
        # required for creating a new object
        model.scheme_of_work_id = int(request.vars.scheme_of_work_id)

    content = {
        "main_heading":"Learning episode",
        "sub_heading":model.scheme_of_work_name,
        "strap_line": model.order_of_delivery_id if model.order_of_delivery_id is not None else "Click next to map the pathway and objectives."
              }
    return dict(content = content, model = model)


@auth.requires_login()
def save_item():
    scheme_of_work_id = int(request.vars.scheme_of_work_id)

    id_ = int(request.vars.id)
    order_of_delivery_id = int(request.vars.order_of_delivery_id)
    scheme_of_work_id = int(request.vars.scheme_of_work_id)
    topic_id = int(request.vars.topic_id)

    model = learningepisodeModel.save(auth.user.id, id_, order_of_delivery_id, scheme_of_work_id, topic_id)

    return redirect(URL('learningobjective', 'index', vars=dict(scheme_of_work_id=scheme_of_work_id, learning_episode_id=model.id, topic_id = model.topic_id)))


@auth.requires_login()
def delete_item():
    scheme_of_work_id = int(request.vars.scheme_of_work_id)
    learningepisodeModel.delete(auth.user.id)

    return redirect(URL('index', vars=dict(scheme_of_work_id=scheme_of_work_id)))
