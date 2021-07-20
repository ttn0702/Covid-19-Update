import requests 
from bs4 import BeautifulSoup
import re
from win10toast_click import ToastNotifier
import webbrowser
import time
def regex_many_value(pattern, input_string):
    regex = re.compile(pattern)
    return regex.search(input_string)

# function 
page_url = 'https://ncov.moh.gov.vn/'

def open_url():
    try: 
        webbrowser.open_new(page_url)
        print('Opening URL...')  
    except: 
        print('Failed to open URL. Unsupported variable type.')

def update():
    urls ='https://ncov.moh.gov.vn/'
    headers = {
        'cookie': 'GUEST_LANGUAGE_ID=vi_VN; COOKIE_SUPPORT=true; _ga=GA1.3.1256510830.1625976041; _gid=GA1.3.1673797526.1625976041; pageStructure=false; _gat=1; LFR_SESSION_STATE_20159=1625978995391; JSESSIONID=C5B5F11154FA04FBE3FC1A8DD15BAC53',
        'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    res = requests.get(urls,headers=headers,verify=False)
    soup = BeautifulSoup(res.text,'lxml')
    list = soup.findAll("div",{"class":"form-row"})
    for e in list:
        list_info_viet_nam = e.findAll("span",{"class":"font24"})
    so_ca_nhiem = list_info_viet_nam[0].text
    dang_dieu_tri =list_info_viet_nam[1].text
    khoi_benh = list_info_viet_nam[2].text
    tu_vong =list_info_viet_nam[3].text
    text = 'Số ca nhiễm: %s\nĐang điều trị: %s\nKhỏi bệnh: %s\nTử vong: %s'%(so_ca_nhiem,dang_dieu_tri,khoi_benh,tu_vong)
    while True:
        t = ToastNotifier()
        t.show_toast("Cập nhật Covid-19 Việt Nam", text ,duration = 20,
        icon_path = 'logo_mobile.ico',threaded=True, # True = run other code in parallel; False = code execution will wait till notification disappears 
        callback_on_click=open_url) 
        time.sleep(1800)
if __name__ == "__main__":
    update()
