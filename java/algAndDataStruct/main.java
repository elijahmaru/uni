import java.util.Scanner;

public class main {
    /** Bubble sort (ascending). Time: O(n^2), Space: O(1). */
    static void bubbleSort(int[] a) {
        if (a == null || a.length < 2) return;

        for (int i = 0; i < a.length - 1; i++) {
            boolean swapped = false;
            for (int j = 0; j < a.length - 1 - i; j++) {
                if (a[j] > a[j + 1]) {
                    int tmp = a[j];
                    a[j] = a[j + 1];
                    a[j + 1] = tmp;
                    swapped = true;
                }
            }
            if (!swapped) return; // already sorted
        }
    }

    public static void main(String[] args) {
        // Input format:
        // n
        // a1 a2 ... an
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] a = new int[Math.max(0, n)];
        for (int i = 0; i < a.length && sc.hasNextInt(); i++) {
            a[i] = sc.nextInt();
        }
        bubbleSort(a);

        for (int i = 0; i < a.length; i++) {
            if (i > 0) System.out.print(" ");
            System.out.print(a[i]);
        }
        System.out.println();
    }
}
