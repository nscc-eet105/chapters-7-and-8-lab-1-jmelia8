#Joe Melia EET-107

def main():
    name = input("What is the name of the file you wish to work with? ")
    action = input("Are you going to (r)ead the file or (w)rite?")
    if action == "w":
        write(name)
    elif action == "r":
        read(name)
        
def write(name):
    fname = input("Enter the first name: ")
    lname = input("Enter the last name: ")
    address = input("Enter the street address: ")
    city = input("Enter the city: ")
    state = input("Enter the state: ")
    zipcode = input("Enter the zip code: ")
    file = open(name, "w")
    file.write(f"{fname} {lname} \n{address} \n{city}, {state} {zipcode}")
    file.close()

def read(name):
    try:
        file = open(name, "r")
        contents = file.read()
        file.close()
        print("The contents of the file is: \n")
        print(contents)
    except FileNotFoundError:
        print("\nThe file is either unreachable or doesnt exist")
main()
