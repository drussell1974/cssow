# -*- coding: utf-8 -*-
from gluon.shell import exec_environment

learningobjectiveModel = exec_environment('applications/schemeofwork/models/learningobjectiveModel.py', request=request)
schemeofworkModel = exec_environment('applications/schemeofwork/models/schemeofworkModel.py', request=request)
solotaxonomyModel = exec_environment('applications/schemeofwork/models/solotaxonomyModel.py')
topicModel = exec_environment('applications/schemeofwork/models/topicModel.py')
contentModel = exec_environment('applications/schemeofwork/models/contentModel.py')
examboardModel = exec_environment('applications/schemeofwork/models/examboardModel.py')
learningepisiodeModel = exec_environment('applications/schemeofwork/models/learningepisodeModel.py')

def index():
    scheme_of_work_id = int(request.vars.scheme_of_work_id)
    learning_episode_id = int(request.vars.learning_episode_id)

    scheme_of_work_name = schemeofworkModel.get_schemeofwork_name_only()
    learning_episode = learningepisiodeModel.get_model(learning_episode_id)
    data = learningobjectiveModel.get_all(learning_episode_id)

    learning_episode_options = learningepisiodeModel.get_options(scheme_of_work_id)

    unassociated_learning_objectives = learningobjectiveModel.get_unassociated_learning_objectives(
        learning_episode_id=learning_episode.id,
        key_stage_id=learning_episode.key_stage_id,
        topic_id=learning_episode.topic_id)

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
        model = learningobjectiveModel.get_new_model(_id)
    else:
        _id = int(request.vars.id if request.vars.id is not None else 0)
        model = learningobjectiveModel.get_model(_id)

    if request.vars.scheme_of_work_id is not None:
        # required for creating a new object
        model.scheme_of_work_id = int(request.vars.scheme_of_work_id)
    if request.vars.learning_episode_id is not None:
        # required for creating a new object
        model.learning_episode_id = int(request.vars.learning_episode_id)
    if request.vars.topic_id is not None:
        model.topic_id = int(request.vars.topic_id)

    learning_episode = learningepisiodeModel.get_model(model.learning_episode_id)

    key_stage_id = schemeofworkModel.get_key_stage_id_only(model.scheme_of_work_id)
    solo_taxonomy_options = solotaxonomyModel.get_options()
    topic_options = topicModel.get_options(learning_episode.parent_topic_id)
    content_options = contentModel.get_options(key_stage_id)
    exam_board_options = examboardModel.get_options()

    parent_learning_objective_options = learningobjectiveModel.get_parent_options(current_key_stage_id = key_stage_id, topic_id = learning_episode.topic_id)

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
    learningobjectiveModel.save(auth.user.id, request.vars.description)

    return redirect(URL('index', vars=dict(scheme_of_work_id = scheme_of_work_id, learning_episode_id = learning_episode_id)))


@auth.requires_login()
def add_existing_objective():
    learning_objective_id = int(request.vars.id)
    scheme_of_work_id = int(request.vars.scheme_of_work_id)
    learning_episode_id = int(request.vars.learning_episode_id)

    learningobjectiveModel.add_existing_objective(auth.user.id, id_=learning_objective_id, learning_episode_id=learning_episode_id)

    return redirect(URL('index', vars=dict(scheme_of_work_id = scheme_of_work_id, learning_episode_id = learning_episode_id)))


@auth.requires_login()
def delete_item():#
    id_ = int(request.vars.id)
    scheme_of_work_id = int(request.vars.scheme_of_work_id)
    learning_episode_id = int(request.vars.learning_episode_id)

    learningobjectiveModel.delete(auth.user.id, id_)

    return redirect(URL('index', vars=dict(scheme_of_work_id=scheme_of_work_id, learning_episode_id=learning_episode_id)))
