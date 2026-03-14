from locust import HttpUser, between

from api.services.portal import PortalServices
from task.base_task import TaskClassForUserOfBaseProfile, TaskClassOfPortalInProfile, TaskClassPortalInTask, TaskWithWalidateResponse


class BaseProfile(HttpUser):

    def on_start(self):
        self.portal_servise = PortalServices(self.client)


class BaseUserWithServiser(HttpUser):
    tasks = [TaskClassOfPortalInProfile]
    wait_time = between(1, 5)
    weight = 1

    def on_start(self):
        self.portal_servise = PortalServices(self.client)


class BaseUserWithoutServise(HttpUser):
    tasks = [TaskClassPortalInTask]
    wait_time = between(1, 5)
    weight = 1


class BaseUserWithWalidateResponse(HttpUser):
    tasks = [TaskWithWalidateResponse]
    wait_time = between(1, 5)
    weight = 1


class UserOfBaseProfile(BaseProfile):
    tasks = [TaskClassForUserOfBaseProfile]
    wait_time = between(1, 5)
    weight = 1