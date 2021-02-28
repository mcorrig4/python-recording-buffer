# test using
python -m timeit -s "import benchmark_circular_buffer as bcb" "bcb.slice_and_copy()"
python -m timeit -s "import benchmark_circular_buffer as bcb" "bcb.circular_buffer()" 
python -m timeit -r 5 -n 4 -s "import benchmark_circular_buffer as bcb" "bcb.slice_and_copy_assignemnt()"
python -m timeit -r 5 -n 4 -s "import benchmark_circular_buffer as bcb" "bcb.circular_buffer_assignment()" 
