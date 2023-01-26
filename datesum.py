year = int(input("Введите год: "))
isLeap = False
dateSum = 0

if year%4 == 0 and year%100 == 0 and year%400 == 0:
    print("Год високосный\n")
    isLeap = True

for i in range(1, 13):
    if i == 2:
        if isLeap:
            for j in range(1, 30):
                dateSum += sum(map(int, str(j)))
        else:
            for j in range(1, 29):
                dateSum += sum(map(int, str(j)))
    else:
        if i in(1, 3, 5, 7, 8, 10, 12):
            for j in range(1, 32):
                dateSum += sum(map(int, str(j)))
        else:
            for j in range(1, 31):
                dateSum += sum(map(int, str(j)))

print(f"Сумма дней месяцев: {dateSum}")