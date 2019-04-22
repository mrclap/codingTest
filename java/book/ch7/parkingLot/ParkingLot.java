package book.ch7.parkingLot;
import java.util.*;

public class ParkingLot {
	private int baseCost;
	List parkingSpaceList;
	int capacity;
	int occupation;
	int totalIncome;

	public ParkingLot(List parkingSpaceList, int capacity, int baseCost) {
		this.parkingSpaceList = parkingSpaceList;
		this.capacity = capacity;
		this.baseCost = baseCost;
		this.totalIncome = 0;
	}

	public void increaseOccupation() {
		this.occupation++;
	}

	public void decreaseOccupation() {
		this.occupation--;
	}

	public int getBaseCost() {
		return baseCost;
	}

	public void setBaseCost(int baseCost) {
		this.baseCost = baseCost;
	}
}
