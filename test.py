import unittest
import payment
import datetime


class TestPayment(unittest.TestCase):

    def test_readFile(self):
        expected = {'ASTRID': ['MO10:00-12:00',
                               'TH12:00-14:00', 'SU20:00-21:00']}

        employees = payment.readFile('./test.txt')

        self.assertDictEqual(expected, employees)

    def test_nonFile(self):
        with self.assertRaises(SystemExit):
            payment.readFile('./foo.txt')

    def test_processHours(self):
        expected_begin = datetime.datetime(100, 1, 1, 10, 0, 0)
        expected_end = datetime.datetime(100, 1, 1, 12, 0, 0)

        begin, end = payment.processHours('10:00-12:00')

        self.assertEqual(expected_begin, begin)
        self.assertEqual(expected_end, end)

    def test_processPayment(self):
        beggin, end = payment.processHours('10:00-12:00')
        weekend = False

        calc_payment = payment.processPayment(beggin, end, weekend)

        self.assertEqual(30, calc_payment)

    def test_processSchedules(self):
        schedules = ['MO10:00-12:00',
                     'TH12:00-14:00', 'SU20:00-21:00']

        calc_payment = payment.processSchedules(schedules)

        self.assertEqual(85, calc_payment)


if __name__ == '__main__':
    unittest.main()
