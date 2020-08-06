from unittest import TestCase
from unittest.mock import Mock
from shared.models.core.log import Log, LOG_TYPE

class test__logger__for__log__error(TestCase):

    def setUp(self):
        # arrange

        ## create test object
        
        db = Mock()
        db.cursor = Mock()

        self.test_log = Log(db, LOG_TYPE.NONE)

        ## mock function to be called as neccessary

        self.test_log._write_to_sql = Mock()
        self.test_log._write_to_django_log = Mock()


    def test_should_log__log_type__verbose(self):

        # act
        self.test_log.write("Something happened", details="we're logging everything", log_type=LOG_TYPE.Verbose)
        
        # assert

        self.test_log._write_to_django_log.assert_not_called()
        self.test_log._write_to_django_log.assert_not_called()


    def test_should_log__log_type__info(self):

        # act
        self.test_log.write("Something happened", "just some information", LOG_TYPE.Information)
        
        # assert

        self.test_log._write_to_django_log.assert_not_called()
        self.test_log._write_to_django_log.assert_not_called()


    def test_should_log__log_type__warning(self):

        # act
        self.test_log.write("Something happened", "", LOG_TYPE.Warning)
        
        # assert

        self.test_log._write_to_django_log.assert_not_called()
        self.test_log._write_to_django_log.assert_not_called()


    def test_should_log__log_type__error(self):

        # act
        self.test_log.write("Something happened", "", log_type=LOG_TYPE.Error)

        # asserts

        self.test_log._write_to_django_log.assert_called()
        self.test_log._write_to_django_log.assert_called()

