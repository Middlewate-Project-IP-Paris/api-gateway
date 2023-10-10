# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import scheduler_pb2 as scheduler__pb2


class SchedulerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateScheduler = channel.unary_unary(
                '/scheduler.SchedulerService/CreateScheduler',
                request_serializer=scheduler__pb2.SchedulerRequest.SerializeToString,
                response_deserializer=scheduler__pb2.SchedulerResponse.FromString,
                )
        self.GetAllSchedulers = channel.unary_unary(
                '/scheduler.SchedulerService/GetAllSchedulers',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=scheduler__pb2.SchedulerList.FromString,
                )
        self.ModifyScheduler = channel.unary_unary(
                '/scheduler.SchedulerService/ModifyScheduler',
                request_serializer=scheduler__pb2.ModifySchedulerRequest.SerializeToString,
                response_deserializer=scheduler__pb2.SchedulerResponse.FromString,
                )


class SchedulerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateScheduler(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllSchedulers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ModifyScheduler(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SchedulerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateScheduler': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateScheduler,
                    request_deserializer=scheduler__pb2.SchedulerRequest.FromString,
                    response_serializer=scheduler__pb2.SchedulerResponse.SerializeToString,
            ),
            'GetAllSchedulers': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllSchedulers,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=scheduler__pb2.SchedulerList.SerializeToString,
            ),
            'ModifyScheduler': grpc.unary_unary_rpc_method_handler(
                    servicer.ModifyScheduler,
                    request_deserializer=scheduler__pb2.ModifySchedulerRequest.FromString,
                    response_serializer=scheduler__pb2.SchedulerResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'scheduler.SchedulerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SchedulerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateScheduler(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/scheduler.SchedulerService/CreateScheduler',
            scheduler__pb2.SchedulerRequest.SerializeToString,
            scheduler__pb2.SchedulerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllSchedulers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/scheduler.SchedulerService/GetAllSchedulers',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            scheduler__pb2.SchedulerList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ModifyScheduler(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/scheduler.SchedulerService/ModifyScheduler',
            scheduler__pb2.ModifySchedulerRequest.SerializeToString,
            scheduler__pb2.SchedulerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
