import csv

def load_csv(filename):
    with open(filename, 'r') as file:
        data = list(csv.reader(file))
    return data[1:]  # skip header


def candidate_elimination(data):
    num_attributes = len(data[0]) - 1

    # Initialize S and G
    S = ['0'] * num_attributes
    G = [['?'] * num_attributes]

    for example in data:
        x, label = example[:-1], example[-1]

        # POSITIVE EXAMPLE
        if label.lower() == 'yes':
            for i in range(num_attributes):
                if S[i] == '0':
                    S[i] = x[i]
                elif S[i] != x[i]:
                    S[i] = '?'

            # Remove inconsistent hypotheses from G
            G = [g for g in G if all(g[i] == '?' or g[i] == S[i] for i in range(num_attributes))]

        # NEGATIVE EXAMPLE
        else:
            new_G = []
            for g in G:
                for i in range(num_attributes):
                    if g[i] == '?' and S[i] != x[i]:
                        new_hypothesis = g.copy()
                        new_hypothesis[i] = S[i]
                        new_G.append(new_hypothesis)
            G = new_G

        print(f"\nAfter example {example}:")
        print("S =", S)
        print("G =", G)

    return S, G


# ---- MAIN ----
data = load_csv("training_data.csv")
S, G = candidate_elimination(data)

print("\nFinal Version Space:")
print("Specific Boundary (S):", S)
print("General Boundary (G):", G)
