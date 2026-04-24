public class hashTable {

    private Integer[] table;
    private int size;
    private int count;

    public hashTable() {
        this.size = 7;
        this.table = new Integer[size];
        this.count = 0;
    }

    private int hash(int key) {
        return Math.abs(key) % size;
    }

    public void add(Integer key) {
        if (count == size) {
            resize();
        }

        int index = hash(key);

        while (table[index] != null && table[index] != null) {
            if (table[index] == key) return;
            index = (index + 1) % size;
        }

        table[index] = key;
        count++;
    }

    public boolean search(Integer key) {
        int index = hash(key);
        int startIndex = index;

        while (table[index] != null) {
            if (table[index] != null && table[index] == key) {
                return true;
            }
            index = (index + 1) % size;

            if (index == startIndex) break;
        }

        return false;
    }

    public void delete(int key) {
        int index = hash(key);
        int startIndex = index;

        while (table[index] != null) {
            if (table[index] != null && table[index] == key) {
                table[index] = null;
                count--;
                return;
            }
            index = (index + 1) % size;

            if (index == startIndex) break;
        }
    }

    private void resize() {
        int newSize = nextPrime(size * 2);
        Integer[] oldTable = table;
        table = new Integer[newSize];
        size = newSize;
        count = 0;

        for (Integer key : oldTable) {
            if (key != null) {
                add(key);
            }
        }
    }

    private int nextPrime(int n) {
        while (!isPrime(n)) {
            n++;
        }
        return n;
    }

    private boolean isPrime(int n) {
        if (n <= 1) return false;
        if (n <= 3) return true;

        if (n % 2 == 0 || n % 3 == 0) return false;

        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) return false;
        }
        return true;
    }

    public void print() {
        for (int i = 0; i < size; i++) {
            if (table[i] != null) {
                System.out.println(i + ": " + table[i]);
            }
        }
        System.out.println(size);
    }
}
