from collections import deque

class Node:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # ---------------- INSERT ----------------
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    # ---------------- SEARCH ----------------
    def search(self, value):
        return self._search(self.root, value)

    def _search(self, current, value):
        if current is None:
            return False
        if value == current.value:
            return True
        elif value < current.value:
            return self._search(current.left, value)
        else:
            return self._search(current.right, value)

    # ---------------- DELETE ----------------
    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, current, value):
        if current is None:
            return current

        if value < current.value:
            current.left = self._delete(current.left, value)
        elif value > current.value:
            current.right = self._delete(current.right, value)
        else:
            # Case 1: No children
            if current.left is None and current.right is None:
                return None

            # Case 2: One child
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left

            # Case 3: Two children (Inorder Successor)
            min_node_value = self._min_node_value(current.right)
            current.value = min_node_value.value
            current.right = self._delete(current.right, min_node_value.value)

        return current

    def _min_node_value(self, current):
        while current.left:
            current = current.left
        return current

    # ---------------- TRAVERSALS ----------------
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, current, result):
        if current:
            self._inorder(current.left, result)
            result.append(current.value)
            self._inorder(current.right, result)

    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, current, result):
        if current:
            result.append(current.value)
            self._preorder(current.left, result)
            self._preorder(current.right, result)

    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, current, result):
        if current:
            self._postorder(current.left, result)
            self._postorder(current.right, result)
            result.append(current.value)

    # ---------------- HEIGHT ----------------
    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))
        
    # ---------------- Balanced ----------------
    def is_balanced(self):
        return self.is_height(self.root) != -1
        
    def is_height(self, node):
        if node is None:
            return 0
        left = self.is_height(node.left)
        if left == -1:
            return -1
        right = self.is_height(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    # ---------------- BFS ----------------
    def bfs(self):
        if self.root is None:
            return []
        queue = deque([self.root])
        result = []
        while queue:
            node = queue.popleft()
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

# ---------------- TESTING ----------------
bst = BinarySearchTree()

bst.insert(15)
bst.insert(7)
bst.insert(25)
bst.insert(3)
bst.insert(10)
bst.insert(20)
bst.insert(30)

print(bst.is_balanced())

print("Inorder:", bst.inorder())
print("Preorder:", bst.preorder())
print("Postorder:", bst.postorder())