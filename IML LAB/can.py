import csv

def candidate_elimination(file):
    data=list(csv.reader(open(file)))[1:]
    n=len(data[0])-1
    S=['0']*n; G=[['?']*n]

    for e in data:
        x,l=e[:-1],e[-1].lower()
        if l=='yes':
            for i in range(n):
                if S[i]=='0': S[i]=x[i]
                elif S[i]!=x[i]: S[i]='?'
            G=[g for g in G if all(g[i]=='?' or g[i]==S[i] for i in range(n))]
        else:
            G=[ [S[i] if j==i else g[j] for j in range(n)]
                for g in G for i in range(n) if g[i]=='?' and S[i]!=x[i] ]

        print(f"\nAfter example {e}:"); print("S =",S); print("G =",G)

    print("\nFinal Version Space:")
    print("Specific Boundary (S):",S)
    print("General Boundary (G):",G)

candidate_elimination("training_data.csv")
