#My answer #######################################################################################
    def reverse(self):
        """Reverse the list in place in O(n) time and O(1) extra space."""
        if self._size <= 1:
            return  

        prev = None
        current = self._head
        # Old head will become the new tail
        self._tail = self._head

        while current is not None:
            nxt = current.get_next()   
            current.set_next(prev)      
            prev = current             
            current = nxt              

        # prev is the new head
        self._head = prev