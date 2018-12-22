# -*- coding: utf-8 -*-
from gluon.contrib.appconfig import AppConfig
configuration = AppConfig(reload=True)

db = DAL(configuration.get('db.uri'),
     pool_size=configuration.get('db.pool_size'),
     migrate_enabled=configuration.get('db.migrate'),
     check_reserved=['all'])


from gluon.shell import exec_environment
db_schemeofwork = exec_environment('applications/schemeofwork/models/db_schemeofwork.py', request=request)
db_learningobjective  = exec_environment('applications/schemeofwork/models/db_learningobjective.py', request=request)
db_schemeofwork = exec_environment('applications/schemeofwork/models/db_schemeofwork.py', request=request)
db_solotaxonomy = exec_environment('applications/schemeofwork/models/db_solotaxonomy.py', request=request)
db_topic = exec_environment('applications/schemeofwork/models/db_topic.py', request=request)
db_content = exec_environment('applications/schemeofwork/models/db_content.py', request=request)
db_examboard = exec_environment('applications/schemeofwork/models/db_examboard.py', request=request)
db_learningepisode = exec_environment('applications/schemeofwork/models/db_learningepisode.py', request=request)

def index():
    scheme_of_work_id = int(request.vars.scheme_of_work_id) # scheme_of_work_id = int(request.vars.scheme_of_work_id if request.vars.scheme_of_work_id is not None else 0)
    learning_episode_id = int(request.vars.learning_episode_id)

    scheme_of_work_name = db_schemeofwork.get_schemeofwork_name_only(scheme_of_work_id)
    learning_episode = db_learningepisode.get_model(learning_episode_id)
    data = db_learningobjective.get_all(learning_episode_id)

    learning_episode_options = db_learningepisode.get_options(scheme_of_work_id)

    unassociated_learning_objectives = db_learningobjective.get_unassociated_learning_objectives(
        learning_episode_id=learning_episode.id,
        key_stage_id=learning_episode.key_stage_id,
        topic_id=learning_episode.topic_id,
        parent_topic_id=learning_episode.parent_topic_id)

    content = {
        "main_heading":"Learning objectives",
        "sub_heading": "for {} - Week {} - {}".format(scheme_of_work_name, learning_episode.order_of_delivery_id, learning_episode.topic_name),
        "background_img":"home-bg.jpg"
              }

    return dict(
        content = content,
        model = data,
        scheme_of_work_id = scheme_of_work_id,
        topic_id = learning_episode.topic_id,
        learning_episode_id = learning_episode_id,
        learningepisiode_options = learning_episode_options,
        unassociated_learning_objectives = unassociated_learning_objectives
    )


@auth.requires_login()
def edit():
    model = None
    # check if an existing_learning_objective_id has been passed
    if request.vars.learning_objective_id is not None:
        _id = int(request.vars.learning_objective_id if request.vars.learning_objective_id is not None else 0)
        model = db_learningobjective.get_new_model(_id)
    else:
        _id = int(request.vars.id if request.vars.id is not None else 0)
        model = db_learningobjective.get_model(_id)

    if request.vars.scheme_of_work_id is not None:
        # required for creating a new object
        model.scheme_of_work_id = int(request.vars.scheme_of_work_id)
    if request.vars.learning_episode_id is not None:
        # required for creating a new object
        model.learning_episode_id = int(request.vars.learning_episode_id)
    if request.vars.topic_id is not None:
        model.topic_id = int(request.vars.topic_id)

    learning_episode = db_learningepisode.get_model(model.learning_episode_id)

    key_stage_id = db_schemeofwork.get_key_stage_id_only(model.scheme_of_work_id)
    solo_taxonomy_options = db_solotaxonomy.get_options()
    topic_options = db_topic.get_options(learning_episode.topic_id, learning_episode.parent_topic_id)
    content_options = db_content.get_options(key_stage_id)
    exam_board_options = db_examboard.get_options()

    parent_learning_objective_options = db_learningobjective.get_parent_options(current_key_stage_id = key_stage_id, topic_id = learning_episode.topic_id)

    content = {
        "main_heading":"Learning objective",
        "sub_heading": "for {} - Week {} - {}".format(learning_episode.scheme_of_work_name, learning_episode.order_of_delivery_id, learning_episode.topic_name),
        "strap_line":"Click save to add objective."
              }
    return dict(
        content = content,
        model = model,
        solo_taxonomy_options = solo_taxonomy_options,
        topic_options = topic_options,
        content_options = content_options,
        exam_board_options = exam_board_options,
        parent_learning_objective_options = parent_learning_objective_options
    )


@auth.requires_login()
def save_item():
    scheme_of_work_id = int(request.vars.scheme_of_work_id)
    learning_episode_id = int(request.vars.learning_episode_id)
    db_learningobjective.save(auth_user_id=auth.user.id,
                                id_ = request.vars.id,
                                description = request.vars.description,
                                solo_taxonomy_id = request.vars.solo_taxonomy_id,
                                topic_id = request.vars.topic_id,
                                content_id = request.vars.content_id,
                                exam_board_id = request.vars.exam_board_id,
                                parent_id = request.vars.parent_id,
                                learning_episode_id = request.vars.learning_episode_id)

    return redirect(URL('index', vars=dict(scheme_of_work_id = scheme_of_work_id, learning_episode_id = learning_episode_id)))


@auth.requires_login()
def add_existing_objective():
    learning_objective_id = int(request.vars.id)
    scheme_of_work_id = int(request.vars.scheme_of_work_id)
    learning_episode_id = int(request.vars.learning_episode_id)

    db_learningobjective.add_existing_objective(auth.user.id, id_=learning_objective_id, learning_episode_id=learning_episode_id)

    return redirect(URL('index', vars=dict(scheme_of_work_id = scheme_of_work_id, learning_episode_id = learning_episode_id)))


@auth.requires_login()
def delete_item():#
    id_ = int(request.vars.id)
    scheme_of_work_id = int(request.vars.scheme_of_work_id)
    learning_episode_id = int(request.vars.learning_episode_id)

    db_learningobjective.delete(auth.user.id, id_)

    return redirect(URL('index', vars=dict(scheme_of_work_id=scheme_of_work_id, learning_episode_id=learning_episode_id)))
