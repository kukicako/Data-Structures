from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.cache = DoublyLinkedList()
        self.limit = limit
        #dictionary stores key value
        self.storage = {}
        


    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage.keys():
            #setting head node to current value
            current_value = self.cache.head
            #looks for match and if not key it loops till it matchess
            while current_value.key is not key:
                current_value = current_value.next
                #taking current value and setting it to the front(head)
            self.cache.move_to_front(current_value)
            return current_value.value
            #if key not in storage return none
        else:
            return None 

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # if the key is in our storage, we're assigning it to value
        # setting current_value to the head node
        if key in self.storage.keys():
            self.storage[key] = value
            current_value = self.cache.head
            # while loop is looking at that current value to see if there is a key, if there is not a key, we are going to the next node in our list, checking to see if
            # there is a key, if so, we are assigning it to our value
            while current_value.key is not key:
                current_value = current_value.next
            current_value.value = value
        # checking to see if our cache is less than the limit, adding that value to the head and storing the key to value
        elif self.cache.length < self.limit:
            self.cache.add_to_head(key, value)
            self.storage[key] = value
        # if our cache.length > the limit, we are removing it the value at the tail and deleting it
        # then taking our node we're trying to insert and adding that to the head and storing the key to our previous value
        else:
            previous_key, previous_value = self.cache.remove_from_tail()
            del self.storage[previous_key]
            self.cache.add_to_head(key, value)
            self.storage[key] = previous_value
