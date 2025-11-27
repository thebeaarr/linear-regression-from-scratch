import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("data.csv")
# no cleaning sorry

# Loss function
def loss_function(m, b, points):
	total_err = 0
	for i in range(len(points)):
		x = points.iloc[i].studytime
		y = points.iloc[i].score
		total_err += (y - (m * x + b)) ** 2
	return total_err / float(len(points))


# Gradient descent
def gradient_descent(m_now, b_now, points, L):
	m_gradient = 0
	b_gradient = 0
	n = len(points)
	for i in range(n):
		x = points.iloc[i].studytime
		y = points.iloc[i].score
		m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
		b_gradient += -(2/n) * (y - (m_now * x + b_now))
	m_now -= L * m_gradient
	b_now -= L * b_gradient
	return m_now, b_now

# Initial values
m = 0
b = 0
L = 0.01
epochs = 1000

eq = 0
# old_loss = 0
# 
for i in range(epochs):
	m, b = gradient_descent(m, b, data, L)
	current_loss = loss_function(m, b, data)

	# if abs(old_loss - current_loss) < 1e-8:
	# 	eq += 1
	# else:
	# 	eq = 0

	# if eq == 3:
	# 	print(f"Converged after {i} epochs")
	# 	break

	# old_loss = current_loss

	if i % 100 == 0:
		print(f"Epoch {i}: Loss = {current_loss}")

print(f"Final: m = {m}, b = {b}")

plt.scatter(list(data.studytime), list(data.score), color="black")

x_values = list(range(int(min(data.studytime)), int(max(data.studytime)) + 1))
y_values = [m * x + b for x in x_values]

plt.plot(x_values, y_values, color="red")
plt.xlabel("Study Time")
plt.ylabel("Score")
plt.show()