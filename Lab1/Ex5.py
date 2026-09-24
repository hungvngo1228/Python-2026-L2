list=["green","red","yellow","blue","pink"]
color=input("What is your favorite color?").lower()
if color in list:
    index = list.index(color)
    print(f"Your color is at index {index}")
else:
    print("Sorry, I could not find your color")