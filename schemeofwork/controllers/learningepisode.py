# -*- coding: utf-8 -*-
from gluon.contrib.appconfig import AppConfig
configuration = AppConfig(reload=True)

db = DAL(configuration.get('db.uri'),
     pool_size=configuration.get('db.pool_size'),
     migrate_enabled=configuration.get('db.migrate'),
     check_reserved=['all'])

from datetime import datetime
from cls_learningepisode import LearningEpisodeModel

from gluon.shell import exec_environment
db_learningepisode = exec_environment('applications/schemeofwork/models/db_learningepisode.py', request=request)
db_learningobjective  = exec_environment('applications/schemeofwork/models/db_learningobjective.py', request=request)
db_schemeofwork = exec_environment('applications/schemeofwork/models/db_schemeofwork.py', request=request)
db_topic = exec_environment('applications/schemeofwork/models/db_topic.py', request=request)

def index():
    scheme_of_work_id = int(request.vars.scheme_of_work_id)
    scheme_of_work_name = db_schemeofwork.get_schemeofwork_name_only(scheme_of_work_id)

    data = db_learningepisode.get_all(scheme_of_work_id)
    schemeofwork_options = db_schemeofwork.get_options()

    content = {
        "main_heading":"Learning episodes",
        "sub_heading": "for {}".format(scheme_of_work_name),
        "background_img":"home-bg.jpg"
              }

    return dict(content = content, model = data, scheme_of_work_id = scheme_of_work_id, schemeofwork_options = schemeofwork_options)


@auth.requires_login()
def edit():
    id_ = int(request.vars.id if request.vars.id is not None else 0)

    model = db_learningepisode.get_model(id_)
    if request.vars.scheme_of_work_id is not None:
        # required for creating a new object
        model.scheme_of_work_id = int(request.vars.scheme_of_work_id)

    topic_options = []
    learningobjectives_data = db_learningobjective.get_all(id_)

    if(len(learningobjectives_data) == 0 or model.id != 0):
        topic_options = db_topic.get_options(model.topic_id, model.parent_topic_id);

    content = {
        "main_heading":"Learning episode",
        "sub_heading":model.get_ui_sub_heading(),
        "strap_line":model.get_ui_title()
              }
    return dict(content = content, model = model, topic_options = topic_options)


@auth.requires_login()
def save_item():
    id_ = int(request.vars.id)
    order_of_delivery_id = int(request.vars.order_of_delivery_id)
    scheme_of_work_id = int(request.vars.scheme_of_work_id)
    topic_id = int(request.vars.topic_id)

    model = LearningEpisodeModel(
        id_ = id_,
        order_of_delivery_id = order_of_delivery_id,
        scheme_of_work_id = scheme_of_work_id,
        topic_id = topic_id,
        created = datetime.now(),
        created_by_id = auth.user.id
    )

    model.validate()
    if model.is_valid == True:
        model = db_learningepisode.save(model)
    else:
        raise Exception("Validation errors:/n/n %s" % model.validation_errors) # TODO: redirect

    return redirect(URL('learningobjective', 'index', vars=dict(scheme_of_work_id=scheme_of_work_id, learning_episode_id=model.id)))


@auth.requires_login()
def delete_item():

    id_ = int(request.vars.id)
    scheme_of_work_id = int(request.vars.scheme_of_work_id)

    db_learningepisode.delete(auth.user.id, id_)

    return redirect(URL('index', vars=dict(scheme_of_work_id=scheme_of_work_id)))
