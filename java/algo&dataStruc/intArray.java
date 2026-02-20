public class intArray {
    private int[] arr;
    private int len;

    public intArray(){
        this.arr = new int[10];
        this.len = 0;
    }

    public int size() {
        return len;
    }

    public void add(int value) {
        if (len == arr.length) {
            int[] newArr = new int[len * 2];
            System.arraycopy(arr, 0, newArr, 0, arr.length);
            arr = newArr;
        }
        arr[len++] = value;
    }

    public int at(int index) {
        if (index < 0 || index >= len) {
            throw new IndexOutOfBoundsException("индекс: " + index + " хотя размер " + len + ". Инднекс за границами");
        }
        return arr[index];
    }

    public int find(int value) {
        for (int i = 0; i < len; i++) {
            if (value == arr[i]){
                return i;
            }
        }
        return -1;
    }

    public void delete(int value) {
        int amountOfValue = 0;
        for (int i = 0; i < len; i++) {
            if (value == arr[i]){
                amountOfValue++;
            }
        }
        int[] newArr = new int[len - amountOfValue];
        int index = 0;
        for (int i = 0; i < len; i++) {
            if (arr[i] != value) {
                newArr[index++] = arr[i];
            }
        }
        arr = newArr;
        len -= amountOfValue;
    }

    public int min() {
        if (len == 0) throw new IllegalArgumentException("Массив пустой");
        int min = arr[0];
        for (int i = 0; i < len; i++) {
            if (arr[i]<min) min = arr[i];
        }
        return min;
    }

    public int max() {
        if (len == 0) throw new IllegalArgumentException("Массив пустой");
        int max = arr[0];
        for (int i = 0; i < len; i++) {
            if (arr[i]>max) max = arr[i];
        }
        return max;
    }

    public int average() {
        if (len == 0) throw new IllegalArgumentException("Массив пустой");
        int sum = 0;
        for (int i = 0; i < len; i++) sum++;
        return sum / len;
    }
}
