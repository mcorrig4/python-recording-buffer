# Streaming Recording Buffer
python-recording-buffer
A circular queue using NumPy ndarray to store streaming data needed for ML

When you have to enqueue a lot of items without needing copy the array, this is 2 magnitudes faster than slicing. Accessing items and replacing items is O(1). Enqueue and peek are both O(1). Copying the array takes O(n) time.

## Benchmarking results
```ps1
(thermal_venv) PS X:\win10\repos\thermal> python -m timeit -s "import benchmark_circular_buffer as bcb" "bcb.slice_and_copy()"
10 loops, best of 5: 36.7 msec per loop

(thermal_venv) PS X:\win10\repos\thermal> python -m timeit -s "import benchmark_circular_buffer as bcb" "bcb.circular_buffer()" 
200000 loops, best of 5: 1.04 usec per loop

(thermal_venv) PS X:\win10\repos\thermal> python -m timeit -s "import benchmark_circular_buffer as bcb" "bcb.slice_and_copy_assignemnt()"
2 loops, best of 5: 166 msec per loop

(thermal_venv) PS X:\win10\repos\thermal> python -m timeit -r 5 -n 4 -s "import benchmark_circular_buffer as bcb" "bcb.slice_and_copy_assignemnt()"
4 loops, best of 5: 159 msec per loop

(thermal_venv) PS X:\win10\repos\thermal> python -m timeit -r 5 -n 4 -s "import benchmark_circular_buffer as bcb" "bcb.circular_buffer_assignment()" 
4 loops, best of 5: 511 msec per loop
```
