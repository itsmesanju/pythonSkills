#Error Handling
while True:
    try:
     age = int(input('whats your age? '))
#     print(age)
     10/age

    except ValueError:
     print('Please enter number')
    except ZeroDivisionError:
     print('no zero please')
    else:
     print('thanks')
     break
