import sys
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    """
    Displays a confusion matrix based on 2 given txt files
    """
    if len(sys.argv) != 3:
        print("Error: Need 2 txt files")
        return
    
    truth_file = sys.argv[1]
    prediction_file = sys.argv[2]

    if not truth_file.endswith('.txt') or not prediction_file.endswith('.txt'):
        print("Error: Need 2 txt files")
        return
    tp, fn, fp, tn = 0, 0, 0, 0
    with open(truth_file, 'r') as truth, open(prediction_file, 'r') as prediction:
        for lineT, lineP in zip(truth, prediction):
            lineT = lineT.strip()
            lineP = lineP.strip()
            if lineP == "Jedi" and lineT == "Jedi":
                tp += 1
            elif lineP == "Jedi" and lineT == "Sith":
                fp += 1
            elif lineP == "Sith" and lineT == "Jedi":
                fn += 1
            elif lineP == "Sith" and lineT == "Sith":
                tn += 1
    accuracy = (tp + tn) / (tp + fn + fp + fn)
    jedi_precision = tp / (tp + fp)
    sith_precision = tn / (tn + fn)
    jedi_recall = tp / (tp + fn)
    sith_recall = tn / (tn + fp)
    jedi_f1_score = (2 * jedi_precision * jedi_recall) / (jedi_precision + jedi_recall)
    sith_f1_score = (2 * sith_precision * sith_recall) / (sith_precision + sith_recall)
    jedi_total = tp + fn
    sith_total = tn + fp
    total = jedi_total + sith_total
    confusion_matrix = [[tp, fn], [fp, tn]]

    print("    ", "precision", "recall", "f1-score", "total")
    print("Jedi", f"    {jedi_precision:.2f}", f"   {jedi_recall:.2f}", f"    {jedi_f1_score:.2f}", f"   {jedi_total}")
    print("Sith", f"    {sith_precision:.2f}", f"   {sith_recall:.2f}", f"    {sith_f1_score:.2f}", f"   {sith_total}")
    print("accuracy", f"                 {accuracy:.2f}", f"  {total}")
    print(confusion_matrix)
    sns.heatmap(confusion_matrix, annot=True)
    plt.show()
    return


if __name__ == "__main__":
    main()