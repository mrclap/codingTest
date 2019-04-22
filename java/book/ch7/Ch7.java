package book.ch7;
import java.util.*;

public class Ch7 {

	public Ch7() {
		Suit suit = Suit.Diamond;
		System.out.println(Suit.getSuitFromValue(1));
	}
}
enum Suit {
	Club(0), Diamond(1), heart(2), Spade(3);
	private int value;
	private Suit(int v) { value = v; }  // 생성자
	public int getValue() { return value; }
	public static Suit getSuitFromValue(int value) {
		Suit suit;
		if ( 0 == value) suit = Suit.Club;
		else if ( 1 == value) suit = Suit.Diamond;
		else if ( 2 == value) suit = Suit.heart;
		else suit = Suit.Spade;

		return suit;
	}
}

class Deck <T extends Card> {
	private ArrayList<T> cards;
	private int dealtIndex = 0;

	public void setDeckOfCards(ArrayList<T> deckOfCards) { }

	public void shuffle() {	}
	public int remainingCards() { return cards.size() - dealtIndex; }
//	public T[] dealHand(int number) { }
//	public T dealCard() {	}
}

abstract class Card {
	private boolean available = true;

	// J:11, Q:12, K:13
	protected int faceValue;
	protected Suit suit;

	public Card(int c, Suit s) {
		faceValue = c;
		suit = s;
	}

	public abstract int value();
	public Suit suit() { return suit; }

	public boolean isAvailable() { return available; }
	public void markUnavailable() { available = false; }
	public void markAvailable() { available = true; }
}

class Hand <T extends Card> {
	protected ArrayList<T> cards = new ArrayList<T>();

	public int score() {
		int score = 0;
		for (T card : cards) {
			score += card.value();
		}
		return score;
	}

	public void addCard(T card) {
		cards.add(card);
	}
}