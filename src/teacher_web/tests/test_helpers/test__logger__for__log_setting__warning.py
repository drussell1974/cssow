from unittest import TestCase
from unittest.mock import Mock, patch
from shared.models.core.log_handlers import Log, LOG_TYPE
from shared.models.core.log import LogDataAccess

@patch.object(LogDataAccess, "_write_to_sql", return_value=[0])
@patch.object(LogDataAccess, "_write_to_django_log", return_value=[0])
class test__logger__for__log__warning(TestCase):

    def setUp(self):
        # arrange

        ## create test object
        
        db = Mock()
        db.cursor = Mock()

        self.test_log = Log(db, LOG_TYPE.Warning)



    def test_should_log__log_type__verbose(self, Log_write_to_sql, Log_write_to_django_log):

        # act
        self.test_log.write(67, "Something happened", "", LOG_TYPE.Verbose)
        
        # assert

        Log_write_to_django_log.assert_not_called()
        Log_write_to_django_log.assert_not_called()


    def test_should_log__log_type__info(self, Log_write_to_sql, Log_write_to_django_log):

        # act
        self.test_log.write(68, "Something happened", "", LOG_TYPE.Information)
        
        # assert

        Log_write_to_django_log.assert_not_called()
        Log_write_to_django_log.assert_not_called()


    def test_should_log__log_type__warning(self, Log_write_to_sql, Log_write_to_django_log):

        # act
        self.test_log.write(66, "Something happened", "", LOG_TYPE.Warning)
        
        # assert

        Log_write_to_django_log.assert_called()
        Log_write_to_django_log.assert_called()


    def test_should_log__log_type__error(self, Log_write_to_sql, Log_write_to_django_log):

        # act
        self.test_log.write(69, "Something happened", "", LOG_TYPE.Error)

        # asserts

        Log_write_to_django_log.assert_called()
        Log_write_to_django_log.assert_called()

