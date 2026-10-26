class rightPyramid {
    private _height: number;
    private _lenghtOfEdge: number;
    public get height(): number {
        return this._height;
    }
    public set height(value: number) {
        this.checkPositive(value);
        this._height = value;
    }
    public get lenghtOfEdge(): number {
        return this._lenghtOfEdge;
    }
    public set lenghtOfEdge(value: number) {
        this.checkPositive(value);
        this._lenghtOfEdge = value;
    }

    private checkPositive(number: number): boolean {
        if (number < 0) {
            throw new Error("Diameter must be positive");
        } else return true;
    }

    public constructor(
        givenHeight: number = 6 ** (1 / 2) / 3,
        givenEdge: number = 1,
    ) {
        this.checkPositive(givenHeight);
        this._height = givenHeight;
        this._lenghtOfEdge = givenEdge;
    }

    public getPerimeterOfBase(): number {
        return 3 * this.lenghtOfEdge;
    }

    public getAreaOfBase(): number {
        return (this.lenghtOfEdge ** 2 * 3 ** (1 / 2)) / 4;
    }

    public getApothem(): number {
        return (this.height ** 2 + this.lenghtOfEdge ** 2 / 12) * (1 / 2);
    }

    public getAreaOfSide(): number {
        return (1 / 2) * this.getPerimeterOfBase() * this.height;
    }

    public getFullArea(): number {
        return this.getAreaOfBase() + this.getAreaOfSide();
    }
    public getVolume(): number {
        return (1 / 3) * this.height * this.getAreaOfBase();
    }
    public getInfo(): string {
        return `Высота: ${this.height}\nДлина ребра в основании: ${this.lenghtOfEdge}\nАпофема: ${this.getApothem()}\nОбъём: ${this.getVolume()}\nПлощадь: ${this.getFullArea()}`;
    }
}

let pyramid = new rightPyramid();
console.log(pyramid.getInfo())
console.log(pyramid.lenghtOfEdge)
console.log(pyramid.height)
pyramid.height = 1 
pyramid.lenghtOfEdge =3;
console.log(pyramid.height)
console.log(pyramid.lenghtOfEdge)
console.log(pyramid.getInfo())
