import random
import datetime
# This program displays daily motivational quotes
# Developed for Git Bash & GitHub project

def load_quotes():
    """
    Returns a list of motivational quotes.
    Each quote is stored as a dictionary.
    """
    return [
        {"text": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
        {"text": "Success is not final, failure is not fatal: it is the courage to continue that counts.", "author": "Winston Churchill"},
        {"text": "Don’t watch the clock; do what it does. Keep going.", "author": "Sam Levenson"},
        {"text": "The future depends on what you do today.", "author": "Mahatma Gandhi"},
        {"text": "Dream big and dare to fail.", "author": "Norman Vaughan"},
        {"text": "Push yourself, because no one else is going to do it for you.", "author": "Unknown"},
        {"text": "Hard work beats talent when talent doesn’t work hard.", "author": "Tim Notke"},
        {"text": "Success doesn’t just find you. You have to go out and get it.", "author": "Unknown"},
        {"text": "Great things never come from comfort zones.", "author": "Unknown"},
        {"text": "Stay positive, work hard, make it happen.", "author": "Unknown"},
	{"text": "Small steps every day lead to big results.", "author": "Unknown"},
    ]

def show_header():
    """Displays program header with date"""
    today = datetime.date.today()
    print("\n="*30)
    print("   DAILY MOTIVATION QUOTES   ")
    print(f"        {today}        ")
    print("=\n"*30)

def get_random_quote(quotes):
    """Selects and returns a random quote"""
    return random.choice(quotes)

def display_quote(quote):
    """Displays quote in formatted style"""
    print(f"\"{quote['text']}\"")
    print(f"— {quote['author']}\n")

def menu():
    """Displays menu options"""
    print("1. Show a motivational quote")
    print("2. Exit")

def main():
    quotes = load_quotes()

    while True:
        show_header()
        menu()
        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            quote = get_random_quote(quotes)
            display_quote(quote)
            input("Press Enter to continue...")
        elif choice == "2":
            print("\nThank you! Stay motivated! 🌟\n")
            break
        else:
            print("\nInvalid choice. Please try again.\n")
            input("Press Enter to continue...")
# ===== Add the test function at the very bottom =====
def test_total_quotes():
    print(f"Total motivational quotes available: {len(quotes)}")

# Call the test function
test_total_quotes()

if __name__ == "__main__":
    main()
