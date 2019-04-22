package book.ch7.parkingLot;
import java.util.*;


public class Car {
	Date inTimeStamp;
	Date outTimeStamp;

	public Car(Date inTimeStamp) {
		this.inTimeStamp = inTimeStamp;
	}

	public Date getInTimeStamp() {
		return inTimeStamp;
	}

	public void setInTimeStamp(Date inTimeStamp) {
		this.inTimeStamp = inTimeStamp;
	}

	public Date getOutTimeStamp() {
		return outTimeStamp;
	}

	public void setOutTimeStamp(Date outTimeStamp) {
		this.outTimeStamp = outTimeStamp;
	}
}
