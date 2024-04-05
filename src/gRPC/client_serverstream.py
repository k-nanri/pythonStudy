import pprint
import sys

import grpc
import user_pb2
import user_pb2_grpc


def main():

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


if __name__ == "__main__":
    main()
