from api.api_client import ApiClient


class PortalServices(ApiClient):
    servise_name = 'servise_name'

    def send_endpoint_name(self):
        return self.send_request(tag='tag', endpoint_name='endpoint_name')