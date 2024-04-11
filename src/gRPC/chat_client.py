import pprint
import sys
import time
import grpc
import user_pb2
import user_pb2_grpc

"""
server streaming
"""


def server_streaming():

    if len(sys.argv) < 2:
        print("usage: {} <user_type".format(sys.argv[0]))
        sys.exit(0)

    try:
        user_type = int(sys.argv[1])
    except ValueError:
        print("error: invalid user_type `{}'".format(sys.argv[1]))
        sys.exit(0)

    req = user_pb2.UserRequest(user_type=user_type)

    with grpc.insecure_channel("localhost:1234") as channel:
        stub = user_pb2_grpc.UserManagerStub(channel)
        response = stub.get_server_stream(req)

    pprint.pprint(response)


def create_data():
    for user_id in [1, 2, 3]:
        time.sleep(10)
        print("user_id = " + str(user_id))
        req = user_pb2.UserRequest(id=user_id)
        yield req


def send_message(stub, msg, id):
    messages = []
    messages.append(user_pb2.ChatMessage(id=id, message=msg))
    responses = stub.connect_chat(iter(messages))
    for res in responses:
        print("Received message [id={}, msg={}]".format(res.id, res.message))


def client_streaming():
    print("call client streaming!!")
    # req_list = []
    id = 1
    with grpc.insecure_channel("localhost:1234") as channel:
        stub = user_pb2_grpc.UserManagerStub(channel)
        print("--- Input your message -------")
        while True:
            msg = input("Input message >")
            send_message(stub, msg, id)
            id += 1

    #    stub = user_pb2_grpc.UserManagerStub(channel)
    #    response = stub.get_client_stream(iter(req_list))
    #    pprint.pprint(response)


if __name__ == "__main__":
    # server_streaming()
    print("Start!!")
    client_streaming()
