import sys


def main():
    """ This script will count the characters of the string you provide """
    try:
        arg = len(sys.argv)
        assert arg <= 2, "more than one argument is provided"
        if arg < 2:
            print("What is the text to count?")
            message = sys.stdin.readline()
        else:
            message = sys.argv[1]
        punct = "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
        print("The text contains", len(message), "characters:")
        print(sum(1 for c in message if c.isupper()), "upper letters")
        print(sum(1 for c in message if c.islower()), "lower letters")
        print(sum(1 for c in message if c in punct), "punctuation marks")
        print(sum(1 for c in message if c.isspace()), "spaces")
        print(sum(1 for c in message if c.isdigit()), "digits")
    except AssertionError as e:
        print(f"AssertionError:{(str(e))}")
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    except Exception as e:
        print(f"Error:{(str(e))}")
    return


if __name__ == "__main__":
    main()
