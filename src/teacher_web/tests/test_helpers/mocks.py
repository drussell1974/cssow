from datetime import datetime
from unittest.mock import Mock, MagicMock, patch
from shared.models.cls_academic_year import AcademicYearModel
from shared.models.cls_academic_year_period import AcademicYearPeriodModel
from shared.models.cls_department import DepartmentContextModel, DepartmentModel
from shared.models.cls_institute import InstituteContextModel, InstituteModel
from shared.models.cls_lesson_schedule import LessonScheduleModel
from shared.models.cls_teacher import TeacherModel
from shared.models.cls_teacher_permission import TeacherPermissionModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel, SchemeOfWorkContextModel
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON
from shared.models.core.context import AuthCtx, Ctx, AcademicYearCtx

def fake_institute(id=1276711):
    institute = InstituteModel(id, "Lorem Ipsum")
    institute.number_of_departments = 2
    institute.departments.append(fake_department(67, institute))
    institute.departments.append(fake_department(76, institute))
    
    return institute


def fake_department(id, institute):
    department = DepartmentModel(id, "Lorem Ipsum", topic_id=3, institute=institute)
    department.number_of_schemes_of_work = 3
    department.number_of_topics = 2
    department.number_of_pathways = 10

    return department


def mock_scheme_of_work(id=99, name="A-Level Computer Science", is_from_db=True, ctx=Ctx(1276711, 826)):
    return SchemeOfWorkModel(id, name=name, study_duration=1, start_study_in_year=12, is_from_db=is_from_db, auth_user=ctx)


def fake_lesson_schedule(id=1, title="Vivamus at porta orci", start_date="2021-04-09T10:00", class_name="7x", class_code="ABCDEF", lesson_id=34, scheme_of_work_id = 12, is_from_db=False, auth_ctx=Ctx(1276711, 826), fn_resolve_url=None):
    return LessonScheduleModel(id_=id, title=title, start_date=start_date, class_name=class_name, class_code=class_code, lesson_id=lesson_id, scheme_of_work_id=scheme_of_work_id, is_from_db=is_from_db, auth_user=auth_ctx, fn_resolve_url=fn_resolve_url)


def fake_academic_year(year=datetime.now().year):
    return AcademicYearModel.default(for_academic_year=year)


def fake_academic_years():
    return [
        #fake_academic_year()
    ]


def fake_academic_year_periods():
    return [
        AcademicYearPeriodModel("09:00", "Period 1", is_from_db=True).__dict__, 
        AcademicYearPeriodModel("10:00", "Period 2", is_from_db=True).__dict__, 
        AcademicYearPeriodModel("11:15", "Period 3", is_from_db=True).__dict__, 
    ]


def fake_resolve_schedule_urls(schedule):
    return "http://localhost/.../schemesofwork/11/lessons/220/whiteboard"


def fake_ctx_model(dep=DEPARTMENT.NONE, sow=SCHEMEOFWORK.NONE, les=LESSON.NONE, fake_request_user_id=6079):
    
    mock_request = MagicMock()
    mock_request.user = MagicMock(id=fake_request_user_id)
    mock_request.session = {
            "academic_year.start_date": datetime(year=2020, month=9, day=1),
            "academic_year.end_date": datetime(year=2021, month=7, day=15),
            "lesson_schedule.show_next_days":7,
    }
    
    mock_db = Mock()
    mock_db.cursor = MagicMock()
    
    with patch.object(InstituteContextModel, "get_context_model", return_value = InstituteContextModel(127671276711, name="Lorum Ipsum")) as institute:
        with patch.object(DepartmentContextModel, "get_context_model", return_value = DepartmentContextModel(67, name="Computer Science", topic_id=3, is_from_db=True)) as department:
            with patch.object(SchemeOfWorkContextModel, "get_context_model", return_value = SchemeOfWorkContextModel(67, name="Nunc maximus purus", is_from_db=True)) as scheme_of_work:
                with patch.object(AcademicYearModel, "get_model", return_value = fake_academic_year()) as academic_year:
                    with patch.object(AcademicYearModel, "get_all", return_value = fake_academic_years()) as academic_year:
                        with patch.object(AcademicYearPeriodModel, "get_all", return_value = fake_academic_year_periods()) as academic_year:
                        
                            institute.name = "Lorum Ipsum"
                            department.name = "Computer Science"
                            #academic_year__start_date = datetime(year=2020, month=9, day=1)
                            #academic_year__end_date = datetime(year=2021, month=7, day=14)

                            scheme_of_work = SchemeOfWorkContextModel(12323232, name="GCSE Computer Science", ctx=Ctx(1276711, 826))

                            auth_ctx = AuthCtx(mock_db, mock_request, institute_id=127671276711, department_id=67, scheme_of_work_id=scheme_of_work.id) #, start_date=academic_year__start_date, end_date=academic_year__end_date)
                            auth_ctx.institute = institute
                            auth_ctx.department = department
                            auth_ctx.scheme_of_work = scheme_of_work
                            auth_ctx.department_permission = dep
                            auth_ctx.scheme_of_work_permission = sow
                            auth_ctx.lesson_permission = les

                            auth_ctx.selected_year = academic_year.start_date.year
                            auth_ctx.academic_year = academic_year

    return auth_ctx


def fake_teacher_permission_model(is_from_db=True, is_authorised=True):

    mock_request = MagicMock()
    mock_request.user = MagicMock(id=6079)
    mock_request.session = {}

    mock_db = Mock()
    mock_db.cursor = MagicMock()
    
    #institute = InstituteContextModel(127671276711, name="Lorum Ipsum")
    
    #department = DepartmentContextModel(67, "Computer Science", is_from_db=True)

    with patch.object(InstituteContextModel, "get_context_model", return_value = InstituteContextModel(127671276711, name="Lorum Ipsum")) as institute:
        with patch.object(DepartmentContextModel, "get_context_model", return_value = DepartmentContextModel(67, name="Computer Science", topic_id=3, is_from_db=True)) as department:
            
            institute.get = MagicMock(return_value="Lorum Ipsum")
            department.get = MagicMock(return_value="Computer Science")

            institute.id = 127671276711

            scheme_of_work = SchemeOfWorkModel(14, name="A-Level Computer Science", study_duration=2, start_study_in_year=12, is_from_db=is_from_db, auth_user=AuthCtx(mock_db, mock_request, institute.id, department.id))
            
            auth_ctx = AuthCtx(mock_db, mock_request, institute_id=127671276711, department_id=34, scheme_of_work_id=14)

    return TeacherPermissionModel(teacher_id=56, teacher_name="Jane Mellor", join_code="ABCDEFGH", scheme_of_work=scheme_of_work, is_from_db=is_from_db, ctx=auth_ctx, scheme_of_work_permission=SCHEMEOFWORK.OWNER, lesson_permission=LESSON.OWNER, department_permission=DEPARTMENT.HEAD, is_authorised=is_authorised)


class fake_settings:
    MIN_NUMBER_OF_DAYS_TO_KEEP_LOGS = 7
    MAX_NUMBER_OF_DAYS_TO_KEEP_LOGS = 30
    PAGER = { 
        "default": {
             "page": 2, "pagesize": 10, "pagesize_options": [5,10,25,50,100]
        },
        "notifications": {
             "page": 1, "pagesize": 100, "pagesize_options": [100,]
        },
        "schedule":{
            "page": 1,
            "pagesize": 7,
            "pagesize_options": { 0:"all", 1:"today", 2:"2 days", 7:"1 week", 14:"2 weeks", 28:"28 days" }
        },
    },
    ISOFORMAT = "%Y-%m-%dT%H:%M",
    ISOFORMAT_DATE = "%Y-%m-%d",
    ISOFORMAT_TIME = "%H:%M",
    ISOFORMAT_TIME_MS = "%H:%M:%S"
    

def fake_breadcrumbs():
    return {"/":{"id":"lnk-bc-home","text":"Home"}}