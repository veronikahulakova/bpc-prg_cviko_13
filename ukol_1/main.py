import re
from collections import Counter

def analyze_text(text):
    if not text.strip():
        return None

    # Sentence count: split by . ! ?
    sentences = re.split(r'[.!?]+', text)
    # Filter out empty strings from splitting
    sentences = [s for s in sentences if s.strip()]
    sentence_count = len(sentences)

    # Word processing: remove punctuation and split
    # We'll replace non-alphanumeric characters (except spaces) with space
    clean_text = re.sub(r'[^\w\s]', '', text).lower()
    words = clean_text.split()
    
    word_count = len(words)
    unique_words = set(words)
    unique_word_count = len(unique_words)
    
    # Most frequent words
    most_common = Counter(words).most_common(5)
    
    return {
        "sentence_count": sentence_count,
        "word_count": word_count,
        "unique_word_count": unique_word_count,
        "most_common": most_common
    }

def print_results(results):
    if not results:
        print("Nebyl zadán žádný text k analýze.")
        return

    print("\n" + "="*40)
    print(f"{'Statistika textu':^40}")
    print("="*40)
    print(f"{'Metrika':<25} | {'Hodnota':<10}")
    print("-" * 40)
    print(f"{'Počet vět':<25} | {results['sentence_count']:<10}")
    print(f"{'Počet slov':<25} | {results['word_count']:<10}")
    print(f"{'Počet unikátních slov':<25} | {results['unique_word_count']:<10}")
    print("-" * 40)
    
    print(f"\n{'Top 5 nejčastějších slov':^55}")
    print("-" * 55)
    print(f"{'Slovo':<25} | {'Četnost':<10} | {'Délka':<10}")
    print("-" * 55)
    for word, count in results['most_common']:
        print(f"{word:<25} | {count:<10} | {len(word):<10}")
    print("="*55)

def main():
    print("Zadejte text pro analýzu (stiskněte Enter pro ukončení):")
    user_input = input("> ")
    
    results = analyze_text(user_input)
    print_results(results)

if __name__ == "__main__":
    main()
