paragraph = """
Python is an easy programming language.
It is useful for web development and automation.
This course teaches basic Python programming.
"""

# Display the length of the paragraph
print("lenght of paragraph:",len(paragraph))

# Display  first and last characters
print("first character:", paragraph[0])
print("last character:", paragraph[-1])

# print first 50 character
print("preview:", paragraph[:50])

# Replace python with PYTHON
print("paragraph.replace:", paragraph.replace("python","PYTHON"))

# Convert paragraph to lowercase
print("lowercase paragraph:",paragraph.lower())

# Remove  extra whitespaces
clean_paragraph = paragraph.strip()
print("removing whitespaces:",clean_paragraph)

# Split paragraph into individual words
words = paragraph.split(" ")
print(words)

# Check whether course exists

print("course" in paragraph)

# Display final message using format()
print("The course description is {} characters long and has {} words.".format(
    len(clean_paragraph), len(words)
))
