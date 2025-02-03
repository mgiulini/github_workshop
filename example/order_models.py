def read_capri_table(capri_file):
    """
    Read CAPRI table without using pandas
    """
    with open(capri_file, "r") as f:
        lines = f.readlines()
    header = lines[0].strip().split(" ")
    data = []
    for line in lines[1:]:
        data.append(line.strip().split(" "))
    return header, data

capri_file = "capri_ss.csv"

header, data = read_capri_table(capri_file)

# our score is the combination
# score = 0.1 * air - 1.0 * elec - 0.1 * vdw
# we will sort the data by this score

idx_list = [header.index(el) for el in ["air", "elec", "vdw"]]

score_list = []
for row in data:
    model = row[0]
    score = 0
    # here we calculate the score assigning the right weight to each term
    for idx, weight in zip(idx_list, [0.1, -1.0, -0.1]):
        score += weight * float(row[idx])
    score_list.append([model, score])

# sort the data by the score
sorted_data = sorted(score_list, key=lambda x: x[1], reverse=False)

for i, sorted_score in enumerate(sorted_data):
    print(f"Model rank {i+1}: {sorted_score[0]}, score = {sorted_score[1]:.2f}")
