import * as fs from "fs";
import * as readline from "readline/promises";
import { stdin as input, stdout as output } from "process";

function getRandomInt(min: number, max: number): number {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

async function createFile(name: string) {
    const readLine = readline.createInterface({ input, output });

    const nInput = await readLine.question("Введите кол-во столбцов: ");
    const mInput = await readLine.question("Введите кол-во строк: ");

    const N = parseInt(nInput, 10);
    const M = parseInt(mInput, 10);

    readLine.close();

    const writeStream = fs.createWriteStream(`${name}.txt`, {
        encoding: "utf-8",
    });

    for (let i = 0; i < M; i++) {
        const textOut: string[] = [];
        for (let j = 0; j < N; j++) {
            textOut.push(getRandomInt(-1000, 1000).toString());
        }
        writeStream.write(textOut.join(" ") + "\n");
    }

    writeStream.end();
}

await createFile("input1");
await createFile("input2");
