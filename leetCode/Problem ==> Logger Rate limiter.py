class Logger:
    """
    Keep a dictionary of next time in the future where a just printed message can become valid to print again.
    Basically the important thing is to set a valid time in the future to check incoming messages against.
    """

    def __init__(self):
        self.messages = dict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        print(self.messages)
        if message in self.messages:
            if timestamp >= self.messages[message]:
                self.messages[message] = timestamp + 10
                return True
            else:
                return False
        else:
            self.messages[message] = timestamp + 10
            return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
