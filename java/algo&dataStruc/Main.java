public class Main {
    static void main() {
        int a = 2;
        int b = 3;
        a = a^b;
        b = a^b;
        a = a^b;
        System.out.println(a + "  " + b);
    }

}
