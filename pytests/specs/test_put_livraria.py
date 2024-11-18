from pytests.support.hooks import *
from pytests.mocks.livraria_mock import *
from pytests.clients.put_livraria_client import PutLivrariaClient
from pytests.support.api_utils import ApiUtils
from pytests.schemas.put_livros_schema import *
from pytests.clients.common import Commom
from pytests.examples.examples_test_put_livraria import *


@pytest.mark.crud_livros
def test_put_livro():
    payload = payload_post_livros()
    ApiUtils.payload_parse(payload)
    response = PutLivrariaClient.put_livros(payload, 12)
    Commom.validate_response(response, 200)
    ApiUtils.validate_json_schema(response, put_schema)


@pytest.mark.crud_livros
@pytest.mark.parametrize("payload, code", examples_put_livraria_invalid_payload)
def test_put_livros_invalid_payload(payload, code):
    payload = Commom.incorrect_payload(payload)
    ApiUtils.payload_parse(payload)
    response = PutLivrariaClient.put_livros(payload, 8)
    Commom.validate_response(response, code)


@pytest.mark.crud_livros
@pytest.mark.parametrize("field, value, code", examples_put_livraria_invalid_values)
def test_put_livros_invalid_values(field, value, code):
    payload = payload_post_livros()
    payload = Commom.change_fields_payload(payload, field, value)
    ApiUtils.payload_parse(payload)
    response = PutLivrariaClient.put_livros(payload, 8)
    Commom.validate_response(response, code)


@pytest.mark.crud_livros
@pytest.mark.parametrize("field, code", examples_put_livraria_no_fields)
def test_put_livros_no_fields(field, code):
    payload = payload_post_livros()
    payload = Commom.remove_fields_payload(payload, field)
    ApiUtils.payload_parse(payload)
    response = PutLivrariaClient.put_livros(payload, 8)
    Commom.validate_response(response, code)


@pytest.mark.crud_livros
@pytest.mark.parametrize("value, code", examples_put_id_livraria_invalid_values)
def test_put_id_livro_invalid_values(value, code):
    payload = payload_post_livros()
    ApiUtils.payload_parse(payload)
    values_change = Commom.values_change(value)
    response = PutLivrariaClient.put_livros(payload, values_change)
    Commom.validate_response(response, code)