import numpy as np


# all operations are O(1) and don't require copying the array
# except to_array which has to copy the array and is O(n)
class RecordingQueue:
    def __init__(self, object: object, maxlen: int, num_sensors: int):
        self.rec_queue: np.array = np.zeros(shape=(maxlen, num_sensors), dtype=np.int32) #allocate the memory we need ahead of time
        self.max_length: int = maxlen
        self.queue_tail: int = maxlen - 1
        if (len(object) > 0):
            for val in object:
                self.enqueue(val)

    def to_array(self) -> np.array:
        head = (self.queue_tail + 1) % self.max_length
        return np.roll(self.rec_queue, -head, axis=0) # this will force a copy

    def enqueue(self, new_data: np.array) -> None:
        # move tail pointer forward then insert at the tail of the queue
        # to enforce max length of recording
        self.queue_tail = (self.queue_tail + 1) % self.max_length        
        self.rec_queue[self.queue_tail] = new_data

    def peek(self) -> int:
        queue_head = (self.queue_tail + 1) % self.max_length
        return self.rec_queue[queue_head]
    def item_at(self, index: int) -> int:
        # the item we want will be at head + index
        loc = (self.queue_tail + 1 + index) % self.max_length
        return self.rec_queue[loc]
    def __repr__(self):
        return "tail: " + str(self.queue_tail) + "\narray: " + str(self.rec_queue)
    def __str__(self):
        return "tail: " + str(self.queue_tail) + "\narray:\n" + str(self.rec_queue)
        return str(self.to_array())

