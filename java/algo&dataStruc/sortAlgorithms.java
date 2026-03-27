import java.util.Arrays;
import java.util.Random;

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
                if (arr[minIndex] > arr[j])
                    minIndex = j;
            }
            int buff = arr[minIndex];
            arr[minIndex] = arr[i];
            arr[i] = buff;
        }
        return arr;
    }

    int[] addValue(int[] arr, int value) {
        if (arr.length == 0) {
            int[] resultArr = { value };
            return resultArr;
        }
        int[] resultArr = new int[arr.length + 1];
        for (int pos = 0; pos < arr.length; pos++) {
            resultArr[pos] = arr[pos];
        }
        resultArr[arr.length] = value;
        return resultArr;
    }

    public int[] mergeSort(int[] arr) {
        if (arr.length <= 1) {
            return arr;
        }
        int[] firstHalf = mergeSort(Arrays.copyOfRange(arr, 0, arr.length / 2));
        int[] secondHalf = mergeSort(Arrays.copyOfRange(arr, arr.length / 2, arr.length));
        int[] resultArr = new int[firstHalf.length + secondHalf.length];
        int i = 0, j = 0, k = 0;
        while (i < firstHalf.length && j < secondHalf.length) {
            if (firstHalf[i] <= secondHalf[j]) {
                resultArr[k++] = firstHalf[i++];
            } else {
                resultArr[k++] = secondHalf[j++];
            }
        }
        while (i < firstHalf.length) {
            resultArr[k++] = firstHalf[i++];
        }
        while (j < secondHalf.length) {
            resultArr[k++] = secondHalf[j++];
        }
        return resultArr;
    }

    int[] quickSort(int[] arr, int choice) {
        if (arr.length <= 1) {
            return arr;
        }
        int pivot;
        Random rand = new Random();
        switch (choice) {
            case 0:
                pivot = arr.length / 2;
                break;
            case 1:
                pivot = 0;
                break;
            case 2:
                pivot = arr.length - 1;
                break;
            case 3:
                pivot = rand.nextInt(arr.length);
                break;
            default:
                pivot = rand.nextInt(arr.length);
                break;
        }
        int valueAtPivot = arr[pivot];
        int[] resultArr = new int[arr.length];
        int[] firstArr = new int[0];
        int[] secondArr = new int[0];
        for (int pos = 0; pos < arr.length; pos++) {
            if (pos == pivot) {
                continue;
            }
            int currentValue = arr[pos];
            if (currentValue <= valueAtPivot) {
                firstArr = addValue(firstArr, currentValue);
            } else {
                secondArr = addValue(secondArr, currentValue);
            }
        }
        firstArr = quickSort(firstArr, choice);
        secondArr = quickSort(secondArr, choice);
        for (int pos = 0; pos < arr.length; pos++) {
            if (pos < firstArr.length) {
                resultArr[pos] = firstArr[pos];
            } else if (pos == firstArr.length) {
                resultArr[pos] = valueAtPivot;
            } else {
                resultArr[pos] = secondArr[pos - firstArr.length - 1];
            }
        }
        return resultArr;
    }

    int[] shellSort(int[] arr) {
        int n = arr.length;
        for (int gap = n / 2; gap > 0; gap /= 2) {
            for (int pos = gap; pos < n; pos++) {
                int buff = arr[pos];
                int j = pos;
                while (j >= gap && arr[j - gap] > buff) {
                    arr[j] = arr[j - gap];
                    j -= gap;
                }
                arr[j] = buff;
            }
        }
        return arr;
    }

    void main() {
        int[] arraysToSort = { 6, 2, 3, 7, 1, 8, 4, 5 };
        int[] arrayToSort1 = Arrays.copyOf(arraysToSort, arraysToSort.length);
        int[] arrayToSort2 = Arrays.copyOf(arraysToSort, arraysToSort.length);
        int[] arrayToSort3 = Arrays.copyOf(arraysToSort, arraysToSort.length);
        int[] arrayToSort4 = Arrays.copyOf(arraysToSort, arraysToSort.length);
        int[] arrayToSort5 = Arrays.copyOf(arraysToSort, arraysToSort.length);
        int[] buff = mergeSort(arraysToSort);
        for (int i = 0; i < buff.length; i++) {
            System.out.print(buff[i] + " ");
        }
        System.out.println();

        System.out.println("Элемент по середине");
        long start = System.nanoTime();
        buff = quickSort(arrayToSort1, 0);
        long end = System.nanoTime();
        System.out.println("Время: " + (end - start));
        for (int i = 0; i < buff.length; i++) {
            System.out.print(buff[i] + " ");
        }
        System.out.println();

        System.out.println("Элемент в начале");
        start = System.nanoTime();
        buff = quickSort(arrayToSort2, 1);
        end = System.nanoTime();
        System.out.println("Время: " + (end - start));
        for (int i = 0; i < buff.length; i++) {
            System.out.print(buff[i] + " ");
        }
        System.out.println();

        System.out.println("Элемент в конце");
        start = System.nanoTime();
        buff = quickSort(arrayToSort3, 2);
        end = System.nanoTime();
        System.out.println("Время: " + (end - start));
        for (int i = 0; i < buff.length; i++) {
            System.out.print(buff[i] + " ");
        }
        System.out.println();

        System.out.println("Рандомный элемент");
        start = System.nanoTime();
        buff = quickSort(arrayToSort4, 3);
        end = System.nanoTime();
        System.out.println("Время: " + (end - start));
        for (int i = 0; i < buff.length; i++) {
            System.out.print(buff[i] + " ");
        }
        System.out.println();

        buff = shellSort(arrayToSort5);
        for (int i = 0; i < buff.length; i++) {
            System.out.print(buff[i] + " ");
        }
        System.out.println();
    }
}
