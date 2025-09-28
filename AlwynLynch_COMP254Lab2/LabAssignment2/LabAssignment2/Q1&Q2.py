# -*- coding: utf-8 -*-
# Experimental analysis of prefix_average1 (O(n^2)) vs prefix_average2 (O(n))
import random
import time
import statistics
from prefix_average import prefix_average1, prefix_average2;

def time_func(func, n: int, trials: int = 5, seed: int = 42) -> float:
    """Return median time (seconds) to run func on a random array of length n."""
    rng = random.Random(seed)
    times = []
    for t in range(trials):
        arr = [rng.random() for _ in range(n)]
        start = time.perf_counter()
        func(arr)
        elapsed = time.perf_counter() - start
        times.append(elapsed)
        rng.seed(seed + t + 1)
    return statistics.median(times)

def run_experiment() -> None:
    # Keep n modest for the O(n^2) algorithm
    ns_quad_safe = [128, 256, 512, 1024, 2048, 3072, 4096]
    ns_linear    = [128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]

    rows = []
    for n in ns_quad_safe:
        t = time_func(prefix_average1, n)
        rows.append(("prefix_average1 O(n^2)", n, t))

    for n in ns_linear:
        t = time_func(prefix_average2, n)
        rows.append(("prefix_average2 O(n)", n, t))

    rows.sort(key=lambda r: (r[0], r[1]))
    print("\nAlgorithm, n, time_sec")
    for algo, n, t in rows:
        print(f"{algo}, {n}, {t:.6f}")

if __name__ == "__main__":
    run_experiment()
