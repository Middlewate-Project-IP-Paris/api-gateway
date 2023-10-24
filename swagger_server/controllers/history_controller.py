import connexion
import six
import grpc
import datetime

from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server import util
from google.protobuf.json_format import MessageToDict

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

                    current_channel['measurements'].append(measurement)
                history_info.append(current_channel)
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
    dict_history_data = {
        "views" : 1,
        "shares" : 2
    }
    history_type = []
    history_type.append(dict_history_data[history_data])

    request = channel_pb2.PostStatHistoryRequest(channel_id = channel_id, post_id = post_id, history_type = history_type)
    response = stub.getPostStatHistory(request)

    post_history = {
        "channel_id" : channel_id,
        "post_id" : post_id,
        "measurements" : []
    }

    d = MessageToDict(response)
    # print(d)
    history_info = []
    values = d['postStatHistory'][0]['postHistory'][0]
    print(values)
    
    if 'historyValues' in values.keys():
        values = values['historyValues']
        for value in values:
            # print(value['moment'])
            # moment = datetime.datetime.fromtimestamp(value['moment'].seconds + value['moment'].nanos / 1e9)
            measurement = {
                        "date": value['moment'],
                        "value": value['value']
                    }
            post_history["measurements"].append(measurement)
    # for i in response.post_stat_history:
        # print(f'''Res: {type(i.post_history.historyValues)}''')
        # history_values = []
        # print(i)
        # for value in i.channel_subs_history:
            # moment = datetime.datetime.fromtimestamp(value.moment.seconds + value.moment.nanos / 1e9)
            # measurement = {
            #     "date": datetime.datetime.fromtimestamp(int(moment.timestamp())),
            #     "value": value.value
            # }

        #     current_channel['measurements'].append(measurement)
        # history_info.append(current_channel)
    # return {"history_data":history_info}

    return post_history

