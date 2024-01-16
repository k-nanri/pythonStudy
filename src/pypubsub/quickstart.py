from pubsub import pub
from pubsub.core import INotificationHandler

class MyNotifHandler(INotificationHandler):
    def notifySubscribe(self, *args, **kwargs):
        print("hoge")

pub.setNotificationFlags(subscribe=True)
pub.addNotificationHandler(MyNotifHandler())

def listener1(arg1, arg2=None):
    print("Function listener1 received:")
    print("  arg1 = ", arg1)
    print("  arg2 = ", arg2)

def listener2(arg1, arg2=None, arg3=None):
    print("Function listener2 received:")
    print("  arg1 = ", arg1)
    print("  arg2 = ", arg2)
    print("  arg3 = ", arg3)

pub.subscribe(listener1, "rootTopic")
pub.subscribe(listener2, "rootTopic.child")

print("Publish something via pubsub")
anObj = dict(a=456, b='abc')

pub.sendMessage("rootTopic.child", arg1 = 123, arg2 = anObj)
print("After sendMessage")