# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 08:40:43 2024

@author: Lenovo
"""
#---------------------MatPlotLib------------------------
#write a code to draw line with labels
import matplotlib.pyplot as plt
X = range(1,50)
Y = [value *3 for value in X]
print("Values of X : ")
print(*range(1,50))
'''
This is equivalent to i in range (1,50):
    print(i,end='')
'''
print("Values of Y (thrice of X: ",Y) 
#Plot lines and markers to the Axes
plt.plot(X,Y)
#Set the X axis label of the current axis
plt.xlabel('x-axis')
plt.ylabel('y-axis')
#set a title
plt.title("Sample Line")
plt.show()

#Sample graph
import matplotlib.pyplot as plt
x = [1,2,3]
y = [2,4,1]
#Plot lines and markers to the Axes
plt.plot(x,y)
#Set the x-axis label of the current axis
plt.xlabel('X-axis : ')
plt.ylabel('Y-axis : ')
plt.title('Sample Graph')
plt.show()

#Write a program to plot two or more lines 
#Two or more lines on same plot with suitable legends
import matplotlib.pyplot as plt
#line 1 points
x1 = [10,20,30]
y1 = [20,40,10]

#line 2 points
x2 = [10,20,30]
y2 = [40,10,30]

#ploting the line 1 points
plt.plot(x1,y1,label='line 1')
#ploting the line 2 points
plt.plot(x2,y2,label="line2")
#Select X and Y axis labels 
plt.xlabel('x-axis')
plt.ylabel('Y-axis')
plt.title("Two line Graph")
plt.legend()
plt.show()

#Write program to plot two or more lines
#with different widts and colors
import matplotlib.pyplot as plt
#line 1 points
x1 = [10,20,30]
y1 = [20,40,10]

#line 2 points
x2 = [10,20,30]
y2 = [40,10,30]
#Select X and Y axis labels 
plt.xlabel('x-axis')
plt.ylabel('Y-axis')
plt.title("Different Width and Color Graph ")
plt.plot(x1,y1,color='blue',linewidth=3,label="line1")
plt.plot(x2,y2,color='red',linewidth=5,label="line2")
plt.legend()
plt.show()

#Write program to plot two or more lines with different style
import matplotlib.pyplot as plt
#line 1 points
x1 = [10,20,30]
y1 = [20,40,10]

#line 2 points
x2 = [10,20,30]
y2 = [40,10,30]
#Select X and Y axis labels 
plt.xlabel('x-axis')
plt.ylabel('Y-axis')
plt.title("Different Width and Color Graph ")
plt.plot(x1,y1,color='blue',linewidth=3,label="dash_line1",linestyle='dotted')
plt.plot(x2,y2,color='red',linewidth=5,label="dash_line2")
plt.legend()
plt.show()

#-------------------------------------------------------------------------
            
                                            #Date: 25 -04 -2024
#Setting the marker to given line
import matplotlib.pyplot as plt
x = [1,4,5,6,7] #x-axis values
y = [2,6,3,6,3] #y-axis values

#plotting the points
plt.plot(x,y,color='red',linestyle='dashdot',linewidth=3,
         marker='o',markerfacecolor='blue',markersize=12)
#set the y-limits of the current axes
plt.ylim(1,8)
#set the x-limits of the  current axes
plt.xlim(1,8)

#naming the x-axis and y-axis
plt.xlabel('x-axis')
plt.ylabel('y-axis')

#giving a title to my graph
plt.title('Display marker ')
#display marker
plt.show()
#----------------------------------------------------------------

#--------------------------BarGraph-------------------
#write a program to display a bar chart of the popularity of prog. language
#'_' annonymous attribute
#with x-ticks
import matplotlib.pyplot as plt
x = ['Java','Python','PHP','JavaScript','C#','C++']
popularity = [22.7,17.6,8.8,8,7.7,6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos,popularity,color='blue')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of programming languages \n "+"Worldwide, oct 2017 compared to a year ago")
plt.xticks(x_pos,x)
plt.minorticks_on()
#Turn on Grid
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()
#----------------------------------------------------------------

#with y-ticks and barh
import matplotlib.pyplot as plt
x = ['Java','Python','PHP','JavaScript','C#','C++']
popularity = [22.7,17.6,8.8,8,7.7,6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.barh(x_pos,popularity,color='blue')
plt.xlabel("Popularity")
plt.ylabel("Languages")
plt.title("Popularity of programming languages \n "+"Worldwide, oct 2017 compared to a year ago")
plt.yticks(x_pos,x)
plt.minorticks_on()
#Turn on Grid
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()
#-----------------------------------------------------------------

#with different color for each data point
import matplotlib.pyplot as plt
x = ['Java','Python','PHP','JavaScript','C#','C++']
popularity = [22.7,17.6,8.8,8,7.7,6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos,popularity,color=['red','blue','yellow','pink','black','green'])
plt.xlabel("Popularity")
plt.ylabel("Languages")
plt.title("Popularity of programming languages \n "+"Worldwide, oct 2017 compared to a year ago")
plt.xticks(x_pos,x)
plt.minorticks_on()
#Turn on Grid
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()
#-----------------------------------------------------------------

#-------------------------Histogram-----------------------
#histogram showing normal , pre-diabetic and diabetic patients 
#distribution
# 80-100: Normal
# 100-125: Pre-Diabetic 
# 125 onwards: Diabetic
import matplotlib.pyplot as plt
blood_sugar =[113,85,90,150,149,88,93,115,135,80,77,82,129]
plt.hist(blood_sugar,rwidth=0.8) #by default number of bins are 10
plt.hist(blood_sugar,rwidth=0.5,bins=4)

plt.xlabel("Sugar level")
plt.ylabel("Number of Patients")
plt.title("Blood Sugar Chart")

plt.hist(blood_sugar,bins=[80,100,125,150],rwidth=0.95,color='g')
plt.xlabel("Sugar level")
plt.ylabel("Number of Patients")
plt.title("Blood Sugar Chart")

#--------------------------BoxPlot-----------------------
import matplotlib.pyplot as plt
import numpy as np
#Creating dataset
np.random.seed(10)
data = np.random.normal(100,20,200)
fig = plt.figure(figsize=(10,7))
#Creating Plot
plt.boxplot(data)
plt.show()
#--------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(10)
data_1 = np.random.normal(100,10,200)
data_2 = np.random.normal(90,20,200)
data_3 = np.random.normal(80,30,200)
data_4 = np.random.normal(70,40,200)
data =[data_1,data_2,data_3,data_4]
fig = plt.figure(figsize =(10,7))
#creating axes instance
ax = fig.add_axes([0,0,1,1])
#creating boxplot
bp = ax.boxplot(data)
#show plot


