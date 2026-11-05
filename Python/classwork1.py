
apple = 15.5
orange = 20
grape = 10.25

# Calculate total volume
total = apple + orange + grape

# Print total volume
print("Total volume:", total)

# Convert total volume to integer
print("Integer volume:", int(total))

# Convert total volume to string
print("Total volume as string: " + str(total) + " liters")

# Random bonus liters between 5 and 10
import random
bonus = random.randint(5, 10)

# Calculate final total
final_total = total + bonus

print("Bonus liters:", bonus)
print("Final total:", final_total, "liters")