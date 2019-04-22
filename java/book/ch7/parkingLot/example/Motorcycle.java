package book.ch7.parkingLot.example;

public class Motorcycle extends Vehicle {
	public Motorcycle() {
		spotsNeeded = 1;
		size = VehicleSize.Motorcycle;
	}

	public boolean canFitInSpot(ParkingSpot spot) {
		return true;
	}
}


