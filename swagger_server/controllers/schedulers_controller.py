import connexion
import six

from swagger_server.models.inline_response2004 import InlineResponse2004  # noqa: E501
from swagger_server.models.scheduler_create_body import SchedulerCreateBody  # noqa: E501
from swagger_server.models.scheduler_update_body import SchedulerUpdateBody  # noqa: E501
from swagger_server import util


def api_v1_scheduler_create_post(body=None):  # noqa: E501
    """Create scheduler

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2004
    """
    if connexion.request.is_json:
        body = SchedulerCreateBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_v1_scheduler_get_all_get():  # noqa: E501
    """Get all the schedulers

     # noqa: E501


    :rtype: List[SchedulerUpdateBody]
    """
    return 'do some magic!'


def api_v1_scheduler_update_put(body=None):  # noqa: E501
    """Create scheduler

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: SchedulerUpdateBody
    """
    if connexion.request.is_json:
        body = SchedulerUpdateBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
