import datetime

class Entry:
    def __init__(self, address, available, last_used):
        """
        Constructor for Entry data structure.

        self.address -> str
        self.available -> bool
        self.last_used -> datetime
        """

        self.address = address
        self.available = available
        self.last_used = last_used

        pass

    def get_address(self):
        return self.address
    
    def __bool__(self):
        if self.available == 1:
            return True
        else:
            return False
    
    def get_datetime(self):
        self.last_used = datetime.datetime.now()
        return self.last_used

