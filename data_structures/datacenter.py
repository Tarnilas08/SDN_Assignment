import re
from cluster import Cluster

class Datacenter:
    def __init__(self, name, cluster_dict):
        """
        Constructor for Datacenter data structure.

        self.name -> str
        self.clusters -> list(Cluster)
        """
        
        self.name = name
        self.cluster = cluster_dict

        pass

    def get_name(self):
        return self.name
    
    def Clusters(self):
        

    def remove_invalid_clusters(self):
        """
        Removes invalid objects from the clusters list.
        """



        pass
