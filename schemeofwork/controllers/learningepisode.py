# -*- coding: utf-8 -*-
from gluon.shell import exec_environment
learningepisodeModel = exec_environment('applications/schemeofwork/models/learningepisodeModel.py', request=request)
learningobjectiveModel = exec_environment('applications/schemeofwork/models/learningobjectiveModel.py', request=request)
schemeofworkModel = exec_environment('applications/schemeofwork/models/schemeofworkModel.py', request=request)
topicModel = exec_environment('applications/schemeofwork/models/topicModel.py', request=request)

def index():
    scheme_of_work_id = int(request.vars.scheme_of_work_id)
    scheme_of_work_name = schemeofworkModel.get_schemeofwork_name_only()

    data = learningepisodeModel.get_all(scheme_of_work_id)
    schemeofwork_options = schemeofworkModel.get_options()

    content = {
        "main_heading":"Learning episodes",
        "sub_heading": "for {}".format(scheme_of_work_name),
        "background_img":"home-bg.jpg"
              }

    return dict(content = content, model = data, scheme_of_work_id = scheme_of_work_id, schemeofwork_options = schemeofwork_options)


@auth.requires_login()
def edit():
    id_ = int(request.vars.id if request.vars.id is not None else 0)

    model = learningepisodeModel.get_model(id_)
    if request.vars.scheme_of_work_id is not None:
        # required for creating a new object
        model.scheme_of_work_id = int(request.vars.scheme_of_work_id)
    topic_options = []
    learningobjectives_data = learningobjectiveModel.get_all(id_)

    if(len(learningobjectives_data) == 0):
        topic_options = topicModel.get_options();

    content = {
        "main_heading":"Learning episode",
        "sub_heading":"for {}".format(model.scheme_of_work_name),
        "strap_line": "Week " + str(model.order_of_delivery_id)
              }
    return dict(content = content, model = model, topic_options = topic_options)


@auth.requires_login()
def save_item():
    id_ = int(request.vars.id)
    order_of_delivery_id = int(request.vars.order_of_delivery_id)
    scheme_of_work_id = int(request.vars.scheme_of_work_id)
    topic_id = int(request.vars.topic_id)

    model = learningepisodeModel.save(auth.user.id, id_, order_of_delivery_id, scheme_of_work_id, topic_id)

    return redirect(URL('learningobjective', 'index', vars=dict(scheme_of_work_id=scheme_of_work_id, learning_episode_id=model.id)))


@auth.requires_login()
def delete_item():
    scheme_of_work_id = int(request.vars.scheme_of_work_id)
    learningepisodeModel.delete(auth.user.id)

    return redirect(URL('index', vars=dict(scheme_of_work_id=scheme_of_work_id)))
