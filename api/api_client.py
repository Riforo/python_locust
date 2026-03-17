from locust.clients import HttpSession

from api.services.endpoints.endpoint_provider import EndpointsProvider



class ApiClient:

    servise_name = ''

    def __init__(self, client: HttpSession):
        if not self.servise_name: ValueError("Services name not set")
        self.client = client
        self.endpoint_provider = EndpointsProvider(self.servise_name)


    def send_request(self, tag, endpoint_name, headers=None, params=None, data=None, catch_response=False):
        endpoint = self.endpoint_provider.get_endpoint(self.servise_name, tag, endpoint_name)
        resp = self.client.request(
            method=endpoint['method'],
            url=endpoint['endpoint'],
            headers=headers,
            params=params,
            data=data,
            name=endpoint_name + ": "+ endpoint['method']+ ' ' + endpoint['endpoint'],
            catch_response=catch_response
        )
        return resp
    