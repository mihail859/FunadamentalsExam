import re


pattern = r'@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+'
n = int(input())

for _ in range(n):
    line = input()
    digits = ''
    result = re.findall(pattern, line)
    if result:
        digits_result = re.findall(r'\d', line)
        if digits_result:
            pass
        else:
            digits = '00'
    else:
        print("Invalid barcode")