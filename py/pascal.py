def pascalLine(n):
    newValue=1
    row = [newValue]
    for i in range (n):
          newValue = (newValue * (n-i)) // ( i + 1 )
          row.append(newValue)
    print(row)

pascalLine(4)
