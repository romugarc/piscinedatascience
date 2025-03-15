import sys
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.metrics import f1_score


def load(path: str) -> pd.DataFrame:
    """
    This function takes a path as argument,
    writes the dimensions of the data set and returns it.
    """
    if not isinstance(path, str):
        return None
    try:
        df = pd.read_csv(path)
        print("Loading dataset of dimensions", df.shape)
        return df
    except Exception as e:
        print(f"Error:{str(e)}")
        return None


def main():
    """
    Makes a decision tree based on the given data sets, and creates a Tree.txt file based on a prediction by the tree on the Test dataset
    """
    if len(sys.argv) != 3:
        print("Error: Need Train_knight.csv and Test_knight.csv as arguments")
        return
    if sys.argv[1] != "../Train_knight.csv" or sys.argv[2] != "../Test_knight.csv":
        print("Error: Need Train_knight.csv and Test_knight.csv as arguments")
        return
    
    try:
        traindf = load(sys.argv[1])
        if traindf is None:
            print("Error: invalid dataframe")
            return None
        testdf = load(sys.argv[2])
        if testdf is None:
            print("Error: invalid dataframe")
            return None
        
        traindf['knight'] = traindf['knight'].apply(lambda x: 0 if x == 'Jedi' else 1)
        training = traindf.sample(frac = 0.8)
        validation = traindf.drop(training.index)

        x_train = training.drop(columns=['knight'])
        y_train = training['knight']
        x_val = validation.drop(columns=['knight'])
        truth_val = validation['knight']

        dtree = tree.DecisionTreeClassifier()
        dtree = dtree.fit(x_train, y_train)
        
        prediction = dtree.predict(x_val)
        score = f1_score(truth_val, prediction)
        print(f"score:{score}")
        
        test_pred = dtree.predict(testdf)
        test_pred = ['Sith' if item == 1 else 'Jedi' for item in test_pred]
        with open("Tree.txt", "w") as tree_file:
            for item in test_pred:
                tree_file.write(f"{item}\n")

        plt.figure(figsize=(20, 20))
        tree.plot_tree(dtree, feature_names=training.columns, class_names = ["Sith", "Jedi"], filled=True)
        plt.show()
        

    except Exception as e:
        print(f"Error: {str(e)}")
        return
    
    return


if __name__ == "__main__":
    main()