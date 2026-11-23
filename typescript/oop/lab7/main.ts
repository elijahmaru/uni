import { readFile } from "fs/promises";

interface Product {
    productId: number;
    supplier: number;
    category: number;
    price: number;
    quantity: number;
    expired: number;
}

async function readMyFile(filePath: string): Promise<string | null> {
    try {
        return await readFile(filePath, "utf-8");
    } catch (error) {
        console.error("Ошибка при чтении файла: ", error);
        return null;
    }
}

function parseProducts(stringFile: string): Product[] {
    const lines = stringFile
        .trim()
        .split(/\r?\n/)
        .filter((line) => line.trim() !== "");

    lines.shift();

    return lines.map((line) => {
        const values = line.trim().split(/\s+/).map(Number);
        return {
            productId: values[0],
            supplier: values[1],
            category: values[2],
            price: values[3],
            quantity: values[4],
            expired: values[5],
        };
    });
}

function analyzeProducts(products: Product[]) {
    const maxPriceBySupplier = new Map<number, Product>();
    for (const p of products) {
        const currentMax = maxPriceBySupplier.get(p.supplier);
        if (!currentMax || p.price > currentMax.price) {
            maxPriceBySupplier.set(p.supplier, p);
        }
    }

    const minQtyByCategory = new Map<number, Product>();
    for (const p of products) {
        const currentMin = minQtyByCategory.get(p.category);
        if (!currentMin || p.quantity < currentMin.quantity) {
            minQtyByCategory.set(p.category, p);
        }
    }

    const totalExpiredValue = products.reduce(
        (sum, p) => sum + p.price * p.expired,
        0,
    );

    const supplierStats = new Map<number, { sum: number; count: number }>();
    for (const p of products) {
        const stat = supplierStats.get(p.supplier) || { sum: 0, count: 0 };
        stat.sum += p.price;
        stat.count += 1;
        supplierStats.set(p.supplier, stat);
    }

    const avgPriceBySupplier = new Map<number, number>();
    for (const [supplier, stat] of supplierStats.entries()) {
        avgPriceBySupplier.set(
            supplier,
            Number((stat.sum / stat.count).toFixed(2)),
        );
    }

    return {
        maxPriceBySupplier,
        minQtyByCategory,
        totalExpiredValue: Number(totalExpiredValue.toFixed(2)),
        avgPriceBySupplier,
    };
}

async function main() {
    const content = await readMyFile("input.txt");
    if (!content) return;

    const products = parseProducts(content);
    const results = analyzeProducts(products);

    console.log("1. Самый дорогой продукт по поставщикам:");
    results.maxPriceBySupplier.forEach((prod, sup) =>
        console.log(
            `   Поставщик ${sup}: ID ${prod.productId} (цена: ${prod.price})`,
        ),
    );

    console.log("\n2. Товар с мин. количеством по категориям:");
    results.minQtyByCategory.forEach((prod, category) =>
        console.log(
            `   Категория ${category}: ID ${prod.productId} (кол-во: ${prod.quantity})`,
        ),
    );

    console.log(
        `\n3. Общий объем просрочки в валюте: ${results.totalExpiredValue}`,
    );

    console.log("\n4. Средняя цена у каждого поставщика:");
    results.avgPriceBySupplier.forEach((avg, sup) =>
        console.log(`   Поставщик ${sup}: ${avg}`),
    );
}

main();
