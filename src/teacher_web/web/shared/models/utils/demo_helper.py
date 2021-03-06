import os
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log_handlers import handle_log_info

class DemoHelper:

    @classmethod
    def restore(cls, db, auth_user):
        
        demo_institute_id = os.environ["TEST_INSTITUTE_ID"]
        demo_department_id = os.environ["TEST_DEPARTMENT_ID"]
        demo_scheme_of_work_id = os.environ["TEST_SCHEME_OF_WORK_ID"]
        demo_content_id = os.environ["TEST_CONTENT_ID"]
        demo_lesson_id = os.environ["TEST_LESSON_ID"] 
        demo_learning_objective_id = os.environ["TEST_LEARNING_OBJECTIVE_ID"]
        demo_reference = os.environ["TEST_RESOURCE_ID"]
        #demo_md_document_name = os.environ["TEST_MD_DOCUMENT_NAME"]
        demo_keyword_id = os.environ["TEST_KEYWORD_ID"]
        
        execHelper = ExecHelper()

        stored_procedure = "demo_restoredata"
        params = (
            auth_user.auth_user_id,
            demo_institute_id,
            demo_department_id,
            demo_scheme_of_work_id,
            demo_content_id,
            demo_lesson_id,
            demo_learning_objective_id,
            demo_reference,
            demo_keyword_id
            )

        execHelper.insert(db, stored_procedure, params, handle_log_info)
