from entry import Entry

class NetworkCollection:
    def __init__(self, ipv4_network, raw_entry_list):
        """
        Constructor for NetworkCollection data structure.

        self.ipv4_network -> ipaddress.IPv4Network
        self.entries -> list(Entry)
        """

        self.ipv4_network = ipv4_network
        self.entries = raw_entry_list

        pass

    def ipaddress(self):

    def entries(self)
        Entry.get_address()
        Entry.__bool__()
        Entry.get_datetime
        self.add.append(address)



    def remove_invalid_records(self):
        """
        Removes invalid objects from the entries list.
        """

        pass

    def sort_records(self):
        """
        Sorts the list of associated entries in ascending order.
        DO NOT change this method, make the changes in entry.py :)
        """

        self.entries = sorted(self.entries)
