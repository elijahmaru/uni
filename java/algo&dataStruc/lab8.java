public class lab8 {
    public static int fibonacci(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("Номер числа фибаначи должен быть натуралным");
        }
        if (n - 1 != 0 && n - 2 != 0) {
            return fibonacci(n - 1) + fibonacci(n - 2);
        } else {
            return 1;
        }
    }

    public static int factorial(int n) {
        if (n == 0 || n == 1) {
            return 1;
        } else {
            if (n < 0) {
                throw new IllegalArgumentException("Нет факториала от " + n);
            } else {
                return factorial(n - 1) * n;
            }
        }
    }

    public static int trianguralNumber(int n) {
        if (n == 1) {
            return 1;
        }
        if (n == 2) {
            return 3;
        }
        if (n < -1) {
            throw new IllegalArgumentException("Номер треугольног числа должен быть натуральным");
        }
        return trianguralNumber(n - 1) - trianguralNumber(n - 2) + 1 + trianguralNumber(n - 1);
    }

    public static void main(String[] args) {
        System.out.println("Треугольные числа: ");
        for (int i = 1; i < 6; i++) {
            System.out.println("Треугольные число" + "(" + i + "): " + trianguralNumber(i));
        }
        System.out.println("Факториалы: ");
        for (int i = 0; i < 6; i++) {
            System.out.println("Факториал от " + i + ": " + factorial(i));
        }
        System.out.println("Числа фибоначи: ");
        for (int i = 1; i < 6; i++) {
            System.out.println("Фибоначи" + "(" + i + "): " + fibonacci(i));
        }
        System.out.println("Фибоначи" + "(" + 0 + "): " + fibonacci(0));
    }
}
