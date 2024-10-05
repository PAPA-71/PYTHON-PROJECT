import random

logo=("""
\033[1;92m███    ███  █████  ██   ██ ██ ███    ██ 
\033[1;92m████  ████ ██   ██ ██   ██ ██ ████   ██ 
\033[1;92m██ ████ ██ ███████ ███████ ██ ██ ██  ██ 
\033[1;92m██  ██  ██ ██   ██ ██   ██ ██ ██  ██ ██ 
\033[1;92m██      ██ ██   ██ ██   ██ ██ ██   ████ 
\033[1;91m╔══════════════════════════════════════╗
\033[1;92m║        WELCOME TO MY KINGDOM         ║     
\033[1;91m╚══════════════════════════════════════╝                                     
\033[1;91m╔══════════════════════════════════════╗
\033[1;92m║\033[1;97m[+] DEVOLPER   : \033[1;92mMAHIN                ║
\033[1;92m║\033[1;97m[+] FACEBOOK   : \033[1;92mMH MAHIN             ║
\033[1;92m║\033[1;97m[+] GITHUB     : \033[1;92mMAHIN-71             ║
\033[1;92m║\033[1;97m[+] VERTION    : \033[1;92m1.4                  ║
\033[1;91m╚══════════════════════════════════════╝""")

#clear()
print(logo)








def bd():
 list=[]
 print("code example : 017 018 019 016 013")
 code=input(" put code : ")
 for i in range(int(input("how many numbet genrate : "))):
  r=''.join(random.choices('0123456789',k=8))
  combine=code+r
  list.append(combine)
  print(list[i])


  
  
  
def ind():
 list=[]
 print("code example : 9163 9183 etc..")
 code=input(" put code : ")
 for i in range(int(input("how many numbet genrate : "))): 
  r=''.join(random.choices('0123456789',k=8))
  combine=code+r
  list.append(combine)
  print(list[i])

print("Which Country Number Generate?")
print("1: Bangladesh (BD)")
print("2: India (IND)")
user = input("Put number: ")

if user in["1", "01"]:
 bd()
elif user in["2", " 02"]:
 ind()
else:
 print(" error")