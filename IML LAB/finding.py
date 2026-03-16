import csv

def find_s_algorithm(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    # Remove header
    header = data[0]
    data = data[1:]

    # Initialize hypothesis with "?" for each attribute
    num_attributes = len(data[0]) - 1
    hypothesis = ["?" for _ in range(num_attributes)]

    # Apply Find-S algorithm
    for row in data:
        attributes = row[:-1]
        target = row[-1].strip().lower()

        if target == "yes":     # Only positive examples
            if hypothesis == ["?"] * num_attributes:
                hypothesis = attributes.copy()
            else:
                for i in range(num_attributes):
                    if hypothesis[i] != attributes[i]:
                        hypothesis[i] = "?"

    return hypothesis


# ----------------------------
# Run the algorithm
# ----------------------------

filename = "enjoysport.csv"

final_hypothesis = find_s_algorithm(filename)
print("Final Hypothesis using Find-S:")
print(final_hypothesis)
