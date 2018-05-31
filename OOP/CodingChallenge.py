# Date: May 15 2018
class Fruit:

    def __init__(self, name, price):
        self.name = name
        self.price = price


    def __str__(self):
        return "Name: {}, Price: {}".format(self.name, self.price)


banana = Fruit("Banana", 10)
apple = Fruit("Apple", 5)
strawberry = Fruit("Strawberry", 2)
grape = Fruit("Grape", 8)
watermelon = Fruit("Watermelon", 19)

soldFruits = [banana, apple, strawberry, banana, apple, strawberry, banana, apple, watermelon, watermelon, grape, strawberry, apple]
dict = dict()

def count_the_total(list):
    for fruit in list:
        if fruit.name in dict:
            dict[fruit.name] += fruit.price
        else:
            dict[fruit.name] = fruit.price

    print(dict)


#count_the_total(soldFruits)
def arrayMaxConsecutiveSum2(inputArray):
    maxNum = inputArray[0]
    for i  in range(0, len(inputArray) - 1):
        if (inputArray[i] + inputArray[i+1]) > maxNum:
            maxNum = (inputArray[i] + inputArray[i+1])

    return maxNum


print(arrayMaxConsecutiveSum2([-3, -2, -1, -4]))


# String convert the words in the right order
def convertString(inputString):
    arrayOfString = inputString.split(" ")
    reversedCharacter = list(map(lambda x: x[::-1], arrayOfString))
    return " ".join(reversedCharacter)

print(convertString("alisher abdukarimov"))