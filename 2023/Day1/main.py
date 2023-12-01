final = 0

with open('2023/Day1/input.txt', 'r') as file:
  for line in file:
    line = line.strip()
    temp = ''
    for char in line:
      if char.isdigit():
        temp += char
        break

    reversed_line = line[::-1]
    for char in reversed_line:
      if char.isdigit():
        temp += char
        final += int(temp)
        break    
      
print(final)