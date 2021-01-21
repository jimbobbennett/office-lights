import logging
import os
import requests
from azure.iot.hub import IoTHubRegistryManager
from azure.iot.hub.models import CloudToDeviceMethod

iot_hub_connection_string = os.environ['IOT_HUB_CONNECTION_STRING']
iot_hub_device_id = os.environ['IOT_HUB_DEVICE_ID']

ifttt_key = os.environ['IFTTT_KEY']
ifttt_on_event_name = os.environ['IFTTT_ON_EVENT']
ifttt_off_event_name = os.environ['IFTTT_OFF_EVENT']

ifttt_on_webhook = 'https://maker.ifttt.com/trigger/' + ifttt_on_event_name + '/with/key/' + ifttt_key
ifttt_off_webhook = 'https://maker.ifttt.com/trigger/' + ifttt_off_event_name + '/with/key/' + ifttt_key

registry_manager = IoTHubRegistryManager(iot_hub_connection_string)

def call_iot_hub(command, body):
    deviceMethod = CloudToDeviceMethod(method_name=command, payload=body)
    registry_manager.invoke_device_method(iot_hub_device_id, deviceMethod)

def call_ifttt_on():
    r = requests.get(ifttt_on_webhook)

    logging.info(r)
    logging.info(r.content)

def call_ifttt_off():
    r = requests.get(ifttt_off_webhook)

    logging.info(r)
    logging.info(r.content)