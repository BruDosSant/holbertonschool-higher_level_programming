class CountedIterator:
    """
    A custom iterator that keeps track of the number of items iterated.
    """
    
    def __init__(self, iterable):
        """
        Initializes the CountedIterator with an iterable and a counter.
        """
        self.iterator = iter(iterable)
        self.counter = 0
    
    def __next__(self):
        """
        Returns the next item from the iterator, incrementing the counter each time.
        If there are no more items, raises StopIteration.
        """
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration
    
    def get_count(self):
        """
        Returns the current count of how many items have been iterated.
        """
        return self.counter

if __name__ == "__main__":
    iterable = [1, 2, 3, 4, 5]
    counted_iter = CountedIterator(iterable)
    
    for item in counted_iter:
        print(f"Item: {item}")
    
    print(f"Total items iterated: {counted_iter.get_count()}")
