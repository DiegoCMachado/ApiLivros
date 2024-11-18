from pytests.support.hooks import *
from pytests.mocks.livraria_mock import *
from pytests.clients.post_livraria_client import PostLivrariaClient
from pytests.support.api_utils import ApiUtils
from pytests.schemas.post_livros_schema import *
from pytests.clients.common import Commom
from pytests.examples.examples_test_post_livraria import *

@pytest.mark.crud_livros
def test_post_livro():
    payload = payload_post_livros()
    ApiUtils.payload_parse(payload)
    response = PostLivrariaClient.post_livros(payload)
    Commom.validate_response(response, 201)
    ApiUtils.validate_json_schema(response, post_schema)

@pytest.mark.crud_livros
@pytest.mark.parametrize("payload, code", examples_post_livraria_invalid_payload)
def test_post_livros_invalid_payload(payload, code):
    payload = Commom.incorrect_payload(payload)
    ApiUtils.payload_parse(payload)
    response = PostLivrariaClient.post_livros(payload)
    Commom.validate_response(response, code)

@pytest.mark.crud_livros
@pytest.mark.parametrize("field, value, code", examples_post_livraria_invalid_values)
def test_post_livros_invalid_values(field, value, code):
    payload = payload_post_livros()
    payload = Commom.change_fields_payload(payload, field, value)
    ApiUtils.payload_parse(payload)
    response = PostLivrariaClient.post_livros(payload)
    Commom.validate_response(response, code)

@pytest.mark.crud_livros
@pytest.mark.parametrize("field, code", examples_post_livraria_no_fields)
def test_post_livros_no_fields(field, code):
    payload = payload_post_livros()
    payload = Commom.remove_fields_payload(payload, field)
    ApiUtils.payload_parse(payload)
    response = PostLivrariaClient.post_livros(payload)
    Commom.validate_response(response, code)