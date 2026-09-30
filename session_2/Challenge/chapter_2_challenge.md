
# 1
| Legal | Illegal |
|-------|---------|
|`hello`|`0123456`|
|`_faux`|`#variab`|
|`sl33p`|`+two+22`|
|-------|---------|

# 2
```py
favourite_foods = [input(f"Favourite food {i+1}") for i in range(2)]
print(f"New food = {" ".join(favourite_foods)}")
```
# 3
```py
bill_cost = float(input("Bill Cost: "))
print(f"15% tip: £{bill_cost*0.15}")
print(f"20% tip: £{bill_cost*0.20}")
```
# 4
```py
base_price = float(input("Base Price > "))
tax_cost = base_price * 0.99        #  99%
license_cost = base_price * 3.15    # 315%
dealer_prep = 4000
destination_charge = 30
doughnut_tire_insurance = base_price * 0.3 + 1000
final_cost = base_price + tax_cost + license_cost + dealer_prep + destination_charge + doughnut_tire_insurance
print(f"Cost of your car (but with the hidden fees): £{final_cost}")
```
