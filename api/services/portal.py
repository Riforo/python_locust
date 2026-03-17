from pydantic import ValidationError

from api.api_client import ApiClient
from api.model.responses.main import MainResponse


class PortalServices(ApiClient):
    servise_name = 'service_name'

    def send_endpoint_name(self):
        return self.send_request(tag='jsonplaceholder', endpoint_name='one_posts')
    

    def send_with_validate(self):
        with self.send_request(tag='jsonplaceholder', endpoint_name='one_posts', catch_response=True) as resp:
            if not resp.ok: 
                resp.failure()
            else:
                try:
                    model = MainResponse.model_json_schema(resp.text)
                    resp.success()
                    return model
                except ValidationError as e:
                    error_msq = f'Pydantic Error: {e.json()}'
                    resp.failure(error_msq)
                    return None
                except Exception as e:
                    resp.failure(f"Unknown error: {e}")
                    return None