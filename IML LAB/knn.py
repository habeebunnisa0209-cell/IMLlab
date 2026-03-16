import numpy as np
from collections import Counter

class KNN:
    def __init__(self,k=3): self.k=k
    def fit(self,X,y):
        self.X,self.y=X,y
        print("Training Data:")
        [print(f"Point: {a}, Label: {b}") for a,b in zip(X,y)]
        print("-"*40)
    def predict(self,T):
        print("Test Data:"); [print(f"Point: {x}") for x in T]; print("-"*40)
        P=[]
        for x in T:
            print(f"\nProcessing Test Point {x}:")
            d=np.linalg.norm(self.X-x,axis=1)
            [print(f"Distance to {self.X[i]} (Label {self.y[i]}): {d[i]:.2f}") for i in range(len(d))]
            k=np.argsort(d)[:self.k]; lab=[self.y[i] for i in k]
            print(f"Nearest {self.k} neighbors: {lab}")
            c=Counter(lab).most_common(1)[0][0]; print("Predicted Label:",c); P.append(c)
        print("\nFinal Predictions:",P); return P

X=np.array([[1,2],[2,3],[3,3],[6,7],[7,8],[8,8]])
y=np.array(['A','A','A','B','B','B'])
T=np.array([[5,5],[2,2]])
knn=KNN(3); knn.fit(X,y); knn.predict(T)
