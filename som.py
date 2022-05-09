# init weights
weights = [
    [0.2, 0.6, 0.5, 0.9],
    [0.8, 0.4, 0.7, 0.3],
]

# init input
input_matrix = [
    [1, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
]

eta = 0.6
epochs = 100



for _ in range(epochs):
    for i in range(len(input_matrix)):
        # calculate d1, d2
        d1, d2 = 0, 0
        for j in range(len(input_matrix[i])):
            d1 += (input_matrix[i][j] - weights[0][j]) ** 2
            d2 += (input_matrix[i][j] - weights[1][j]) ** 2

        # select minimum
        selected = 0 if d1 < d2 else 1

        # update weights
        for k in range(len(weights[selected])):
            weights[selected][k] = weights[selected][k] + eta * (input_matrix[i][k] - weights[selected][k])
    eta *= 0.5

print(f"final weights: \n{weights[0]}\n{weights[1]}")

clusters = [[], []]
for i in range(len(input_matrix)):

    d1, d2 = 0, 0
    for k in range(len(input_matrix[i])):
        d1 += (input_matrix[i][k] - weights[0][k]) ** 2
        d2 += (input_matrix[i][k] - weights[1][k]) ** 2

    selected = 0 if d1 < d2 else 1
    clusters[selected].append(i)

print(clusters)
