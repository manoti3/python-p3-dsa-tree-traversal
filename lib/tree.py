class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        # perform depth-first traversal
        stack = [self.root]

        while stack:
            node = stack.pop()

            # check if the current node matches the desired ID
            if node['id'] == id:
                return node
            
            # Add children to the traversal
            stack.extend(node['children'])

        # return None, if no matching element is found
        return None