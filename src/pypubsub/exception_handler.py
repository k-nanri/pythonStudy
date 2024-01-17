from pubsub import pub

class MyHandler(pub.IListenerExcHandler):
    def __call__(self, listerID, topicObj):
        print("listerID = " + str(listerID))
        print("topicObj = " + str(topicObj))

def listener1(arg1, arg2=None):
    print("Call listener1")
    raise Exception("aa")

def listener2(arg1, arg2=None):
    print("Call listener2")
    raise Exception("aa")

def start_pubsub():

    pub.setListenerExcHandler(MyHandler())

    print("subscribe")
    pub.subscribe(listener1, "topic1")
    pub.subscribe(listener2, "topic1")

    print("sendMessage!!")
    try:
        pub.sendMessage("topic1", arg1="hoge1", arg2="hoge2")
    except Exception as e:
        print("Occur Exception")


start_pubsub()