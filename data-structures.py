class Author():
    def __init__(self, name, books):
        self.name = name
        self.books = books

# newAuthor = Author("Rick Riordan", ???)

# teamName = input("What is your team name? ")
# numGames = int(input("How many games should we play? "))

# for game in range(numGames):
#     opponentName = input("What is the opponent name? ")
#     # Continued...

# print(opponents???)

# Tuples
# Tuples are immutable lists. They are created using parentheses instead of square brackets.
#
# >>> myTuple = (1, 2, 3)
# classicBooks = ("The Great Gatsby", "The Catcher in the Rye", "To Kill a Mockingbird")
# classicBooks.append("The Grapes of Wrath")
# # ERROR: 'tuple' object has no attribute 'append'
# print(classicBooks)
# # Output: The Great Gatsby


# Sets
# Sets are unordered collections of unique elements. They are created using curly braces.
#
# Romance Authors
# romanceAuthors = {"Jane Austen", "Charlotte Bronte", "Emily Bronte", "George Eliot", "Louisa May Alcott", "Mark Twain", "Oscar Wilde", "William Shakespeare"}
# # Fantasy authors
# fantasyAuthors = {"J.R.R. Tolkien", "J.K. Rowling", "George R.R. Martin", "Terry Pratchett", "Mark Twain", "Oscar Wilde", "William Shakespeare"}

# romanceNotFantasy = romanceAuthors.difference(fantasyAuthors)
# print(romanceNotFantasy)
# # Output: {'Jane Austen', 'Louisa May Alcott', 'Charlotte Bronte', 'Emily Bronte', 'George Eliot'}

# Dictionary
# Dictionaries are unordered collections of key-value pairs. They are created using curly braces.
#

# Add author names to dictionary for loop

# Implementing a stack in python
# authors = []
# authors.append("Jane Austen")
# authors.append("Charlotte Bronte")
# authors.append("Emily Bronte")
# authors.append("George Eliot")

# print("LIFO Stack")
# print("----------")

# for count in range(len(authors) - 1, -1, -1):
#     print(authors[count])

# while len(authors) > 0:
#     authors.pop()
#     print("\n" + str(len(authors)) + " items remain in the stack")
#     print("---------------------------")
#     for iCount in range(len(authors) - 1, -1, -1) :
#         print(authors[iCount])

# Queue
authors = []
authors.append("Jane Austen")
authors.append("Charlotte Bronte")
authors.append("Emily Bronte")
authors.append("George Eliot")

print("FIFO Stack")
print("----------")

for count in range(0, len(authors)):
    print(authors[count])

while len(authors) > 0:
    authors.pop(0)
    print("\n" + str(len(authors)) + " items remain in the stack")
    print("---------------------------")
    for iCount in range(0, len(authors)) :
        print(authors[iCount])