# -*- coding: utf-8 -*-
from db_keyword import KeywordModel, get_by_id, get_all, save
from pager import Pager

@auth.requires_login()
def index():

    page_to_display = int(request.vars.page if request.vars.page is not None else 1)

    # TODO: get keywords
    data = get_all(db)

    # page the data
    pager = Pager(page = page_to_display, page_size = 10, data = data)

    pager_html = pager.render_html(URL('keyword', 'index'))
    data = pager.data_to_display()

    content = {
        "main_heading":T("Key terms and definitions"),
        "sub_heading":T("Key terms and their definitions for all key stages"),
        "strap_line":""
              }

    return dict(content = content, pager_html = pager_html, view_model = data)


@auth.requires_login()
def get():
    keyword_id = int(request.vars.id)
    keyword = get_by_id(db, keyword_id)

    definition = dict(
        val = "",
        found = False
    )

    if keyword.id == keyword_id:
        definition = dict(
            val = keyword.definition,
            found = True
        )

    import gluon.contrib.simplejson
    return gluon.contrib.simplejson.dumps(definition)


@auth.requires_login()
def update():

    model = KeywordModel(
        id_ = int(request.vars.id),
        term = request.vars.term,
        definition = request.vars.definition
    )

    # validate the model and save if valid otherwise redirect to default invalid

    model.validate()
    if model.is_valid == True:
        ' save keywords '
        save(db, model)
    else:
        raise Exception(model.validation_errors) #model.validation_errors

    return "definition updated"

