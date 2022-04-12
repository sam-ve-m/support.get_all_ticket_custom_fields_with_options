# Third party
from etria_logger import Gladsheim
from flask import Response

# Standards
from json import dumps


# Jormungandr
from src.service import get_all_custom_fields
from src.exceptions import InvalidEndpointZendeskApi, ErrorToRequestZendeskApi, ErrorToGetRedisClient


def get_all_ticket_custom_fields():
    message = 'Jormungandr::get_all_ticket_custom_fields'
    try:
        service_response = get_all_custom_fields()
        response = Response(
            dumps({'result': service_response, 'success': True}), mimetype='application/json', status=200)
        return response

    except InvalidEndpointZendeskApi as ex:
        Gladsheim.error(ex, f'{message}::{ex.msg}')
        response = Response(
            dumps({'message': ex.msg, 'success': False}), mimetype='application/json', status=ex.status_code)
        return response

    except ErrorToRequestZendeskApi as ex:
        Gladsheim.error(ex, f'{message}::{ex.msg}')
        response = Response(
            dumps({'message': ex.msg, 'success': False}), mimetype='application/json', status=ex.status_code)
        return response

    except ErrorToGetRedisClient as ex:
        Gladsheim.error(ex, f'{message}::{ex.msg}')
        response = Response(
            dumps({'message': ex.msg, 'success': False}), mimetype='application/json', status=ex.status_code)
        return response

    except Exception as ex:
        Gladsheim.error(ex, f'{message}::{str(ex)}')
        response = Response(
            dumps({'message': str(ex), 'success': False}), mimetype='application/json', status=400
        )
        return response
