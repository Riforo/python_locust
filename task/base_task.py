from locust import TaskSet, task

from api.model.responses.main import MainResponse
from api.services.portal import PortalServices
from profile.base_user import BaseProfile, BaseUserWithServiser


class TaskClassOfPortalInProfile(TaskSet):

    user: BaseUserWithServiser
    
    @task
    def send_request(self):
        self.user.portal_servise.send_endpoint_name()


class TaskClassPortalInTask(TaskSet):

    def on_start(self):
        self.portal_servise = PortalServices()

    @task
    def send_request(self):
        self.portal_servise.send_endpoint_name()


class TaskWithWalidateResponse(TaskSet):

    def on_start(self):
        self.portal_servise = PortalServices()
    
    @task
    def send_with_walidate(self):
        with self,self.portal_servise.send_endpoint_name() as resp:
            if resp.ok: MainResponse.model_json_schema(resp.text)


class TaskClassForUserOfBaseProfile(TaskSet):
    
    user: BaseProfile
    
    @task
    def send_request(self):
        self.user.portal_servise.send_endpoint_name()