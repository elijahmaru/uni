public class pyramid {
    private Integer[] heap;
    private int amount;
    private int size;

    public pyramid(int size) {
        this.size = size;
        this.heap = new Integer[size];
        this.amount = 0;
    }

    public int size() {
        return amount;
    }

    public boolean isEmpty() {
        return amount == 0;
    }

    private int getParent(int index) {
        return (index - 1) / 2;
    }

    private int getLeft(int index) {
        return 2 * index + 1;
    }

    private int getRight(int index) {
        return 2 * index + 2;
    }

    private boolean hasParent(int index) {
        return getParent(index) >= 0;
    }

    private boolean hasLeft(int index) {
        return getLeft(index) < amount;
    }

    private boolean hasRight(int index) {
        return getRight(index) < amount;
    }

    private int parent(int index) {
        return heap[getParent(index)];
    }

    private int leftChild(int index) {
        return heap[getLeft(index)];
    }

    private int rightChild(int index) {
        return heap[getRight(index)];
    }

    private void swap(int fstIndex, int sndIndex) {
        int temp = heap[fstIndex];
        heap[fstIndex] = heap[sndIndex];
        heap[sndIndex] = temp;
    }

    private void resize() {
        if (amount == size) {
            size *= 2;
            Integer[] newHeap = new Integer[size];
            System.arraycopy(heap, 0, newHeap, 0, amount);
            heap = newHeap;
        }
    }

    public int pop(int index) {
        if (index < 0 || index >= amount) {
            throw new IndexOutOfBoundsException("Некорректный индекс");
        }
        int removedElement = heap[index];
        heap[index] = heap[amount - 1];
        amount--;

        if (hasParent(index) && heap[index] > parent(index)) {
            fixUpwards(index);
        } else {
            fixDownwards(index);
        }
        return removedElement;
    }

    private void fixDownwards(int index) {
        while (hasLeft(index)) {
            int largerChildIndex = getLeft(index);

            if (hasRight(index) && rightChild(index) > leftChild(index)) {
                largerChildIndex = getRight(index);
            }

            if (heap[index] > heap[largerChildIndex]) {
                break;
            } else {
                swap(index, largerChildIndex);
            }
            index = largerChildIndex;
        }
    }

    public void output() {
        System.out.println("Базовый массив:");
        for (int i = 0; i < amount; i++) {
            System.out.println(i + ": " + heap[i]);
        }
    }

    public void printTree() {
        if (amount == 0) {
            System.out.println("Дерво пустое");
            return;
        }
        System.out.println("Дерево: ");
        int level = 0;
        int nodesInLevel = 1;
        int index = 0;
        while (index < amount) {
            int spaces = (int) Math.pow(2, Math.max(0, 4 - level));
            for (int s = 0; s < spaces; s++) {
                System.out.print(" ");
            }
            int count = 0;
            while (count < nodesInLevel && index < amount) {
                System.out.print(heap[index] + " ");
                for (int s = 0; s < spaces * 2; s++) {
                    System.out.print(" ");
                }
    
                index++;
                count++;
            }
            System.out.println();
            level++;
            nodesInLevel *= 2;
        }
    }

    public void insert(int value) {
        resize();
        heap[amount] = value;
        amount++;
        fixUpwards(amount - 1);
    }

    private void fixUpwards(int index) {
        while (hasParent(index) && parent(index) < heap[index]) {
            swap(getParent(index), index);
            index = getParent(index);
        }
    }

}
