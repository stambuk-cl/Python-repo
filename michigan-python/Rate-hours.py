sh = ("Enter hours: ")
su = ("Enter rate: ")
fh = float(sh) #Transform fh to a float value
fr = float(su) #Transform fr to a float value
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