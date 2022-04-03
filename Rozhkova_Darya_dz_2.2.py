main_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

main_list [1] = '05'
main_list [8] = '+05'

main_list = main_list[:1] + ['"'] + main_list[1:2] + ['"'] + main_list[2:3] + ['"'] + main_list[3:4] + ['"'] + main_list[4:8] + ['"'] + main_list[8:9] + ['"'] + main_list[9:]
print(main_list)

#print(type(main_list))

print(*main_list)


print(', '.join(x for x in main_list if x.isdigit()))
