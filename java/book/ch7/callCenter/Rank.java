package book.ch7.callCenter;

public enum Rank {
	Director(0), Manager(1), Responder(2);
	int level;

	Rank(int level) {
		this.level = level;
	}

	public int getLevel() {
		return level;
	}

	public void setLevel(int level) {
		this.level = level;
	}

	public void incrementLevel() {
		if (level < 2) { this.level += 1; }
	}
}
