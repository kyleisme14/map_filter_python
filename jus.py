#----1----
# map: raising the price of all prices in a shopping list 2 x's
# filter: sorting a shopping list by specific price (high & low)…

# DECLARING THE DATA
shopping_total = [150, 200, 300, 100, 50, 20, 9]

#MAP / NAME FUNCTION
def double_shopping_total(num):
    return num + num


result = map(double_shopping_total, shopping_total)
print('LIST OF SHOPPING TOTALS UP 2X', list(result))

# MAP / LAMBDA FUNCTION
double_result = map(lambda x: x * 2, shopping_total)
print('LIST OF SHOPPING TOTALS UP 2X', list(double_result))

# FILTER / NAME FUNCTION
def is_high(shopping_price):
    if shopping_price > 100:
        return True
    else:
        return False

high_cost = list(filter(is_high, shopping_total))
print('HIGH COST', high_cost)

# FILTER / LAMBDA FUNCTION
low_price = list(
    filter(lambda shopping_price: shopping_price < 100, shopping_total))
print('LOW PRICE', low_price)


#----2----
# MAP: Display all of the game scores for the blazers this season.
# FILTER:  Only display the games when they scored over 100 points.

# DECLARING THE DATA
game_scores = [124, 134, 116, 116, 112]

#MAP / NAME FUNCTION
def blazers_scores(num):
    return num

result = map(blazers_scores, game_scores)
print('BLAZERS INDIVIDUAL SCORES', list(result))

#MAP / LAMBDA FUNCTION
results2 = map(lambda x: x, game_scores)
print('BLAZERS INDIVIDUAL SCORES', list(results2))

# FILTER / NAME FUNCTION
def high_score(game_scores):
    if game_scores > 100:
        return True
    else:
        return False

blazer_high = list(filter(high_score, game_scores))
print('OVER 100 POINTS!', blazer_high)

#FILTER / LAMBDA FUNCTION
over_hun = list(
    filter(lambda scores: scores > 100, game_scores))
print('OVER 100 POINTS!', over_hun)

#-----3-----
# MAP: though a list of jordan retro s and
# FILTER: out the ones you dont buy

# DECLARING THE DATA
jeffery_jordans = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# MAP / NAME FUNCTION
def all_jordans(num):
    return num

result = map(all_jordans, jeffery_jordans)
print('LIST OF ALL JORDANS', list(result))

# MAP / LAMBDA FUNCTION
jresults = map(lambda x: x, jeffery_jordans)
print('LIST OF ALL JORDANS', list(jresults))

# FILTER / NAME FUNCTION
def naw_dog(dont_buy):
    if dont_buy > 13:
        return True
    else:
        return False

not_these = list(filter(naw_dog, jeffery_jordans))
print('DONT BUY THESE JORDANS', not_these)

# FILTER / LAMBDA FUNCTION
dont_cop = list(
    filter(lambda nah: nah > 13, jeffery_jordans))
print('DONT BUY THESE JORDANS', dont_cop)
