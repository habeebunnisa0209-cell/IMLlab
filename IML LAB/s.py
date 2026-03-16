import csv

def find_s_algorithm(file):
    data = list(csv.reader(open(file)))[1:]
    h = ["?"]*(len(data[0])-1)

    for row in data:
        if row[-1].lower() == "yes":
            if h == ["?"]*(len(row)-1): 
                h = row[:-1]
            else:
                h = [x if x==y else "?" for x,y in zip(h,row[:-1])]
    return h

print("Final Hypothesis using Find-S:")
print(find_s_algorithm("enjoysport.csv"))
