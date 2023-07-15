import pickle
import os

classes = []
for _ in range(12):
    classes.append([])

index = 0

if os.path.isfile("bckp.pkl"):
    classes = pickle.load(open("bckp.pkl", 'rb'))
    print(f"Classes : {classes}")
    index = int(input("Index : "))

def print_classes(classes):
    for i in range(len(classes)):
        print(f"============ Class : {i + 1} ============")
        for e in classes[i]:
            print(f"\t{e}")
    print()

while 1:
    try:
        nb = int(input("Nb to add : "))
        lang = input("Lang : ")
        option1 = input("Option 1 : ")
        option2 = input("Option 2 : ")
        if option1 == "":
            option1 = None
        if option2 == "":
            option2 = None
        for _ in range(nb):
            classes[index].append({"Lang": lang, "Option1": option1, "Option2": option2})
        if input("Change index : ") != "":
            index += 1
        print("Current classes :")
        print_classes(classes)
    except Exception as e:
        print(f"An error occured : {e}")
        pickle.dump(classes, open("bckp.pkl", 'wb+'))
        break
