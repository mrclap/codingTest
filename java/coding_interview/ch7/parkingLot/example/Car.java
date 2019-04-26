package book.ch7.parkingLot.example;

public class Car extends Vehicle{
	public Car() {
		spotsNeeded = 1;
		size = VehicleSize.Compact;
	}

	public boolean canFitInSpot(ParkingSpot spot) {
		if(spot.getSize() == this.size) {
			return true;
		}
		return false;
	}
}
