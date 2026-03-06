import java.util.Stack;

public class lab5 {
    public static String reverseString(String start) {
        Stack<String> startString = new Stack<>();
        for (int i = 0; i < start.length(); i++) {
            startString.push("" + start.charAt(i));
        }
        String reversedString = "";
        for (int i = 0; i < start.length(); i++) {
            reversedString += startString.pop();
        }
        return reversedString;
    }

    public static boolean checkParentheses(String str) {
        Stack<String> buff = new Stack<String>();
        for (int i = 0; i < str.length(); i++) {
            String currentString = "" + str.charAt(i);
            if (buff.isEmpty() && currentString.equals(")")) {
                return false;
            } else if (currentString.equals("(")) {
                buff.push(currentString);
            } else if (currentString.equals(")") && buff.peek().equals("(")) {
                buff.pop();
            }
        }
        if (buff.isEmpty()) {
            return true;
        }
        return false;
    }

    public static void main(String[] args) {
        String strTask1 = "abcd";
        System.out.println("Изначальная строка: " + strTask1);
        strTask1 = reverseString(strTask1);
        System.out.println("Изменёная стока: " + strTask1);
        String strTask2 = "(()))";
        if (checkParentheses(strTask2)) {
            System.out.println("Правильно");
        } else {
            System.out.println("Неправильно");
        }
        String strTask3 = ")(";
        if (checkParentheses(strTask3)) {
            System.out.println("Правильно");
        } else {
            System.out.println("Неправильно");
        }
        String strTask4 = "(())()";
        if (checkParentheses(strTask4)) {
            System.out.println("Правильно");
        } else {
            System.out.println("Неправильно");
        }
    }
}
