# mergesort_solution.py

from queue_class import LinkedQueue, Empty


def merge(q1: LinkedQueue, q2: LinkedQueue) -> LinkedQueue:
    """Merge two sorted queues into and return a new sorted queue.

    Consumes q1 and q2 (they will be empty at the end).
    """
    result = LinkedQueue()

    while not q1.is_empty() and not q2.is_empty():
        if q1.first() <= q2.first():
            result.enqueue(q1.dequeue())
        else:
            result.enqueue(q2.dequeue())

    # Move any remaining elements
    while not q1.is_empty():
        result.enqueue(q1.dequeue())

    while not q2.is_empty():
        result.enqueue(q2.dequeue())

    return result


def bottom_up_merge_sort(iterable):
    """Bottom-up merge-sort using a queue-of-queues.

    Args:
        iterable: Any iterable of comparable items (e.g., list of ints).

    Returns:
        A new Python list with the elements sorted in nondecreasing order.
    """
    # Step 1: create a queue-of-queues, each containing a single element
    master = LinkedQueue()  # this is our "queue of queues"

    for item in iterable:
        q = LinkedQueue()
        q.enqueue(item)
        master.enqueue(q)

    # Edge case: empty input
    if master.is_empty():
        return []

    # Step 2: repeatedly merge pairs of queues until one queue remains
    while len(master) > 1:
        q1 = master.dequeue()
        if master.is_empty():
            # If odd number of runs, just re-enqueue q1
            master.enqueue(q1)
        else:
            q2 = master.dequeue()
            merged = merge(q1, q2)
            master.enqueue(merged)

    # Step 3: extract the sorted elements from the final queue
    sorted_queue = master.dequeue()
    result = []
    while not sorted_queue.is_empty():
        result.append(sorted_queue.dequeue())

    return result
