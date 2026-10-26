class Sphere {
    private _radius: number;
    public get radius(): number {
        return this._radius;
    }
    public set radius(value: number) {
        this.checkPositive(value);
        this._radius = value;
    }
    private _position: [number, number];
    public get position(): [number, number] {
        return this._position;
    }
    public set position(value: [number, number]) {
        this._position = value;
    }

    public constructor(
        newRadius: number = 1,
        newPosition: [number, number] = [0, 0],
    ) {
        this._radius = newRadius;
        this._position = newPosition;
    }

    private checkPositive(number: number): boolean {
        if (number < 0) {
            throw new Error("Diameter must be positive");
        } else return true;
    }

    public getDiameter(): number {
        return this.radius * 2;
    }

    public getVolume(): number {
        return (4 / 3) * Math.PI * this.radius ** 3;
    }

    public getArea(): number {
        return 4 * Math.PI * this.radius ** 2;
    }

    public getInfo(): string {
        return `Радиус: ${this.radius}\nДиаметр: ${this.getDiameter()}\nПозиция: ${this.position[0]}, ${this.position[1]}\nОбъём: ${this.getVolume()}\nПлощадь: ${this.getArea()}`;
    }
}

let mySphere = new Sphere();
console.log(mySphere.getInfo());
console.log(mySphere.radius);
console.log(mySphere.position);
mySphere.radius = 14;
mySphere.position = [10, mySphere.position[1]];
console.log(mySphere.radius);
console.log(mySphere.position);
