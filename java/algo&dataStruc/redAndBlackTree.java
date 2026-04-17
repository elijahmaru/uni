public class redAndBlackTree {
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

    public redAndBlackTree() {
        NIL = new Node(0);
        NIL.isRed = false;
        NIL.left = NIL.right = NIL;
        root = NIL;
    }

    private Node root;
    private Node NIL;

    private void leftRotate(Node middleNode) {
        Node rightSon = middleNode.right;
        middleNode.right = rightSon.left;
        if (rightSon.left != NIL)
            rightSon.left.parent = middleNode;
        rightSon.parent = middleNode.parent;
        if (middleNode.parent == null)
            root = rightSon;
        else if (middleNode == middleNode.parent.left)
            middleNode.parent.left = rightSon;
        else
            middleNode.parent.right = rightSon;
        rightSon.left = middleNode;
        middleNode.parent = rightSon;
    }

    private void rightRotate(Node middleNode) {
        Node leftSon = middleNode.left;
        middleNode.left = leftSon.right;

        if (leftSon.right != NIL)
            leftSon.right.parent = middleNode;
        leftSon.parent = middleNode.parent;

        if (middleNode.parent == null)
            root = leftSon;
        else if (middleNode == middleNode.parent.right)
            middleNode.parent.right = leftSon;
        else
            middleNode.parent.left = leftSon;

        leftSon.right = middleNode;
        middleNode.parent = leftSon;
    }

    private void fixAdd(Node nodeFixed) {
        while (nodeFixed != root && nodeFixed.parent.isRed) {
            if (nodeFixed.parent == nodeFixed.parent.parent.left) {
                Node uncleRight = nodeFixed.parent.parent.right;

                if (uncleRight.isRed) {
                    nodeFixed.parent.isRed = false;
                    uncleRight.isRed = false;
                    nodeFixed.parent.parent.isRed = true;
                    nodeFixed = nodeFixed.parent.parent;
                } else {
                    if (nodeFixed == nodeFixed.parent.right) {
                        nodeFixed = nodeFixed.parent;
                        leftRotate(nodeFixed);
                    }
                    nodeFixed.parent.isRed = false;
                    nodeFixed.parent.parent.isRed = true;
                    rightRotate(nodeFixed.parent.parent);
                }
            } else {
                Node uncle = nodeFixed.parent.parent.left;

                if (uncle.isRed) {
                    nodeFixed.parent.isRed = false;
                    uncle.isRed = false;
                    nodeFixed.parent.parent.isRed = true;
                    nodeFixed = nodeFixed.parent.parent;
                } else {
                    if (nodeFixed == nodeFixed.parent.left) {
                        nodeFixed = nodeFixed.parent;
                        rightRotate(nodeFixed);
                    }
                    nodeFixed.parent.isRed = false;
                    nodeFixed.parent.parent.isRed = true;
                    leftRotate(nodeFixed.parent.parent);
                }
            }
        }
        root.isRed = false;
    }

    public void add(int data) {
        Node node = new Node(data);
        node.left = node.right = NIL;

        Node parent = null;
        Node current = root;

        while (current != NIL) {
            parent = current;
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
        if (nodeForDeletion == null || nodeForDeletion == NIL) {
            throw new IllegalArgumentException("Value not found in tree");
        }

        Node replacedNode = nodeForDeletion;
        boolean OGColorIsRed = replacedNode.isRed;
        Node movedNode;

        if (nodeForDeletion.left == NIL) {
            movedNode = nodeForDeletion.right;
            replace(nodeForDeletion, nodeForDeletion.right);
        } else if (nodeForDeletion.right == NIL) {
            movedNode = nodeForDeletion.left;
            replace(nodeForDeletion, nodeForDeletion.left);
        } else {
            replacedNode = minNode(nodeForDeletion.right);
            OGColorIsRed = replacedNode.isRed;
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

        if (!OGColorIsRed) {
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
        while (node.left != NIL) {
            node = node.left;
        }
        return node;
    }

    public int min() {
        if (root == null) {
            throw new IndexOutOfBoundsException("Binary tree must be not empty to find min value");
        }
        return minNode(root).data;
    }

    public int max() {
        if (root == null) {
            throw new IndexOutOfBoundsException("Binary tree must be not empty to find min value");
        }
        Node currentNode = root;
        while (currentNode.right != NIL) {
            currentNode = currentNode.right;
        }
        return currentNode.data;
    }

    public void print() {
        printTree(root, 0);
    }

    private void printTree(Node node, int level) {
        if (node == NIL)
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
        if (root == null) {
            return null;
        }
        Node currentNode = root;
        while (true) {
            if (currentNode.data == value) {
                return currentNode;
            } else if (currentNode.data > value) {
                if (currentNode.left == NIL) {
                    return null;
                } else {
                    currentNode = currentNode.left;
                }
            } else if (currentNode.data < value) {
                if (currentNode.right == NIL) {
                    return null;
                } else {
                    currentNode = currentNode.right;
                }
            }
        }
    }
}
