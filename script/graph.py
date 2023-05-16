import matplotlib.pyplot as plt
import pandas as pd
import csv
import sys
import  japanize_matplotlib

args = sys.argv

file_path = args[1]

list = []
D1=[]
D2=[]
D3=[]
D4=[]
D5=[]
D6=[]
D7=[]
D8=[]
D9=[]
D10=[]
graph_sorce_x = []
graph_sorce_y = []
label = []

with open(file_path, 'r', encoding="utf-8") as f:
    header = next(csv.reader(f))
    for line in csv.reader(f):
        count = len(line)
        try:
            D1.append(float(line[0]))
            D2.append(float(line[1]))
            D3.append(float(line[2]))
            D4.append(float(line[3]))
            D5.append(float(line[4]))
            D6.append(float(line[5]))
            D7.append(float(line[6]))
            D8.append(float(line[7]))
            D9.append(float(line[8]))
            D10.append(float(line[9]))

        except:
            pass



def single(x,y,colors="red",markers="o"):
    y_max = max(y) + 5
    plt.ylim(0,y_max)
    plt.plot(x, y,color = colors, marker = markers)
    plt.show(block=True)
    
def multi(labels,colors="red",markers="o"):
    try:
        plt.plot(D1,D2,label=labels[0],color = "red", marker = markers)
        plt.legend()
        plt.plot(D1,D3,label=labels[1],color = "blue", marker = markers)
        plt.legend()
        plt.plot(D1,D4,label=labels[2],color = colors, marker = markers)
        plt.legend()
        plt.plot(D1,D5,label=labels[3],color = colors, marker = markers)
        plt.legend()
        plt.plot(D1,D6,label=labels[4],color = colors, marker = markers)
        plt.legend()
        plt.plot(D1,D7,label=labels[5],color = colors, marker = markers)
        plt.legend()
        plt.plot(D1,D8,label=labels[6],color = colors, marker = markers)
        plt.legend()
        plt.plot(D1,D9,label=labels[7],color = colors, marker = markers)
        plt.legend()
        plt.plot(D1,D10,label=labels[8],color = colors, marker = markers)
        plt.legend()
    except:
        pass
    
    plt.show(block=True)








try:
    xlabel_id = args.index("-xlabel") + 1
    xlabel = args[xlabel_id]
    print(xlabel)
    plt.xlabel(xlabel)
except:
    xlabel = None
try:
    ylabel_id = args.index("-ylabel") + 1
    ylabel = args[ylabel_id]
    print(ylabel)
    plt.ylabel(ylabel)
except:
    ylabel = None

plot_type_id = args.index("-pt") + 1    #plot type
plot_type = args[plot_type_id]
if plot_type == "s":
    rangexy = args[plot_type_id+1]
    x = rangexy[:1]
    exec('graph_sorce_x = D' + x)
    if xlabel is None:
        plt.xlabel(header[int(x)-1])
    y = rangexy[2:]
    exec("graph_sorce_y = D" + y)
    if ylabel is None:
        plt.ylabel(header[int(y)-1])
    single(graph_sorce_x,graph_sorce_y)
elif plot_type == "m":
    try:
        label_id = args.index("-ln") #labelName
    except:
        label_id = None

    if label_id is None:
        for x  in range(count-1):
            label.append(x+1)
    else:
        for x  in range(count-1):
            label.append(args[int(label_id) + int(x+1)])
    multi(label)




plot_type_name = ["s","m","kinji","sanpu"]





    


