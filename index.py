# Electricity Bill Calculator (Protected & Unprotected)

units = int(input("Enter consumed units: "))
consumer_type = input("Enter consumer type (protected/unprotected): ").lower()

bill = 0

if consumer_type == "protected":
    
    if units <= 100:
        bill = units * 10.54
    elif units <= 200:
        bill = (100 * 10.54) + (units - 100) * 13.01
    else:
        print("Usage above 200 units is NOT protected.")
        exit()

elif consumer_type == "unprotected":
    
    if units <= 100:
        bill = units * 22.44
    elif units <= 200:
        bill = 2244 + (units - 100) * 28.91
    elif units <= 300:
        bill = 2244 + 2891 + (units - 200) * 33.10
    elif units <= 400:
        bill = 2244 + 2891 + 3310 + (units - 300) * 37.10
    elif units <= 500:
        bill = 2244 + 2891 + 3310 + 3710 + (units - 400) * 40.20
    elif units <= 600:
        bill = 2244 + 2891 + 3310 + 3710 + 4020 + (units - 500) * 41.62
    elif units <= 700:
        bill = 2244 + 2891 + 3310 + 3710 + 4020 + 4162 + (units - 600) * 42.76
    else:
        bill = 2244 + 2891 + 3310 + 3710 + 4020 + 4162 + 4276 + (units - 700) * 47.69

else:
    print("Invalid consumer type")
    exit()

print("Total Electricity Bill = Rs.", round(bill, 2))
