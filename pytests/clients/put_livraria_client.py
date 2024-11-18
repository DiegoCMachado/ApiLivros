from playwright.sync_api import sync_playwright
from pytests.support.hooks import *
import os

class PutLivrariaClient:

    @staticmethod
    def put_livros(payload, id):
        with sync_playwright() as p:
            context = p.request.new_context()
            response = context.put(f"{os.environ['BASE_URL']}/{id}", data=payload)
            LOG.log_info("PUT")
            LOG.log_info(f"{os.environ['BASE_URL']}/{id}")
            return {"code": response.status, "body": response.text(), "headers": response.headers}