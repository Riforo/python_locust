import httpx


class ApiClient():
    

    def __init__(self, url):
        self.url = url


    def request(self, method, endpint):
        request = httpx.request(
            method=method,
            url=self.url + endpint
        )
        return request