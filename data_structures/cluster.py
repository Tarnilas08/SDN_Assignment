from network_collection import NetworkCollection

class Cluster:
    def __init__(self, name, network_dict, security_level):
        """
        Constructor for Cluster data structure.

        self.name -> str
        self.security_level -> int
        self.networks -> list(NetworkCollection)
        """

        self.name = name
        self.security_level = security_level
        self.network_dict = network_dict

        pass

    def get_name(self):
        return self.name
    
    def get_securitylevel(self):
        return self.security_level

    def networks(self):
        
