# mergesort_demo.py

from mergesort_solution import bottom_up_merge_sort


def main():
    data_sets = [
        [5, 1, 4, 2, 8, 3],
        [10, 9, 8, 7, 6, 5, 4],
        [],
        [42],
    ]

    for data in data_sets:
        print(f"Original: {data}")
        sorted_data = bottom_up_merge_sort(data)
        print(f"Sorted:   {sorted_data}")
        print("-" * 40)


if __name__ == "__main__":
    main()

