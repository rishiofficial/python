# 1. Display all available books
# 2. Borrow a book
# 3. Return a book
# 4. View my borrowed books
# 5. Exit

import json
def load_booksdata():
    with open("books.txt", 'r') as file:
        test = json.load(file)
        return test
    
books = load_booksdata()

def list_of_allbooks(books):
    # for index, book in enumerate(books, start=1):
    #     print(f"{index}.{book}")
     for book in books:
        print(f"- {book['book']}")

# list_of_allbooks(books)


def load_studentdata():
    with open("student.txt", 'r') as file:
        student_data = json.load(file)
        return student_data
    
student = load_studentdata()

def list_of_allbookborrowed(student):
    # for index, book in enumerate(student, start=1):
    #     print(f"{index}.{book}")
    for entry in student:
        print(f"- {entry['book']}")

        
# print(load_studentdata())
def save_data(books):
    with open ("books.txt",'w') as file:
       json.dump(books, file)

def save_studentdata(student):
    with open ("student.txt", 'w') as file:
        json.dump(student, file)

def book_borrow(books,student):
    list_of_allbooks(books)
    name = input("Enter the name of book you want to borrow: ")
    # print(f"Looking for book: {name} ")

    book_found = False
    book_index = -1
    for index, book in enumerate(books):
        # print(f"Checking book: {book['book']}")
        if book["book"] == name:
            
            book_found = True
            book_index = index
            # print(f"book index: {book_index}")
            break
    if book_found:
        student.append({"book": name})
        del books[book_index]
        save_data(books)
        save_studentdata(student)
        list_of_allbookborrowed(student) 
    else: 
        print(f"Book {name} is not available in books section")  
    print(f"you succesfully borrowed the book {name}")
    
    


def return_the_book(books,student):
    list_of_allbookborrowed(student)
    name = input("Enter the name of book to return: ")
    # print(f"Looking for the book: {name}")
    book_found = False
    book_index = -1
    for index, student_book in enumerate(student):
        # print(f"checking book: {student_book["book"]} ")
        if student_book['book'] == name:
            book_found = True
            book_index = index
            # print(f"book index: {book_index}")
            break
    if book_found:
        books.append({"book": name})
        del student[book_index]
        save_data(books)
        save_studentdata(student)
        list_of_allbooks(books)
    else:
        print(f"We do not find the book {name} in student section")
    print("Thanks for returning it, Have a great day")

# print(return_the_book(books,student))

def main(): 
    while True:
        print("/n Welcome to library management system")
        print("1.List of all the book ")
        print("2.Enter the book you want to be borrow")
        print("3.Return the book you borrowed")
        print("4.View list of all borrowed book")
        print("5.Exit the app")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_of_allbooks(books)
            case '2':
                book_borrow(books,student)
            case '3':
                return_the_book(books,student)
            case '4':
                list_of_allbookborrowed(student)
            case '5':
                exit()

if __name__ == "__main__":
    main()