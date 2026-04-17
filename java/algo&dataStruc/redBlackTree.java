public class redBlackTree {
    private static class Node {
        int data;
        boolean isRed;
        Node left, right, parent;

        Node(int value) {
            this.data = value;
            this.isRed = true;
            this.left = null;
            this.right = null;
            this.parent = null;
        }
    }

    public redBlackTree() {
        leafNULL = new Node(0);
        leafNULL.isRed = false;
        leafNULL.left = leafNULL.right = leafNULL;
        root = leafNULL;
    }

    private Node root;
    private Node leafNULL;

    private void leftRotate(Node parrentNode) {
        Node middleNode = parrentNode.right;
        parrentNode.right = middleNode.left;
        if (middleNode.left != leafNULL)
            middleNode.left.parent = parrentNode;
        middleNode.parent = parrentNode.parent;
        if (parrentNode.parent == null)
            root = middleNode;
        else if (parrentNode == parrentNode.parent.left)
            parrentNode.parent.left = middleNode;
        else
            parrentNode.parent.right = middleNode;
        middleNode.left = parrentNode;
        parrentNode.parent = middleNode;
    }

    private void rightRotate(Node parentNode) {
        Node middleNode = parentNode.left;
        parentNode.left = middleNode.right;

        if (middleNode.right != leafNULL)
            middleNode.right.parent = parentNode;
        middleNode.parent = parentNode.parent;

        if (parentNode.parent == null)
            root = middleNode;
        else if (parentNode == parentNode.parent.right)
            parentNode.parent.right = middleNode;
        else
            parentNode.parent.left = middleNode;

        middleNode.right = parentNode;
        parentNode.parent = middleNode;
    }

    private void fixAdd(Node nodeForFixing) {
        while (nodeForFixing != root && nodeForFixing.parent.isRed) {
            if (nodeForFixing.parent == nodeForFixing.parent.parent.left) {
                Node uncleNode = nodeForFixing.parent.parent.right;

                if (uncleNode.isRed) {
                    nodeForFixing.parent.isRed = false;
                    uncleNode.isRed = false;
                    nodeForFixing.parent.parent.isRed = true;
                    nodeForFixing = nodeForFixing.parent.parent;
                } else {
                    if (nodeForFixing == nodeForFixing.parent.right) {
                        nodeForFixing = nodeForFixing.parent;
                        leftRotate(nodeForFixing);
                    }
                    nodeForFixing.parent.isRed = false;
                    nodeForFixing.parent.parent.isRed = true;
                    rightRotate(nodeForFixing.parent.parent);
                }
            } else {
                Node uncleNode = nodeForFixing.parent.parent.left;

                if (uncleNode.isRed) {
                    nodeForFixing.parent.isRed = false;
                    uncleNode.isRed = false;
                    nodeForFixing.parent.parent.isRed = true;
                    nodeForFixing = nodeForFixing.parent.parent;
                } else {
                    if (nodeForFixing == nodeForFixing.parent.left) {
                        nodeForFixing = nodeForFixing.parent;
                        rightRotate(nodeForFixing);
                    }
                    nodeForFixing.parent.isRed = false;
                    nodeForFixing.parent.parent.isRed = true;
                    leftRotate(nodeForFixing.parent.parent);
                }
            }
        }
        root.isRed = false;
    }

    public void add(int data) {
        Node node = new Node(data);
        node.left = node.right = leafNULL;

        Node parent = null;
        Node current = root;

        while (current != leafNULL) {
            parent = current;
            if (current.data == node.data) {
                return;
            }
            if (node.data < current.data)
                current = current.left;
            else
                current = current.right;
        }

        node.parent = parent;

        if (parent == null)
            root = node;
        else if (node.data < parent.data)
            parent.left = node;
        else
            parent.right = node;

        if (node.parent == null) {
            node.isRed = false;
            return;
        }
        if (node.parent.parent == null)
            return;

        fixAdd(node);
    }

    public void delete(int value) {
        Node nodeForDeletion = find(value);
        if (nodeForDeletion == null || nodeForDeletion == leafNULL) {
            throw new IllegalArgumentException("Value not found in tree");
        }

        Node replacedNode = nodeForDeletion;
        boolean isOGColorRed = replacedNode.isRed;
        Node movedNode;

        if (nodeForDeletion.left == leafNULL) {
            movedNode = nodeForDeletion.right;
            replace(nodeForDeletion, nodeForDeletion.right);
        } else if (nodeForDeletion.right == leafNULL) {
            movedNode = nodeForDeletion.left;
            replace(nodeForDeletion, nodeForDeletion.left);
        } else {
            replacedNode = minNode(nodeForDeletion.right);
            isOGColorRed = replacedNode.isRed;
            movedNode = replacedNode.right;

            if (replacedNode.parent == nodeForDeletion) {
                movedNode.parent = replacedNode;
            } else {
                replace(replacedNode, replacedNode.right);
                replacedNode.right = nodeForDeletion.right;
                replacedNode.right.parent = replacedNode;
            }

            replace(nodeForDeletion, replacedNode);
            replacedNode.left = nodeForDeletion.left;
            replacedNode.left.parent = replacedNode;
            replacedNode.isRed = nodeForDeletion.isRed;
        }

        if (!isOGColorRed) {
            fixDelete(movedNode);
        }
    }

    private void replace(Node replaced, Node replacedBy) {
        if (replaced.parent == null) {
            root = replacedBy;
        } else if (replaced == replaced.parent.left) {
            replaced.parent.left = replacedBy;
        } else {
            replaced.parent.right = replacedBy;
        }
        replacedBy.parent = replaced.parent;
    }

    private void fixDelete(Node fixedNode) {
        while (fixedNode != root && !fixedNode.isRed) {
            if (fixedNode == fixedNode.parent.left) {
                Node sisterNode = fixedNode.parent.right;

                if (sisterNode.isRed) {
                    sisterNode.isRed = false;
                    fixedNode.parent.isRed = true;
                    leftRotate(fixedNode.parent);
                    sisterNode = fixedNode.parent.right;
                }

                if (!sisterNode.left.isRed && !sisterNode.right.isRed) {
                    sisterNode.isRed = true;
                    fixedNode = fixedNode.parent;
                } else {
                    if (!sisterNode.right.isRed) {
                        sisterNode.left.isRed = false;
                        sisterNode.isRed = true;
                        rightRotate(sisterNode);
                        sisterNode = fixedNode.parent.right;
                    }

                    sisterNode.isRed = fixedNode.parent.isRed;
                    fixedNode.parent.isRed = false;
                    sisterNode.right.isRed = false;
                    leftRotate(fixedNode.parent);
                    fixedNode = root;
                }
            } else {
                Node sistedNode = fixedNode.parent.left;

                if (sistedNode.isRed) {
                    sistedNode.isRed = false;
                    fixedNode.parent.isRed = true;
                    rightRotate(fixedNode.parent);
                    sistedNode = fixedNode.parent.left;
                }

                if (!sistedNode.right.isRed && !sistedNode.left.isRed) {
                    sistedNode.isRed = true;
                    fixedNode = fixedNode.parent;
                } else {
                    if (!sistedNode.left.isRed) {
                        sistedNode.right.isRed = false;
                        sistedNode.isRed = true;
                        leftRotate(sistedNode);
                        sistedNode = fixedNode.parent.left;
                    }

                    sistedNode.isRed = fixedNode.parent.isRed;
                    fixedNode.parent.isRed = false;
                    sistedNode.left.isRed = false;
                    rightRotate(fixedNode.parent);
                    fixedNode = root;
                }
            }
        }
        fixedNode.isRed = false;
    }

    private Node minNode(Node node) {
        while (node.left != leafNULL) {
            node = node.left;
        }
        return node;
    }

    public int min() {
        if (root == leafNULL) {
            throw new IndexOutOfBoundsException("Binary tree must be not empty to find min value");
        }
        return minNode(root).data;
    }

    public int max() {
        if (root == leafNULL) {
            throw new IndexOutOfBoundsException("Binary tree must be not empty to find min value");
        }
        Node currentNode = root;
        while (currentNode.right != leafNULL) {
            currentNode = currentNode.right;
        }
        return currentNode.data;
    }

    public void print() {
        printTree(root, 0);
        System.out.println("--------------");
    }

    private void printTree(Node node, int level) {
        if (node == leafNULL)
            return;

        printTree(node.right, level + 1);

        for (int i = 0; i < level; i++) {
            System.out.print("    ");
        }
        String color = (node.isRed) ? "R" : "B";
        System.out.println(node.data + " " + color);

        printTree(node.left, level + 1);
    }

    private Node find(int value) {
        if (root == leafNULL) {
            return null;
        }
        Node currentNode = root;
        while (true) {
            if (currentNode.data == value) {
                return currentNode;
            } else if (currentNode.data > value) {
                if (currentNode.left == leafNULL) {
                    return null;
                } else {
                    currentNode = currentNode.left;
                }
            } else if (currentNode.data < value) {
                if (currentNode.right == leafNULL) {
                    return null;
                } else {
                    currentNode = currentNode.right;
                }
            }
        }
    }
}
