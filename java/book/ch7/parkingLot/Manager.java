package book.ch7.parkingLot;

public class Manager {
	ParkingLot parkingLot;
	int totalIncome;

	public Manager(ParkingLot parkingLot) {
		this.parkingLot = parkingLot;
	}

	public int calculateCost(Car car){
		int cost;
		int baseCost = this.parkingLot.getBaseCost();
		long msStayPeriod = car.getOutTimeStamp().getTime() - car.getInTimeStamp().getTime();
		long hrStayPeriod = msStayPeriod / 1000 / 60 / 60;

		cost = (int)(baseCost * hrStayPeriod);
		return cost;
	}

	public void acceptCar(Car car) {
		parkingLot.increaseOccupation();
	}

	public void leaveCar(Car car) {
		parkingLot.decreaseOccupation();
	}
}
