# -*- coding: utf-8 -*-
from gluon.shell import exec_environment

learningobjectiveModel = exec_environment('applications/schemeofwork/models/learningobjectiveModel.py', request=request)
#learningepisodeModel = exec_environment('applications/schemeofwork/models/learningepisodeModel.py', request=request)
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
    order_of_delivery_name = learningepisiodeModel.get_order_of_delivery_name_only(learning_episode_id)

    data = learningobjectiveModel.get_all(learning_episode_id)

    learning_episode_options = learningepisiodeModel.get_options(scheme_of_work_id)

    content = {
        "main_heading":"Learning objectives",
        "sub_heading": "for {} ({})".format(scheme_of_work_name, order_of_delivery_name),
        "background_img":"home-bg.jpg"
              }

    return dict(
        content = content,
        model = data,
        scheme_of_work_id = scheme_of_work_id,
        learning_episode_id = learning_episode_id,
        learningepisiode_options = learning_episode_options
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


    key_stage_id = schemeofworkModel.get_key_stage_id_only(model.scheme_of_work_id)
    solo_taxonomy_options = solotaxonomyModel.get_options()
    topic_options = topicModel.get_options()
    content_options = contentModel.get_options(key_stage_id)
    exam_board_options = examboardModel.get_options()

    other_learning_objective_options = learningobjectiveModel.get_options(not_in_learning_episode = model.learning_episode_id, key_stage_id = key_stage_id)

    content = {
        "main_heading":"Learning objective",
        "sub_heading":model.description,
        "strap_line":"Click save to add objective."
              }
    return dict(
        content = content,
        model = model,
        solo_taxonomy_options = solo_taxonomy_options,
        topic_options = topic_options,
        content_options = content_options,
        exam_board_options = exam_board_options,
        other_learning_objective_options = other_learning_objective_options
    )


@auth.requires_login()
def save_item():
    scheme_of_work_id = int(request.vars.scheme_of_work_id)
    learning_episode_id = int(request.vars.learning_episode_id)
    learningobjectiveModel.save(auth.user.id, request.vars.description)

    return redirect(URL('index', vars=dict(scheme_of_work_id = scheme_of_work_id, learning_episode_id = learning_episode_id)))


@auth.requires_login()
def delete_item():
    scheme_of_work_id = int(request.vars.scheme_of_work_id)
    learning_episode_id = int(request.vars.learning_episode_id)

    learningobjectiveModel.delete(auth.user.id)

    return redirect(URL('index', vars=dict(scheme_of_work_id = scheme_of_work_id, learning_episode_id = learning_episode_id)))
