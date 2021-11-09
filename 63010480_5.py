numOfCar, booking = input('Enter Input : ').split('/')
booking = booking.split()
listOfCar = [0]*int(numOfCar)
customer = 1
for i in booking:
    booked = False
    while not booked:
        if 0 in listOfCar:
            for n in range(0,len(listOfCar)):
                if listOfCar[n] == 0:
                    index = n
                    break
            listOfCar[index] += int(i)
            print(f'Customer {customer} Booking Van {index+1} | {i} day(s)')
            customer += 1
            booked = True
        else:
            for n in range(0,len(listOfCar)):
                listOfCar[n] -= 1