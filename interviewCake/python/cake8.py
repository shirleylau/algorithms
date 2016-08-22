test1 = [[1, 2], 2]
test2 = [[3, 2, 1], 4]
test3 = [[3, 5, 2], 7]
# test3 = [(-2, 1), (4, 5), (3, 6), (0, 2), (10, 13)]
# test3 = [0, 3, 7, 7, 7, 0]

class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

def create_tree():
    root = attach_nodes(BinaryTreeNode(8), 4, 12)
    # attach_nodes(root.left, 2, 5)
    attach_nodes(root.right, 11, 14)
    root.right.right.insert_right(20)
    root.right.left.insert_left(9)
    root.right.left.left.insert_right(10)
    return root

def attach_nodes(parent, left_val, right_val):
    parent.insert_left(left_val)
    parent.insert_right(right_val)
    return parent

tree_root = create_tree()

################## Start of Solution #####################

def check_superbalanced(root):
    is_superbalanced, leaf_depth_bounds = traverse_preorder(root, 0, [])
    print is_superbalanced and leaf_depth_bounds[1] - leaf_depth_bounds[0] <= 1

def traverse_preorder(node, curr_depth, leaf_depth_bounds):
    print 'Current Value: ', node.value
    is_superbalanced = True
    curr_depth += 1
    if node.left is None and node.right is None:
        if (curr_depth not in leaf_depth_bounds):
            leaf_depth_bounds.append(curr_depth)
            if len(leaf_depth_bounds) > 1:
                leaf_depth_bounds = [min(leaf_depth_bounds), max(leaf_depth_bounds)]
                is_superbalanced = leaf_depth_bounds[1] - leaf_depth_bounds[0] <= 1
    else:
        if node.left:
            is_superbalanced, leaf_depth_bounds = traverse_preorder(node.left, curr_depth, leaf_depth_bounds)
        if is_superbalanced and node.right:
            is_superbalanced, leaf_depth_bounds = traverse_preorder(node.right, curr_depth, leaf_depth_bounds)

    return is_superbalanced, leaf_depth_bounds

check_superbalanced(tree_root)


#                   8
#         4                   12
#                         11      14
#                      9


#                      10
