public class Main {
    static void main() {
        myDoubleLinkedList list = new myDoubleLinkedList();
        list.addEnd(1);
        list.display();
        list.addStart(2);
        list.display();
        list.addEnd(5);
        list.display();
        list.addAfter(3, 1);
        list.display();
        list.addEnd(3);
        list.addEnd(3);
        list.addEnd(5);
        list.addEnd(3);
        list.addEnd(3);
        list.display();
        list.addAfter(0, 5);
        list.display();
        list.remove(3);
        list.display();
        list.displayRev();
    }
}
