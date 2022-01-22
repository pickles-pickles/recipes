export class Vehicle {
  type: string
  constructor (type: string) {
    this.type = type
  }
}

export class Car extends Vehicle {
  name: string
  constructor (name: string, type: string) {
    super(type)
    this.name = name
  }
}

export const ford = new Car('ford', 'car')
