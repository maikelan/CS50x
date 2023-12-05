# Counts favorites using dictionary

import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Counts
    counts = {}

    # Iterate over CSV file, counting favorites
    for row in reader:
        favorite = row["problem"]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1
def getvalue(i):
    return counts[i]

# Print counts
for i in sorted(counts,key=lambda language:counts[language]):
    '''
    lamada 传入参数：返回值
    '''
    print(f"{i}: {counts[i]}")
