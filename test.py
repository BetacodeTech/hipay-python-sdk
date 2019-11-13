import unittest
from hipay_python_sdk.HiPayMBService import HiPayMBService
from hipay_python_sdk.HiPayPayshopService import HiPayPayshopService


class HiPayTest(unittest.TestCase):
    def setUp(self):
        self.hipay_mb_service = HiPayMBService(username="*", password="*")
        self.hipay_payshop_service = HiPayPayshopService(username="*", password="*")

    def tearDown(self):
        pass

    def testGetReferenceMB(self):
        mb_reference = self.hipay_mb_service.get_reference_mb(email="mac.mendao@gmail.com", amount=10,
                                                              sendEmailBuyer=False)

        self.assertIsNotNone(mb_reference)
        self.assertIsNotNone(mb_reference["reference"])
        self.assertIsNotNone(mb_reference["amountOut"])
        self.assertEqual(mb_reference["amountOut"], 10)
        self.assertIsNotNone(mb_reference["entity"])

    def testGetReferenceInfoMB(self):
        mb_reference = self.hipay_mb_service.get_reference_mb(email="mac.mendao@gmail.com", amount=10,
                                                              sendEmailBuyer=False)

        reference_info = self.hipay_mb_service.get_info_reference(mb_reference["reference"])

        self.assertIsNotNone(reference_info)
        self.assertIsNotNone(reference_info["paid"])
        self.assertIsNotNone(reference_info["status"])

    def testGetReferencePayshop(self):
        mb_reference = self.hipay_payshop_service.get_reference_payshop(email="mac.mendao@gmail.com", amount=10,
                                                              sendEmailBuyer=False)

        self.assertIsNotNone(mb_reference)
        self.assertIsNotNone(mb_reference["reference"])
        self.assertIsNotNone(mb_reference["amountOut"])
        self.assertEqual(mb_reference["amountOut"], 10)

    def testGetReferenceInfoPayshop(self):
        mb_reference = self.hipay_payshop_service.get_reference_payshop(email="mac.mendao@gmail.com", amount=10,
                                                              sendEmailBuyer=False)

        reference_info = self.hipay_payshop_service.get_info_reference(mb_reference["reference"])

        self.assertIsNotNone(reference_info)
        self.assertIsNotNone(reference_info["paid"])
        self.assertIsNotNone(reference_info["status"])
