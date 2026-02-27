public class Main {
    static void main() {
        int[] array = {9, 8, 3, 4, 3, 1, 2};
        for (int i = 0; i < array.length; i++) {
            System.out.println(array[i]);
        }
        array = bubbleSort(array);
        for (int i = 0; i < array.length; i++) {
            System.out.println(array[i]);
        }
    }
}
