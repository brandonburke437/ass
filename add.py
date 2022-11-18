# Define the list
list = ["Dell", "HP", "Leveno", "Asus"]

#print list before append
print("List before addition")
print(list)

# Insert data using append method
list.append("Toshiba")

# Display the list after insert
print("The list elements are")

for i in range(0, len(list)):
  print(list[i])

  # Remove an item
list.remove("Asus")

# Print the list after delete
print("List after delete")
print(list)
