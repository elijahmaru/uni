public class Main {
    static void main() {
        intArray testArr = new intArray();
        for (int i = 0; i < 12; i++) {
            testArr.add(1);
        }
        for (int i = 0; i < testArr.size(); i++) {
            System.out.println(testArr.at(i));
        }
        testArr.delete(1);
        for (int i = 0; i < testArr.size(); i++) {
            System.out.println(testArr.at(i));
        }
    }

}
