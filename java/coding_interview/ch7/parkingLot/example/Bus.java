package book.ch7.parkingLot.example;

public class Bus extends Vehicle {
	public Bus() {
		spotsNeeded = 5;
		size = VehicleSize.Large;
	}

	public boolean canFitInSpot(ParkingSpot spot) {
		if(spot.getSize() == this.size) {
			return true;
		}
		return false;
	}
}
