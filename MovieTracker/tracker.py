import json

#empty list
library = []

#add book in library
def add_to_library (title, category, rating):
    for item in library: 
        if item["title"].lower() == title.lower():
            print("Υπάρχει ήδη στη βιβλιοθήκη.")
            return #σταματαει την εκτελεση της add_book()
        
    item = {
         "title":title,
         "category":category,
         "rating":rating
    }
    #add book
    library.append(item)
    #save in file
    save_library()  
    print(title + " προστέθηκε!")

#user input 
def user_input():

    #title
    while True:
        title_input = input("Τίτλος: ").strip()
        if title_input != "":  #αν δεν ειναι κενός
            break
        else: 
            print("Ο τιτλος δεν μπορεί να είναι κενός. Δοκίμασε ξανά.")

    #category
    while True:
        category_input = input("Κατηγορία (book/movie): ").strip().lower()
        if category_input in ["book","movie"]:
            break
        else: 
            print("Πληκτρολόγησε μόνο 'book' ή 'movie'.")

    #rating
    while True:
        try:
            rating_input = int(input("Βαθμολογία (1-10): "))
            if 1 <= rating_input <= 10:
                break
            else: 
                print("Η βαθμολογία πρέπει να είναι μεταξύ 1 και 10.")
        except ValueError:
            print("Πρέπει να πληκτρολογήσεις έναν αριθμό (1-10).")
    
    add_to_library(title_input, category_input, rating_input)
 
#show library
def show_library():
    if not library:
        print("Η βιβλιοθήκη είναι άδεια!")
        return
    # Απλή εκτύπωση
    for item in library:
        print("Title:",item["title"],"- Category:", item["category"], "- Rating:", item["rating"])

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
    except json.JSONDecodeError:
        library = []
        print("Το αρχείο library.json είναι κατεστραμμένο. Δημιουργείται νέο αρχείο.")
        

#save library se Json
def save_library():
    with open("library.json", "w", encoding="utf-8") as f:
        json.dump(library, f, ensure_ascii=False, indent=4)
    print("Η βιβλιοθήκη αποθηκεύτηκε στο αρχείο.")


#delete 
def delete_from_library():

    delete_title = input("Δωσε τον τίτλο του στοιχείου που θέλεις να διαγράψεις: ").strip()
    for item in library:
        if item["title"].lower() == delete_title.lower():
            library.remove(item)
            save_library()  # για να ενημερώνεται και το JSON
            print("Το στοιχείο διαγράφηκε με επιτυχία!.")
            break
    else: 
        print("Δεν υπάρχει στοιχείο με τίτλο", delete_title, "στην βιβλιοθήκη")
        return

#main
def main():
    load_library()  # load previous data

    while True:
        print("\nΤι θέλεις να κάνεις;")
        print("1 - Προσθήκη βιβλίου")
        print("2 - Προβολή βιβλιοθήκης")
        print("3 - Διαγραφή στοιχείου")
        print("4 - Έξοδος")

        choice = input("Επέλεξε: ")

        if choice == "1":
            user_input()
        elif choice == "2":
            show_library()
        elif choice == "3":
            delete_from_library()
        elif choice == "4":
            print("Έξοδος από το πρόγραμμα.")
            break
        else:
            print("Μη έγκυρη επιλογή, δοκίμασε ξανά.")

if __name__ == "__main__": 
    main()