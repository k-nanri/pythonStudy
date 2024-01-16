from pubsub import pub

def listener1(arg1, arg2=None):
    print("Function listener1 received:")
    print("  arg1 = ", arg1)
    print("  arg2 = ", arg2)

def listener2(arg1, arg2=None, arg3=None):
    print("Function listener2 received:")
    print("  arg1 = ", arg1)
    print("  arg2 = ", arg2)

def start_pubsub():

    pub.subscribe(listener1, "topic1")
    pub.subscribe(listener2, "topic2")

    print(pub.isSubscribed(listener1, "topic2"))
    pub.sendMessage("topic1", arg1="hoge1", arg2="hoge2")
    

start_pubsub()