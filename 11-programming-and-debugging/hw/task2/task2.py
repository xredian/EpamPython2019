import hashlib
import os

h = hashlib.sha256(b'hw.py')
my_dir = '/Users/xredian/Documents/EpamPython2019/11-programming-and-debugging/hw/'
my_hash = h.hexdigest()


def path(directory, hash256):
    paths = []
    files = os.listdir(directory)
    for file in files:
        file_hash = hashlib.sha256(bytes(file, encoding='utf8')).hexdigest()
        if file_hash == hash256:
            paths.append(os.path.abspath(file))
    return paths


print(path(my_dir, my_hash))

"""
1) sudo dtruss -c python3 task2.py 2> ./trace.txt
>>>
most commonly used system call is stat64 = 208 calls

2) python3 -m cProfile -s time task2.py 1000001 > ./profile.txt
>>>
the "hottest" piece of code is {built-in method _imp.create_dynamic}
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    0.011    0.004    0.011    0.004 {built-in method _imp.create_dynamic}
        
3) strace -c python3 task2.py 2> ./time.txt
most time consuming system call is mmap 

% time     seconds  usecs/call     calls    errors syscall
------ ----------- ----------- --------- --------- ----------------
 16,67    0,000538           9        55           mmap
 
 
full results are in files trace.txt, profile.txt and time.txt
"""


