# -*- coding: utf-8 -*-
from datetime import datetime
from cls_learningobjective import LearningObjectiveModel, sort_by_solo_taxonomy_level
from pager import Pager
from validation_helper import html_validation_message
import db_schemeofwork
import db_learningobjective
import db_solotaxonomy
import db_topic
import db_content
import db_examboard
import db_learningepisode
import db_keyword

def index():
    """ index action """

    # TODO: ensure correct number of args are passed

    scheme_of_work_id = int(request.args(0))
    learning_episode_id = int(request.args(1))

    page_to_display = int(request.vars.page if request.vars.page is not None else 1)

    scheme_of_work_name = db_schemeofwork.get_schemeofwork_name_only(db, scheme_of_work_id)
    learning_episode = db_learningepisode.get_model(db, learning_episode_id, auth.user_id)
    data = db_learningobjective.get_all(db, learning_episode_id, auth.user_id)

    # bubble sort by solo
    sorted_data = data

    while True:
        swapped = False
        for i in range(len(sorted_data)-1):
            if sorted_data[i].solo_taxonomy_level > sorted_data[i+1].solo_taxonomy_level:
                """ put item in the correct position """
                temp1 = sorted_data[i]
                temp2 = sorted_data[i+1]

                sorted_data[i] = temp2
                sorted_data[i+1] = temp1
                swapped = True

        if swapped == False:
            """ no more sorting required so finish """
            break

    # page the data
    pager = Pager(page = page_to_display, page_size = 10, data = sorted_data)

    learning_episode_options = db_learningepisode.get_options(db, scheme_of_work_id, auth.user_id)  #TODO: create view_learningepisiode_options: remove this line

    pager_html = pager.render_html(URL('learningobjective', 'index', args=[scheme_of_work_id, learning_episode_id]))
    paged_data = pager.data_to_display()

    content = {
        "main_heading":T("learning objectives"),
        "sub_heading":T("for {scheme_of_work_name} - Week {order_of_delivery_id} - {topic_name}").format(scheme_of_work_name=scheme_of_work_name, order_of_delivery_id=learning_episode.order_of_delivery_id, topic_name=learning_episode.topic_name),
        "background_img":"home-bg.jpg",
        "strap_line": T("{scheme_of_work_name} - Week {order_of_delivery_id} - {topic_name}\n{summary}").format(scheme_of_work_name=scheme_of_work_name, order_of_delivery_id=learning_episode.order_of_delivery_id, topic_name=learning_episode.topic_name, summary=learning_episode.summary)
              }

    return dict(
        content = content,
        model = paged_data,
        scheme_of_work_id = scheme_of_work_id,
        topic_id = learning_episode.topic_id,
        learning_episode_id = learning_episode_id,
        learningepisiode_options = learning_episode_options, #TODO: create view_learningepisiode_options: remove this line
        page = page_to_display,
        pager_html = pager_html)


@auth.requires_login()
def edit():
    """ edit action """

    model = None
    # check if an existing_learning_objective_id has been passed
    if request.vars.learning_objective_id is not None:
        _id = int(request.vars.learning_objective_id if request.vars.learning_objective_id is not None else 0)
        model = db_learningobjective.get_new_model(db, _id, auth.user_id)
    else:
        _id = int(request.vars.id if request.vars.id is not None else 0)
        model = db_learningobjective.get_model(db, _id, auth.user_id)

    if request.vars.scheme_of_work_id is not None:
        # required for creating a new object
        model.scheme_of_work_id = int(request.vars.scheme_of_work_id)
    if request.vars.learning_episode_id is not None:
        # required for creating a new object
        model.learning_episode_id = int(request.vars.learning_episode_id)
    if request.vars.topic_id is not None:
        model.topic_id = int(request.vars.topic_id)

    learning_episode = db_learningepisode.get_model(db, model.learning_episode_id, auth.user_id)
    key_stage_id = db_schemeofwork.get_key_stage_id_only(db, int(request.vars.scheme_of_work_id))

    model.learning_episode_id = learning_episode.id
    model.key_stage_id = key_stage_id

    solo_taxonomy_options = db_solotaxonomy.get_options(db)
    topic_options = []
    for item in db_learningepisode.get_related_topic_ids(db, learning_episode.id, learning_episode.topic_id):
        if item["checked"] == True:
            topic_options.append(item)

    content_options = db_content.get_options(db, key_stage_id)
    exam_board_options = db_examboard.get_options(db)

    content = {
        "main_heading":T("learning objective"),
        "sub_heading":T("for {} - Week {} - {}").format(learning_episode.scheme_of_work_name, learning_episode.order_of_delivery_id, learning_episode.topic_name),
        "strap_line":T("fill out the form below then click save")
              }
    return dict(
        content = content,
        model = model,
        solo_taxonomy_options = solo_taxonomy_options,
        topic_options = topic_options,
        content_options = content_options,
        exam_board_options = exam_board_options,
        main_topic_id=learning_episode.topic_id
    )


@auth.requires_login()
def save_item():
    """ save_item non-view action """
    published = int(request.vars.published if request.vars.published is not None else 1)

    scheme_of_work_id = int(request.vars.scheme_of_work_id)
    learning_episode_id = int(request.vars.learning_episode_id)
    main_topic_id = int(request.vars.main_topic_id)

    # create instance of model from request.vars

    model = LearningObjectiveModel(
        id_=request.vars.id,
        description=request.vars.description,
        solo_taxonomy_id=request.vars.solo_taxonomy_id,
        topic_id=request.vars.topic_id,
        content_id=request.vars.content_id,
        exam_board_id=request.vars.exam_board_id,
        key_stage_id=request.vars.key_stage_id,
        parent_id=request.vars.parent_id,
        learning_episode_id=request.vars.learning_episode_id,
        key_words = request.vars.key_words,
        notes = request.vars.notes,
        created=datetime.now(),
        created_by_id=auth.user.id
    )

    # validate the model and save if valid otherwise redirect to default invalid

    model.validate()
    if model.is_valid == True:
        ' save learning objectives'
        model = db_learningobjective.save(db, model, published)
        ' save keywords '
        db_keyword.save(db, model.key_words.split(','), main_topic_id)
    else:
        """ redirect back to page and show message """
        session.alert_message = html_validation_message(model.validation_errors) #model.validation_errors
        if request.env.http_referer:
            redirect(request.env.http_referer)

    return redirect(URL('index', args=[scheme_of_work_id, learning_episode_id]))


@auth.requires_login()
def add_existing_objective():
    """ add objective non-view action """

    learning_objective_id = int(request.vars.id)
    scheme_of_work_id = int(request.vars.scheme_of_work_id)
    learning_episode_id = int(request.vars.learning_episode_id)

    db_learningobjective.add_existing_objective(db, auth.user.id, id_=learning_objective_id, learning_episode_id=learning_episode_id)

    return redirect(URL('index', args=[scheme_of_work_id, learning_episode_id]))


@auth.requires_login()
def delete_item():
    """ delete_item non-view action """

    id_ = int(request.vars.id)
    scheme_of_work_id = int(request.vars.scheme_of_work_id)
    learning_episode_id = int(request.vars.learning_episode_id)

    db_learningobjective.delete(db, auth.user.id, id_)

    return redirect(URL('index', args=[scheme_of_work_id, learning_episode_id]))


