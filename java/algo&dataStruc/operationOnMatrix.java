public class operationOnMatrix {

    public static int[][] multiplyMatrixes(int[][] matrixA, int[][] matrixB) {
        int rowsA = matrixA.length;
        int colomsA = matrixA[0].length;
        int rowsB = matrixB.length;
        int colomsB = matrixB[0].length;
        int[][] result = new int[rowsA][colomsB];
        if (colomsA != rowsB) {
            throw new IllegalArgumentException("Несовпадение размеров");
        }
        for (int i = 0; i < rowsA; i++) {
            for (int j = 0; j < colomsB; j++) {
                result[i][j] = 0;
                for (int k = 0; k < colomsA; k++) {
                    result[i][j] += matrixA[i][k] * matrixB[k][j];
                }
            }
        }

        return result;
    }

    public static int[][] multiplyMatrixByNum(int[][] matrix, int k) {
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                matrix[i][j] *= k;
            }
        }
        return matrix;
    }

    public static int[][] addMatrixes(int[][] matrixA, int[][] matrixB) {
        int rowsA = matrixA.length;
        int colomsA = matrixA[0].length;
        int rowsB = matrixB.length;
        int colomsB = matrixB[0].length;
        int[][] result = new int[rowsA][colomsA];
        if (colomsA != colomsB && rowsA != rowsB) {
            throw new IllegalArgumentException("Несовпадение размеров");
        }
        for (int i = 0; i < matrixA.length; i++) {
            for (int j = 0; j < matrixA[0].length; j++) {
                result[i][j] = matrixA[i][j] + matrixB[i][j];
            }
        }
        return result;
    }

    public static void printMatrix(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                System.out.printf("%4d", matrix[i][j]);
            }
            System.out.println();
        }
    }
}
