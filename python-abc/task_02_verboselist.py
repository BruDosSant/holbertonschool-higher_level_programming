class VerboseList(list):
    """
    A custom list class that prints notifications when items are added or removed.
    """
    
    def append(self, item):
        """
        Adds an item to the list and prints a notification.
        """
        super().append(item)
        print(f"Added {item} to the list.")
    
    def extend(self, iterable):
        """
        Extends the list with items from an iterable and prints a notification.
        """
        super().extend(iterable)
        print(f"Extended the list with {len(iterable)} items.")
    
    def remove(self, item):
        """
        Removes an item from the list and prints a notification.
        If the item doesn't exist, raise a ValueError.
        """
        print(f"Removed {item} from the list.")
        super().remove(item)
    
    def pop(self, index=-1):
        """
        Pops an item from the list and prints a notification.
        If no index is provided, the last item is popped by default.
        """
        item = super().pop(index)
        print(f"Popped {item} from the list.")
        return item
