import connexion
import six
import grpc

from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server import util
from proto.channel import channel_pb2, channel_pb2_grpc
from google.protobuf.json_format import MessageToDict


import VARS as vars


def api_v1_posts_channel_id_idids_get(ids, channel_id):  # noqa: E501
    """Get Posts by ID

     # noqa: E501

    :param ids: IDs of posts
    :type ids: int
    :param channel_id: IDs of channel
    :type channel_id: List[int]

    :rtype: List[InlineResponse2002]
    """
    channel = grpc.insecure_channel(f'''localhost:{vars.CHANNEL_SERICE_PORT}''')
    stub = channel_pb2_grpc.channelServiceStub(channel)
    request = channel_pb2.GetPostsInfoRequest(channel_id = ids, post_ids = channel_id)
    response = stub.getPostInfo(request)
    posts = []
    for i in response.post_info:
        
        info = MessageToDict(i)
        posts.append(info)
    

    return {'posts': posts}
