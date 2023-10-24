import connexion
import grpc
import six
import VARS as vars

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util

from proto.channel import channel_pb2, channel_pb2_grpc
from proto.assitant import assistant_on_demand_pb2, assistant_on_demand_pb2_grpc

def api_v1_channel_idids_get(ids):  # noqa: E501
    """Get Channels by ID

     # noqa: E501

    :param ids: IDs of channels
    :type ids: List[int]

    :rtype: List[InlineResponse200]
    """
    channel = grpc.insecure_channel(f'''localhost:{vars.CHANNEL_SERICE_PORT}''')
    stub = channel_pb2_grpc.channelServiceStub(channel)
    request = channel_pb2.ChannelInfoRequest(channel_id=[1, 2, 3])
    response = stub.getChannelInfo(request)
    channels = []
    for channel_info in response.channel_info:
        current_channel = {}
        current_channel['channel_id'] =channel_info.channel_id
        current_channel['name'] = channel_info.name
        current_channel['link'] = channel_info.link
        current_channel['description'] = channel_info.description
        current_channel['subs'] = channel_info.subscribers
        channels.append(current_channel)

    return {"channels":channels}


def api_v1_channel_join_invite_link_get(invite_link):  # noqa: E501
    """Join channel by link

     # noqa: E501

    :param invite_link: invite link to channel
    :type invite_link: str

    :rtype: None
    """

    assistant = grpc.insecure_channel(f'''localhost:{vars.ASSISTANT_SERVICE_PORT}''')
    stub = assistant_on_demand_pb2_grpc.assistanceOnDemandStub(assistant)
    request = assistant_on_demand_pb2.InviteRequest(invite_link = invite_link)
    response = stub.joinChannel(request)
    if response.status_code == 200:
        return 'Channel will be joined'
    else:
        return 'Some error occured'
