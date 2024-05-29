def draw_retangle(lines=1, columns=1):

    
    lines = max(1, min(lines, 20))
    columns = max(1, min(columns, 20))
    
   
    for i in range(lines):


        for j in range(columns):


            if i == 0 or i == lines - 1:
                if j == 0 or j == columns - 1:
                    print("+", end="")
                else:
                    print("-", end="")


                    
            else:
                if j == 0 or j == columns - 1:
                    print("|", end="")
                else:
                    print(" ", end="")
        print()  

# Exemplos de uso
draw_retangle(5, 10)
print()
draw_retangle(3, 5)
print()
draw_retangle(25, 30)
print()
draw_retangle()
