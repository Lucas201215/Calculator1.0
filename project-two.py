class function:
    def add():
        print("Ask me any addtion qustion")
        a = float(input("First:"))
        b = float(input("Second:"))
        c = float(a + b)
        print(float(c))
    def subtract():
        print("Ask me any subtraction question")
        a = float(input("First:"))
        b = float(input("Second:"))
        c = float(a - b)
        print(float(c))
running = True
while running:
    a = input("Would you like to add,subtract or quit the program:")
    if a == "add":
        function.add()
    elif a == "subtract":
        function.subtract()
    else:
        running = False


    
