import unittest
from HiPayMBService import HiPayMBService

class HiPayTesy(unittest.TestCase):
    def setUp(self):
        self.hipay_mb_service = HiPayMBService(username="*", password="*")

    def tearDown(self):
        pass

    def testGetReferenceMB(self):
        mb_reference = self.hipay_mb_service.get_reference_mb(email="mac.mendao@gmail.com", amount=10, sendEmailBuyer=False)

        self.assertIsNotNone(mb_reference)
        self.assertIsNotNone(mb_reference["reference"])
        self.assertIsNotNone(mb_reference["amountOut"])
        self.assertEqual(mb_reference["amountOut"], 10)
        self.assertIsNotNone(mb_reference["entity"])

    def testGetReferenceInfo(self):
        mb_reference = self.hipay_mb_service.get_reference_mb(email="mac.mendao@gmail.com", amount=10, sendEmailBuyer=False)

        reference_info = self.hipay_mb_service.get_info_reference(mb_reference["reference"])

        self.assertIsNotNone(reference_info)
        self.assertIsNotNone(reference_info["paid"])
        self.assertIsNotNone(reference_info["status"])
