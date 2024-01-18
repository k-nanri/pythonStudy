from pubsub import pub
from pubsub.core import INotificationHandler
from pubsub.core.listener import Listener
from pubsub.core.topicobj import Topic

class MyNotifHandler(INotificationHandler):
    def notifySubscribe(self, *args, **kwargs):
        print("notifySubscribe#MyNotifHandler called")

    def notifySend(self, stage: str, topicObj: Topic, pubListener: Listener = None):
        print("notifySend#MyNotifHandler called")


def listener1(arg1, arg2=None):
    print("Call listener1")


pub.addNotificationHandler(MyNotifHandler())
pub.setNotificationFlags(subscribe=True, sendMessage=True)

print("Call subscribe function")
pub.subscribe(listener1, "topic1")
print("Call sendMessage")
pub.sendMessage("topic1", arg1="sendmessage")

