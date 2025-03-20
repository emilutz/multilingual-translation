
from translator import translate_test, Language


def main():
    print(translate_test("What's the weather like today?", Language.ENGLISH, Language.FRENCH))


if __name__ == "__main__":
    main()
