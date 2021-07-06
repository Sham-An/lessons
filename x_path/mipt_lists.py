#URL=https://youtu.be/OR8W7MJGGGo
from selenium import webdriver
from selenium.webdriver.support.select import Select
import xlsxwriter
import time
import pandas as pd
import re
date = time.strftime("%d%m_%H%M", time.localtime())
writer = pd.ExcelWriter('43_'+date+'.xlsx', engine='xlsxwriter')
print('Текущее время',date)
list_okso_new=['01.03.02_0','01.03.02_1','03.03.01_0','03.03.01_1','03.03.01_2','03.03.01_3','03.03.01_4','03.03.01_5',
'03.03.01_6','03.03.01_7','03.03.01_8','03.03.01_9', '09.03.01_0','09.03.01_1','16.03.01', '19.03.01', '27.03.03',
'10.05.01']
list_titles=['ФАКТ Математика и информатика', 'ФПМИ Математика и информатика', 'ФРКТ Математика и физика',
'ЛФИ (ФФПФ) Математика и физика','ФАКТ Математика и физика','ФЭФМ Математика и физика','ФПМИ Математика и физика',
'ФБМФ Математика и физика','ИНБИКСТ Математика и физика','ФЭФМ Математика и химия','ФБМФ Биоинформатика',
'ФПМИ Компьютерные технологии', 'ФПМИ Информатика и вычислительная техника','ИНБИКСТ Информатика и вычислительная техника',
'ФАКТ Техническая физика', 'ФБМФ Биотехнология', 'ФАКТ Системный анализ и управление совместно с РАНХиГС', 
'ФРКТ Компьютерная безопасность']
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://pk.mipt.ru/bachelor/list/')
#driver.find_element_by_class_name('table ')
for j in range(18):
    time.sleep(2)
    Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[3]/div[2]/select')).select_by_value('1')
    Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[6]/div[2]/select')).select_by_value('2')
    if j==0:     #group1
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[4]/div[2]/select')).select_by_value('1')
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[5]/div[2]/select')).select_by_value('1011')
    elif j==1:   #group1
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[4]/div[2]/select')).select_by_value('1')
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[5]/div[2]/select')).select_by_value('1012')
    elif j==2:   #group2
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[4]/div[2]/select')).select_by_value('2')
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[5]/div[2]/select')).select_by_value('1000')
    elif j==3:   #group2
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[4]/div[2]/select')).select_by_value('2')
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[5]/div[2]/select')).select_by_value('1001')
    elif j==4:   #group2
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[4]/div[2]/select')).select_by_value('2')
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[5]/div[2]/select')).select_by_value('1002')
    elif j==5:   #group2
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[4]/div[2]/select')).select_by_value('2')
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[5]/div[2]/select')).select_by_value('1003')
    elif j==6:   #group2
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[4]/div[2]/select')).select_by_value('2')
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[5]/div[2]/select')).select_by_value('1004')
    elif j==7:   #group2
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[4]/div[2]/select')).select_by_value('2')
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[5]/div[2]/select')).select_by_value('1005')
    elif j==8:   #group2
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[4]/div[2]/select')).select_by_value('2')
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[5]/div[2]/select')).select_by_value('1006')
    elif j==9:   #group2
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[4]/div[2]/select')).select_by_value('2')
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[5]/div[2]/select')).select_by_value('1007')
    elif j==10:   #group2
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[4]/div[2]/select')).select_by_value('2')
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[5]/div[2]/select')).select_by_value('1009')
    elif j==11:   #group2
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[4]/div[2]/select')).select_by_value('2')
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[5]/div[2]/select')).select_by_value('1410')
    elif j==12:   #group3
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[4]/div[2]/select')).select_by_value('3')
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[5]/div[2]/select')).select_by_value('1015')
    elif j==13:   #group3
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[4]/div[2]/select')).select_by_value('3')
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[5]/div[2]/select')).select_by_value('1411')
    elif j==14:   #group4
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[4]/div[2]/select')).select_by_value('4')
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[5]/div[2]/select')).select_by_value('1412')
    elif j==15:   #group5
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[4]/div[2]/select')).select_by_value('5')
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[5]/div[2]/select')).select_by_value('1413')
    elif j==16:   #group6
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[4]/div[2]/select')).select_by_value('6')
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[5]/div[2]/select')).select_by_value('1017')
    elif j==17:   #group7
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[4]/div[2]/select')).select_by_value('7')
        Select(driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[5]/div[2]/select')).select_by_value('1018')    
    #submit
    driver.find_element_by_xpath('//*[@id="name_list"]/div[1]/div[2]/div/div[1]/div/div').click()
    time.sleep(12)
    if j==0:
        driver.find_element_by_xpath('//*[@id="name_list"]/div[4]/div/label').click()
        time.sleep(5)
    html=driver.page_source
    print('Получил html #',j)
    df=pd.read_html(html)
    print('Получил DataFrame')
    soglasie=re.findall('<td class="agreement">(.*?)</td>',html.replace('\n',''))
    for i in range(len(soglasie)):
        soglasie[i]=re.sub(' ','',soglasie[i])
    soglasie1=[]
    for i in range(len(soglasie)):
        soglasie1.append(re.findall('checkbox_round_(.*?)">',soglasie[i])[0])
    rus0=[]
    for i in range(len(soglasie1)):
        if soglasie1[i]=='green_empty':
            rus0.append("Нет")
        if soglasie1[i]=='green':
            rus0.append("Есть")
    abc=re.findall('<td>(.*?)</td>',html.replace('\n',''))
    for i in range(len(abc)):
        try:
            abc[i]=re.findall('<div class="checkbox_round_(.*?)"></div>',abc[i])[0]
        except:
            abc[i]=0
    abc1=[]
    for i in abc:
        if i!=0:
            abc1.append(i)
    rus1=[]
    for i in range(len(abc1)):
        if abc1[i]=='green_empty':
            rus1.append("Нет")
        if abc1[i]=='green':
            rus1.append("Есть")
    print(len(rus0),len(rus1))
    df[0]['Согласие о зачислении']=rus0
    df[0]['Преимущественное право']=rus1
    df[0].loc[0,'№']=list_titles[j]
    df[0].to_excel(writer, sheet_name=list_okso_new[j])
    print('Записал данные в новый лист', list_okso_new[j])
    time.sleep(1)
writer.save()
print('Я всё!', date)
driver.close()