print('This program will calculate all of the coordinates\nfor the corners of a rectangle.\nBut first you will need to enter a little data.\n')
x_coord = int(input("Enter the x coordinate for the lower left corner of the\nrectangle:\t"))
y_coord = int(input("Enter the y coordinate for the lower left corner of the\nrectangle:\t"))


width = int(input("\nEnter the width of the rectangle:\t"))
height = int(input("Enter the height of the rectangle:\t"))
# print(f'{width}\n{height}\n')


upper_left = (x_coord,height)
upper_right = (width,height)
lower_right = (x_coord,y_coord)
lower_left = (width,y_coord)
print('\nHere are your results.')
print(f'Upper Left Corner Coordinates:\t{upper_left}\nUpper Right Corner Coordinates:\t{upper_right}\nLower Left Corner Coordinates:\t{lower_left}\nLower Right Corner Coordinates:\t{lower_right}')
