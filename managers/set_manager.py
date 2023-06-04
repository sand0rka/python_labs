"""
This is set manager file
"""


class SetManager:
    """
    A class that represents a set manager.

    Args:
        regular_manager (TransportManager): The regular manager object containing the transports.

    Attributes:
        regular_manager (TransportManager): The regular manager object containing the transports.
        current_index (int): The current index for iterating over the transports.

    """

    def __init__(self, regular_manager):
        """
        Initializes a set_manager object.

        """
        self.regular_manager = regular_manager
        self.current_index = 0

    def __iter__(self):
        """
        Iterates over the transports in the transport manager.

        Yields:
            Transport: The next transport object in the iteration.

        """
        for transport in self.regular_manager.transports:
            yield transport

    def __len__(self):
        """
        Returns the total length of all fuel sets in the transport manager.

        Returns:
            int: The total length of the fuel sets.

        """
        length = 0
        for transport in self.regular_manager.transports:
            length += len(transport)
        return length

    def __getitem__(self, index):
        """
        Retrieves the item at the specified index from the combined fuel sets.

        Args:
            index (int): The index of the item to retrieve.

        Returns:
            object: The item at the specified index.

        Raises:
            IndexError: If the index is out of range.

        """
        for transport in self.regular_manager.transports:
            return transport[index]
        raise IndexError("Index out of range")

    def __next__(self):
        """
        Returns the next fuel set in the iteration.

        Returns:
            set: The next fuel set.

        Raises:
            StopIteration: If all fuel sets have been iterated over.

        """
        if self.current_index >= len(self):
            raise StopIteration
        result = self[self.current_index]
        self.current_index += 1
        return result
