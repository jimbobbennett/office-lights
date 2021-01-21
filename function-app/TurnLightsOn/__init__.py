import os
import sys
sys.path.append(os.path.abspath(""))

import logging
import azure.functions as func

from ..shared import api

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Turning lights on')

    api.call_ifttt_on()
    api.call_iot_central('TurnOn', {})
