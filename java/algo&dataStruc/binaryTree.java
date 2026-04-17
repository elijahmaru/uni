public class binaryTree {
    private static class Node {
        int data;
        Node left;
        Node right;
        Node parent;

        Node(int value) {
            this.data = value;
            this.right = null;
            this.left = null;
            this.parent = null;
        }
    }

    private Node root;

    public void add(int value) {
        Node newNode = new Node(value);
        if (root == null) {
            root = newNode;
            return;
        }
        Node currentNode = root;
        Node parentNode = null;
        while (currentNode != null) {
            parentNode = currentNode;
            if (value == currentNode.data)
                return;
            if (currentNode.data > value) {
                currentNode = currentNode.left;
            } else {
                currentNode = currentNode.right;
            }
        }
        if (parentNode.data > value) {
            parentNode.left = newNode;
            parentNode.left.parent = parentNode;
        } else {
            parentNode.right = newNode;
            parentNode.right.parent = parentNode;
        }
    }

    public int min() {
        if (root == null) {
            throw new IndexOutOfBoundsException("Binary tree must be not empty to find min value");
        }
        Node currentNode = root;
        while (currentNode.left != null) {
            currentNode = currentNode.left;
        }
        return currentNode.data;
    }

    public int max() {
        if (root == null) {
            throw new IndexOutOfBoundsException("Binary tree must be not empty to find min value");
        }
        Node currentNode = root;
        while (currentNode.right != null) {
            currentNode = currentNode.right;
        }
        return currentNode.data;
    }

    public void print() {
        printTree(root, 0);
    }

    private void printTree(Node node, int level) {
        if (node == null)
            return;

        printTree(node.right, level + 1);

        for (int i = 0; i < level; i++) {
            System.out.print("    ");
        }
        System.out.println(node.data);

        printTree(node.left, level + 1);
    }

    public void delete(int value) {
        Node nodeForDeletion = find(value);
        if (nodeForDeletion == null) {
            throw new IllegalArgumentException("Valus you want to delete must be in binary tree");
        }
        if (nodeForDeletion.left == null && nodeForDeletion.right == null) {
            if (nodeForDeletion == root) {
                root = null;
            } else if (nodeForDeletion.parent.left == nodeForDeletion) {
                nodeForDeletion.parent.left = null;
            } else {
                nodeForDeletion.parent.right = null;
            }
        } else if (nodeForDeletion.left != null && nodeForDeletion.right == null) {
            if (nodeForDeletion == root) {
                root = nodeForDeletion.left;
                root.parent = null;
            } else if (nodeForDeletion.parent.left == nodeForDeletion) {
                nodeForDeletion.parent.left = nodeForDeletion.left;
                nodeForDeletion.left.parent = nodeForDeletion.parent;
            } else {
                nodeForDeletion.parent.right = nodeForDeletion.left;
                nodeForDeletion.left.parent = nodeForDeletion.parent;
            }
        } else if (nodeForDeletion.left == null && nodeForDeletion.right != null) {
            if (nodeForDeletion == root) {
                root = nodeForDeletion.right;
                root.parent = null;
            } else if (nodeForDeletion.parent.left == nodeForDeletion) {
                nodeForDeletion.parent.left = nodeForDeletion.right;
                nodeForDeletion.right.parent = nodeForDeletion.parent;
            } else {
                nodeForDeletion.parent.right = nodeForDeletion.right;
                nodeForDeletion.right.parent = nodeForDeletion.parent;
            }
        } else {
            Node successor = nodeForDeletion.right;
            while (successor.left != null) {
                successor = successor.left;
            }
            nodeForDeletion.data = successor.data;
            if (successor.parent.left == successor) {
                successor.parent.left = successor.right;
            } else {
                successor.parent.right = successor.right;
            }
            if (successor.right != null) {
                successor.right.parent = successor.parent;
            }
        }
    }

    private Node find(int value) {
        if (root == null) {
            return null;
        }
        Node currentNode = root;
        while (true) {
            if (currentNode.data == value) {
                return currentNode;
            } else if (currentNode.data > value) {
                if (currentNode.left == null) {
                    return null;
                } else {
                    currentNode = currentNode.left;
                }
            } else if (currentNode.data < value) {
                if (currentNode.right == null) {
                    return null;
                } else {
                    currentNode = currentNode.right;
                }
            }
        }
    }
}
