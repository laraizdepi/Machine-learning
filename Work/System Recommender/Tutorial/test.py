class triangle():
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    number_of_sides = 3
    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False
my_triangle = triangle(60, 90, 30)
print(my_triangle.number_of_sides)
print(my_triangle.check_angles())

# class Lunch():
#     def __init__(self, menu):
#         self.menu = menu
    
#     def menu_price(self):
#         if self.menu == "menu1":
#             print("Your choice: ", menu, "Price 12.00")
#         if self.menu == "menu2":
#             print("Your choice: ", menu, "Price 13.40")
#         else:
#             print("Error in Menu")
# Paul = Lunch("menu1")
class Lunch(object):
    def __init__(self,menu):
      self.menu=menu

    def menu_price(self):
       if self.menu=="menu 1":
          print ("Your choice:", self.menu, "Price 12.00")
       elif self.menu=="menu 2":
          print ("Your choice:", self.menu, "Price 13.40")
       else:
          print ("Error in menu")

Paul=Lunch("menu 4")
Paul.menu_price()