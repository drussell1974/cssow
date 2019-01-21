# -*- coding: utf-8 -*-
from datetime import datetime
from cls_learningepisode import LearningEpisodeModel
from pager import Pager
from validation_helper import html_validation_message
import db_schemeofwork
import db_learningepisode
import db_learningobjective
import db_topic
import db_keyword


def index():
    """ index action """
    scheme_of_work_id = int(request.args(0)) #int(request.vars.scheme_of_work_id)

    scheme_of_work_name = db_schemeofwork.get_schemeofwork_name_only(db, scheme_of_work_id)

    page_to_display = int(request.vars.page if request.vars.page is not None else 1)

    data = db_learningepisode.get_all(db, scheme_of_work_id, auth.user_id)
    schemeofwork_options = db_schemeofwork.get_options(db,  auth_user=auth.user_id)
    # page the data
    pager = Pager(page = page_to_display, page_size = 10, data = data)

    pager_html = pager.render_html(URL('learningepisode', 'index', args=[scheme_of_work_id]))
    data = pager.data_to_display()

    content = {
        "main_heading":T("learning episodes"),
        "sub_heading": T("for {}").format(scheme_of_work_name),
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


@auth.requires_login()
def edit():
    """ edit action """
    id_ = int(request.vars.id if request.vars.id is not None else 0)

    model = db_learningepisode.get_model(db, id_, auth.user_id)
    if request.vars.scheme_of_work_id is not None:
        # required for creating a new object
        model.scheme_of_work_id = int(request.vars.scheme_of_work_id)
        model.scheme_of_work_name = db_schemeofwork.get_schemeofwork_name_only(db, model.scheme_of_work_id)


    key_stage_id = db_schemeofwork.get_key_stage_id_only(db, model.scheme_of_work_id)
    model.key_stage_id = key_stage_id

    topic_options = db_topic.get_options(db, lvl=1)

    has_objectives = False
    for item in db_learningepisode.get_related_topic_ids(db, model.id, model.topic_id):
        if item["disabled"] == True:
            has_objectives = True
            break

    content = {
        "main_heading":T("learning episode"),
        "sub_heading":T("for {scheme_of_work_name} {topic_name} - Week {order_of_delivery_id}").format(scheme_of_work_name=model.scheme_of_work_name, topic_name=model.topic_name, order_of_delivery_id=model.order_of_delivery_id),
        "strap_line":T("{topic_name} - Week {order_of_delivery_id}\n{summary}").format(scheme_of_work_name=model.scheme_of_work_name, topic_name=model.topic_name, order_of_delivery_id=model.order_of_delivery_id, summary=model.summary)
              }

    return dict(content = content, model = model, topic_options = topic_options, has_objectives = has_objectives, topic_id = model.topic_id)


@auth.requires_login()
def save_item():
    """ save_item non-view action """

    published = int(request.vars.published if request.vars.published is not None else 1)


    model = LearningEpisodeModel(
        id_ = request.vars.id,
        order_of_delivery_id = request.vars.order_of_delivery_id,
        scheme_of_work_id = request.vars.scheme_of_work_id,
        topic_id = request.vars.topic_id,
        related_topic_ids = request.vars.related_topic_ids,
        key_stage_id= request.vars.key_stage_id,
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

    print("save_item:pathway_objective_ids={}".format(model.pathway_objective_ids))

    model.validate()

    if model.is_valid == True:

        ' save the learning episode '
        model = db_learningepisode.save(db, model, published)
        ' save keywords '
        db_keyword.save(db, model.key_words.split(','), model.topic_id)

    else:
        """ redirect back to page and show message """
        session.alert_message = html_validation_message(model.validation_errors) #model.validation_errors
        if request.env.http_referer:
            redirect(request.env.http_referer)


    ' if the request.vars.id was 0 then this is a new scheme of work '
    ' the user should be take create learning episodes '
    redirect_to_url = ""
    if int(request.vars.id) == 0:
        redirect_to_url = URL('learningobjective', 'index', args=[request.vars.scheme_of_work_id, model.id])
    else:
        redirect_to_url = URL('learningepisode', 'index', args=[request.vars.scheme_of_work_id])

    return redirect(redirect_to_url)


@auth.requires_login()
def delete_item():
    """ delete_item non-view action """

    id_ = int(request.vars.id)
    scheme_of_work_id = int(request.vars.scheme_of_work_id)

    db_learningepisode.delete(db, auth.user.id, id_)

    return redirect(URL('index', args=[scheme_of_work_id]))


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


