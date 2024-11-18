from playwright.sync_api import sync_playwright
from pytests.support.hooks import *
import os

class PostLivrariaClient:

    @staticmethod
    def post_livros(payload):
        with sync_playwright() as p:
            context = p.request.new_context()
            response = context.post(f"{os.environ['BASE_URL']}", data=payload)
            LOG.log_info("POST")
            LOG.log_info(f"{os.environ['BASE_URL']}")
            return {"code": response.status, "body": response.text(), "headers": response.headers}



