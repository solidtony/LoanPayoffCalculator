import unittest

from ..pay_schedule import DummyPaySchedule,Date

class TestDummyPaySchedule(unittest.TestCase):
    def test_individual_date_is_correct_202226(self):
        expected = Date(2022,2,6)
        pay_sched = DummyPaySchedule(expected)
        self.assertEqual(expected, pay_sched.base_dates[0])

    def test_individual_date_is_correct_2000521(self):
        expected = Date(2000,5,21)
        pay_sched = DummyPaySchedule(expected)
        self.assertEqual(expected, pay_sched.base_dates[0])
