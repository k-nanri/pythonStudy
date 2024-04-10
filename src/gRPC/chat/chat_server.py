from concurrent.futures import ThreadPoolExecutor
import json

import grpc
import user_pb2
import user_pb2_grpc
from typing import Iterable
import time

with open("users.json") as fp:
    users = json.load(fp)


class UserManager(user_pb2_grpc.UserManagerServicer):
    def get(self, request, context):
        """
        ユーザ情報を取得する
        """
        user_id = request.id

        if str(user_id) not in users:
            return user_pb2.UserResponse(error=True, message="not found")

        user = users[str(user_id)]

        result = user_pb2.User()
        result.id = user["id"]
        result.nickname = user["nickname"]
        result.mail_address = user["mail_address"]
        result.user_type = user_pb2.User.UserType.Value(user["user_type"])

        return user_pb2.UserResponse(error=False, user=result)

    def get_client_stream(self, request_iter: Iterable[user_pb2.UserRequest], context):
        print("call get_client_stream!!")
        user_cnt = 0
        for request in request_iter:
            user_id = request.id
            if str(user_id) in users:
                print("user count up")
                user_cnt += 1
                time.sleep(5)

        result = user_pb2.User()
        result.id = user_cnt
        return user_pb2.UserResponse(error=False, user=result)

    def get_server_stream(self, request, context):
        print("リクエストを受信")
        user_id_list = [u for u in users]
        print("user_id_list", user_id_list)

        for u_id in user_id_list:
            user = users[u_id]

            """
            if user_pb2.User.UserType.Name(request.user_type) == user["user_type"]:
                print(f"{user['id']}---該当あり---")
                result = user_pb2.User(
                    id=user["id"],
                    nickname=user["nickname"],
                    mail_address=user["mail_address"],
                    user_type=user_pb2.User.UserType.Value(user["user_type"]),
                )
                yield user_pb2.UserResponse(error=False, user=result)
            """
            result = user_pb2.User(
                id=user["id"],
                nickname=user["nickname"],
                mail_address=user["mail_address"],
                user_type=user_pb2.User.UserType.Value(user["user_type"]),
            )
            yield user_pb2.UserResponse(error=False, user=result)


def main():

    server = grpc.server(ThreadPoolExecutor(max_workers=2))
    user_pb2_grpc.add_UserManagerServicer_to_server(UserManager(), server)
    server.add_insecure_port("[::]:1234")
    print("Start Server!!!")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    main()
