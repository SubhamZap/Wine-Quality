class NotInRange(Exception):
    def __init__(self, message = "value not in range"):
        self.message = message
        super().__init__(self.message)

def test_generic():
    a = 5
    if a not in range(10, 15):
        raise NotInRange
    