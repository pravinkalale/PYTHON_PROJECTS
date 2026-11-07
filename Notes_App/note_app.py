f = open("notes.txt","w")
f.close()

while True:
    print("\n--- Notes App ---")
    print("1. Add a Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        note = input("Enter your note: ")

        f = open("notes.txt", "a")
        f.write(note + "\n")
        f.close()

        print("Note saved successfully!")

    elif choice == "2":
        try:
            f = open("notes.txt", "r")
            content = f.read()
            f.close()

            print("\nYour Notes:")
            print(content)

        except FileNotFoundError:
            print("Notes file not found!")

    elif choice == "3":
        print("Exiting Notes App. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")