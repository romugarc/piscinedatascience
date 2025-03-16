import sys
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import f1_score, accuracy_score
from sklearn.neighbors import KNeighborsClassifier


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
    Makes a decision tree based on the given data sets, and creates a KNN.txt file based on a prediction by the tree on the Test dataset
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

        best_k = 0
        best_score = 0
        accuracy_list = []
        for k in range(1, 31):
            knn = KNeighborsClassifier(n_neighbors=k)
            knn = knn.fit(x_train, y_train)
            prediction = knn.predict(x_val)
            accuracy = accuracy_score(truth_val, prediction)
            accuracy_list.append(accuracy)
            if accuracy > best_score:
                best_score = accuracy
                best_k = k

        best_knn = KNeighborsClassifier(n_neighbors=best_k)
        best_knn = best_knn.fit(x_train, y_train)
        prediction = best_knn.predict(x_val)
        score = f1_score(truth_val, prediction)
        print(f"score:{score}")
        
        test_pred = best_knn.predict(testdf)
        test_pred = ['Sith' if item == 1 else 'Jedi' for item in test_pred]
        with open("KNN.txt", "w") as tree_file:
            for item in test_pred:
                tree_file.write(f"{item}\n")
 
        plt.figure(figsize=(20, 20))
        plt.plot(accuracy_list)
        plt.show()
        

    except Exception as e:
        print(f"Error: {str(e)}")
        return
    
    return


if __name__ == "__main__":
    main()