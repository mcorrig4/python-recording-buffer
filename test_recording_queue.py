from recording_buffer import RecordingQueue

start_data = np.array([
    [1,1],
    [2,2],
    [3,3]
])

my_queue = RecordingQueue(start_data, maxlen=RECORDING_BUFFER_SIZE, num_sensors=2)
print ("The current state of the circular array: ")
print(my_queue)
print("Which represents the array:")
print(my_queue.to_array())

my_queue.enqueue([11,11])
my_queue.enqueue([22,22])
my_queue.enqueue([33,33])
my_queue.enqueue([44,44])
print ("The current state of the circular array: ")
print(my_queue)
print("Which represents the array:")
print(my_queue.to_array())

# Peek at the first element in the queue
print("Front of the queue: ", my_queue.peek())

print("See all the items in the queue:")
for i in range(8):
    print("Item ", i , " = ", my_queue.item_at(i))
