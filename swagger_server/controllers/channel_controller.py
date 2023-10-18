import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util


def api_v1_channel_idids_get(ids):  # noqa: E501
    """Get Channels by ID

     # noqa: E501

    :param ids: IDs of channels
    :type ids: List[int]

    :rtype: List[InlineResponse200]
    """
    return 'do some magic!'


def api_v1_channel_join_invite_link_get(invite_link):  # noqa: E501
    """Join channel by link

     # noqa: E501

    :param invite_link: invite link to channel
    :type invite_link: str

    :rtype: None
    """
    return 'do some magic!'
