import pytest
from dotenv import load_dotenv
from pytests.support.log_service import LogService
LOG = LogService

@pytest.fixture(scope="session", autouse=True)
def before_all():
    LOG.log_info("Teste log before all")
    load_dotenv()

@pytest.fixture(autouse=True)
def before_after():
    LOG.log_info("Teste log before")
    yield
    LOG.log_info("Teste log after")

