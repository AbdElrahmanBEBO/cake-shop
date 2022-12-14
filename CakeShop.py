import random as r
import matplotlib.pyplot as plt

# Start Generating Random Variables with uniform interval [0, 1]
random_intervals_and_values = [
    {'start': 0.00, 'end': 0.04, 'value' : 0},
    {'start': 0.05, 'end': 0.14, 'value' : 1},
    {'start': 0.15, 'end': 0.19, 'value' : 2},
    {'start': 0.20, 'end': 0.29, 'value' : 3},
    {'start': 0.30, 'end': 0.44, 'value' : 4},
    {'start': 0.45, 'end': 0.74, 'value' : 5},
    {'start': 0.75, 'end': 0.89, 'value' : 6},
    {'start': 0.90, 'end': 0.94, 'value' : 7},
    {'start': 0.95, 'end': 0.99, 'value' : 8},
]

def generalizeing_numbers():
    random_uniform = r.uniform(0.0,1.0)
    for i in random_intervals_and_values:
        if random_uniform >= i['start'] and random_uniform <= i['end']:
            return i['value']
    return 0
# End Generating Random Variables with uniform interval [0, 1]



Xs=[1, 2, 3, 4, 5, 6, 7, 8]
selling_price = 4.5
old_selling_price = 1.5
cakes_cost = 2

optimal_Xs_per_days = []
optimal_profit_per_days = []


def get_cakes_profit(no_of_days):
    optimal_Xs = 0
    optimal_price  = 0
    total_profit = []

    print ("x","  ","total profit")
    for x in Xs:
        tp = 0
        z = 0

        for i in range(0, no_of_days):

            d = generalizeing_numbers()

            if x <= d :
                z = (selling_price - cakes_cost) * x
            else:
                z = (selling_price - old_selling_price) * d + (old_selling_price - cakes_cost) * x

            tp += z

            if optimal_price < tp :
                optimal_Xs = x
                optimal_price  = tp
                
        print (x,"  ",tp)   
        total_profit.append(tp)

    print('------------------------------------------')
    print('optimal x : ',optimal_Xs,', optimal profit: ',optimal_price , '\n\n')
    optimal_Xs_per_days.append(optimal_Xs)
    optimal_profit_per_days.append(optimal_price)
    return total_profit


fig, all_plt = plt.subplots(3, 3, figsize=(16, 10))

days_test = [50, 200, 400, 800, 1000, 2500, 5000]

for i in range(len(days_test)):
    all_plt[int(i/3), int(i%3)].plot(Xs,get_cakes_profit(days_test[i]))
    all_plt[int(i/3), int(i%3)].title.set_text(str(days_test[i]) + ' days')

all_plt[2, 1].plot(days_test, optimal_Xs_per_days)
all_plt[2, 1].title.set_text('optimal Xs per days')

all_plt[2, 2].plot(days_test, optimal_profit_per_days)
all_plt[2, 2].title.set_text('optimal profit per days')

plt.show()

    