import { readFile } from "fs/promises";

async function readMyFile(filePath: string): Promise<string> {
    let content: string;
    try {
        content = await readFile(filePath, "utf-8");
    } catch (error) {
        console.error("Error reading file: ", error);
        return "error opening a file";
    }
    return content;
}

function fileToMatrix(stringFile: string): number[][] {
    const lines: string[] = stringFile.split(/\r?\n/).slice(0, -1);
    let matrix: number[][] = [];
    for (const line of lines) {
        const lineValues: number[] = line.split(" ").map(Number);
        matrix.push(lineValues);
    }
    const sizeOfline: number = matrix[0].length;
    for (const line of matrix) {
        if (sizeOfline != line.length) {
            console.error("given file doesn't contain matrix");
            return [[]];
        }
    }
    return matrix;
}

function printMatrix(matrix: number[][]) {
    for (const line of matrix) {
        console.log(line);
    }
}

function findMax(matrix1: number[][], matrix2: number[][]) {
    const matrix: number[][] = [...matrix1, ...matrix2];
    let max: number = matrix[0][0];
    for (const line of matrix) {
        for (const element of line) {
            if (element > max) {
                max = element;
            }
        }
    }
    return max;
}

const matrix1 = fileToMatrix(await readMyFile("input1.txt"));
const matrix2 = fileToMatrix(await readMyFile("input2.txt"));
console.log("Первая матирца: \n", printMatrix(matrix1));
console.log("Вторая матирца: \n", printMatrix(matrix2));
console.log("Максимальное число: ", findMax(matrix1, matrix2));
