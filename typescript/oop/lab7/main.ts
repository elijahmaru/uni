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

function fileToInfo(stringFile: string): void {
    const lines: string[] = stringFile.split(/\r?\n/).slice(0, -1);
    const names: string[] = lines[0].split(" ");
    lines.shift();
    const template: Record<string, number> = {};
    for (const name in names) {
        template[name] = 0;
    }
    let info: Record<string, number>[] = [];
    for (const line of lines) {
        const lineValues: number[] = line.split(" ").map(Number);
        let recordLine = template;
        for (const name in names){
            recordLine[name] = lineValues.shift();
        }
        info.push(recordLine);
    }
}
