# driver_ex1.py
from experiments import run_experiments

def main():
    print("=== COMP254 Lab 6 - Exercise 1 ===")
    print("Configurable load factor experiments on ChainHashMap and ProbeHashMap")
    print()

    results = run_experiments()

    # Friendly tabular output
    header = f"{'Map Type':<15} {'Max Load':<10} {'n_keys':<10} {'Insert (s)':<12} {'Get (s)':<12}"
    print(header)
    print("-" * len(header))

    for r in results:
        line = (
            f"{r['map_type']:<15} "
            f"{r['max_load']:<10.2f} "
            f"{r['n_keys']:<10d} "
            f"{r['insert_time']:<12.4f} "
            f"{r['get_time']:<12.4f}"
        )
        print(line)

    print("\nNote: Smaller times indicate better performance.")
    print("Observe how changing the maximum load factor affects performance.")


if __name__ == "__main__":
    main()

