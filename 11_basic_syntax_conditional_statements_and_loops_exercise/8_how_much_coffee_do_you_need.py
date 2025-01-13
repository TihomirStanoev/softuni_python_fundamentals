command = input()

coffiees = 0

while command != "END":

    event = command

    if event.lower() == "coding" or event.lower() == "dog" or event.lower() == "cat" or event.lower() == "movie":
        coffiees += 1
        if event.isupper():
            coffiees += 1

    command = input()

if coffiees > 5:
    print("You need extra sleep")
else:
    print(coffiees)