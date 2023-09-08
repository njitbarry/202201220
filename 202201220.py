# Open the file file_to_read.txt in read mode
with open("file_to_read.txt", "r") as f:
  # Read the content of the file as a string
  content = f.read()
  # Count the number of times the word "terrible" appears in the content
  count = content.count("terrible")
  # Display the count
  print("The word 'terrible' appears", count, "times in the file.")

# Create a list of words from the content by splitting on whitespace
words = content.split()
# Initialize a variable to keep track of the occurrence of the word "terrible"
occurrence = 0
# Loop through the words list
for i in range(len(words)):
  # If the word is "terrible"
  if words[i] == "terrible":
    # Increment the occurrence
    occurrence += 1
    # If the occurrence is even
    if occurrence % 2 == 0:
      # Replace the word with "pathetic"
      words[i] = "pathetic"
    # Else, if the occurrence is odd
    else:
      # Replace the word with "marvellous"
      words[i] = "marvellous"

# Join the words list back into a string
new_content = " ".join(words)
# Open a new file result.txt in write mode
with open("result.txt", "w") as f:
  # Write the new content to the file
  f.write(new_content)

# Commit your exercise solution to your GitHub account
# Enter the URL of your exercise repository in the “Exercise 1 Submission Box”