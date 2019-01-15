# -*- coding: utf-8 -*-
from datetime import datetime
from cls_learningepisode import LearningEpisodeModel
from pager import Pager
import db_schemeofwork
import db_learningepisode
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
        "main_heading":"Learning episodes",
        "sub_heading": "for {}".format(scheme_of_work_name),
        "background_img":"home-bg.jpg"
              }

    return dict(content = content,
                model = data,
                scheme_of_work_id = scheme_of_work_id,
                schemeofwork_options = schemeofwork_options,
                page = page_to_display,
                pager_html = pager_html)


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

    topic_options = db_topic.get_options(db, model.topic_id, 1)

    content = {
        "main_heading":"Learning episode",
        "sub_heading":model.get_ui_sub_heading(),
        "strap_line":model.get_ui_title()
              }

    return dict(content = content, model = model, topic_options = topic_options, has_objectives = True, topic_id = model.topic_id)


@auth.requires_login()
def save_item():
    """ save_item non-view action """

    published = int(request.vars.published if request.vars.published is not None else 1)

    model = LearningEpisodeModel(
        id_ = request.vars.id,
        order_of_delivery_id = request.vars.order_of_delivery_id,
        scheme_of_work_id = request.vars.scheme_of_work_id,
        topic_id = request.vars.topic_id,
        key_stage_id= request.vars.key_stage_id,
        key_words = request.vars.key_words,
        summary = request.vars.summary,
        created = datetime.now(),
        created_by_id = auth.user.id
    )

    model.validate()
    if model.is_valid == True:

        ' save the learning episode '
        model = db_learningepisode.save(db, model, published)
        ' save keywords '
        db_keyword.save(db, model.key_words.split(','), model.topic_id)

    else:
        raise Exception("Validation errors:/n/n %s" % model.validation_errors) # TODO: redirect

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



