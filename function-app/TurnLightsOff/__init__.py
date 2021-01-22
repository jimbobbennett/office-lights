import os
import sys
sys.path.append(os.path.abspath(""))

import logging
import azure.functions as func

from ..shared import api

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Turning lights on')

    api.call_ifttt_off()
    api.call_iot_hub('TurnOff', {})

    return func.HttpResponse("OK", status_code=200)
