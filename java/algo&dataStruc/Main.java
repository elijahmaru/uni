public class Main {
    static void main() {
        arrayQueue a = new arrayQueue();
        a.push(10);
        a.push(12);
        a.push(16);
        System.out.println(a.size());
        System.out.println(a.peek());
        System.out.println(a.pop());
        System.out.println(a.peek());
        a.pop();
        a.pop();
        System.out.println(a.isEmpty());
    }
}
