/** linkedList */
public class myLinkedList {
    private static class Node {
        int data;
        Node next;

        Node(int value) {
            this.data = value;
            this.next = null;
        }
    }

    private Node head;
    private Node tail;
    private int length = 0;

    public void addEnd(int value) {
        Node newValue = new Node(value);
        if (head == null) {
            tail = newValue;
            head = newValue;
        } else {
            tail.next = newValue;
            tail = newValue;
        }
        length++;
        return;
    }

    public void addStart(int value) {
        Node newValue = new Node(value);
        if (head == null) {
            head = newValue;
            tail = newValue;
        } else {
            newValue.next = head;
            head = newValue;
        }
        length++;
        return;
    }

    public void addAfter(int value, int afterWhich) {
        if (head == null) return;
        Node newValue = new Node(value);
        Node pointer = head;
        if (tail.data == afterWhich) {
            tail.next = newValue;
            tail = newValue;
            length++;
            return;
        }
        for (int i = 0; i < length; i++) {
            if (pointer.data == afterWhich) {
                newValue.next = pointer.next;
                pointer.next = newValue;
                length++;
                return;
            }
            pointer = pointer.next;
        }
        return;
    }

    public void remove(int value) {
        if (head == null) return;
        Node pointer = head;

        while (pointer != null && pointer.data == value) {
            if (pointer.next != null) {
                pointer = pointer.next;
            } else {
                head = null;
                tail = null;
                length = 0;
                return;
            }
            head = pointer;
            length--;
        }

        if (pointer == null) return;

        for (int i = 0; i < length;) {
            if (pointer.data == value) {
                if (pointer.next != null) {
                    pointer.next = pointer.next;
                    pointer = pointer.next;
                    length--;
                } else {
                    pointer.next = null;
                    tail = pointer;
                    length--;
                    break;
                }
            } else {
                i++;
                pointer = pointer.next;
            }
        }
    }

    public Node find(int value) {
        Node pointer = head;
        for (int i = 0; i < length; i++) {
            if (pointer.data == value) {
                return pointer;
            }
            pointer = pointer.next;
        }
        return null;
    }

    public void display() {
        if (length == 0) {
            System.out.println("Пустой список");
            return;
        }
        Node pointer = head;
        for (int i = 0; i < length; i++) {
            if (i == length - 1) {
                System.out.print(pointer.data);
                System.out.println();
            } else {
                System.out.print(pointer.data + " -> ");
            }
            pointer = pointer.next;
        }
        System.out.println(length);
    }

    public void displayRev() {
        if (length == 0) {
            System.out.println("Пустой список");
            return;
        }
        displayRevRecursive(head);
        System.out.println(length);
    }

    private void displayRevRecursive(Node node) {
        if (node == null) return;
        displayRevRecursive(node.next);
        if (node == head) {
            System.out.print(node.data);
            System.out.println();
        } else {
            System.out.print(node.data + " <- ");
        }
    }
}
