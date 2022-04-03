price_list = [3.89, 96.05, 28.56, 1.82, 5.40, 28.88, 67.39, 84.97, 95.55, 5.79, 92.16, 62.30, 66.97, 68.31, 90.13, 26.16, 67.69, 93.58, 7.39, 29.68, 40.47]

print(id(price_list))

for price in price_list:
  rub, cents = map(int, str(price).split('.'))
    
  print(f'{rub:02} руб {cents:02} коп', end = ', ')
    
print('\n')

print(sorted(price_list)) 

print(id(price_list))


new_price_list = sorted(price_list, reverse=True)
print(new_price_list)
print(id(new_price_list))

print('\n')

print(sorted(new_price_list[:5]))

