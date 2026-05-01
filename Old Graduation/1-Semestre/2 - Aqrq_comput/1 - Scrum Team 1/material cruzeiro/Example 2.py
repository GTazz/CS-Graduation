import time

# Define the boolean variables
A = True
B = False
C = True
D = False

# Measure execution time for the first condition
start_time = time.time()
# Repeat the operation multiple times to perceive the time difference
for _ in range(100_000_000):  # Adjust the number of iterations as needed
    if A or ((B or (C and D)) and (B or A)):
        pass
end_time = time.time()
execution_time1 = end_time - start_time

print(f"Result of first condition: {A or ((B or (C and D)) and (B or A))}")
print(f"Execution time for first condition: {execution_time1:.10f} seconds")

# Measure execution time for the second condition
start_time = time.time()
for _ in range(100_000_000):  # Adjust the number of iterations as needed
    if A or B:
        pass
end_time = time.time()
execution_time2 = end_time - start_time

print(f"Result of second condition: {A or B}")
print(f"Execution time for second condition: {execution_time2:.10f} seconds")
