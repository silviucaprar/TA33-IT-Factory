"""
Ex4.
1.   Sa se creeze un dictionar cu 5 carti care sa contina numele cartii, autorul, nr_pag, mesaj (daca este available sau nu)
2.   Sa se creeze o functie care sa ii permita bibliotecarului sa poate adauga carti noi in biblioteca (dictionar).
3.   Sa se creeze o functie care sa ii permita bibliotecarului sa poata sterge carti din biblioteca
4.   Sa se creeze o functie care sa ii permita bibliotecarului sa introduca un nume de carte si sa verifice daca este available sau nu
"""

books = [{"title": "Singur pe lume",
          "page_nr": 200,
          "author": "Hector Malot",
          "available": True
         },

         {"title": "Lestat Vampire",
          "page_nr": 500,
          "author": "Anne Rice",
          "available": True
          },

         {"title": "Jack the Ripper",
          "page_nr": 250,
          "author": "Kerri Maniscalco",
          "available": False
         },

         {"title": "City of Bones",
          "page_nr": 560,
          "author": "Cassandra Claire",
          "available": False
         },

         {"title": "Girls of Nightmare",
          "page_nr": 180,
          "author": "Kendare Blake",
          "available": True
         },
]

def add_book(books, title, page_nr, author, is_available):
    book_dict = {"title": title,
                 "page_nr": page_nr,
                 "author": author,
                 "available": is_available}
    books.append(book_dict)

def display_books(book_list):
    for book in book_list:
        print(book)

def del_book(book_list, book):
    for i in range(len(book_list)):
        if book_list[i]["title"] == book:
            del book_list[i]
            break
    return "The book is not in the list"

def show_availability(book_list, book):
    for i in range(len(book_list)):
        if book_list[i]["title"] == book:
            return book_list[i]["available"]
    return "The book is not in the list"


# afisam lista de carti
print("###### afisam lista de carti ######")
display_books(books)

# adaugam o carte in lista
add_book(books,"Shogun", 560, "James Clavel", True )
print("###### afisam lista de carti ######")
display_books(books)
del_book(books, "Shogun")
print("###### afisam lista de carti ######")
display_books(books)

# verificam daca cartea este sau nu available
print(show_availability(books, "Singur pe lume"))


