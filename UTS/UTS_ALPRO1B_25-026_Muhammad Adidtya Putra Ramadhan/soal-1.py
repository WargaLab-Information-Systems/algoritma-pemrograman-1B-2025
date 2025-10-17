print("Rental Motor Aconk")

Motor_Matic = 50000
Motor_Trail = 100000
Motor_Sport = 75000

print(input("Aconk meiliki 3 pilihan motor : "))
print("Motor Matic Rp:", Motor_Matic)
print("Motor Trail Rp:", Motor_Trail)
print("Motor Sport Rp:", Motor_Sport)

Asuransi = 15000
sewa = 3
diskon = 10

total_biaya = (Motor_Matic, Motor_Trail, Motor_Sport)
total_asuransi = Asuransi * sewa
total_sewa = total_asuransi * sewa
diskon = total_biaya * diskon +total_sewa

print("total sewa selama 3 hari", total_sewa)