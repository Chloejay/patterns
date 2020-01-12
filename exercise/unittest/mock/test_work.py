from unittest import TestCase, mock
# make all the test units isolated from each other 
from work import work_on


class TestWorkMockingModule(TestCase):

    def test_using_context_manager(self):
        with mock.patch('work.os') as mocked_os:
            work_on()
            mocked_os.getcwd.assert_called_once()

    @mock.patch('work.os')
    def test_using_decorator(self, mocked_os):
        work_on()
        mocked_os.getcwd.assert_called_once()

    def test_using_return_value(self):
        with mock.patch('work.os.getcwd', return_value='patch_testing') as whatever:
            assert work_on() == 'patch_testing'