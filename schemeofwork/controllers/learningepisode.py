# -*- coding: utf-8 -*-
from datetime import datetime
from cls_learningepisode import LearningEpisodeModel
import db_schemeofwork  #= exec_environment('applications/schemeofwork/models/db_schemeofwork.py', request=request)
import db_learningepisode  #= exec_environment('applications/schemeofwork/models/db_learningepisode.py', request=request)
import db_learningobjective  #= exec_environment('applications/schemeofwork/models/db_learningobjective.py', request=request)
import db_topic  #= exec_environment('applications/schemeofwork/models/db_topic.py', request=request)

def index():
    """ index action """
    scheme_of_work_id = int(request.vars.scheme_of_work_id)
    scheme_of_work_name = db_schemeofwork.get_schemeofwork_name_only(db, scheme_of_work_id)

    data = db_learningepisode.get_all(db, scheme_of_work_id)
    schemeofwork_options = db_schemeofwork.get_options(db)

    content = {
        "main_heading":"Learning episodes",
        "sub_heading": "for {}".format(scheme_of_work_name),
        "background_img":"home-bg.jpg"
              }

    return dict(content = content, model = data, scheme_of_work_id = scheme_of_work_id, schemeofwork_options = schemeofwork_options)


@auth.requires_login()
def edit():
    """ edit action """
    id_ = int(request.vars.id if request.vars.id is not None else 0)

    model = db_learningepisode.get_model(db, id_)
    if request.vars.scheme_of_work_id is not None:
        # required for creating a new object
        model.scheme_of_work_id = int(request.vars.scheme_of_work_id)
        model.scheme_of_work_name = db_schemeofwork.get_schemeofwork_name_only(db, model.scheme_of_work_id)


    key_stage_id = db_schemeofwork.get_key_stage_id_only(db, model.scheme_of_work_id)
    model.key_stage_id = key_stage_id

    topic_options = []
    learningobjectives_data = db_learningobjective.get_all(db, id_)

    #if(len(learningobjectives_data) == 0):
    topic_options = db_topic.get_options(db, model.topic_id, 1) #, model.parent_topic_id);


    content = {
        "main_heading":"Learning episode",
        "sub_heading":model.get_ui_sub_heading(),
        "strap_line":model.get_ui_title()
              }

    return dict(content = content, model = model, topic_options = topic_options, has_objectives = True)


@auth.requires_login()
def save_item():
    """ save_item non-view action """

    model = LearningEpisodeModel(
        id_ = request.vars.id,
        order_of_delivery_id = request.vars.order_of_delivery_id,
        scheme_of_work_id = request.vars.scheme_of_work_id,
        topic_id = request.vars.topic_id,
        key_stage_id= request.vars.key_stage_id,
        created = datetime.now(),
        created_by_id = auth.user.id
    )

    model.validate()
    if model.is_valid == True:
        model = db_learningepisode.save(db, model)
    else:
        raise Exception("Validation errors:/n/n %s" % model.validation_errors) # TODO: redirect

    ' if the request.vars.id was 0 then this is a new scheme of work '
    ' the user should be take create learning episodes '
    redirect_to_url = ""
    if int(request.vars.id) == 0:
        redirect_to_url = URL('learningobjective', 'index', vars=dict(scheme_of_work_id=request.vars.scheme_of_work_id, learning_episode_id=model.id))
    else:
        redirect_to_url = URL('learningepisode', 'index', vars=dict(scheme_of_work_id=request.vars.scheme_of_work_id))

    return redirect(redirect_to_url)


@auth.requires_login()
def delete_item():
    """ delete_item non-view action """

    id_ = int(request.vars.id)
    scheme_of_work_id = int(request.vars.scheme_of_work_id)

    db_learningepisode.delete(db, auth.user.id, id_)

    return redirect(URL('index', vars=dict(scheme_of_work_id=scheme_of_work_id)))
