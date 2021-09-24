from os import name
import pandas as pd
import csv
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv('studentMarks.csv')
data = df["Math_score"].tolist()

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list=[]
for i in range(0,1000):
    set_of_mean = random_set_of_mean(100)
    mean_list.append(set_of_mean)

#fig=ff.create_distplot([data],['Math_score'], show_hist=False)
#fig.show()

mean = statistics.mean(data)
std_dev = statistics.stdev(data)
print("Population Mean: ",mean)
print("Population Standard Deviation: ",std_dev )

sample_mean = statistics.mean(mean_list)
sample_std_dev = statistics.stdev(mean_list)
print("Sample Mean: ",sample_mean)
print("Sample Standard Deviation: ",sample_std_dev )

first_stdev_start, first_stdev_end = mean - std_dev, mean + std_dev
second_stdev_start, second_stdev_end = mean-(2*std_dev), mean+(2*std_dev)
third_stdev_start, third_stdev_end = mean-(3*std_dev), mean+(3*std_dev)

#print("std1",first_stdev_start, first_stdev_end)
#print("std2",second_stdev_start, second_stdev_end)
#print("std3",third_stdev_start, third_stdev_end)

df = pd.read_csv("data1.csv")
data = df["Math_score"].tolist()
mean_of_sample1 = statistics.mean(data)
print("Mean of sample1:- ",mean_of_sample1)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode="lines", name="MEAN OF STUDENTS WHO HAD MATH LABS"))
fig.add_trace(go.Scatter(x=[first_stdev_end, first_stdev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_stdev_end, second_stdev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_stdev_end, third_stdev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

df = pd.read_csv("data2.csv")
data = df["Math_score"].tolist()
mean_of_sample2 = statistics.mean(data)
print("mean of sample 2:- ",mean_of_sample2)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample2, mean_of_sample2], y=[0, 0.17], mode="lines", name="MEAN OF STUDENTS WHO USED THE APP"))
fig.add_trace(go.Scatter(x=[first_stdev_end, first_stdev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_stdev_end, second_stdev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_stdev_end, third_stdev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

df = pd.read_csv("data3.csv")
data = df["Math_score"].tolist()
mean_of_sample3 = statistics.mean(data)
print("mean of sample3:- ",mean_of_sample3)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample3, mean_of_sample3], y=[0, 0.17], mode="lines", name="MEAN OF STUDNETS WHO WERE ENFORCED WITH MATH REGISTERS"))
fig.add_trace(go.Scatter(x=[second_stdev_end, second_stdev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_stdev_end, third_stdev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()


#finding the z score using the formula
z_score = (mean_of_sample3 - mean)/std_dev
print("The z score is = ",z_score)

#fig=ff.create_distplot([mean_list],['Math_score'], show_hist=False)
#fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="MEAN"))
#fig.add_trace(go.Scatter(x=[first_stdev_start,first_stdev_start],y=[0,0.20],mode="lines",name="STANDARD DEVITION 1 START"))
#fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.20],mode="lines",name="STANDARD DEVITION 1 END"))
#fig.add_trace(go.Scatter(x=[second_stdev_start,second_stdev_start],y=[0,0.20],mode="lines",name="STANDARD DEVITION 2 START"))
#fig.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.20],mode="lines",name="STANDARD DEVITION 2 END"))
#fig.add_trace(go.Scatter(x=[third_stdev_start,third_stdev_start],y=[0,0.20],mode="lines",name="STANDARD DEVITION 3 START"))
#fig.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.20],mode="lines",name="STANDARD DEVITION 3 END"))
#fig.show()

