car=int(input("Enter the total number of car="))
main_body=40*car
side_mirror=8*car
tyres=12*car
remote=25*car
Total_bugdet_required=18*car
cost_of_each_required=Total_bugdet_required/car
selling_rate_car=500*car
Total_profit=selling_rate_car-Total_bugdet_required
profit_on_each_car=(selling_rate_car-Total_bugdet_required)/car

output=f'''order of the car ={main_body}:
side mirror = {side_mirror}:
tyres = {tyres}:
remote = {remote}
Total budget required Rs = {Total_bugdet_required}
cost on each car Rs = {cost_of_each_required}
Total profit Rs = {Total_profit}
profit_on_each_car Rs = {profit_on_each_car}'''
print(output)