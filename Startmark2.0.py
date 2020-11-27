##IN this alpha version of the app, there is an example of how our system would work, here in it used by a profession seminar where 11 students
#would enter their job demand and 5 compagnies of different sectors: Bar, restaurant, NightClub, Office and Store would have access to the data
import random
import csv
import json
import os

#creation of graphs for storing data
class Person:
    def __init__(self, fname, lname, birth, gender,university,
                 job,day,time,hours):
        self.fname = fname
        self.lname = lname
        self.birth = birth
        self.gender = gender
        self.university=university

        self.job = job
        self.day=day
        self.time=time
        self.hours=hours
        self.adjacencyList = []
        self.visited = False

    def personrecom(self):
        queue = []
        queue.append(self)
        while queue:
            actualNode = queue.pop(0)
            actualNode.visited = False

            for n in actualNode.adjacencyList:
                queue.append(n)
        self.img()

    def img(self):
        self.visited = True
        print(self.fname,self.lname,self.birth,self.gender,self.university,self.day,self.time,self.hours)
        for n in self.adjacencyList:
            if not n.visited:
                n.img()

def cvs_read():
    jsonArray = []
    with open('data.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            jsonArray.append(row)

        return jsonArray

def csv_write(data):
    with open('data.csv', 'a+', newline='') as file:
        fieldnames = ['First name', 'last name', 'age', 'gender', 'university',"job", 'day', 'time', 'hours']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(data)
        return {"success": "T", "data": data}

print("Welcome to STARTMARK  \n")
print(" EVERY STEP COUNTS\n")
print("On your mark, Get set, Go!\n")
data_append = {'First name': 'First Name', 'last name': 'last name', 'age': 'age', 'gender': 'gender',
               'university': 'university', 'job': 'job',
               'day': 'day', 'time': 'time', 'hours': 'hours''\n'}
x = csv_write(data_append)
#it creates an csv file "data.csv",which can be acces on python text file and CSV, here it create the columns names, later
#the values in columns will be added
info=True
while info>0:
    print("\nTo Sign Up new users type 1")
    print("To see data, login using your code\n"
          "To quit, type 0")
    a = int(input("Sign Up/Login\n"))
# those are the log in for the 5 compagnies to see the different data:
# 4789 for Office
# 4930 for Restaurant
# 9459 for Bar
# 3080 for Club
# 7899 for Store

    if a==1:
        start = Person(fname=None, lname=None, birth=None, gender=None,university=None, job=None, day=None, time=None, hours=None)
        RestaurantN = Person(fname="First Name/", lname="Last Name/", birth="Age/", gender="Gender/",university="University/", job="Restaurant", day="Day/",
                         time="Time/", hours="Hours/")
        BarN = Person(fname="First Name/", lname="Last Name/", birth="Age/", gender="Gender/",university="University/", job="Bar", day="Day/",
                         time="Time/", hours="Hours/")
        ClubN = Person(fname="First Name/", lname="Last Name/", birth="Age/", gender="Gender/",university="University/", job="Club", day="Day/",
                         time="Time/", hours="Hours/")
        StoreN = Person(fname="First Name/", lname="Last Name/", birth="Age/", gender="Gender/",university="University/", job="Store",day="Day/",
                         time="Time/", hours="Hours/")
        OfficeN = Person(fname="First Name/", lname="Last Name/", birth="Age/", gender="Gender/",university="University/", job="Office/", day="Day/",
                         time="Time/", hours="Hours/")
#the way are graph would work is that the starting note would be an empty one without values, and the 5 other that would connect to it
#represents the type of compagny, it will allow to create later an automatic append where the person info will append to one of those 5 nodes based on job area
        start.adjacencyList.append(RestaurantN)
        start.adjacencyList.append(BarN)
        start.adjacencyList.append(ClubN)
        start.adjacencyList.append(StoreN)
        start.adjacencyList.append(OfficeN)

##we created for a total input of 11, but you can select less with below p value
        p=int(input("How many people you would like to sign in? (maximum 11 people)\n"))
        if p==11:
            print("\nNEW DEMAND (11 left):")
            name = input('What is your First name?\n')
            lname = input('What is your Last name?\n')
            birth = int(input("What is your Age?\n"))
            if birth <18:
                print("This person is UNDERAGED and can't work!!\n"
                      "Please restart the App")
                break
    # prevents underage people to work by crashing the app on purpose to avoid law issues
            print("What is your Gender:")
            gender = input("Male/Female/Other\n")
            university=input("Which University do you study in?\n")
            print("Choice of Jobs:\n"
                  "Restaurant\n"
                  "Bar\n"
                  "Club\n"
                  "Store\n"
                  "Office\n"
                  )
            area=input("Type for which Job you would like to apply:\n")
            day=input("Type which day(s) of the week you would like to work:\nMonday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday\n")
            time=input("When during this day(s) you would like to work:\nMorning/Afternoon/Night\n")
            hours=int(input("How many Hours you would like to work per day?\n"))
            person=Person(fname=name,lname=lname,birth=birth,gender=gender,university=university,job=area, day=day,time=time,hours=hours)
            data_append = {'First name':name, 'last name':lname, 'age':birth, 'gender':gender, 'university':university,"job":area,
                           'day':day, 'time':time, 'hours':hours}
            x = csv_write(data_append)
            print(x)
#its add to csv columms

            if area=="Restaurant":
                RestaurantN.adjacencyList.append(person)

            if area=="Bar":
                BarN.adjacencyList.append(person)

            if area=="Club":
                ClubN.adjacencyList.append(person)

            if area=="Store":
                StoreN.adjacencyList.append(person)

            if area=="Office":
                OfficeN.adjacencyList.append(person)
# as mentioned previously, there is an automated append to job category nodes
        if p >= 10:
            print("\nNEW DEMAND (10 left):")
            name1 = input('What is your First name?\n')
            lname1= input('What is your Last name?\n')
            birth1 = int(input("What is your Age?\n"))
            if birth1<18:
                print("This person is UNDERAGED and can't work!!\n"
                  "Please restart the App")
                break

            print("What is your Gender:")
            gender1 = input("Male/Female/Other\n")
            university1=input("Which University do you study in?\n")
            print("Choice of Jobs:\n"
                  "Restaurant\n"
                  "Bar\n"
                  "Club\n"
                  "Store\n"
                  "Office\n"
                  )
            area1=input("Type for which Job you would like to apply\n")
            day1=input("Type which day(s) of the week you would like to work:\nMonday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday\n")
            time1=input("When during this day(s) could you work:\nMorning/Afternoon/Night\n")
            hours1=int(input("How many Hours would like to work per day\n"))
            person1=Person(fname=name1,lname=lname1,birth=birth1,gender=gender1,university=university1,job=area1, day=day1,time=time1,hours=hours1)
            data_append = {'First name': name1, 'last name': lname1, 'age': birth1, 'gender': gender1,
                           'university': university1, "job": area1,
                           'day': day1, 'time': time1, 'hours': hours1}
            x = csv_write(data_append)
            print(x)

            if area1 == "Restaurant":
                RestaurantN.adjacencyList.append(person1)

            if area1 == "Bar":
                BarN.adjacencyList.append(person1)

            if area1 == "Club":
                ClubN.adjacencyList.append(person1)

            if area1 == "Store":
                StoreN.adjacencyList.append(person1)

            if area1=="Office":
                OfficeN.adjacencyList.append(person1)

        if p >= 9:
            print("\nNEW DEMAND (9 left)")
            name2 = input('What is your First name?\n')
            lname2= input('What is your Last name?\n')
            birth2 = int(input("What is your Age?\n"))
            if birth2<18:
                print("This person is UNDERAGED and can't work!!\n"
                  "Please restart the App")
                break
            print("What is your Gender")
            gender2 = input("Male/Female/Other\n")
            university2 = input("Which University do you study in?\n")
            print("Choice of Jobs:\n"
                  "Restaurant\n"
                  "Bar\n"
                  "Club\n"
                  "Store\n"
                  "Office\n"
                  )
            area2=input("Type for which Job you would like to apply:\n")
            day2=input("Type which day(s) of the week you would like to work:\nMonday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday\n")
            time2=input("When during this day(s) could you work:\nMorning/Afternoon/Night\n")
            hours2=int(input("How many Hours would like to work per day\n"))
            person2=Person(fname=name2,lname=lname2,birth=birth2,gender=gender2,university=university2,job=area2, day=day2,time=time2,hours=hours2)
            data_append = {'First name': name2, 'last name': lname2, 'age': birth2, 'gender': gender2,
                           'university': university2, "job": area2,
                           'day': day2, 'time': time2, 'hours': hours2}
            x = csv_write(data_append)
            print(x)

            if area2 == "Restaurant":
                RestaurantN.adjacencyList.append(person2)

            if area2 == "Bar":
                BarN.adjacencyList.append(person2)

            if area2 == "Club":
                ClubN.adjacencyList.append(person2)

            if area2 == "Store":
                StoreN.adjacencyList.append(person2)

            if area2=="Office":
                OfficeN.adjacencyList.append(person2)

# In this example we imagined there was 11 people in the seminar for jobs, so 11 inputs in total,
# since there all the same, you don't have to check each individual input until next # and you can select as many inputs as you would like to test on
        if p >= 8 :
            print("\nNEW DEMAND (8 left)")
            name3 = input('What is your First name?\n')
            lname3= input('What is your Last name?\n')
            birth3 = int(input("What is your Age?\n"))
            if birth3 < 18:
                print("This person is UNDERAGED and can't work!!\n"
                      "Please restart the App")
                break
            print("What is your Gender")
            gender3 = input("Male/Female/Other\n")
            university3 = input("Which University do you study in?\n")
            print("Choice of Jobs:\n"
                  "Restaurant\n"
                  "Bar\n"
                  "Club\n"
                  "Store\n"
                  "Office"
                  )
            area3=input("Type for which Job you would like to apply\n")
            day3=input("Type which day(s) of the week you would like to work:\nMonday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday\n")
            time3=input("When during this day(s) could you work:\nMorning/Afternoon/Night\n")
            hours3=int(input("How many Hours would like to work per day\n"))
            person3=Person(fname=name3,lname=lname3,birth=birth3,gender=gender3,university=university3,job=area3, day=day3,time=time3,hours=hours3)
            data_append = {'First name': name3, 'last name': lname3, 'age': birth3, 'gender': gender3,
                           'university': university3, "job": area3,
                           'day': day3, 'time': time3, 'hours': hours3}
            x = csv_write(data_append)
            print(x)

            if area3 == "Restaurant":
                RestaurantN.adjacencyList.append(person3)

            if area3 == "Bar":
                BarN.adjacencyList.append(person3)

            if area3 == "Club":
                ClubN.adjacencyList.append(person3)

            if area3 == "Store":
                StoreN.adjacencyList.append(person3)

            if area3=="Office":
                OfficeN.adjacencyList.append(person3)

        if p >= 7:
            print("\nNEW DEMAND (7 left)")
            name4 = input('What is your First name?\n')
            lname4= input('What is your Last name?\n')
            birth4 = int(input("What is your Age?\n"))
            if birth4 < 18:
                print("This person is UNDERAGED and can't work!!\n"
                      "Please restart the App")
                break
            print("What is your Gender")
            gender4 = input("Male/Female/Other\n")
            university4 = input("Which University do you study in?\n")
            print("Choice of Jobs:\n"
                  "Restaurant\n"
                  "Bar\n"
                  "Club\n"
                  "Store\n"
                  "Office"
                  )
            area4=input("Type for which Job you would like to apply\n")
            day4=input("Type which day(s) of the week you would like to work:\nMonday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday\n")
            time4=input("When during this day(s) could you work:\nMorning/Afternoon/Night\n")
            hours4=int(input("How many Hours would like to work per day\n"))
            person4=Person(fname=name4,lname=lname4,birth=birth4,gender=gender4,university=university4,job=area4, day=day4,time=time4,hours=hours4)
            data_append = {'First name': name4, 'last name': lname4, 'age': birth4, 'gender': gender4,
                           'university': university4, "job": area4,
                           'day': day4, 'time': time4, 'hours': hours4}
            x = csv_write(data_append)
            print(x)

            if area4 == "Restaurant":
                RestaurantN.adjacencyList.append(person4)

            if area4 == "Bar":
                BarN.adjacencyList.append(person4)

            if area4 == "Club":
                ClubN.adjacencyList.append(person4)

            if area4 == "Store":
                StoreN.adjacencyList.append(person4)

            if area4=="Office":
                OfficeN.adjacencyList.append(person4)

        if p >= 6:
            print("\nNEW DEMAND (6 left)")
            name5 = input('What is your First name?\n')
            lname5 = input('What is your Last name?\n')
            birth5 = int(input("What is your Age?\n"))
            if birth5 < 18:
                print("This person is UNDERAGED and can't work!!\n"
                      "Please restart the App")
                break
            print("What is your Gender")
            gender5 = input("Male/Female/Other\n")
            university5 = input("Which University do you study in?\n")
            print("Choice of Jobs:\n"
                  "Restaurant\n"
                  "Bar\n"
                  "Club\n"
                  "Store\n"
                  "Office"
                  )
            area5 = input("Type for which Job you would like to apply\n")
            day5 = input(
                "Type which day(s) of the week you would like to work:\nMonday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday\n")
            time5 = input("When during this day(s) could you work:\nMorning/Afternoon/Night\n")
            hours5 = int(input("How many Hours would like to work per day\n"))
            person5 = Person(fname=name5, lname=lname5, birth=birth5, gender=gender5,university=university5, job=area5, day=day5, time=time5,
                             hours=hours5)
            data_append = {'First name': name5, 'last name': lname5, 'age': birth5, 'gender': gender5,
                           'university': university5, "job": area5,
                           'day': day5, 'time': time5, 'hours': hours5}
            x = csv_write(data_append)
            print(x)

            if area5 == "Restaurant":
                RestaurantN.adjacencyList.append(person5)

            if area5 == "Bar":
                BarN.adjacencyList.append(person5)

            if area5 == "Club":
                ClubN.adjacencyList.append(person5)

            if area5 == "Store":
                StoreN.adjacencyList.append(person5)

            if area5=="Office":
                OfficeN.adjacencyList.append(person5)

        if p >= 5:
            print("\nNEW DEMAND (5 left)")
            name6 = input('What is your First name?\n')
            lname6 = input('What is your Last name?\n')
            birth6 = int(input("What is your Age?\n"))
            if birth6 < 18:
                print("This person is UNDERAGED and can't work!!\n"
                      "Please restart the App")
                break
            print("What is your Gender")
            gender6 = input("Male/Female/Other\n")
            university6 = input("Which University do you study in?\n")
            print("Choice of Jobs:\n"
                  "Restaurant\n"
                  "Bar\n"
                  "Club\n"
                  "Store\n"
                  "Office"
                  )
            area6 = input("Type for which Job you would like to apply\n")
            day6 = input(
                "Type which day(s) of the week you would like to work:\nMonday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday\n")
            time6 = input("When during this day(s) could you work:\nMorning/Afternoon/Night\n")
            hours6 = int(input("How many Hours would like to work per day\n"))
            person6 = Person(fname=name6, lname=lname6, birth=birth6, gender=gender6,university=university6, job=area6, day=day6, time=time6,
                             hours=hours6)
            data_append = {'First name': name6, 'last name': lname6, 'age': birth6, 'gender': gender6,
                           'university': university6, "job": area6,
                           'day': day6, 'time': time6, 'hours': hours6}
            x = csv_write(data_append)
            print(x)

            if area6 == "Restaurant":
                RestaurantN.adjacencyList.append(person6)

            if area6 == "Bar":
                BarN.adjacencyList.append(person6)

            if area6 == "Club":
                ClubN.adjacencyList.append(person6)

            if area6 == "Store":
                StoreN.adjacencyList.append(person6)

            if area6=="Office":
                OfficeN.adjacencyList.append(person6)

        if p >= 4:
            print("\nNEW DEMAND (4 left)")
            name7 = input('What is your First name?\n')
            lname7 = input('What is your Last name?\n')
            birth7 = int(input("What is your Age?\n"))
            if birth7 < 18:
                print("This person is UNDERAGED and can't work!!\n"
                      "Please restart the App")
                break
            print("What is your Gender")
            gender7 = input("Male/Female/Other\n")
            university7 = input("Which University do you study in?\n")
            print("Choice of Jobs:\n"
                  "Restaurant\n"
                  "Bar\n"
                  "Club\n"
                  "Store\n"
                  "Office"
                  )
            area7 = input("Type for which Job you would like to apply\n")
            day7 = input(
                "Type which day(s) of the week you would like to work:\nMonday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday\n")
            time7 = input("When during this day(s) could you work:\nMorning/Afternoon/Night\n")
            hours7 = int(input("How many Hours would like to work per day\n"))
            person7 = Person(fname=name7, lname=lname7, birth=birth7, gender=gender7,university=university7, job=area7, day=day7, time=time7,
                             hours=hours7)
            data_append = {'First name': name7, 'last name': lname7, 'age': birth7, 'gender': gender7,
                           'university': university7, "job": area7,
                           'day': day7, 'time': time7, 'hours': hours7}
            x = csv_write(data_append)
            print(x)

            if area7 == "Restaurant":
                RestaurantN.adjacencyList.append(person7)

            if area7 == "Bar":
                BarN.adjacencyList.append(person7)

            if area7 == "Club":
                ClubN.adjacencyList.append(person7)

            if area7 == "Store":
                StoreN.adjacencyList.append(person7)

            if area7=="Office":
                OfficeN.adjacencyList.append(person7)

        if p >= 3:
            print("Ninth demand:")
            name8 = input('What is your First name?\n')
            lname8 = input('What is your Last name?\n')
            birth8 = int(input("What is your Age?\n"))
            if birth8 < 18:
                print("This person is UNDERAGED and can't work!!\n"
                      "Please restart the App")
                break
            print("What is your Gender")
            gender8 = input("Male/Female/Other\n")
            university8 = input("Which University do you study in?\n")
            print("Choice of Jobs:\n"
                  "Restaurant\n"
                  "Bar\n"
                  "Club\n"
                  "Store\n"
                  "Office"
                  )
            area8 = input("Type for which Job you would like to apply\n")
            day8 = input(
                "Type which day(s) of the week you would like to work:\nMonday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday\n")
            time8 = input("When during this day(s) could you work:\nMorning/Afternoon/Night\n")
            hours8 = int(input("How many Hours would like to work per day\n"))
            person8 = Person(fname=name8, lname=lname8, birth=birth8, gender=gender8,university=university8, job=area8, day=day8, time=time8,
                             hours=hours8)
            data_append = {'First name': name8, 'last name': lname8, 'age': birth8, 'gender': gender8,
                           'university': university8, "job": area8,
                           'day': day8, 'time': time8, 'hours': hours8}
            x = csv_write(data_append)
            print(x)

            if area8 == "Restaurant":
                RestaurantN.adjacencyList.append(person8)

            if area8 == "Bar":
                BarN.adjacencyList.append(person8)

            if area8 == "Club":
                ClubN.adjacencyList.append(person8)

            if area8 == "Store":
                StoreN.adjacencyList.append(person8)

            if area8=="Office":
                OfficeN.adjacencyList.append(person8)

        if p >= 2:
            print("\nNEW DEMAND (2 left)")
            name9 = input('What is your First name?\n')
            lname9 = input('What is your Last name?\n')
            birth9 = int(input("What is your Age?\n"))
            if birth9 < 18:
                print("This person is UNDERAGED and can't work!!\n"
                      "Please restart the App")
                break
            print("What is your Gender")
            gender9 = input("Male/Female/Other\n")
            university9 = input("Which University do you study in?\n")
            print("Choice of Jobs:\n"
                  "Restaurant\n"
                  "Bar\n"
                  "Club\n"
                  "Store\n"
                  "Office"
                  )
            area9 = input("Type for which Job you would like to apply\n")
            day9 = input(
                "Type which day(s) of the week you would like to work:\nMonday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday\n")
            time9 = input("and when during this day(s):\nMorning/Afternoon/Night\n")
            hours9 = int(input("How many Hours would like to work per day?\n"))
            person9 = Person(fname=name9, lname=lname9, birth=birth9, gender=gender9,university=university9, job=area9, day=day9, time=time9,
                             hours=hours9)
            data_append = {'First name': name9, 'last name': lname9, 'age': birth9, 'gender': gender9,
                           'university': university9, "job": area9,
                           'day': day9, 'time': time9, 'hours': hours9}
            x = csv_write(data_append)
            print(x)

            if area9 == "Restaurant":
                RestaurantN.adjacencyList.append(person9)

            if area9 == "Bar":
                BarN.adjacencyList.append(person9)

            if area9 == "Club":
                ClubN.adjacencyList.append(person9)

            if area9 == "Store":
                StoreN.adjacencyList.append(person9)

            if area9=="Office":
                OfficeN.adjacencyList.append(person9)

        if p >= 1:
            print("\nNEW DEMAND (1 left)")
            name10 = input('What is your First name?\n')
            lname10 = input('What is your Last name?\n')
            birth10 = int(input("What is your Age?\n"))
            if birth10 < 18:
                print("This person is UNDERAGED and can't work!!\n"
                      "Please restart the App")
                break
            print("What is your Gender")
            gender10 = input("Male/Female/Other\n")
            university10 = input("Which University do you study in?\n")
            print("Choice of Jobs:\n"
                  "Restaurant\n"
                  "Bar\n"
                  "Club\n"
                  "Store\n"
                  "Office"
                  )
            area10 = input("Type for which Job you would like to apply\n")
            day10 = input(
                "Type which day(s) of the week you would like to work:\nMonday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday\n")
            time10 = input("and when during this day(s):\nMorning/Afternoon/Night\n")
            hours10 = int(input("How many Hours would like to work per day\n"))
            person10 = Person(fname=name10, lname=lname10, birth=birth10, gender=gender10,university=university10, job=area10, day=day10, time=time10,
                             hours=hours10)

            data_append = {'First name': name10, 'last name': lname10, 'age': birth10, 'gender': gender10,
                           'university': university10, "job": area10,
                           'day': day10, 'time': time10, 'hours': hours10}
            x = csv_write(data_append)
            print(x)

            print("Demand send, StartMark is working on your demand\n")
            print("Have a good day/night!")

            if area10 == "Restaurant":
                RestaurantN.adjacencyList.append(person10)

            if area10 == "Bar":
                BarN.adjacencyList.append(person10)

            if area10 == "Club":
                ClubN.adjacencyList.append(person10)

            if area10 == "Store":
                StoreN.adjacencyList.append(person10)

            if area10=="Office":
                OfficeN.adjacencyList.append(person10)

#STOP!! the copies of inputs are finished now it is the login part for compagnies, each one of them have a different code so they don't see each other data
#and student can't see either

    if a==4789:
        print("Demand for job in Office:")
        OfficeN.img()
#the research start from the second node which is the node to which each demand was assigned based on the job area, like this it is faster and acts
#as a filter for job
    if a == 4930:
        print("Demand for job in Restaurant:")
        RestaurantN.img()

    if a == 9459:
        print("Demand for job in Bar:")
        BarN.img()

    if a == 3080:
        print("Demand for job in Club:")
        ClubN.img()

    if a==7899:
        print("Demand for job in Store:")
        StoreN.img()

    if a==0:
        break
#the quit option to quit the program