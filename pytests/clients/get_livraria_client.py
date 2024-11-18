from playwright.sync_api import sync_playwright
from pytests.support.hooks import *
import os

class GetLivrariaClient:

    @staticmethod
    def get_livros(id=""):
        with sync_playwright() as p:
            context = p.request.new_context()
            response = context.get(f"{os.environ['BASE_URL']}/{id}")
            LOG.log_info("GET")
            LOG.log_info(f"{os.environ['BASE_URL']}/{id}")
            return {"code": response.status, "body": response.text(), "headers": response.headers}

