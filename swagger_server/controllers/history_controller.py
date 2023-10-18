import connexion
import six

from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server import util


def api_v1_history_object_type_history_data_idids_get(ids, object_type, history_data):  # noqa: E501
    """Get Channels history by ID

     # noqa: E501

    :param ids: IDs of channels
    :type ids: List[int]
    :param object_type: Type of object, channel or post
    :type object_type: str
    :param history_data: Type of object, subs or views
    :type history_data: str

    :rtype: List[InlineResponse2001]
    """
    return 'do some magic!'
