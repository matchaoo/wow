import sys
randomList = ['a', 0, 2]
for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occured.")
        print("Next ecntry.")
        print()
print("The reciprocal of", entry, "is", r)

'''
try:
      input1 = int(input("A :"))
      input2 = int(input("B :"))
      print(input1/input2)
    except ValueError:
       print("Error ! Please Re-Enter Number")
    except ZeroDivisionError:
      print("Error ! You Can’t Enter 0")
    except:
      print("Error !")
'''