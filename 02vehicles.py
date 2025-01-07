i = True

while i:
    vehicle = input("ENter the Vehicle name : ").lower()
    if vehicle != "bus":
        print("Waiting")
        continue
    elif vehicle == "bus":
        print("Finally the wait is over")
        break
    else:
        pass
