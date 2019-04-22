package book.ch7.callCenter;

abstract class Employee {
	private Call currentCall = null;
	protected Rank rank;

	public Employee(CallHandler handler) { }
	public void receiveCall(Call call) {
		this.currentCall = call;
		/*
		* start conversation!
		* */
	}
	public void callCompleted() { }
	public void escalateAndReassign() { }
	public boolean assignNewCall() { }
	public boolean isFree() { return currentCall == null; }
	public Rank getRank() { return rank; }
}
