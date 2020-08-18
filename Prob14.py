def oddProgression(current) -> int:
    return current * 3 + 1

def evenProgression(current) -> int:
    return current / 2

def progression(current) -> int:
    if current % 2 == 0:
        return evenProgression(current)
    
    return oddProgression(current)

def countProgressions(num) -> int:
    
    current = num
    count = 0

    while current > 1:
        current = progression(current)
        count += 1

    return count

highestCount = 0
highestStart = 0
for number in range(1000000, 0, -1):
    count = countProgressions(number)
    if count > highestCount:
        highestCount = count
        highestStart = number

print("Highest Start: "+str(highestStart))