import string
def string_check(s):
    c = 0
    a = 0
    k = 0
    l = 0
    p = 0
    t = 0
    for i in s:
        alphanum = i.isalnum()
        if alphanum == True:
            c=c+1
            if c == 1:
                print("Alphanumeric characters: ",alphanum)
        else:
            t=t+1
            if t == len(s):
                print("Alphanumeric characters: ",False)
            continue
            
    t = 0
    for i in s:
        alpha = i.isalpha()
        if alpha == True:
            a=a+1
            if a == 1:
                print("Alphabets: ",alpha)
        else:
            t=t+1 
            if t == len(s):
                print("Alphabets: ",False)
            continue

    t = 0   
    for i in s:
        digi = i.isdigit()
        if digi == True:
            l=l+1
            if l == 1: 
                print("Digits: ",digi)
        else:
            t=t+1
            if t == len(s):
                print("Digits: ",False)
            continue
                          
    t = 0   
    for i in s:   
        lowercase = i.islower()
        if lowercase == True:
            k=k+1
            if k == 1: 
                print("Lowercase: ",lowercase)
        else:
            t=t+1
            if t == len(s):
                print("Lowercase: ",False)
            continue
    t = 0
    for i in s:       
        uppercase = i.isupper()
        if uppercase == True:
            p=p+1
            if p == 1: 
                print("Uppercase: ",uppercase)
        else:
            t=t+1
            if t == len(s):
                print("Uppercase: ",False)
            continue
if __name__ == '__main__':
  s = input("Enter your string: ")
  string_check(s)
