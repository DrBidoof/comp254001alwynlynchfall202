# q1_solution.py
from __future__ import annotations
from typing import Optional
from positional_list import PositionalList

class ExtendedPositionalList(PositionalList):
    def indexOf(self, p: PositionalList.Position) -> int:
        idx = 0
        cur = self.first()
        while cur is not None:
            if cur == p:          
                return idx
            idx += 1
            cur = self.after(cur)
        raise ValueError("Position does not belong to this list.")


