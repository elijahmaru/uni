public class sortAlgorithms {

    public int[] bubbleSort(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length - 1 - i; j++) {
                if (arr[j] < arr[j + 1]) {
                    arr[j] = arr[j] ^ arr[j + 1];
                    arr[j + 1] = arr[j] ^ arr[j + 1];
                    arr[j] = arr[j] ^ arr[j + 1];
                }
            }
        }
        return arr;
    }

    public int[] insertionSort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int numberMoved = arr[i];
            int j = i - 1;
            while (j >= 0 && numberMoved < arr[j]) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = numberMoved;
        }
        return arr;
    }

    public int[] selectionSort(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            int minIndex = i;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[minIndex] > arr[j]) minIndex = j;
            }
            int buff = arr[minIndex];
            arr[minIndex] = arr[i];
            arr[i] = buff;
        }
        return arr;
    }

    void main() {
        int[] array = {3, 4, 2, 7, 1, 9, 1};
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + " ");
        }
        System.out.println();
        int[] arrayBubble = bubbleSort(array);
        for (int i = 0; i < array.length; i++) {
            System.out.print(arrayBubble[i] + " ");
        }
        System.out.println();
        int[] arrayInsert = insertionSort(array);
        for (int i = 0; i < arrayInsert.length; i++) {
            System.out.print(arrayInsert[i] + " ");
        }
        System.out.println();
        int[] arraySelect = selectionSort(array);
        for (int i = 0; i < arraySelect.length; i++) {
            System.out.print(arraySelect[i] + " ");
        }
        System.out.println();
    }
}
