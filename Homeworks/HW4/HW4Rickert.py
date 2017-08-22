import random
import timeit
import plotly
import plotly.plotly
import plotly.graph_objs as go
from plotly.graph_objs import Scatter, Layout




RandomList = random.sample(range(10), 10)


def BubbleSort(list):
    for j in range(0,len(list)):
        for i in range(j+1, len(list)):
            if list[i] >= list[j]:
                pass
            else:
                list[i], list[j] = list[j], list[i]
    return list

def SelectionSort(list):
    min(list)


def selectionSort(list):
    for i in range(len(list)-1,0,-1):
        Max=0
        for location in range(1,i+1):
            if list[location]>list[Max]:
                Max = location
        temp = list[i]
        list[i] = list[Max]
        list[Max] = temp
    return list

def BubbleSortTimer(listlength):
    time = []
    runs = []
    while len(runs) < 50:
        RandoList = random.sample(xrange(1000), listlength)
        Start = timeit.default_timer()
        BubbleSort(RandoList)
        End = timeit.default_timer()
        time.append(End - Start)
        runs.append(1)
    average = sum(time)/len(time)
    return average



def SelectionSortTimer(listlength):
    time = []
    runs = []
    while len(runs) < 50:
        RandoList = random.sample(xrange(1000), listlength)
        Start = timeit.default_timer()
        selectionSort(RandoList)
        End = timeit.default_timer()
        time.append(End - Start)
        runs.append(1)
    average = sum(time)/len(time)
    return average

SelectionSortN = []
SelectionSortRuntime = []
for i in range(1,500):
    SelectionSortN.append(i)
    SelectionSortRuntime.append(SelectionSortTimer(i))

BubbleSortN = []
BubbleSortRuntime = []
for i in range(1, 500):
    BubbleSortN.append(i)
    BubbleSortRuntime.append(BubbleSortTimer(i))

Trace0 = Scatter(
    x=BubbleSortN,
    y=BubbleSortRuntime,
    name = "Bubble Sort"
)
Trace1 = Scatter(
    x=SelectionSortN,
    y=SelectionSortRuntime,
    name = "Selection Sort"
)
data = [Trace0, Trace1]

plotly.offline.plot({
    "data": data,
    "layout" : Layout(title = "Sort Comparisons", xaxis = dict(title = "Length of List"), yaxis = dict(title = 'Time in Seconds'))
})
