# -*- coding: utf-8 -*-
from basemodel import BaseModel, try_int
from db_helper import sql_safe

class LessonPlanModel (BaseModel):

    def __init__(self, id_, lesson_id, title, description, order_of_delivery_id = 0, duration = 0, task_icon = ""):
        self.id = int(id_)
        self.lesson_id = lesson_id
        self.title = title
        self.description = description
        self.order_of_delivery_id = order_of_delivery_id
        self.duration = duration
        self.task_icon = task_icon


    def validate(self):
        """ clean up and validate model """

        self._on_before_validate()

        # clean properties before validation
        self._clean_up()

        # validate title
        self._validate_required_string("title", self.title, 1, 40)

        # validate description
        self._validate_required_string("description", self.description, 1, 1000)

        # validate task_icon
        self._validate_optional_string("task_icon", self.task_icon, 500)

        # validate order_of_delivery_id
        if self.order_of_delivery_id is None or self.order_of_delivery_id < 1 or self.order_of_delivery_id > 9999:
            self.validation_errors["order_of_delivery_id"] = "{} is not a valid selection".format(self.order_of_delivery_id)
            self.is_valid = False


    def _clean_up(self):
        """ clean up properties by casting and ensuring safe for inserting etc """

        self.id = int(self.id)

        # trim title
        if self.title is not None:
            self.title = sql_safe(self.title)

        # trim description
        if self.description is not None:
            self.description = sql_safe(self.description)

        # trim task_icon
        if self.task_icon is not None:
            self.task_icon = sql_safe(self.task_icon)


"""
DAL
"""
from datetime import datetime
from db_helper import to_db_null, to_empty

def get_all(db, lesson_id, auth_user):
    """
    Get all the lesson plan for this lesson
    :param db: database context
    :param lesson_id: the lesson
    :param auth_user: TODO: Use to only show the user who created the lesson plan the information
    :return: the lesson plan_model
    """

    str_select = "SELECT" \
                 " pln.id as id," \
                 " pln.title as title," \
                 " pln.description as description," \
                 " pln.duration_minutes as duration," \
                 " pln.task_icon, " \
                 " pln.order_of_delivery_id "\
                 "FROM sow_lesson_plan as pln " \
                 "INNER JOIN sow_lesson as le ON le.id = pln.lesson_id" \
                 " WHERE le.id = {lesson_id}" \
                 " ORDER BY pln.order_of_delivery_id;"

    str_select = str_select.format(lesson_id=int(lesson_id))

    rows = db.executesql(str_select)

    lesson_duration = 0
    data = []
    for row in rows:
        lesson_duration = lesson_duration + int(row[3])
        data.append(LessonPlanModel(id_=row[0], lesson_id=lesson_id, title=row[1], description=row[2], duration=row[3], task_icon=row[4], order_of_delivery_id=row[5]))

    lesson_duration_h = lesson_duration / 60
    lesson_duration_m = lesson_duration % 60

    return data, lesson_duration_h, lesson_duration_m


def get_model(db, id_, lesson_id, auth_user):
    model = LessonPlanModel(id_=id_, lesson_id=lesson_id, title="", description="")

    str_select = "SELECT" \
                 " pln.id as id," \
                 " pln.title as title," \
                 " pln.description as description," \
                 " pln.duration_minutes as duration," \
                 " pln.task_icon, " \
                 " pln.order_of_delivery_id "\
                 "FROM sow_lesson_plan as pln " \
                 "INNER JOIN sow_lesson as le ON le.id = pln.lesson_id" \
                 " WHERE pln.id = {id_} AND le.id = {lesson_id};"

    str_select = str_select.format(id_=int(id_), lesson_id=int(lesson_id))

    rows = db.executesql(str_select)

    for row in rows:
        model = LessonPlanModel(id_=row[0], lesson_id = lesson_id, title=row[1], description=row[2], duration=row[3], task_icon=row[4], order_of_delivery_id=row[5])

    return model


def get_last_item(db, lesson_id):
    model = LessonPlanModel(id_=0, lesson_id=lesson_id, title="", description="")

    str_select = "SELECT" \
                 " pln.id as id," \
                 " pln.title as title," \
                 " pln.description as description," \
                 " pln.duration_minutes as duration," \
                 " pln.task_icon, " \
                 " pln.order_of_delivery_id "\
                 "FROM sow_lesson_plan as pln " \
                 "INNER JOIN sow_lesson as le ON le.id = pln.lesson_id" \
                 " WHERE le.id = {lesson_id}" \
                 " ORDER BY pln.order_of_delivery_id DESC " \
                 " LIMIT 1;"

    str_select = str_select.format(lesson_id=int(lesson_id))

    rows = db.executesql(str_select)

    for row in rows:
        model = LessonPlanModel(id_=row[0], lesson_id = lesson_id, title=row[1], description=row[2], duration=row[3], task_icon=row[4], order_of_delivery_id=row[5])

    return model

def save(db, model):
    """
    Upsert the reference
    :param db: database context
    :param model: the LessonPlanModel
    :return: the updated LessonPlanModel
    """
    if model.is_new() == True:
        model.id = _insert(db, model)
    else:
        _update(db, model)

    return model


def delete(db, id_):
    """

    :param db: the database context
    :param id_: the id of the record to delete
    :return: nothing
    """
    _delete(db, id_);

"""
Private CRUD functions 
"""

def _update(db, model):
    """ updates the sow_lesson_plan """

    # Update the lesson plan step

    str_update = "UPDATE sow_lesson_plan SET lesson_id = {lesson_id}, order_of_delivery_id = {order_of_delivery_id}, title = '{title}', description = '{description}', duration_minutes = {duration}, task_icon = '{task_icon}' WHERE id = {id};"
    str_update = str_update.format(
        id=model.id,
        lesson_id=model.lesson_id,
        order_of_delivery_id=model.order_of_delivery_id,
        title=model.title,
        description=model.description,
        duration=model.duration,
        task_icon=model.task_icon)

    db.executesql(str_update)

    return True


def _insert(db, model):
    """ inserts the sow_reference and sow_scheme_of_work__has__reference """

    ## 1. Insert the reference

    str_insert = "INSERT INTO sow_lesson_plan (lesson_id, order_of_delivery_id, title, description, duration_minutes, task_icon) VALUES ({lesson_id}, {order_of_delivery_id}, '{title}', '{description}', {duration_minutes}, '{task_icon}')"
    str_insert = str_insert.format(
        id=model.id,
        lesson_id=model.lesson_id,
        order_of_delivery_id=model.order_of_delivery_id,
        title=model.title,
        description=model.description,
        duration_minutes=model.duration,
        task_icon=model.task_icon)

    db.executesql(str_insert)

    rows = db.executesql("SELECT LAST_INSERT_ID();")

    for row in rows:
        model.id = int(row[0])

    return model.id


def update_order_of_delivery(db, id_, lesson_id, order_of_delivery_id):

    """ updates the order of delivery for sow_lesson_plan """

    # Update the lesson plan step

    str_update = "UPDATE sow_lesson_plan SET order_of_delivery_id = {order_of_delivery_id} WHERE id = {id} AND lesson_id = {lesson_id};"
    str_update = str_update.format(
        id= id_,
        order_of_delivery_id=order_of_delivery_id,
        lesson_id=lesson_id
    )

    db.executesql(str_update)


def _delete(db, id_):
    str_delete = "DELETE FROM sow_lesson_plan WHERE id = {id_};"
    str_delete = str_delete.format(id_=int(id_))

    rval = db.executesql(str_delete)

    return rval
