import turtle
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from time import sleep
from turtle import Turtle
email = "angelohenaoreyes@yahoo.com"
password = os.getenv("password")
link = Service("C:\Development\chromedriver.exe")
coordinates = []
where = input("what travel plan do you want to give your turtle(city1|city2|city...|)")
final = where.split("|") #list (organization)

driver = webdriver.Chrome(service=link)
driver.get("https://www.latlong.net/")
sleep(2)
driver.find_element(by=By.LINK_TEXT, value="User Login").click()
sleep(1)
email_1 = driver.find_element(by=By.ID, value="email")
password_1 = driver.find_element(by=By.ID, value="password1")
email_1.send_keys(email)
password_1.send_keys(password)
password_1.send_keys(Keys.ENTER)
driver.find_element(by=By.CLASS_NAME, value="logolink").click()
sleep(3)


#Katy, Texas|Dehli, India
def math_func(lng, lat):
    lng = float(lng)
    lat = float(lat)
    return [lat, lng]


def initiate(city_name):
    entry = driver.find_element(by=By.ID, value="place")
    entry.clear()
    entry.send_keys(city_name)
    button = driver.find_element(by=By.ID, value="btnfind")
    button.click()
    sleep(2)
    span = driver.find_element(by=By.ID, value="latlngspan").text
    latlong = span.split(",")
    lat = latlong[0].replace("(", "")
    long = latlong[1].replace(")", "")
    return math_func(lng=long, lat=lat)

sleep(2)
for city in final:
    coordinates.append(initiate(city))


def turtle_travel(cords):
    for coordinate in cords:#3/3
        timmy.goto(coordinate[1], coordinate[0])
    sleep(8)


# importing package

# make screen object and
# set screen mode to world
sleep(2)
sc = turtle.Screen()
sc.mode('world')

# set world coordinates
turtle.setworldcoordinates(-180, -90, 180, 90)
turtle.bgpic('Map_LNGLAT.png')
# turtle.bgpic("")
timmy = Turtle()
turtle_travel(coordinates)
sleep(8)
turtle.mainloop()




# katy, texas|Bali, Indonesia|London, England