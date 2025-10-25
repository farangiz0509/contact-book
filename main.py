from app.contact_book import ContactBook


def main() -> None:
    book = ContactBook()

    while True:
        print(
            "1 Add new contact\n"
            "2kontactlarni korsatish hammasini\n"
            "3 contactni ismi buyicha izlash\n"
            "4 yangilash yoki ochirish contactni\n"
            "5 chiqish"
        )

        choice = input("> ")
        if choice == '1':
            name = input("name: ")
            phone = input("phone: ")
            email = input("email: ")
            book.add_contact(name, phone, email)

        elif choice == '2':
            book.show_all()

        elif choice == '3':
            name = input("izlash uchun ism kiriting: ")
            book.search(name)

        elif choice == '4':
            name = input("yangilash yoki ochirish uchun ism kiriting: ")
            book.update_or_delete(name)

        elif choice == '5':
            print("xayr!")
            break

        else:
            print("Invalid tanlov.")


if __name__ == "__main__":
    main()