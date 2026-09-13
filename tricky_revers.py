"""Reversing letters in words of text according to special rules."""


def _reverse_word(word: str) -> str:
    """Reverse the letters of one word according to the rules of the problem."""
    letters = []
    for char in word:
        if char.isalpha():
            letters.append(char)

    non_letters = []
    for char in word:
        if not char.isalpha():
            non_letters.append(char)

    if non_letters and non_letters[0] == "0":
        non_letters.insert(0, "0")

    letters.reverse()

    result = ""
    letter_index = 0
    non_letter_index = 0
    for char in word:
        if char.isalpha():
            result += letters[letter_index]
            letter_index += 1
        else:
            result += non_letters[non_letter_index]
            non_letter_index += 1
    return result


def get_tricky_revers(text: str) -> str:
    """Reversing the letters of each word in the text."""
    words = text.split(" ")
    reversed_words = []
    for word in words:
        reversed_words.append(_reverse_word(word))
    return " ".join(reversed_words)


def _run_tests() -> None:
    cases = (
        ("", ""),
        ("qwerty", "ytrewq"),
        ("abcd efgh", "dcba hgfe"),
        ("2a%bcd efg!h", "2d%cba hgf!e"),
        ("as01! hgf_0ert", "sa001 tre_0fgh"),
    )
    for text, expected in cases:
        assert get_tricky_revers(text) == expected
    print("All tests passed ✅")


def main() -> None:
    """Read a line from the user and print the reversed text."""
    user_text = input("Enter text: ")
    print(get_tricky_revers(user_text))


if __name__ == "__main__":
    _run_tests()
    main()
