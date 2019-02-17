# -*- coding: utf-8 -*-
from datetime import datetime
from cls_learningepisode import LearningEpisodeModel
from pager import Pager
from validation_helper import html_validation_message
import db_keyword
import db_ks123pathway
import db_learningepisode
import db_learningobjective
import db_reference
import db_schemeofwork
import db_topic
import db_year


def index():
    """ index action """
    scheme_of_work_id = int(request.args(0))
    scheme_of_work_name = db_schemeofwork.get_schemeofwork_name_only(db, scheme_of_work_id)

    page_to_display = int(request.vars.page if request.vars.page is not None else 1)

    data = db_learningepisode.get_all(db, scheme_of_work_id, auth.user_id)
    schemeofwork_options = db_schemeofwork.get_options(db,  auth_user=auth.user_id)

    # page the data
    pager = Pager(page = page_to_display, page_size = 10, data = data)

    pager_html = pager.render_html(URL('learningepisode', 'index', args=[scheme_of_work_id]))
    data = pager.data_to_display()

    content = {
        "main_heading":T("Lessons"),
        "sub_heading": T("{}").format(scheme_of_work_name),
        "strap_line":None,
        "background_img":"home-bg.jpg"
              }

    return dict(content = content,
                model = data,
                scheme_of_work_id = scheme_of_work_id,
                schemeofwork_options = schemeofwork_options,
                page = page_to_display,
                pager_html = pager_html)


def _view_pathway_objectives():
    learning_episode_id = 0 if request.vars.learning_episode_id  is None else request.vars.learning_episode_id
    key_stage_id = 0 if request.vars.key_stage_id is None else request.vars.key_stage_id
    key_words = "" if request.vars.keywords is None else request.vars.keywords

    data = db_learningobjective.get_all_pathway_objectives(db, key_stage_id = key_stage_id, key_words = key_words)
    should_be_checked = db_learningepisode.get_pathway_objective_ids(db, learning_episode_id)

    return dict(data=data, should_be_checked=should_be_checked)


def _view_pathway_objectives_readonly():
    learning_episode_id = 0 if request.vars.learning_episode_id  is None else request.vars.learning_episode_id

    data = db_learningobjective.get_linked_pathway_objectives(db, learning_episode_id = learning_episode_id)

    return dict(data=data)


def _view_pathway_ks123():
    learning_episode_id = 0 if request.vars.learning_episode_id  is None else request.vars.learning_episode_id
    year_id = 0 if request.vars.year_id is None else request.vars.year_id
    topic_id = 0 if request.vars.topic_id is None else request.vars.topic_id

    data = db_ks123pathway.get_options(db, year_id = year_id, topic_id = topic_id)
    should_be_checked = db_ks123pathway.get_linked_pathway_ks123(db, learning_episode_id)

    view_model = []
    for item in data:
        for check in should_be_checked:
            if item.id == check[0]:
                item.is_checked = True
            else:
                item.is_checked = False

        view_model.append(item)

    return dict(view_model=view_model)


def _view_pathway_ks123_readonly():
    learning_episode_id = 0 if request.vars.learning_episode_id  is None else request.vars.learning_episode_id

    data = db_ks123pathway.get_linked_pathway_ks123(db, learning_episode_id = learning_episode_id)

    return dict(data=data)


@auth.requires_login()
def edit():
    """ edit action """
    id_ = int(request.vars.id if request.vars.id is not None else 0)
    duplicate = int(request.vars.duplicate if request.vars.duplicate is not None else 0)

    model = db_learningepisode.get_model(db, id_, auth.user_id)

    if request.vars.scheme_of_work_id is not None:
        # required for creating a new object
        model.scheme_of_work_id = int(request.vars.scheme_of_work_id)
        model.scheme_of_work_name = db_schemeofwork.get_schemeofwork_name_only(db, model.scheme_of_work_id)


    key_stage_id = db_schemeofwork.get_key_stage_id_only(db, model.scheme_of_work_id)
    model.key_stage_id = key_stage_id

    year_options = db_year.get_options(db, key_stage_id)

    topic_options = db_topic.get_options(db, lvl=1)

    has_objectives = False
    for item in db_learningepisode.get_related_topic_ids(db, model.id, model.topic_id):
        if item["disabled"] == True:
            has_objectives = True
            break


    ' reset id to zero if a copy '
    if duplicate == 1:
        model.copy()

    content = {
        "main_heading":T("Lesson"),
        "sub_heading":T("{scheme_of_work_name} {topic_name} - Lesson {order_of_delivery_id}").format(scheme_of_work_name=model.scheme_of_work_name, topic_name=model.topic_name, order_of_delivery_id=model.order_of_delivery_id),
        "strap_line":T("{topic_name} - Lesson {order_of_delivery_id}\n{summary}").format(scheme_of_work_name=model.scheme_of_work_name, topic_name=model.topic_name, order_of_delivery_id=model.order_of_delivery_id, summary=model.summary)
              }

    return dict(content = content, model = model, topic_options = topic_options, year_options = year_options, has_objectives = has_objectives, topic_id = model.topic_id)


@auth.requires_login()
def save_item():
    """ save_item non-view action """

    published = int(request.vars.published if request.vars.published is not None else 1)


    model = LearningEpisodeModel(
        id_ = request.vars.id,
        orig_id = int(request.vars.orig_id),
        title = request.vars.title,
        order_of_delivery_id = request.vars.order_of_delivery_id,
        scheme_of_work_id = request.vars.scheme_of_work_id,
        topic_id = request.vars.topic_id,
        related_topic_ids = request.vars.related_topic_ids,
        key_stage_id= request.vars.key_stage_id,
        year_id = request.vars.year_id,
        key_words = request.vars.key_words,
        summary = request.vars.summary,
        created = datetime.now(),
        created_by_id = auth.user.id
    )



    # ensure pathway_objective_ids is assigned as a list
    if type(request.vars.pathway_objective_ids) is str:
        model.pathway_objective_ids = []
        model.pathway_objective_ids.append(request.vars.pathway_objective_ids)
    else:
        model.pathway_objective_ids = request.vars.pathway_objective_ids

    # ensure pathway_ks123_ids is assigned as a list
    if type(request.vars.pathway_ks123_ids) is str:
        model.pathway_ks123_ids = []
        model.pathway_ks123_ids.append(request.vars.pathway_ks123_ids)
    else:
        model.pathway_ks123_ids = request.vars.pathway_ks123_ids


    # reset id if a copy
    if int(request.vars.orig_id) > 0:
        model.id = 0

    model.validate()

    if model.is_valid == True:

        ' save the lesson '
        model = db_learningepisode.save(db, model, published)

        ' save keywords '
        db_keyword.save(db, model.key_words.split(','), model.topic_id)

    else:
        """ redirect back to page and show message """
        session.alert_message = html_validation_message(model.validation_errors) #model.validation_errors
        if request.env.http_referer:
            redirect(request.env.http_referer)


    ' redirect if necessary '
    redirect_to_url = ""
    if request.vars._next != "None"  and request.vars._next != "":
        redirect_to_url = request.vars._next
    else:
        redirect_to_url = URL('learningobjective', 'index', args=[request.vars.scheme_of_work_id, model.id])

    return redirect(redirect_to_url)


@auth.requires_login()
def delete_item():
    """ delete_item non-view action """

    id_ = int(request.vars.id)
    scheme_of_work_id = int(request.vars.scheme_of_work_id)

    db_learningepisode.delete(db, auth.user.id, id_)

    return redirect(URL('index', args=[scheme_of_work_id]))


@auth.requires_login()
def publish_item():
    """ delete_item non-view action """

    id_ = int(request.vars.id)
    _next = request.vars._next
    db_learningepisode.publish(db, auth_user_id=auth.user.id, id_ = id_)
    return redirect(_next)


def get_related_topics():
    """ returns topics as json """
    ' get the topic_id from the url'
    learning_episode_id = int(request.args(0))
    parent_topic_id = int(request.args(1))

    topics = db_learningepisode.get_related_topic_ids(db, learning_episode_id=learning_episode_id, parent_topic_id=parent_topic_id)

    import gluon.contrib.simplejson
    return gluon.contrib.simplejson.dumps(topics)


def _view_learning_episiode_menu():

    scheme_of_work_id = int(request.args(0))
    learning_episode_id = int(request.args(1))
    topic_id = int(request.args(2))

    view_model = db_learningepisode.get_options(db, scheme_of_work_id, auth.user_id)  #TODO: create view_learningepisiode_options: remove this line

    return dict(view_model=view_model, learning_episode_id=learning_episode_id, topic_id=topic_id)


