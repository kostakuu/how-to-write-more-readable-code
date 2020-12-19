from abc import ABC


def send_email(address: str) -> None:
    # Imagine I sent the email
    pass


def send_push_notification(address: str) -> None:
    # Imagine I sent the push notification
    pass


# Bad example

class Subscription:
    def __init__(self, channel: str, where: str):
        self.channel = channel
        self.where = where

    def notify(self) -> None:
        if self.channel == 'email':
            send_email(self.where)
        elif self.channel == 'push':
            send_push_notification(self.where)

        raise Exception("Channel not implemented yet...")


# Good example

class SubscriptionBase(ABC):
    def __init__(self, channel: str, where: str):
        self.channel = channel
        self.where = where

    def notify(self) -> None:
        pass


class EmailSubscription(SubscriptionBase):
    def notify(self) -> None:
        send_email(self.where)


class PushSubscription(SubscriptionBase):
    def notify(self) -> None:
        send_push_notification(self.where)
