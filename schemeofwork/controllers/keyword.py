# -*- coding: utf-8 -*-
from cls_keyword import KeywordModel, get_by_id, get_by_terms, save, delete as db_delete
from pager import Pager

@auth.requires_login()
def index():

    content = {
        "main_heading":T("Key terms and definitions"),
        "sub_heading":T("Key terms and their definitions for all key stages"),
        "strap_line":""
              }

    return dict(content = content)


def _search_keywords():
    search_term = request.vars.s if request.vars.s is not None else ""

    data = get_by_terms(db, search_term, True)

    return dict(view_model = data)


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


@auth.requires_login()
def delete():

    id = int(request.vars.id)
    db_delete(db, id)

    return "definition deleted"

