package book.ch7.parkingLot.example;

public class Level {
	private int floor;
	private ParkingSpot[] spots;
	private int availableSpots = 0;
	private static final int SPOTS_PER_ROW = 10;

	public Level(int flr, int numberSpots) {
		this.floor = flr;
		spots = new ParkingSpot[numberSpots];
	}

	public int availableSpots() { return availableSpots; }

	public boolean parkVehicle(Vehicle vehicle) { }
	private boolean parkStartingAtSpot(int num, Vehicle v) { }

	private int findAvailableSports(Vehicle vehicle) { }
	public void spotFreed() { availableSpots++; }
}
