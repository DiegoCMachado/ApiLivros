import logging

from pytests.support.hooks import *
from jsonschema import validate
import json

class ApiUtils:
    @staticmethod
    def validate_status_code(request, code):
        try:
            LOG.log_info(f"Status code Esperado: {code}")
            LOG.log_info(f"Status code Recebido: {request['code']}")
            assert request['code'] == code
        except Exception as e:
            LOG.log_error("Codes Divergentes")
            raise e

    @staticmethod
    def request_parse_log(request):
        if "{" in request['body']:
            load = json.loads(request['body'])
            resp = json.dumps(load, indent=1, ensure_ascii=False)
            LOG.log_info(f"Response:\n{resp}")
            return load
        else:
            LOG.log_info(f"Response:\n{request['body']}")
            return request['body']

    @staticmethod
    def payload_parse(payload):
        resp = json.dumps(payload, indent=1, ensure_ascii=False)
        LOG.log_info(f"Payload:\n{resp}")

    @staticmethod
    def validate_json_schema(response, schema):
        try:
            response_json = json.loads(response['body'])
            validate(instance=response_json, schema=schema)
            LOG.log_info("Contrato validado com sucesso")
        except Exception as e:
            LOG.log_error("Erro ao validar o contrato")
            raise e
