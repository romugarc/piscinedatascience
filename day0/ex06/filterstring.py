from ft_filter import ft_filter
import sys


def main():
    """
    This program accepts two arguments: a string (S) and an integer (N).
    The program will output a list of words from S that have a length greater
    than N
    """
    docfilter = filter.__doc__
    docftfilter = ft_filter.__doc__
    print(docfilter == docftfilter)
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        S = sys.argv[1]
        N = sys.argv[2]
        assert isinstance(S, str), "the arguments are bad"
        assert N.isnumeric(), "the arguments are bad"
        N = int(N)
        if any(not c.isalnum() and not c.isspace() for c in S):
            raise AssertionError("the arguments are bad")
        words = S.split()
        word_list = [word for word in words if word]
        word_filter = ft_filter(lambda x: len(x) > N, word_list)
        print(word_filter)
    except AssertionError as e:
        print(f"AssertionError: {(str(e))}")
    except Exception as e:
        print(f"Error: {(str(e))}")
    return


if __name__ == "__main__":
    main()
