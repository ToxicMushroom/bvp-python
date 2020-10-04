gallons_in_tank = float(input('How many gallons are in your tank: '))
fuel_efficiency = float(input('What is your fuel efficiency (miles per gallon): '))  # miles per gallon
gallon_price = float(input('What is the price per gallon: '))

DISTANCE = 100

fuel_usage = DISTANCE/fuel_efficiency
price = gallon_price * fuel_usage
max_distance = fuel_efficiency * gallons_in_tank

print(f'fuel usage per 100 miles: {fuel_usage} gallons')
print(f'price per 100 miles {price}')
print(f'max distance with {gallons_in_tank} gallons: {max_distance} miles')
