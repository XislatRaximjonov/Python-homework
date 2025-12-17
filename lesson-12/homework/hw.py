def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

import threading

def check_primes(start, end, result):
    for num in range(start, end):
        if is_prime(num):
            result.append(num)

import threading

start_range = 1
end_range = 100
num_threads = 4

threads = []
results = []

step = (end_range - start_range) // num_threads

for i in range(num_threads):
    start = start_range + i * step
    end = start_range + (i + 1) * step

    if i == num_threads - 1:
        end = end_range

    t = threading.Thread(target=check_primes, args=(start, end, results))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

results.sort()
print("Topilgan tub sonlar:")
print(results)


import threading
from collections import Counter


def count_words(lines, result):
    local_counter = Counter()

    for line in lines:
        words = line.lower().split()
        local_counter.update(words)

    result.append(local_counter)


filename = "text.txt"
num_threads = 4

with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()

chunk_size = len(lines) // num_threads
threads = []
results = []

for i in range(num_threads):
    start = i * chunk_size
    end = (i + 1) * chunk_size

    if i == num_threads - 1:
        end = len(lines)

    t = threading.Thread(
        target=count_words,
        args=(lines[start:end], results)
    )
    threads.append(t)
    t.start()

for t in threads:
    t.join()

final_count = Counter()
for counter in results:
    final_count.update(counter)

print("So‘zlar statistikasi:")
for word, count in final_count.most_common(10):
    print(f"{word}: {count}")
