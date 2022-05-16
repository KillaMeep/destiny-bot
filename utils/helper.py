import os
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import datetime
import time
class utils:
    def txtcln(text):
        return text.encode('ascii','ignore').decode()
    def dt_check():
        year = datetime.datetime.now().year
        day = datetime.datetime.now().day
        month = datetime.datetime.now().month
        hour = datetime.datetime.now().hour
        if hour > 11:
            day+=1
        date_time = datetime.datetime(year, month, day, 11, 00)
        return '<t:'+str(int(time.mktime(date_time.timetuple())))+':R>'
class chromedriver_init:
    def get_path():
        path = os.getcwd()
        return path
    
    def start(path):
        myoptions = Options()
        global driver
        myoptions.headless = True
        myoptions.add_argument("--start-maximized")
        driver = webdriver.Chrome(path+'\\utils\\chromedriver.exe', options=myoptions)
        driver.get('https://www.todayindestiny.com')
        chromedriver_init.clear_ads()
        return driver
    def clear_ads():
        all_iframes = driver.find_elements_by_tag_name("iframe")
        if len(all_iframes) > 0:
            driver.execute_script("""
                var elems = document.getElementsByTagName("iframe"); 
                for(var i = 0, max = elems.length; i < max; i++)
                     {
                         elems[i].hidden=true;
                     }
                                  """)

class tid_lookup:
    def LS():
        driver.refresh()
        chromedriver_init.clear_ads()
        LS_DAT = {}
        LS = driver.find_element(By.XPATH,'/html/body/main/div[2]/div[1]/div[12]/div[3]')
        LS.click()
        LS_text = LS.text
        LS_DAT['sectorname']=utils.txtcln(LS_text).strip('LOST SECTOR \n')
        LS_ACTUAL = utils.txtcln(driver.find_element(By.XPATH,'/html/body/main/div[2]/div[1]/div[13]/div[2]/div').text)
        LS_DAT['champs'] = LS_ACTUAL.split('Champions: ')[1].split('Burn:')[0].replace('  ',' ')[1:]
        LS_DAT['burn'] = LS_ACTUAL.split('Burn: ')[1].split('Shields:')[0][1:]
        LS_DAT['shield'] = LS_ACTUAL.split('Shields: ')[1].split('Modifiers:')[0][1:]
        LS_DAT['desc'] = LS_ACTUAL.split('Champions: ')[0]
        LS_DAT['time'] = utils.dt_check()
        os.system('if exist rewards.png del rewards.png')
        time.sleep(1)
        driver.find_element(By.XPATH,'/html/body/main/div[2]/div[1]/div[13]/div[5]').screenshot('LS.png')
        for key in LS_DAT:
            LS_DAT[key]=LS_DAT[key].strip('\n')
        return LS_DAT
    def VOG():
        driver.refresh()
        chromedriver_init.clear_ads()
        VOG_DAT = {}
        driver.find_element(By.XPATH,'/html/body/main/div[2]/div[20]/div[12]/div[1]').click()
        time.sleep(1)
        driver.find_element(By.XPATH,'/html/body/main/div[2]/div[20]/div[13]/div[4]').screenshot('vog.png')
        return VOG_DAT
    def NIGHTFALL():
        driver.refresh()
        chromedriver_init.clear_ads()
        NF_DAT = {}
        NF = driver.find_element(By.XPATH,'/html/body/main/div[2]/div[6]/div[12]/div[3]/p[2]')
        NF.click()
        NF_DAT['name']=utils.txtcln(NF.text)
        time.sleep(1)
        driver.find_element(By.XPATH,'/html/body/main/div[2]/div[6]/div[13]/div[3]').screenshot('nf.png')
        return NF_DAT