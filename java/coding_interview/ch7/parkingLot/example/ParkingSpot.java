package book.ch7.parkingLot.example;

public class ParkingSpot {
	private Vehicle vehicle;
	private VehicleSize spotSize;
	private int row;
	private int spotNumber;
	private Level level;

	public ParkingSpot(Level lvl, int r, int n, VehicleSize s) { }
	public boolean isAvailable() { return vehicle == null; }

	public boolean canFitVehicle(Vehicle vehicle) { }

	public boolean park(Vehicle v) {
		if(canFitVehicle(v)) {
			this.vehicle = v;
			return true;
		}
		return false;
	}

	public int getRow() { return row; }
	public int getSpotNumber() { return spotNumber; }

	public void removeVehicle() {
		this.vehicle = null;
		this.level.spotFreed();
	}
}
