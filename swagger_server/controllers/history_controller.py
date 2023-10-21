import connexion
import six
import grpc

from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server import util

from proto.channel import channel_pb2, channel_pb2_grpc
import VARS as vars



def transform():
    pass

def api_v1_history_history_data_idids_get(ids, history_data):  # noqa: E501
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
    channel = grpc.insecure_channel(f'''localhost:{vars.CHANNEL_SERICE_PORT}''')
    stub = channel_pb2_grpc.channelServiceStub(channel)

 
    match history_data:
        case "subs":
            print(ids)
            request = channel_pb2.ChannelSubsHistoryRequest(channel_id = ids)
            response = stub.getChannelSubsHistory(request)
            print(f'''Response: {response}''')
            pass
        case "views":
            pass
    return 'do some magic!'

def api_v1_history_history_data_channel_idchannel_id_post_idspost_id_get(channel_id, post_id, history_data):  # noqa: E501
    """Get Channels history by ID

     # noqa: E501

    :param channel_id: IDs of channels
    :type channel_id: int
    :param post_id: IDs of channels
    :type post_id: int
    :param history_data: Type of object,views or shares
    :type history_data: str

    :rtype: List[InlineResponse2002]
    """
    return 'do some magic!'
