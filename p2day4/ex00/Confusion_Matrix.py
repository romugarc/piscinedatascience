import sys
import matplotlib.pyplot as plt


def main():
    """
    Displays a confusion matrix based on 2 given txt files
    """
    if len(sys.argv) != 3:
        print("Error: Need 2 txt files")
        return
    
    truth = sys.argv[1]
    prediction = sys.argv[2]

    if not truth.endswith('.txt') or not prediction.endswith('.txt'):
        print("Error: Need 2 txt files")
        return
    #https://www.geeksforgeeks.org/confusion-matrix-machine-learning/
    return


if __name__ == "__main__":
    main()