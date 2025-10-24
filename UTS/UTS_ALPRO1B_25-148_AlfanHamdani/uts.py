# ulang = "y"

# while "y":
rentalMotor = input("Masukkan jenis motor: ")

total_rental = 0

motorMatic = "motor matic"
motorTrail = "motor trail"
motorSport = "motor sport"

hargaMotorMatic = 50000
hargaMotorTrail = 100000
hargaMotorSport = 75000

if rentalMotor == motorMatic:
    print("harga motor matic adalah", hargaMotorMatic)
elif rentalMotor == motorTrail:
    print("harga motor trail adalah", hargaMotorTrail)
else:
    print("harga motor sport adalah", hargaMotorSport)