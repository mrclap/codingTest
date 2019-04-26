package book.ch7.parkingLot.example;
import java.util.*;

public abstract class Vehicle {
	protected ArrayList<ParkingSpot> parkingSpots = new ArrayList<ParkingSpot>();
	protected String licensePlate;
	protected int spotsNeeded;
	protected VehicleSize size;

	public int getSpotsNeeded() { return spotsNeeded; }
	public VehicleSize getSize() { return size; }

	public void parkInSpot(ParkingSpot s) { parkingSpots.add(s); }
	public void clearSpots() { }

	public abstract boolean canFitInSpot(ParkingSpot spot);
}
