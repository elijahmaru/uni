abstract class Weaponry {
    protected name: string;
    protected countryMade: "USA" | "Russia" | "China" | "EU";
    protected year: number;

    constructor(
        name: string,
        countryMade: "USA" | "Russia" | "China" | "EU",
        year: number
    ) {
        this.name = name;
        this.countryMade = countryMade;
        this.year = year;
    }

    get info(): string {
        return `Название: ${this.name}, страна: ${this.countryMade}, год выпуска: ${this.year}`;
    }

    showInfo(): void {
        console.log(this.info);
    }

    abstract use(): void;
}

class Artilery extends Weaponry {
    override get info(): string {
        return `Артиллерия: ${this.name}, страна: ${this.countryMade}, год выпуска: ${this.year}`;
    }

    override use(): void {
        this.showInfo();
        console.log(`${this.name}: артиллерийская система.`);
    }
}

class Tank extends Weaponry {
    override get info(): string {
        return `Танк: ${this.name}, страна: ${this.countryMade}, год выпуска: ${this.year}`;
    }

    override use(): void {
        this.showInfo();
        console.log(`${this.name}: боевая машина наземного назначения.`);
    }
}

class Aircraft extends Weaponry {
    override get info(): string {
        return `Самолёт: ${this.name}, страна: ${this.countryMade}, год выпуска: ${this.year}`;
    }

    override use(): void {
        this.showInfo();
        console.log(`${this.name}: летательный аппарат.`);
    }
}

const weapons: Weaponry[] = [
    new Artilery("M777", "USA", 2005),
    new Tank("Т-90", "Russia", 1992),
    new Aircraft("Су-27", "Russia", 1985)
];

for (const weapon of weapons) {
    weapon.showInfo();
    weapon.use();
    console.log("--------------------");
}

