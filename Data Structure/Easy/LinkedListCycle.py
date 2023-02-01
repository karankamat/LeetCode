def hasCycle(self, head):
        curr_node = head
        curr_next_node = head

        while curr_next_node and curr_next_node.next:
            curr_node = curr_node.next
            curr_next_node = curr_next_node.next.next

            if curr_node == curr_next_node:
                return True
        
        return False