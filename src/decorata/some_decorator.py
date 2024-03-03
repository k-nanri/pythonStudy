from typing import final, override, overload


class Base:
    @final
    def done(self) -> None:
        print("done from Base")

    def call(self) -> None:
        print("call!!")


class Child(Base):
    def done(self) -> None:
        print("done from Child")

    @override
    def call(self) -> None:
        print("Child call")


@overload
def say(name: str, address: str):
    print("say name = " + name + ", address = " + address)


def say(name: str):
    print("say name = " + name)


child = Child()
child.done()
child.call()

say("sato")
say("sato", "Tokyo")
