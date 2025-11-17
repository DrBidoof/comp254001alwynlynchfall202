# driver_ex2.py
from sorted_table_map_solution import SortedTableMapSolution

def main():
    m = SortedTableMapSolution()

    # Insert keys (including a None value to test ambiguity)
    m["apple"] = 1
    m["banana"] = None
    m["cherry"] = 3

    test_keys = ["apple", "banana", "date"]

    for key in test_keys:
        print(f"containsKey({key!r}) -> {m.containsKey(key)}")
        if m.containsKey(key):
            print(f"  value = {m[key]!r}")
        print()

if __name__ == "__main__":
    main()
