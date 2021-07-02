import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "celebrities"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB:%s") % e


def get_record():
    print("")
    first = input("Enter first name >")
    last = input("Enter last name >")

    try:
        doc = find_one({"first": first.lower(), "last": last.lower()})
    except:
        print("Error accessing the database")

    if not doc:
        print("")
        print("ERROR!No results found.")

    return doc


def add_record():
    print("")
    first = input("Enter first name >")
    last = input("Enter last name >")
    dob = input("Enter date of birth>")
    gender = input("Enter gender >")
    hair_color = input("Enter hair color >")
    occupation = input("Enter occupation >")
    nationality = input("Enter nationality >")

    new_doc = {
        "first": first.lower(),
        "last": last.lower(),
        "dob": dob,
        "gender": gender,
        "hair_color": hair_color,
        "occupaton": occupation,
        "nationality": nationality
    }

    try:
        coll.insert(new_doc)
        print("")
        print("Documrnt inserted")
    except:
        print("Error accessing the database")


def show_menu():
    print("")
    add_record()
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")
    print("")

    option = input("Enter option:")
    return option


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            print("You selected option 1")
        elif option == "2":
            print("You selected option 2")
        elif option == "3":
            print("You selected option 3")
        elif option == "4":
            print("You selected option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")


conn = mongo_connect(MONGO_URI)
coll = conn[DATABASE][COLLECTION]
main_loop()
