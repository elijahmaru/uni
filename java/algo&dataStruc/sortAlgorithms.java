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

    public int[] insersionSort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int numberMoved = arr[i];
            int j = i - 1;
            while (j >= 0 & numberMoved < arr[j]) {
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
                if (arr[minIndex] > arr[j])
                    minIndex = j;
            }
            arr[minIndex] = arr[minIndex] ^ arr[i];
            arr[i] = arr[minIndex] ^ arr[i];
            arr[minIndex] = arr[minIndex] ^ arr[i];
        }
        return arr;
    }
}
