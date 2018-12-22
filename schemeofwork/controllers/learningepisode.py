# -*- coding: utf-8 -*-
from gluon.contrib.appconfig import AppConfig
configuration = AppConfig(reload=True)

db = DAL(configuration.get('db.uri'),
     pool_size=configuration.get('db.pool_size'),
     migrate_enabled=configuration.get('db.migrate'),
     check_reserved=['all'])

import learningepisode as learningepisodeModel
import learningobjective as learningobjectiveModel
import schemeofwork as schemeofworkModel
import topic as topicModel


def index():
    scheme_of_work_id = int(request.vars.scheme_of_work_id)
    scheme_of_work_name = schemeofworkModel.get_schemeofwork_name_only(db, scheme_of_work_id)

    data = learningepisodeModel.get_all(db, scheme_of_work_id)
    schemeofwork_options = schemeofworkModel.get_options(db)

    content = {
        "main_heading":"Learning episodes",
        "sub_heading": "for {}".format(scheme_of_work_name),
        "background_img":"home-bg.jpg"
              }

    return dict(content = content, model = data, scheme_of_work_id = scheme_of_work_id, schemeofwork_options = schemeofwork_options)


@auth.requires_login()
def edit():
    id_ = int(request.vars.id if request.vars.id is not None else 0)

    model = learningepisodeModel.get_model(db, id_)
    if request.vars.scheme_of_work_id is not None:
        # required for creating a new object
        model.scheme_of_work_id = int(request.vars.scheme_of_work_id)

    topic_options = []
    learningobjectives_data = learningobjectiveModel.get_all(db, id_)

    if(len(learningobjectives_data) == 0 or model.id != 0):
        topic_options = topicModel.get_options(model.topic_id, model.parent_topic_id);

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

    model = learningepisodeModel.save(db, auth.user.id, id_, order_of_delivery_id, scheme_of_work_id, topic_id)

    return redirect(URL('learningobjective', 'index', vars=dict(scheme_of_work_id=scheme_of_work_id, learning_episode_id=model.id)))


@auth.requires_login()
def delete_item():

    id_ = int(request.vars.id)
    scheme_of_work_id = int(request.vars.scheme_of_work_id)

    learningepisodeModel.delete(db, auth.user.id, id_)

    return redirect(URL('index', vars=dict(scheme_of_work_id=scheme_of_work_id)))
