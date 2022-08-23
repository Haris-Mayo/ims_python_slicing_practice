x = input('Enter the client Name =')
y = int(input("Enter the total required Area in Sqft ="))

"""total Brick Quantity=77130
total Brick Price =694170
Avg cost of per Brick=(Total brick price/total brick quantity)"""
Avg_cost_per_Brick = int(694170 / 77130)
z = (42.85)
per_sqft_brick = (385.72)
Total_Brick_cost = int(per_sqft_brick * y)
Total_quantity = int(Total_Brick_cost / Avg_cost_per_Brick)

"""Total cement bag =180
  total cement cost =216000
  avg cement cost (total cement cost/total cement bag"""
Avg_per_cement_cost = (216000 / 180)
per_sqft_cement = (128.572)
Total_cement_cost = int(per_sqft_cement * y)
Total_bag_cement = int(Total_cement_cost / Avg_per_cement_cost)

"""iron weight 1800kg 
cost of iron 39600
avg iron cost (cost of iron/iron weight)"""
Avg_iron_cost = (396000 / 1800)
Total_sqft_iron = int(1 * y)
Total_cost_iron = int(Total_sqft_iron * Avg_iron_cost)

print("***************************output********************************")

output = f'''Dear,Mr.{x}
      Our building construction analysis system has calculated the required 
    quantity of material, material cost, labour cost and total cost for the 
    construction of grey structure of your building. Please find the
    below mentioned details

    Bricks Quantity ={Total_quantity} \t\t Brick cost ={Total_Brick_cost}:
         cement Quantity ={Total_bag_cement}\t\tcement cost ={Total_cement_cost}:
      Iron Required Weight  ={Total_sqft_iron}kg \t Iron Cost:{Total_cost_iron}'''

Labour_cost = int(300 * y)
Total_cost = int(Total_Brick_cost + Total_cement_cost + Total_cost_iron)

print(output)

print("\nTotal labour cost=", Labour_cost, "Rs")
print("Total cost=", Total_cost, "Rs")
print("  \n with Best Regards,\n ABC Construction Company")
print("***************************Thank You**************************")

