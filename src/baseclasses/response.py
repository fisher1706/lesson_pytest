from jsonschema import validate
from src.enums.global_enums import GlobalErrorMessages


class Response:
    def __init__(self, resp):
        self.resp = resp
        self.resp_json = resp.json()
        self.resp_status = resp.status_code

    def validate_json(self, schema):
        if isinstance(self.resp_json, list):
            for item in self.resp_json:
                validate(item, schema)
        else:
            validate(self.resp_json, schema)
        return self

    def validate_pydantic(self, schema):
        if isinstance(self.resp_json, list):
            for item in self.resp_json:
                schema.parse_obj(item)
        else:
            schema.parse_obj(self.resp_json)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.resp_status in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.resp_status == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self


class ResponseNew:
    def __init__(self, resp):
        self.parsed_object = None
        self.resp = resp
        self.resp_json = resp.json().get('data')
        self.resp_status = resp.status_code

    def validate(self, schema):
        if isinstance(self.resp_json, list):
            for item in self.resp_json:
                # schema.parse_obj(item)
                passed_object = schema.parse_obj(item)
                self.parsed_object = passed_object
        else:
            schema.parse_obj(self.resp_json)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.resp_status in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.resp_status == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self

    def get_parsed_object(self):
        return self.parsed_object

    def __str__(self):
        return \
            f'\nStaus code: {self.resp_status}' \
            f'\nRequested url: {self.resp.url}' \
            f'\nResponse_body: {self.resp_json}'