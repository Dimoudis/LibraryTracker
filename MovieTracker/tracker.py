import json

#empty list
library = []

#add book in library
def add_book(title, category, rating):
    book = {
         "title":title,
         "category":category,
         "rating":rating
    }
    #add book
    library.append(book)
    #save in file
    save_library()  
    print(title + " προστέθηκε!")

#user input 
def user_input():
    title_input = input("Τίτλος: ")
    category_input = input("Κατηγορία (book/movie): ")
    rating_input = int(input("Βαθμολογία (1-10): "))
    add_book(title_input, category_input, rating_input)
 
#show library
def show_library():
    if not library:
        print("Η βιβλιοθήκη είναι άδεια!")
        return
    # Απλή εκτύπωση
    for book in library:
        print("Title:",book["title"],"- Category:", book["category"], "- Rating:", book["rating"])

#load library se Json
def load_library():
    global library
    try:
        with open("library.json", "r", encoding="utf-8") as f:
            library = json.load(f)
            print("Φορτώθηκε η βιβλιοθήκη από το αρχείο.")
    except FileNotFoundError:
        library = []
        print("Δεν βρέθηκε αρχείο, ξεκινάμε νέα βιβλιοθήκη.")

#save library se Json
def save_library():
    with open("library.json", "w", encoding="utf-8") as f:
        json.dump(library, f, ensure_ascii=False, indent=4)
    print("Η βιβλιοθήκη αποθηκεύτηκε στο αρχείο.")

#main
def main():
    load_library()  # load previous data

    while True:
        print("\nΤι θέλεις να κάνεις;")
        print("1 - Προσθήκη βιβλίου")
        print("2 - Προβολή βιβλιοθήκης")
        print("3 - Έξοδος")

        choice = input("Επέλεξε: ")

        if choice == "1":
            user_input()
        elif choice == "2":
            show_library()
            break
        elif choice == "3":
            print("Έξοδος από το πρόγραμμα.")
            break
        else:
            print("Μη έγκυρη επιλογή, δοκίμασε ξανά.")
            break

if __name__ == "__main__": 
    main()