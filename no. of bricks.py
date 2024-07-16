#write a python program to count total no. of bricks in wall. take dimensions of brick and wall from user.
WL=int(input("Enter lenghth of wall :"))
WB=int(input("Enter breadth of wall :"))
WH=int(input("Enter height of wall :"))
BL=int(input("Enter lenght of brick :"))
BB=int(input("Enter breadth of brick :"))
BH=int(input("Enter height of brick :"))
wall=WL*WB*WH
brick=BL*BB*BH
x=wall//brick
print(f"NO. of bricks in a wall are : {x}")
