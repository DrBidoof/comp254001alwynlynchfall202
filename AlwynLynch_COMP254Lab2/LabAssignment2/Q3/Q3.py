# main.py — Simple doubling-time experiment for unique1 vs unique2
import sys
import time
from uniqueness import unique1, unique2

def gen_unique_array(n: int):
    # Worst case for a naive duplicate check is "no duplicates"
    return list(range(n))

def time_once(func, n: int) -> float:
    arr = gen_unique_array(n)
    t0 = time.perf_counter()
    func(arr)
    return (time.perf_counter() - t0) * 1000.0  # milliseconds

def run_trials(func, label: str, trials: int, start_n: int):
    n = start_n
    print(f"Testing {label}...")
    for _ in range(trials):
        elapsed_ms = time_once(func, n)
        print(f"n: {n:9d} took {int(elapsed_ms):12d} ms")
        n *= 2  # double the problem size

def main():
    # Defaults chosen to keep unique1 from taking forever;
    trials = 8
    start_n = 256



    # Run the quicker one first (analogy to repeat2), then the slower one.
    run_trials(unique2, "unique2 (O(n log n))", trials, start_n)
    run_trials(unique1, "unique1 (O(n^2))",     trials, start_n)

if __name__ == "__main__":
    main()
