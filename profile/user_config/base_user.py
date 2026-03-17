from config import config
from locust import HttpUser, FastHttpUser
from api.services.portal import PortalServices


class BaseProfile(HttpUser):
    abstract = True
    host = config.base_url
    def on_start(self):
        self.portal_servise = PortalServices(self.client)


class FastBaseProfile(FastHttpUser):
    abstract = True
    host = config.base_url
    def on_start(self):
        self.portal_servise = PortalServices(self.client)