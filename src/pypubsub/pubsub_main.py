from pubsub import pub

class MyHandler(pub.IListenerExcHandler):
    def __call__(self, listerID, topicObj):
        print("listerID = " + str(listerID))
        print("topicObj = " + str(topicObj))

def listener1(a, b, arg1, arg2=None):
    print("Function listener1 received:")
    print("  arg1 = ", arg1)
    print("  arg2 = ", arg2)
    raise Exception("aa")

def listener2(arg1, arg2=None, arg3=None):
    print("Function listener2 received:")
    print("  arg1 = ", arg1)
    print("  arg2 = ", arg2)

def start_pubsub():

    pub.setListenerExcHandler(MyHandler())

    pub.subscribe(listener1, "topic1", a=2, b=3)
    pub.subscribe(listener2, "topic2")

    print(pub.isSubscribed(listener1, "topic2"))
    pub.sendMessage("topic1", arg1="hoge1", arg2="hoge2")

    print("=== isValid ============")
    pub.isValid(listener1, "topic1", curriedArgNames=None)
    pub.isValid(listener1, "topic1", curriedArgNames=["a", "b"])

    

start_pubsub()