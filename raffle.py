# enter first name, last name, and grade
# draw a random entry
import random


def find_winner():
    if len(entries) > 0:
        winner = entries[random.randint(0, len(entries)-1)].split()
        print("The winner is: {} {} in Grade {}!".format(winner[0], winner[1], winner[2]))
    else:
        print("No winner found.")


with open("records.txt", "r") as file:
    entries = eval(file.readline())

while True:
    entry = input("Enter a name: ")
    if entry == "exit":
        break
    elif entry == "remove" and len(entries) > 0:
        entries.remove(entries[len(entries)-1])
        print(">> Last entry removed")
    elif entry == "last" and len(entries) > 0:
        print(">> The last entry was: {}".format(entries[len(entries)-1]))
    elif entry == "people":
        print(">> {} people have bought a candle.".format(len(set(entries))))
    elif entry == "sold":
        print(">> {} candles have been sold.".format(len(entries)))
    elif entry == "winner":
        find_winner()
        break
    else:
        entries.append(entry)

# save list to separate file
with open("records.txt", "w") as file:
    file.write(str(entries))
