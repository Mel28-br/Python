num = []
n = str(input("Insirar tres número: "))

for i in n.split():
    num.append(int(i))

print(f"O número maior é {max(num)} e o menor é {min(num)}")