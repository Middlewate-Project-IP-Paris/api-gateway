import connexion
import six
import grpc
import datetime

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
            request = channel_pb2.ChannelSubsHistoryRequest(channel_id = ids)
            response = stub.getChannelSubsHistory(request)
            # print(f'''Response: {response}''')
            history_info = []
            for i in response.channel_subs_history:
                current_channel = {}
                current_channel['channel_id'] = i.channel_id
                current_channel['measurements'] = []
                history_values = []
                for value in i.history_values:
                    moment = datetime.datetime.fromtimestamp(value.moment.seconds + value.moment.nanos / 1e9)
                    measurement = {
                        "date": datetime.datetime.fromtimestamp(int(moment.timestamp())),
                        "value": value.value
                    }
                    # history_values.append(measurement)
                    current_channel['measurements'].append(measurement)
                history_info.append(current_channel)
                


                # print(i.history_values)
                
            # print(history_info)
            return {"history_data":history_info}
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
    channel = grpc.insecure_channel(f'''localhost:{vars.CHANNEL_SERICE_PORT}''')
    stub = channel_pb2_grpc.channelServiceStub(channel)


    return 'do some magic!'
