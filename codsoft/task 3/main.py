import random
import string as st

specChar = ["@","#", "$", "%", "&", ".", "*"]
pass_length = int(input("Enter the length of password: "))
password = []
ch = st.ascii_letters + st.digits + random.choice(specChar)
if pass_length < 8:
    print("Password length should be at least 8 characters")
else:
    for i in range(0,pass_length):
        password.append(random.choice(ch))
    print("".join(password[0:pass_length]))


    
