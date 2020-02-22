from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.current is None and self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
        elif self.storage.length == self.capacity:
            if self.current is None:
                self.current = self.storage.head.next
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
            elif self.current != self.storage.tail:
                self.current = self.current.next
                self.storage.delete(self.current.prev)
                self.current.insert_before(item)
                self.storage.length += 1
            else:
                self.current = None
                self.storage.remove_from_tail()
                self.storage.add_to_tail(item)


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        cur_node = self.storage.head
        while cur_node is not None:
            if cur_node.value is not None:
                list_buffer_contents.append(cur_node.value)
            cur_node = cur_node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
