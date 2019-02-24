# -*- coding: utf-8 -*-
# try something like
from datetime import datetime
from cls_reference import ReferenceModel
from cls_reference_note import ReferenceNoteModel
from helper_string import to_cs_string
from pager import Pager
from validation_helper import html_validation_message
import db_reference, db_schemeofwork, db_reference_type

def index():
    """ index action """
    scheme_of_work_id = int(request.args(0))

    data = db_reference.get_scheme_of_work_options(db, scheme_of_work_id, auth.user_id)
    page_to_display = int(request.vars.page if request.vars.page is not None else 1)

    # page the data
    pager = Pager(page = page_to_display, page_size = 10, data = data)

    pager_html = pager.render_html(URL('reference', 'index'))
    data = pager.data_to_display()

    content = {
        "main_heading":T("Learning materials"),
        "sub_heading": T("List of learning materials"),
        "strap_line":None,
        "background_img":"home-bg.jpg"
              }

    return dict(content = content,
                model = data,
                page = page_to_display,
                pager_html = pager_html)


@auth.requires_login()
def edit():
    """ edit action """
    id_ = int(request.vars.id if request.vars.id is not None else 0)
    scheme_of_work_id = request.vars.scheme_of_work_id
    scheme_of_work_name = db_schemeofwork.get_schemeofwork_name_only(db, scheme_of_work_id)

    model = db_reference.get_model(db, id_, scheme_of_work_id=scheme_of_work_id, auth_user=auth.user_id)
    reference_type_options = db_reference_type.get_options(db)

    sub_heading = ""
    if model.is_new():
        sub_heading = T("Text book, Website or Video for {scheme_of_work_name}".format(scheme_of_work_name=scheme_of_work_name))
    else:
        sub_heading = T("{title} from {publisher} for {scheme_of_work_name}").format(title=model.title, publisher=model.publisher, scheme_of_work_name=scheme_of_work_name)

    content = {
        "main_heading":T("Learning materials"),
        "sub_heading":sub_heading,
        "strap_line":None
    }

    return dict(content = content, model = model, reference_type_options = reference_type_options)


@auth.requires_login()
def save_item():
    """ save_item non-view action """

    model = ReferenceModel(
        id_ = request.vars.id,
        reference_type_id = request.vars.reference_type_id,
        title = request.vars.title,
        authors = request.vars.authors,
        publisher = request.vars.publisher,
        year_published = request.vars.year_published,
        uri = request.vars.uri,
        created = datetime.now(),
        created_by_id = auth.user.id,
        scheme_of_work_id = request.vars.scheme_of_work_id
    )

    model.validate()

    if model.is_valid == True:
        """ save the lesson """
        db_reference.save(db, model)

    else:
        """ redirect back to page and show message """
        session.alert_message = html_validation_message(model.validation_errors) #model.validation_errors
        if request.env.http_referer:
            redirect(request.env.http_referer)


    ' redirect if necessary '
    redirect_to_url = ""
    if request.vars._next is not None:
        redirect_to_url = request.vars._next
    else:
        redirect_to_url = URL('reference', 'index')

    return redirect(redirect_to_url)


@auth.requires_login()
def delete_item():
    """ delete_item non-view action """

    id_ = int(request.vars.id)
    scheme_of_work_id = int(request.vars.scheme_of_work_id)

    db_reference.delete(db, id_)

    return redirect(request.vars._next)


@auth.requires_login()
def save_page_note():
    page_id = request.vars.page_id
    page_note = request.vars.page_note
    page_uri = request.vars.page_uri

    task_icon = to_cs_string(request.vars.group_task_icon,
                        request.vars.individual_task_icon,
                        request.vars.hands_up_task_icon,
                        request.vars.discussion_task_icon,
                        request.vars.listening_task_icon,
                        request.vars.reading_task_icon,
                        request.vars.watching_task_icon,
                        request.vars.question_task_icon,
                        request.vars.research_task_icon)

    learning_episode_id = request.vars.learning_episode_id
    reference_id = int(request.vars.reference_id)

    model = ReferenceNoteModel(page_id, reference_id=reference_id, learning_episode_id=learning_episode_id, page_note=page_note, page_uri=page_uri, task_icon = task_icon)

    model.validate()

    if model.is_valid == True:
        if model.is_new():
            db_reference.insert_page_note(db, model)
        else:
            db_reference.update_page_note(db, model)
    else:
        return model.validation_errors

    return "saved"


@auth.requires_login()
def delete_page_note():
    id = request.vars.id

    db_reference.delete_page_note(db, id)

    return "deleted"


def _view_scheme_of_work_references():
    scheme_of_work_id = int(request.vars.scheme_of_work_id)

    view_model = db_reference.get_options(db, scheme_of_work_id, auth.user_id)

    return dict(view_model=view_model)


def _view_learning_episode_references():
    scheme_of_work_id = int(request.vars.scheme_of_work_id)
    learning_episode_id = int(request.vars.learning_episode_id)

    view_model = db_reference.get_learning_episode_options(db, scheme_of_work_id, learning_episode_id, auth.user_id)

    return dict(view_model=view_model, learning_episode_id = learning_episode_id)

"""
def _edit_learning_episode_references():
    scheme_of_work_id = int(request.vars.scheme_of_work_id)
    learning_episode_id = int(request.vars.learning_episode_id)

    view_model = db_reference.get_learning_episode_options(db, scheme_of_work_id, learning_episode_id, auth.user_id)

    return dict(view_model=view_model)
"""
