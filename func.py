import random
import matplotlib.pyplot as plt
import seaborn as sns

def scale(oMin, oMax, num, nMin, nMax) -> int: 
    oRange = oMax - oMin
    oPercent = (num -  oMin) / oRange
    nRange = nMax - nMin
    newNum = oPercent * (nMax - nMin)
    newNum = int(newNum + nMin)
    return newNum

def linearRandom(max) -> int:
    num1 = random.randint(1, max)
    num2 = random.randint(1, max)
    if num1 < num2:
        return num1
    else:
        return num2
    
def log2Random(max) -> int:
    num = random.randint(1, max)
    threshold = random.randint(1, max)

    while num > threshold:
        num = random.randint(1, max)
    return num
    
def log3Random(max) -> int:
    num1 = random.randint(1, max)
    num2 = random.randint(1, max)

    while num1 > num2:
        num3 = random.randint(1, num2)
        while num1 > num3:
            num1 = random.randint(1, num3)
    return num1 

def logRandom(max, logNum) -> int:
    num = random.randint(1, max)
    for _ in range(logNum - 1):
        threshold = random.randint(1, max)
        while num > threshold:
            num = random.randint(1, threshold)
    return num



def main():
    random_numbers = [logRandom(10000, 5) for _ in range(100000)]

    plt.figure(figsize=(10, 6))
    sns.histplot(random_numbers, bins=1000, kde=True)
    plt.xlabel('Random Number')
    plt.ylabel('Frequency')
    plt.title('Distribution of Non-Uniform Random Numbers')
    plt.show()

if __name__ == "__main__":
    main()
