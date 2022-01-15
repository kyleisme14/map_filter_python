# getting specific titles from like a list of books?
# going through a list of books to get all mtheir names?
#instead. pricing through books.

import re


bookPrice = [11, 22, 33 ,44]
HarryPotter = 11
MobyDick = 22
Bible = 33
Shakespeare = 44

def double_bookPrice(num):
    return num * 2

results1 = map(double_bookPrice, bookPrice)
print("lambda", list(results1))

low_price = list(
    filter(lambda book_price: book_price < 33, bookPrice)
    )
print("Low price", low_price)

high_price = list(
    filter(lambda book_price: book_price >= 33, bookPrice)
    )
print("High price", high_price)

def bookpricer(book):
    if book in low_price:
        print("buy this")
    else: 
        print("too much")

bookpricer(MobyDick)


## menu items price increase    

sandwich = 1
soda = 2
chips = 3
salad = 4
food = [1,2,3,4]

def foodPriceAdjuster(nums):
    return nums + .99

results2 = map(foodPriceAdjuster, food)
print("new price = ", list(results2))

def foodPricer(nums):
    if nums > 2:
        print("YUP")
    else:
        print("NO WAY")

foodPricer(salad)