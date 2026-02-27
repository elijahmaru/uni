public class arrayQueue {
    private int[] data;
    private int len;
    private int indexOfStart;

    public arrayQueue() {
        this.data = new int[10];
        this.len = 0;
        this.indexOfStart = 0;
    }

    public boolean isEmpty() {
        if (len == 0) {
            return true;
        } else {
            return false;
        }
    }

    public void push(int value) {
        if (len == data.length) {
            int[] newData = new int[len * 2];
            System.arraycopy(data, 0, newData, 0, data.length);
            data = newData;
        }
        data[(indexOfStart + len++) % data.length] = value;
    }

    public int pop() {
        if (this.isEmpty()) {
            throw new IndexOutOfBoundsException("stack already empty");
        } else {
            len--;
            return data[indexOfStart++];
        }
    }

    public int peek() {
        if (this.isEmpty()) {
            throw new IndexOutOfBoundsException("stack is empty");
        } else {
            return data[indexOfStart];
        }
    }

    public int size() {
        return len;
    }
}
