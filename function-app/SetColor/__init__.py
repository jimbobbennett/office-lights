import os
import sys
sys.path.append(os.path.abspath(""))

import logging
import azure.functions as func

from ..shared import api


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    logging.info(req.params)

    style = req.params.get('style')
    hex_color = req.params.get('hexcolor')

    if style is not None:
        req_body = {'ColorType':'Style','Color':{'Style':style}}
    elif hex_color is not None:
        req_body = {'ColorType':'HexColor','Color':{'HexColor':hex_color}}
    else:
        req_body = req.get_json()

    api.call_iot_hub('SetColor', req_body)
    
    return func.HttpResponse("OK", status_code=200)
