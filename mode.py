from collections import Counter
import csv

with open('hw.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
	n_num = file_data[i][1]
	new_data.append(n_num)



#Calculating Mode
data = Counter(new_data)

moderanges = {
                        "50-60": 0,
                        "60-70": 0,
                        "70-80": 0
                    }
for height, occurence in data.items():
    if 50 < float(height) < 60:
        moderanges["50-60"] += occurence
    elif 60 < float(height) < 70:
        moderanges["60-70"] += occurence
    elif 70 < float(height) < 80:
        moderanges["70-80"] += occurence

mode_range, mode_occurence = 0, 0
for range, occurence in moderanges.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
print("Mode ="+str(mode))