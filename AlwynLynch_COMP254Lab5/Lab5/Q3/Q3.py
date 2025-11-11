# q3_driver.py
from q3_heap import HeapPriorityQueue

def main():
    print("Building heap with (key,value):")
    items = [(5, "E"), (3, "C"), (7, "G"), (1, "A"), (4, "D"), (2, "B")]
    pq = HeapPriorityQueue()
    for k, v in items:
        print(f"  add({k}, {v})")
        pq.add(k, v)

    print("\nPeek min():", pq.min())

    popped = []
    while not pq.is_empty():
        popped.append(pq.remove_min())
    print("remove_min() order:", popped)
    # Expect ascending by key: [(1,'A'), (2,'B'), (3,'C'), (4,'D'), (5,'E'), (7,'G')]

if __name__ == "__main__":
    main()
