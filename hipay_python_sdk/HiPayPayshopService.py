import zeep

class HiPayPayshopService:

    def __init__(self, username, password, wsdl='https://comprafacil2.hipay.pt/webservice/comprafacilWS.asmx?WSDL'):
        self.client = zeep.Client(wsdl=wsdl)
        self.username = username
        self.password = password

    def get_reference_payshop(self, email, amount, origin="", additionalInfo="", name="", address="", postCode="",
                              city="", NIC="", externalReference="", contactPhone="", IDUserBackoffice=-1, sendEmailBuyer=True):


        genereated_reference = self.client.service.getReferencePS(
            username=self.username,
            password=self.password,
            email=email,
            amount=amount,
            origin=origin,
            additionalInfo=additionalInfo,
            name=name,
            address=address,
            postCode=postCode,
            city=city,
            NIC=NIC,
            externalReference=externalReference,
            contactPhone=contactPhone,
            IDUserBackoffice=IDUserBackoffice,
            sendEmailBuyer=sendEmailBuyer
        )

        return genereated_reference

    def get_info_reference(self, reference):
        reference_info = self.client.service.getInfoReference(reference=reference, username=self.username, password=self.password)

        return reference_info
