import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "nato_phonetic_alphabet.csv")

# Load CSV into a dict: {'A': 'Alfa', 'B': 'Bravo', ...}
df = pd.read_csv(DATA_FILE)
nato_dict = {row.Letter: row.Code for _, row in df.iterrows()}

print("=" * 45)
print("   📻  NATO Phonetic Alphabet Converter")
print("   Enter a word to get its NATO spelling.")
print("   Type 'exit' to quit.")
print("=" * 45)

while True:
    word = input("\nEnter word: ").strip().upper()

    if word == "EXIT":
        print("Goodbye!")
        break

    # List comprehension to convert each letter
    try:
        result = [nato_dict[letter] for letter in word if letter != " "]
        print(" - ".join(result))
    except KeyError as e:
        # Handle non-alphabet characters
        print(f"⚠️  Invalid character: {e}. Use letters only.")
