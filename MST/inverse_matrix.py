import numpy as np

XTX = np.array([
    [3, 6, 20],
    [6, 14, 41],
    [20, 41, 142]
])

# XTX_inv = np.linalg.inv(XTX)
# print(np.round(XTX_inv, 3))  # Rounded for readability

X = np.array([
    [1, 2, 9],
    [1, 1, 5],
    [1, 3, 6]
])

# y = np.array([78, 60, 72]).reshape(-1, 1)
y = np.array([[78], [60], [72]])


# Calculate weights
w = np.linalg.inv(X.T @ X) @ X.T @ y
print(w)

