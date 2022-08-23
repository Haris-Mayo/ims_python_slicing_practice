car=int(input("Enter the total number of car="))
main_body=40
side_mirror=8
tyres=12
remote=25
other_cost=18
total_cost=main_body+side_mirror+tyres+remote+other_cost
selling_rate=500
total_profit=(selling_rate-total_cost)
profit_on_each_car=(total_profit)/car
print( total_cost)
print(total_profit)
print(profit_on_each_car)