# Define the list
list = ["Dog", "Cat", "Hen", "Sheep"]

#print list before append
print("List before addition")
print(list)

# Insert data using append method
list.append("Cow")

# Display the list after insert
print("The list elements are")

for i in range(0, len(list)):
  print(list[i])

  # Remove an item
list.remove("Hen")

# Print the list after delete
print("List after delete")
print(list)
