package book.ch7.callCenter;
import java.util.*;

public class CallHandler {
	private final int LEVELS = 3;

	private final int NUM_RESPONDENTS = 10;
	private final int NUM_MANAGERS = 4;
	private final int NUM_DIRECTORS = 2;

	/*
	* employeeLevels[0] = respondents
	* employeeLevels[1] = managers
	* employeeLevels[2] = directors
	*
	* */

	List<List<Employee>> employeeLevels;
	List<List<Call>> callQueues;

	public CallHandler() { }

	public Employee getHandlerForCall(Call call) {
		return employeeLevels[call.getRank().getLevel()];
	}

	public void dispatchCall(Caller caller) {
		Call call = new Call(caller);
		dispatchCall(call);
	}

	public void dispatchCall(Call call) {
		Employee emp = getHandlerForCall(call);
		if (emp != null) {
			emp.receiveCall(call);
			call.setHandler(emp);
		} else {
			call.reply("Please wiat for free employee to reply");
			callQueues.get(call.getRank().getLevel()).add(call);
		}
	}

	public boolean assignCall(Employee emp) { }
}
