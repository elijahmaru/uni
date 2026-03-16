/** linkedList */
public class myDoubleLinkedList {
    private static class Node {
        int data;
        Node next;
        Node prev; //

        Node(int value) {
            this.data = value;
            this.next = null;
            this.prev = null; //
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
            newValue.prev = tail; //
            tail = newValue;
        }
        length++;
        return;
    }

    public void addStart(int value) {
        Node newValue = new Node(value);
        if (head == null) {
            tail = newValue;
            head = newValue;
        } else {
            newValue.next = head;
            head.prev = newValue; //
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
            addEnd(value);
            return;
        }
        for (int i = 0; i < length; i++) {
            if (pointer.data == afterWhich) {
                newValue.prev = pointer;
                newValue.next = pointer.next;
                pointer.next.prev = newValue;
                pointer.next = newValue;
                length++;
                return;
            } else {
                pointer = pointer.next;
            }
        }
        return;
    }

    public void remove(int value) {
        if (head == null) return;
        Node pointer = head;

        while (pointer != null && pointer.data == value) {
            if (pointer.next != null) {
                pointer.next.prev = null;
            } else {
                head = null;
                tail = null;
                length = 0;
                return;
            }
            pointer = pointer.next;
            head = pointer;
            length--;
        }

        if (pointer == null) return;

        for (int i = 0; i < length;) {
            if (pointer.data == value) {
                if (pointer.next != null) {
                    pointer.prev.next = pointer.next;
                    pointer.next.prev = pointer.prev;
                    pointer = pointer.next;
                    length--;
                } else {
                    pointer.prev.next = null;
                    tail = pointer.prev;
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
        for (int i = 0; pointer.next != null; i++) {
            if (i == length - 1) {
                System.out.print(pointer.data);
                System.out.println();
            } else {
                System.out.print(pointer.data + " <-> ");
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
        Node pointer = tail;
        for (int i = 0; pointer.prev != null; i++) {
            if (i == length - 1) {
                System.out.print(pointer.data);
                System.out.println();
            } else {
                System.out.print(pointer.data + " <-> ");
            }
            pointer = pointer.prev;
        }
        System.out.println(length);
    }
}
