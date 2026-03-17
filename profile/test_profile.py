from locust import HttpUser, between

from api.services.portal import PortalServices
from profile.user_config.base_user import BaseProfile
from task.base_task import TaskClassForUserOfBaseProfile, TaskClassOfPortalInProfile, TaskClassPortalInTask, TaskWithWalidateResponse


class BaseUserWithServiser(HttpUser):
    host = "https://jsonplaceholder.typicode.com"
    tasks = [TaskClassOfPortalInProfile]
    wait_time = between(1, 5)
    weight = 1

    def on_start(self):
        self.portal_servise = PortalServices(self.client)


class BaseUserWithoutServise(HttpUser):
    host = "https://jsonplaceholder.typicode.com"
    tasks = [TaskClassPortalInTask]
    wait_time = between(1, 5)
    weight = 1


class BaseUserWithWalidateResponse(HttpUser):
    host = "https://jsonplaceholder.typicode.com"
    tasks = [TaskWithWalidateResponse]
    wait_time = between(1, 5)
    weight = 1


class UserOfBaseProfile(BaseProfile):
    tasks = [TaskClassForUserOfBaseProfile]
    wait_time = between(1, 5)
    weight = 1