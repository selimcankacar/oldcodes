#login system
#sign up
#sign in
#check if user exist
#check if password matches
#least 4, most 10 charachters
#only numbers and words
#no dublicates
import re

userpas ={"selobaba" : "selobaba234", "pancar":"pancar"}


#sign-up functions

def checkusernamewords(username):
    #least 4, most 10 charachters
    #only numbers and words

    username = str(username)
    if re.fullmatch(r'[A-Za-z0-9]{4,10}', username):
        print("acceptable username!")
        return True
    else:
        print("you can not use this username!")

def checkifusernameexists(username):
    #reach out to usernames
    #check if username exist

    usernamelist = userpas.keys()
    a=False
    for i in usernamelist:
        if i == username:
            print("this username exist!")
            return False

def checkpasswordwords(password):
    #check password is valid

    password = str(password)
    if re.fullmatch(r'[A-Za-z0-9]{4,10}', password):
        print("acceptable password!")
        return True
    else:
        print("you can not use this password!")




def signup():
    while True:
        username = str(input("Enter a username: "))
        a = checkusernamewords(username)
        if a == True:
            b = checkifusernameexists(username)
            if b == False:
                continue
            else:
                password = str(input("Enter a paswword: "))
                c = checkpasswordwords(password)
                if c == True:
                    userpas[username] = password
                    print(userpas)
                    break

#sign-in functions

def checkusername(username):
    usernames = userpas.keys()
    for i in usernames:
        if i == username:
            return True
        else:
            print("this username does not exist!")

def checkpassword(username , password):
    if userpas[username] == password:
        return True

def signin():
    while True:
        username = str(input("Enter a username: "))
        a = checkusername(username)
        if a == True:
            password = str(input("Enter a password: "))
            b = checkpassword(username, password)
            if b == True:
                print("You are in! Enjoy!")
                break
            else:
                continue
while True:
    x = str(input("Want to sign in our sign up?, Type sign in or sign up! : "))
    if x == "sign up":
        signup()
        continue
    elif(x == "sign in"):
        signin()
        break
    else:
        print("you did not type right!! Try again!")
        continue