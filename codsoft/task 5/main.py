import pandas as pd
import os

listName = []
listCont = []
listMail = []

print("Welcome to your contact list")
print("-" * 20)
print("Enter choice 1 to add contact")
print("Enter choice 2 to delete contact")
print("Enter choice 3 to search contact")
print("Enter choice 4 to update contact")
print("Enter choice 5 to view contact list")
print("Enter choice 6 to exit")
print("-" * 20)

if not os.path.exists("contact.csv"):
    df = pd.DataFrame(columns=["Name", "Contact No", "E-mail"])
    df.to_csv("contact.csv", index=False)

while True:
    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            addname = input("Enter a name: ")
            addcontact = input("Enter contact: ")
            addmail = input("Enter mail: ")

            new_entry = pd.DataFrame([[addname, addcontact, addmail]], columns=["Name", "Contact No", "E-mail"])
            df = pd.read_csv("contact.csv")
            df = pd.concat([df, new_entry], ignore_index = True)
            df.to_csv("contact.csv", index=False)
            print("Contact added successfully")

        elif choice == 2:
            delname = input("Enter name to delete contact: ")
            df = pd.read_csv("contact.csv")

            if delname in df["Name"].values:
                df = df[df["Name"] != delname]
                df.to_csv("contact.csv", index=False)
                print("Your contact has been deleted")
            else:
                print("Your contact is not found")

        elif choice == 3:
            searchname = input("Enter name to search contact: ")
            df = pd.read_csv("contact.csv")

            if searchname in df["Name"].values:
                df = df[df["Name"] == searchname]
                print(df)
            else:
                print("Your contact is not found")

        elif choice == 4:
            print("-" * 20)
            print("Enter choice 1 to update name")
            print("Enter choice 2 to update contact")
            print("Enter choice 3 to update mail")
            print("-" * 20)

            updatechoice = int(input("Enter your choice: "))
            df = pd.read_csv("contact.csv")

            if updatechoice == 1:
                old_name = input("Enter the name you want to update: ")
                new_name = input("Enter the new name: ")

                if old_name in df["Name"].values:
                    df.loc[df["Name"] == old_name, "Name"] = new_name
                    df.to_csv("contact.csv", index = False)
                    print("Name updated successfully")
                else:
                    print("Your contact is not found")

            elif updatechoice == 2:
                name = input("Enter the name whose contact you want to update: ")
                new_contact = input("Enter the new contact number: ")

                if name in df["Name"].values:
                    df.loc[df["Name"] == name, "Contact No"] = new_contact
                    df.to_csv("contact.csv", index=False)
                    print("Contact updated successfully")
                else:
                    print("Your contact is not found")

            elif updatechoice == 3:
                name = input("Enter the name whose email you want to update: ")
                new_email = input("Enter the new email: ")

                if name in df["Name"].values:
                    df.loc[df["Name"] == name, "E-mail"] = new_email
                    df.to_csv("contact.csv", index=False)
                    print("Email updated successfully")
                else:
                    print("Your contact is not found")

            else:
                print("Invalid choice for updating")

        elif choice == 5:
            df = pd.read_csv("contact.csv")
            print(df)

        elif choice == 6:
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please Check the instructions again")

    except ValueError:
        print("Please enter a valid numeric choice")
