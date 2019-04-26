package book.ch7.parkingLot;

public class ParkingSpace {
	boolean isUsing = false;
	Location location;

	public ParkingSpace(Location location) {
		this.location = location;
	}

	public boolean isUsing() {
		return isUsing;
	}

	public void setUsing(boolean using) {
		isUsing = using;
	}

	public Location getLocation() {
		return location;
	}

	public void setLocation(Location location) {
		this.location = location;
	}
}
