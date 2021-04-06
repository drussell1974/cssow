from unittest import TestCase
from unittest.mock import Mock, patch
from shared.models.core.log_handlers import Log, LOG_TYPE
from shared.models.core.log import LogDataAccess

@patch.object(LogDataAccess, "_write_to_sql", return_value=[0])
@patch.object(LogDataAccess, "_write_to_django_log", return_value=[0])
class test__logger__for__log__error(TestCase):

    def setUp(self):
        # arrange

        ## create test object
        
        db = Mock()
        db.cursor = Mock()

        self.test_log = Log(db, LOG_TYPE.NONE)

        ## mock function to be called as neccessary

        self.test_log._write_to_sql = Mock()
        Log_write_to_django_log = Mock()


    def test_should_log__log_type__verbose(self, Log_write_to_sql, Log_write_to_django_log):

        # act
        self.test_log.write(73, "Something happened", details="we're logging everything", log_type=LOG_TYPE.Verbose)
        
        # assert

        Log_write_to_django_log.assert_not_called()
        Log_write_to_django_log.assert_not_called()


    def test_should_log__log_type__info(self, Log_write_to_sql, Log_write_to_django_log):

        # act
        self.test_log.write(74, "Something happened", "just some information", LOG_TYPE.Information)
        
        # assert

        Log_write_to_django_log.assert_not_called()
        Log_write_to_django_log.assert_not_called()


    def test_should_log__log_type__warning(self, Log_write_to_sql, Log_write_to_django_log):

        # act
        self.test_log.write(73, "Something happened", "", LOG_TYPE.Warning)
        
        # assert

        Log_write_to_django_log.assert_not_called()
        Log_write_to_django_log.assert_not_called()


    def test_should_log__log_type__error(self, Log_write_to_sql, Log_write_to_django_log):

        # act
        self.test_log.write(75, "Something happened", "", log_type=LOG_TYPE.Error)

        # asserts

        Log_write_to_django_log.assert_called()
        Log_write_to_django_log.assert_called()

