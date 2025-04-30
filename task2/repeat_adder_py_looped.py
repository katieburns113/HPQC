import sys

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
except:
    print("Please enter two integers as command-line arguments.")
    sys.exit(1)

# Simulate heavier load
repeat = 10_000_000  # Repeat the addition this many times
total = 0

for i in range(repeat):
    total += a + b

print(f"Final result after {repeat} repetitions: {total}")

