import unittest
from hipay_python_sdk.HiPayMBService import HiPayMBService
from hipay_python_sdk.HiPayPayshopService import HiPayPayshopService
from hipay_python_sdk.HiPayCreditService import HiPayCreditService


class HiPayTest(unittest.TestCase):
    def setUp(self):
        self.hipay_mb_service = HiPayMBService(username="*", password="*")
        self.hipay_payshop_service = HiPayPayshopService(username="*", password="*")
        self.hipay_credit_service = HiPayCreditService(ws_login="1b0440cfb702df4312be974ba35ae335",
                                                       ws_password="3b9084471988203899411cf62749bf33",
                                                       callback_email="vgbetacode@gmail.com",
                                                       url_callback="http://dev.api.paymentgateways.betacode.tech/v1/hipay/credit_payment/callback",
                                                       url_decline="http://dev.api.paymentgateways.betacode.tech/v1/hipay/credit_payment/decline",
                                                       url_cancel="http://dev.api.paymentgateways.betacode.tech/v1/hipay/credit_payment/cancel",
                                                       url_logo="https://trello-attachments.s3.amazonaws.com/5d0795d0a145ea1c06ca85d9/5d9dbd6a82de740fec5a4228/8182f9ebb57ed1f0cb8d93375b7f0f75/logo_youpi2.png")

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

    def testGenerateCreditPaymentPage(self):
        generated_page = self.hipay_credit_service.generate_payment(website_id=573633, category_id=665, amount=11.0,
                                                                    customer_email="tiago.marques@betacode.tech")

        self.assertIsNotNone(generated_page)

