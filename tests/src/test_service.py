from unittest.mock import patch
import pytest

from .stubs import StubRequestObj

# Jormungandr
from func.src.service import get_all_custom_fields, __request_zendesk_custom_fields, __treatment_ticket_custom_fields


@patch('func.src.service.requests.get', return_value=StubRequestObj(status_code=200))
def test_when_valid_api_url_then_return_ticket_custom_fields(mock_requests_get):
    response = __request_zendesk_custom_fields()
    print('teste')
