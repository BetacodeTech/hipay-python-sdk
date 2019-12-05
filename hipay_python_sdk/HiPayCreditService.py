import zeep


class HiPayCreditService:
    def __init__(self, ws_login, ws_password, callback_email, url_callback=None, url_decline=None, url_cancel=None,
                 url_logo=None, wsdl='https://test-ws.hipay.com/soap/payment-v2?wsdl'):
        self.client = zeep.Client(wsdl=wsdl)
        self.ws_login = ws_login
        self.ws_password = ws_password
        self.callback_email = callback_email
        self.url_callback = url_callback
        self.url_decline = url_decline
        self.url_cancel = url_cancel
        self.url_logo = url_logo

    def generate_payment(self, website_id, category_id, amount, customer_email, currency="EUR", rating="ALL",
                         locale="pt_PT", customer_ip_address="127.0.0.1", description="Default description",
                         manual_capture=False):
        request_data = {
            "websiteId": website_id,
            "categoryId": category_id,
            "currency": currency,
            "amount": amount,
            "rating": rating,
            "locale": locale,
            "customerIpAddress": customer_ip_address,
            "description": description,
            "manualCapture": manual_capture,
            "customerEmail": customer_email,
            "emailCallback": self.callback_email,
            "urlCallback": self.url_callback,
            "urlDecline": self.url_decline,
            "urlCancel": self.url_cancel,
            "urlLogo": self.url_logo,
            "wsLogin": self.ws_login,
            "wsPassword": self.ws_password
        }

        return self.client.service.generate(parameters=request_data)

    def generate_refund(self):
        pass
