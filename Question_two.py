# Define a python class named "Book" with attributes: title ,author, and pages.
#provide a method in class to display information about the book. create an instance of the class
#and display the information.

class Book:
    def __init__(self,title,pages,author):
        self.title = title
        self.author = author
        self.pages = pages

B1 = Book("LET GOD BE TRUE", 50, "SANDRA NAKAWUKA")
print(B1.title)
print(B1.pages)
print(B1.author)

#(ii) create aderived class "EBook" that inherits from the "Book"class.
#Add an additional attribute"formart" to the EBook class. Display information for an instance of the EBook class.

class EBook:
    def __init__(self,title,pages,author):
        self.title = title
        self.author = author
        self.pages = pages

B2 = EBook("DON'T LIMIT GOD", 100, "SANDRA NAKAWUKA")
print(B2.title)
print(B2.pages)
print(B2.author)

#(iii)Create a function on the "Book" class that returns only the book title and its author
Book = B1.title
Book = B1.author

print(f"Book's title:{B1.title}")
print(f"Book's title:{B1.author}")

#(iv) Define the following terms 

