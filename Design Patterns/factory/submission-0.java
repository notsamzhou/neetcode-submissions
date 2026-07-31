interface Vehicle {
    String getType();
}

class Car implements Vehicle {
    @Override
    public String getType() {
        return "Car";
    }
}

class Bike implements Vehicle {
    @Override
    public String getType() {
        return "Bike";
    }
}

class Truck implements Vehicle {
    @Override
    public String getType() {
        return "Truck";
    }
}

abstract class VehicleFactory {
    abstract Vehicle createVehicle();
}

class CarFactory extends VehicleFactory {
    Vehicle createVehicle() {
        Car car = new Car();
        return car;
    }
}

class BikeFactory extends VehicleFactory {
    Vehicle createVehicle() {
        Bike car = new Bike();
        return car;
    }
}

class TruckFactory extends VehicleFactory {
    Vehicle createVehicle() {
        Truck car = new Truck();
        return car;
    }
}
