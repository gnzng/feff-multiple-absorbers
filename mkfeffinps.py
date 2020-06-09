from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from pynput.keyboard import Key, Controller

keyboard = Controller()
import time
import os

drv = webdriver.Firefox()
drv.get("https://millenia.cars.aps.anl.gov/webatoms/")

print(os.getcwd())

drv.find_element_by_xpath('//*[@id="getting-started"]/form[1]/fieldset/input[1]').send_keys(os.getcwd()+"/testfiles/test.cif")


# driver.find_element_by_xpath('//*[@id="getting-started"]/form[1]/fieldset/input[1]').click()


drv.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/form[1]/fieldset/input[2]').click()


#choose Edge
selectEdge = Select(drv.find_element_by_name("ed"))
selectEdge.select_by_value('K')
#choose ipot
selectIpot = Select(drv.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/form[3]/div[1]/table/tbody/tr[2]/td[4]/select"))
selectIpot.select_by_value('8elements')
#set Cluster Size
cs = '10.0'
clustersize = drv.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/form[3]/div[3]/table/tbody/tr[1]/td[2]/input")
clustersize.clear()
clustersize.send_keys(cs)
#set Longes Path
lp = '8.0'
longestpath = drv.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/form[3]/div[3]/table/tbody/tr[1]/td[4]/input")
longestpath.clear()
longestpath.send_keys(lp)




def calcSave():
    drv.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div/button[1]").click()
    time.sleep(3)
    drv.find_element_by_xpath('//*[@id="btn-save"]').click()
    time.sleep(4)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(2)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(4)

calcSave()

drv.close()



