# experiments.py
import random
import time
from hashmap_base import ChainHashMap, ProbeHashMap

def measure_inserts(MapClass, max_load, n_keys=20_000, repeats=3):
    """Return average insertion time (seconds) for n_keys random keys."""
    avg_time = 0.0
    for _ in range(repeats):
        m = MapClass(max_load=max_load)
        keys = random.sample(range(10 * n_keys), n_keys)
        start = time.perf_counter()
        for k in keys:
            m[k] = k
        end = time.perf_counter()
        avg_time += (end - start)
    return avg_time / repeats


def measure_gets(MapClass, max_load, n_keys=20_000, repeats=3):
    """Insert keys once, then measure average successful lookup time."""
    avg_time = 0.0
    for _ in range(repeats):
        m = MapClass(max_load=max_load)
        keys = random.sample(range(10 * n_keys), n_keys)
        # build table
        for k in keys:
            m[k] = k

        start = time.perf_counter()
        for k in keys:
            _ = m[k]
        end = time.perf_counter()
        avg_time += (end - start)
    return avg_time / repeats


def run_experiments():
    """
    Run experiments on ChainHashMap and ProbeHashMap
    for different max load factors, and return a summary
    dictionary for the driver to print.
    """
    results = []

    # you can tweak these lists if you want more / fewer points
    chain_loads = [0.3, 0.5, 0.75, 0.9]
    probe_loads = [0.3, 0.5, 0.6]

    n_keys = 20_000
    repeats = 3

    # ChainHashMap experiments
    for lf in chain_loads:
        ins_time = measure_inserts(ChainHashMap, lf, n_keys=n_keys, repeats=repeats)
        get_time = measure_gets(ChainHashMap, lf, n_keys=n_keys, repeats=repeats)
        results.append({
            "map_type": "ChainHashMap",
            "max_load": lf,
            "insert_time": ins_time,
            "get_time": get_time,
            "n_keys": n_keys,
        })

    # ProbeHashMap experiments
    for lf in probe_loads:
        ins_time = measure_inserts(ProbeHashMap, lf, n_keys=n_keys, repeats=repeats)
        get_time = measure_gets(ProbeHashMap, lf, n_keys=n_keys, repeats=repeats)
        results.append({
            "map_type": "ProbeHashMap",
            "max_load": lf,
            "insert_time": ins_time,
            "get_time": get_time,
            "n_keys": n_keys,
        })

    return results
