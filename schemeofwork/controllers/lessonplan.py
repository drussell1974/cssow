import cls_learningepisode
import cls_learningobjective
import cls_schemeofwork
from cls_lessonplan import LessonPlanModel, get_model, get_all, save, delete, update_order_of_delivery, get_last_item
from helper_sort_and_search import _sort_by_solo_and_group

@auth.requires_login()
def index():
    """ index action """

    scheme_of_work_id = int(request.vars.scheme_of_work_id)
    learning_episode_id = int(request.vars.learning_episode_id)

    scheme_of_work_name = cls_schemeofwork.get_schemeofwork_name_only(db, scheme_of_work_id)
    learning_episode = cls_learningepisode.get_model(db, learning_episode_id, auth.user_id)
    topic_id = learning_episode.topic_id

    learning_objectives = cls_learningobjective.get_key_objectives(db, learning_episode_id, auth.user_id)
    learning_objectives = _sort_by_solo_and_group(learning_objectives)

    content = {
        "main_heading":learning_episode.title,
        "sub_heading":learning_episode.summary,
        "strap_line":T("{scheme_of_work_name} - Lesson {order_of_delivery_id}").format(scheme_of_work_name=scheme_of_work_name, order_of_delivery_id=learning_episode.order_of_delivery_id)
              }

    return dict(
        content = content,
        learning_episode_id = learning_episode_id,
        scheme_of_work_id = scheme_of_work_id,
        topic_id = topic_id,
        learning_objectives = learning_objectives)


@auth.requires_login()
def _view_lesson_plan():
    learning_episode_id = int(request.vars.learning_episode_id)

    model, lesson_duration_h, lesson_duration_m = get_all(db, learning_episode_id, auth.user_id)

    return dict(view_model=model, learning_episode_id=learning_episode_id, lesson_duration_h=lesson_duration_h, lesson_duration_m = lesson_duration_m)


@auth.requires_login()
def _edit_lesson_plan():
    id = int(request.vars.id)
    learning_episode_id = int(request.vars.learning_episode_id)

    model = get_model(db, id, learning_episode_id, auth.user_id)

    return dict(view_model=model)


@auth.requires_login()
def save_item():

    id = int(request.vars.id)
    learning_episode_id = int(request.vars.learning_episode_id)
    order_of_delivery_id = int(request.vars.order_of_delivery_id)
    title = request.vars.title
    description = request.vars.description
    task_icon = request.vars.task_icon
    duration = int(request.vars.duration)

    model = LessonPlanModel(id_=id, learning_episode_id=learning_episode_id, order_of_delivery_id=order_of_delivery_id, title=title, description=description, duration=duration, task_icon=task_icon)

    # increment the order of delivery id if set to 0
    if model.order_of_delivery_id == 0:
        # get the last item to find the last order of delivery
        last_item = get_last_item(db, model.learning_episode_id)
        model.order_of_delivery_id = last_item.order_of_delivery_id + 1

    save(db, model)

    return None


@auth.requires_login()
def order_item():
    """ delete_item non-view action """

    id_ = int(request.vars.id)
    order_of_delivery_id = int(request.vars.order_of_delivery_id)
    learning_episode_id = int(request.vars.learning_episode_id)

    update_order_of_delivery(db, id_, learning_episode_id, order_of_delivery_id)

    return None


@auth.requires_login()
def delete_item():
    """ delete_item non-view action """

    id_ = int(request.vars.id)

    delete(db, auth.user.id, id_)

    return None
