import sys
if len(sys.argv) == 1:
	print(f'Usage: "python3 pass.checker.py <PASSWORD>"\n(Use "-h" como opcion para obtener mas informacion)')
	sys.exit()
if '-h' in sys.argv or '--help' in sys.argv:
	print('''
Ejemplo use: python3 pass.checker.py 1234 
-h                     ''')
	sys.exit()

 
import time 
import sys 
import os 
  

def load_animation(): 
  

    load_str = "Cargando Verifcador de passwords, gracias por usar este tool :}"
    ls_len = len(load_str) 
  
  
  
    animation = "|/-\\"
    anicount = 0
  
    counttime = 0        
      
 
    i = 0                     
  
    while (counttime != 40): 
          
        
        time.sleep(0.075)  
                              
       
        load_str_list = list(load_str)  
          
       
        x = ord(load_str_list[i]) 
          
    
        y = 0                             
   
        if x != 32 and x != 46:              
            if x>90: 
                y = x-32
            else: 
                y = x + 32
            load_str_list[i]= chr(y) 
          
       
        res =''              
        for j in range(ls_len): 
            res = res + load_str_list[j] 
              
       
        sys.stdout.write("\r"+res + animation[anicount]) 
        sys.stdout.flush() 
  
      
        load_str = res 
  
          
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len 
        counttime = counttime + 1
      
   
    if os.name =="nt": 
        os.system("cls") 
          

    else: 
        os.system("clear") 
  

if __name__ == '__main__':  
    load_animation() 


banner = r'''
 ____    ____  _____ _____                       
|    \  /    T/ ___// ___/                       
|  o  )Y  o  (   \_(   \_                        
|   _/ |     |\__  T\__  T                       
|  |   |  _  |/  \ |/  \ |                       
|  |   |  |  |\    |\    |                       
l__j   l__j__j \___j \___j                       
                                                 
    __  __ __    ___     __  __  _    ___  ____  
   /  ]|  T  T  /  _]   /  ]|  l/ ]  /  _]|    \ 
  /  / |  l  | /  [_   /  / |  ' /  /  [_ |  D  )
 /  /  |  _  |Y    _] /  /  |    \ Y    _]|    / 
/   \_ |  |  ||   [_ /   \_ |     Y|   [_ |    \ 
\     ||  |  ||     T\     ||  .  ||     T|  .  Y
 \____jl__j__jl_____j \____jl__j\_jl_____jl__j\_j

 Created por: ZQYS
 Instagram: payl0add
 Tiktok: bye.zqys

 Gracias por elegir este tool.

'''

def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))  
red = "\033[91m {}\033[00m"
prYellow(banner)






from time import sleep
import sys

line_1 = red+"Verificador de passwords creado por: ZQYS "
for x in line_1:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.1)

prCyan("\nVerficando Password!...")


import sys
import time


def updt(total, progress):
    

    barLength, status = 20, ""
    progress = float(progress) / float(total)
    if progress >= 1.:
        progress, status = 1, "\r\n"
    block = int(round(barLength * progress))
    text = "\r[{}] {:.0f}% {}".format(
        "#" * block + "-" * (barLength - block), round(progress * 100, 0),
        status)
    sys.stdout.write(text)
    sys.stdout.flush()


runs = 10
for run_num in range(runs):
    time.sleep(.1)
    updt(runs, run_num + 1)



prGreen("\n+++++++++++++++++++++++++++++++++++++++++++++++")




import requests
import hashlib
import sys


def request_api_data(query_char):
  url = 'https://api.pwnedpasswords.com/range/' + query_char
  res = requests.get(url)
  if res.status_code != 200:
    raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
  return res

def get_password_leaks_count(hashes, hash_to_check):
  hashes = (line.split(':') for line in hashes.text.splitlines())
  for h, count in hashes:
    if h == hash_to_check:
      return count
  return 0

def pwned_api_check(password):
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  first5_char, tail = sha1password[:5], sha1password[5:]
  response = request_api_data(first5_char)
  return get_password_leaks_count(response, tail)
  


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
             print('\x1b[6;30;42m' + f'\n{password} se encontró {count} veces en una violación de datos... \n¡probablemente debería cambiar su password!' + '\x1b[0m')
             prGreen("\n+++++++++++++++++++++++++++++++++++++++++++++++")
        else:
            print('\x1b[6;30;42m' + f'\n{password} NO se encontró en filtraciones de datos. \n¡Continúa!' + '\x1b[0m')           
            prGreen("\n+++++++++++++++++++++++++++++++++++++++++++++++")
    prRed("Gracias por aver usado este tool, espero te haya servido, ahora puedes disfutar de lo que estas ingeriendo o tomando")

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))

