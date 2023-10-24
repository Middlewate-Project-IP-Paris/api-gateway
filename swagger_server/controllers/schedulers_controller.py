import connexion
import six
import grpc

from swagger_server.models.inline_response2004 import InlineResponse2004  # noqa: E501
from swagger_server.models.scheduler_create_body import SchedulerCreateBody  # noqa: E501
from swagger_server.models.scheduler_update_body import SchedulerUpdateBody  # noqa: E501
from swagger_server import util


from proto.scheduler import scheduler_pb2, scheduler_pb2_grpc
from google.protobuf.json_format import MessageToDict
import VARS as vars

import google.protobuf.empty_pb2 

def api_v1_scheduler_create_post(body):  # noqa: E501
    """Create scheduler

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2004
    """
    scheduler = grpc.insecure_channel(f'''localhost:{vars.SCHEDULER_SERVICE_PORT}''')
    stub = scheduler_pb2_grpc.SchedulerServiceStub(scheduler)
    request = scheduler_pb2.SchedulerRequest(
        name=body["name"],
        target_service_method=body["action"],
        repeat_minutes= body["time_repeat"]
    )
    response = stub.CreateScheduler(request)
    dict_response = MessageToDict(response)
    scheduler = {
        "scheduler": {
            "action": dict_response["targetServiceMethod"],
            "name": dict_response["name"],
            "scheduler_id": dict_response["id"],
            "time_repeat": dict_response["repeatMinutes"]
        }
    }
    
    return scheduler


def api_v1_scheduler_get_all_get():  # noqa: E501
    """Get all the schedulers

     # noqa: E501


    :rtype: List[SchedulerUpdateBody]
    """

    scheduler = grpc.insecure_channel(f'''localhost:{vars.SCHEDULER_SERVICE_PORT}''')
    stub = scheduler_pb2_grpc.SchedulerServiceStub(scheduler)
    request = google.protobuf.empty_pb2.Empty()
    response = stub.GetAllSchedulers(request)
    schedulers = []
    print(response)
    for scheduler in response.schedulers:
        dict_scheduler = MessageToDict(scheduler)
        cur_scheduler = {
            "action": dict_scheduler["targetServiceMethod"],
            "name": dict_scheduler["name"],
            "scheduler_id": dict_scheduler["id"],
            "time_repeat": dict_scheduler["repeatMinutes"]
        }
        schedulers.append(cur_scheduler)

    return {"schedulers": schedulers}


def api_v1_scheduler_update_put(body=None):  # noqa: E501
    """Create scheduler

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: SchedulerUpdateBody
    """
    scheduler = grpc.insecure_channel(f'''localhost:{vars.SCHEDULER_SERVICE_PORT}''')
    stub = scheduler_pb2_grpc.SchedulerServiceStub(scheduler)
    request = scheduler_pb2.ModifySchedulerRequest(
        id=body["scheduler_id"],
        target_service_method=body["action"],
        repeat_minutes= body["time_repeat"],
        name=body["name"]
    )
    response = stub.ModifyScheduler(request)
    
    return {"schedule": MessageToDict(response)}
    # return 'do some magic!'
