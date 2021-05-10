sh = input("Enter hours: ")
su = input("Enter rate: ")
try: #Dangerous zone, here you put the try to handle the error
    fh = float(sh) #Transform fh to a float value
    fr = float(su) #Transform fr to a float value
except:
    print("Please enter a numeric value")
    quit()
# print (fr, fh)
if fh > 40 :
    #print("Overtime")
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    #print(reg, otp)
    xp = reg + otp
else:
    # print('Regular')
    xp = fh * fr
print("Pay:",xp)