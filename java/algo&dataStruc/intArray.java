public class intArray {
    private int[] data;
    private int len;

    public intArray() {
        this.data = new int[10];
        this.len = 0;
    }

    public int size() {
        return len;
    }

    public void add(int value) {
        if (len == data.length) {
            int[] newArr = new int[len * 2];
            System.arraycopy(data, 0, newArr, 0, data.length);
            data = newArr;
        }
        data[len++] = value;
    }

    public int at(int index) {
        if (index < 0 || index >= len) {
            throw new IndexOutOfBoundsException(
                    "индекс: " + index + " хотя размер " + len + ". Инднекс за границами");
        }
        return data[index];
    }

    public int find(int value) {
        for (int i = 0; i < len; i++) {
            if (value == data[i]) {
                return i;
            }
        }
        return -1;
    }

    public void delete(int value) {
        int amountOfValue = 0;
        for (int i = 0; i < len; i++) {
            if (value == data[i]) {
                amountOfValue++;
            }
        }
        int[] newArr = new int[len - amountOfValue];
        int index = 0;
        for (int i = 0; i < len; i++) {
            if (data[i] != value) {
                newArr[index++] = data[i];
            }
        }
        data = newArr;
        len -= amountOfValue;
    }

    public int min() {
        if (len == 0)
            throw new IllegalArgumentException("Массив пустой");
        int min = data[0];
        for (int i = 0; i < len; i++) {
            if (data[i] < min)
                min = data[i];
        }
        return min;
    }

    public int max() {
        if (len == 0)
            throw new IllegalArgumentException("Массив пустой");
        int max = data[0];
        for (int i = 0; i < len; i++) {
            if (data[i] > max)
                max = data[i];
        }
        return max;
    }

    public int average() {
        if (len == 0)
            throw new IllegalArgumentException("Массив пустой");
        int sum = 0;
        for (int i = 0; i < len; i++)
            sum++;
        return sum / len;
    }
}
