# Define the equation as a function
def f(n):
  return 1 - (365 ** n) * math.factorial(365) / (math.factorial(365 - n) * (365 ** 365))

# Define the target value
target = 0.65

# Define the initial interval
a = 1 # lower bound
b = 365 # upper bound

# Define the tolerance
tol = 1e-6 # acceptable error

# Initialize the error
err = 1 # initial error

# Loop until the error is smaller than the tolerance
while err > tol:
  # Find the midpoint of the interval
  c = (a + b) / 2

  # Evaluate the function at the midpoint
  fc = f(c)

  # Check if the midpoint is close enough to the target
  if abs(fc - target) < tol:
    # Break the loop
    break
  else:
    # Update the interval
    if fc < target:
      # Move the lower bound to the midpoint
      a = c
    else:
      # Move the upper bound to the midpoint
      b = c

    # Update the error
    err = abs(b - a)

# Print the result
print("The solution is", c)
