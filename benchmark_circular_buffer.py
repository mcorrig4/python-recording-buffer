# benchmark_circular_buffer.py
import numpy as np

# all operations are O(1) and don't require copying the array
# except to_array which has to copy the array and is O(n)
class RecordingQueue1D:
    def __init__(self, object: object, maxlen: int):
        #allocate the memory we need ahead of time
        self.max_length: int = maxlen
        self.queue_tail: int = maxlen - 1
        o_len = len(object)
        if (o_len == maxlen):
            self.rec_queue = np.array(object, dtype=np.int64)
        elif (o_len > maxlen):
            self.rec_queue = np.array(object[o_len-maxlen:], dtype=np.int64)
        else:
            self.rec_queue = np.append(np.array(object, dtype=np.int64), np.zeros(maxlen-o_len, dtype=np.int64))
            self.queue_tail = o_len - 1

    def to_array(self) -> np.array:
        head = (self.queue_tail + 1) % self.max_length
        return np.roll(self.rec_queue, -head) # this will force a copy

    def enqueue(self, new_data: np.array) -> None:
        # move tail pointer forward then insert at the tail of the queue
        # to enforce max length of recording
        self.queue_tail = (self.queue_tail + 1) % self.max_length        
        self.rec_queue[self.queue_tail] = new_data

    def peek(self) -> int:
        queue_head = (self.queue_tail + 1) % self.max_length
        return self.rec_queue[queue_head]

    def replace_item_at(self, index: int, new_value: int):
        loc = (self.queue_tail + 1 + index) % self.max_length
        self.rec_queue[loc] = new_val

    def item_at(self, index: int) -> int:
        # the item we want will be at head + index
        loc = (self.queue_tail + 1 + index) % self.max_length
        return self.rec_queue[loc]

    def __repr__(self):
        return "tail: " + str(self.queue_tail) + "\narray: " + str(self.rec_queue)

    def __str__(self):
        return "tail: " + str(self.queue_tail) + "\narray: " + str(self.rec_queue)
        # return str(self.to_array())


rnd_arr = np.random.randint(0, 1e6, 10**8)
new_val = -100

slice_arr = rnd_arr.copy()
c_buf_arr = RecordingQueue1D(rnd_arr.copy(), len(rnd_arr))

# Test speed for queuing new a new item
# swapping items 100 and 1000
# swapping items 10000 and 100000
def slice_and_copy():
    slice_arr[:-1] = slice_arr[1:]
    slice_arr[-1] = new_val
    old = slice_arr[100]
    slice_arr[100] = slice_arr[1000]
    old = slice_arr[10000]
    slice_arr[10000] = slice_arr[100000]

def circular_buffer():
    c_buf_arr.enqueue(new_val)
    old = c_buf_arr.item_at(100)
    slice_arr[100] = slice_arr[1000]
    old = slice_arr[10000]
    slice_arr[10000] = slice_arr[100000]

# lets add copying the array to a new numpy.array
# this will take O(N) time for the circular buffer because we use numpy.roll()
# which copies the array.
def slice_and_copy_assignemnt():
    slice_and_copy()
    my_throwaway_arr = slice_arr.copy()
    return my_throwaway_arr

def circular_buffer_assignment():
    circular_buffer()
    my_throwaway_arr = c_buf_arr.to_array().copy()
    return my_throwaway_arr


# test using
# python -m timeit -s "import benchmark_circular_buffer as bcb" "bcb.slice_and_copy()"
# python -m timeit -s "import benchmark_circular_buffer as bcb" "bcb.circular_buffer()" 
# python -m timeit -r 5 -n 4 -s "import benchmark_circular_buffer as bcb" "bcb.slice_and_copy_assignemnt()"
# python -m timeit -r 5 -n 4 -s "import benchmark_circular_buffer as bcb" "bcb.circular_buffer_assignment()" 
