# main.py
import time, random, math
from uniqueness import unique1, unique2

TIME_LIMIT = 30.0     # seconds
TOL = 1.0             # stop binary search when |t-60| <= 1s
MAX_PRINT = 40        # cap log lines

print_count = 0
def log(msg):
    global print_count
    if print_count < MAX_PRINT:
        print(msg)
        print_count += 1

def gen_unique_array(n: int):
    # Worst case for unique1 is "no duplicates"; no need to shuffle.
    # Using list(range(n)) keeps it simple and avoids extra cost.
    return list(range(n))

def time_once(func, n: int) -> float:
    arr = gen_unique_array(n)
    t0 = time.perf_counter()
    func(arr)
    return time.perf_counter() - t0

def max_n_within(func, label: str, limit: float = TIME_LIMIT) -> int:
    # 0) quick warm-up
    _ = time_once(func, 256)

    # 1) small model-based guess (reduces probing):
    #    For unique1 ~ k*n^2; for unique2 ~ k*n*log2(n).
    #    Estimate k from two quick points, then solve for n.
    def estimate_k_quad():
        t = max(time_once(func, 1024), 1e-9)
        return t / (1024**2)
    def estimate_k_nlogn():
        n = 4096
        t = max(time_once(func, n), 1e-9)
        return t / (n * math.log2(n))

    if func is unique1:
        k = estimate_k_quad()
        n_guess = int(math.sqrt(limit / k))
    else:
        k = estimate_k_nlogn()
        # Solve limit = k * n * log2(n) by doubling up then binary
        n_guess = 1
        while k * n_guess * max(math.log2(n_guess), 1) < limit:
            n_guess *= 2
        # back off a bit
        n_guess = n_guess // 2 or 1

    # 2) bracket around guess by exponential expand/contract
    lo = max(1, n_guess // 2)
    hi = max(n_guess, lo + 1)
    while True:
        t = time_once(func, hi)
        log(f"[{label}] try n={hi} time={t:.3f}s")
        if t > limit:
            break
        lo = hi
        hi = int(hi * 1.5) + 1  # gentler than x2 to avoid huge overshoot

    # 3) binary search with tolerance
    best = lo
    while lo <= hi:
        mid = (lo + hi) // 2
        t = time_once(func, mid)
        # keep logs limited
        log(f"[{label}] mid n={mid} time={t:.3f}s")
        if t <= limit:
            best = mid
            # close enough? stop early
            if abs(t - limit) <= TOL:
                break
            lo = mid + 1
        else:
            hi = mid - 1
    print(f"[{label}] max n within {limit:.1f}s: {best}")
    return best

def main():
    print("=== Experimental max n within 60 seconds ===")
    n1 = max_n_within(unique1, "unique1  O(n^2)")
    print()
    n2 = max_n_within(unique2, "unique2  O(n log n)")
    print("\n=== Results ===")
    print(f"unique1  (O(n^2))    max n ≈ {n1}")
    print(f"unique2  (O(n log n)) max n ≈ {n2}")

if __name__ == "__main__":
    main()
