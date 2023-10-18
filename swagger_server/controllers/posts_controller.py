import connexion
import six

from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server import util


def api_v1_posts_channel_id_idids_get(ids, channel_id):  # noqa: E501
    """Get Posts by ID

     # noqa: E501

    :param ids: IDs of posts
    :type ids: int
    :param channel_id: IDs of channel
    :type channel_id: List[int]

    :rtype: List[InlineResponse2002]
    """
    return 'do some magic!'
