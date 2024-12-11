# locate  a treasure program

row1 = ["😎","😎","😎"]
row2 = ["😎","😎","😎"]
row3 = ["😎","😎","😎"]

print(f"{row1} \n{row2} \n{row3}")

position = input('Where do you want to put the treasure \n')
map = [row1, row2, row3]

horizontal_positon = int(position[0])
vertical_positon = int(position[1])

map[horizontal_positon][vertical_positon] = "x"
print(map)
print(f"{row1} \n{row2} \n{row3}")