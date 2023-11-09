import unittest
import utils
#

class UtilsTest(unittest.TestCase):
    def test_find_numbers_in_text(self):
        test_object = utils.Utils()
        result = test_object.find_numbers_in_text("e2423o3453pkrtpkegl34")
        self.assertEqual(result, 2423345334, "num finder error")

    def test_check_for_positive_number(self):
        test_object = utils.Utils()
        msg = "NEGATIVE EXCEPTION"

        with self.assertRaises(ValueError):
            test_object.check_for_positive_number(-1, msg)

        test_object.check_for_positive_number(0, msg)
        test_object.check_for_positive_number(13, msg)

    def test_check_if_exist(self):
        test_object = utils.Utils()
        msg = "NON-EXISTENT EXCEPTION"

        argument = None
        with self.assertRaises(ValueError):
            test_object.check_if_exist(argument, msg)