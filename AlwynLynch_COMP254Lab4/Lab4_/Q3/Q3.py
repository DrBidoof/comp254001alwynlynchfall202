# driver_q3.py
from ans_q3 import AnswerLinkedQueue

def main():
    print("== Q3 Driver: AnswerLinkedQueue.concatenate(Q2) ==")
    q1 = AnswerLinkedQueue()
    q2 = AnswerLinkedQueue()

    for x in [10, 20, 30]:
        q1.enqueue(x)
    for x in [40, 50]:
        q2.enqueue(x)

    print("Before concatenate:")
    print("q1:", q1, "(len:", len(q1), ")")
    print("q2:", q2, "(len:", len(q2), ")")

    q1.concatenate(q2)

    print("After q1.concatenate(q2):")
    print("q1:", q1, "(len:", len(q1), ")")
    print("q2:", q2, "(len:", len(q2), ")  # should be empty")

    out = []
    while not q1.is_empty():
        out.append(q1.dequeue())
    print("Dequeued sequence from q1 (expect [10, 20, 30, 40, 50]):", out)

if __name__ == "__main__":
    main()
