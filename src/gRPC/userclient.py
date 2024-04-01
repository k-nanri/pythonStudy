import pprint
import sys

import grpc
import user_pb2
import user_pb2_grpc


def main():

    if len(sys.argv) < 2:
        print("usage: {} <user_id".format(sys.argv[0]))
        sys.exit(0)

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        print("error: invalid user_id `{}'".format(sys.argv[1]))
        sys.exit(0)

    req = user_pb2.UserRequest(id=user_id)

    with grpc.insecure_channel("localhost:1234") as channel:
        stub = user_pb2_grpc.UserManagerStub(channel)
        response = stub.get(req)

    pprint.pprint(response)


if __name__ == "__main__":
    main()
