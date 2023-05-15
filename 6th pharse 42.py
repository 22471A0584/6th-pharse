input = input('Enter string:')
output = ''.join(['Yes' if input == 'yes' or input =='YES' or input =='Yes' else 'No' ])
print(str(output))
