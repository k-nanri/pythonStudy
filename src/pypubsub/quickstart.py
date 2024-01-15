from pubsub import pub

def listener1(arg1, arg2=None):
    print("Function listener1 received:")
    print("  arg1 = ", arg1)
    print("  arg2 = ", arg2)

def listener2(arg1, arg2=None):
    print("Function listener2 received:")
    print("  arg1 = ", arg1)
    print("  arg2 = ", arg2)

pub.subscribe(listener1, "rootTopic")
pub.subscribe(listener2, "rootTopic")

print("Publish something via pubsub")
anObj = dict(a=456, b='abc')

pub.sendMessage("rootTopic", arg1 = 123, arg2 = anObj)
print("After sendMessage")