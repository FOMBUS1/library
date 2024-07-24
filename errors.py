class BookAlreadyExists(Exception):
    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return self.message

class BookNotFound(Exception):
    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return self.message
    
class OutOfBounds(Exception):
    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return self.message
    
class InvalidArguments(Exception):
    def __init__(self, message):
        self.message = message
    
    def __repr__(self):
        return self.message
    
class InvalidStatus(Exception):
    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return self.message