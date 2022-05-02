import random
import math
import matplotlib.pyplot as plt
import numpy as np
import pylab
from pylab import text
from matplotlib.widgets import Button, RadioButtons, CheckButtons

class function:
    fig, axs =plt.subplots(1,2)
    #a=0.1, b=20, n=9
    def __init__(self, a = float(input("Enter a (x1): ")), b = float(input("Enter b (x2): ")), n = int(input("Enter n: "))):
    #def __init__(self, a=1, b=20, n=20):
        self.a = a
        self.b = b
        self.n = n
        self.e = (self.b-self.a)/(self.n-1)


    def f(x):
        return x**(1/x)

    def f1(t):
        return ((t+1)**2)/4

    def f2(t):
        return ((t-1)**2)/4

    #tab function
    def func(self, plot_function):
        F=[];X=[];FX=[]
        while self.a < self.b+self.e :
            F.append(plot_function(self.a))
            X.append(self.a)
            self.a += self.e
        FX.append(F)
        FX.append(X)
        return FX

    #for max and min points
    def get_max_or_min(self, min_max, plot_function):
        arr = function().func(plot_function)
        min_or_max_y = min_max(arr[0])
        for i in arr[0]:
            if min_or_max_y==i:
                ind = arr[0].index(i)
        return arr[1][ind], min_or_max_y

    #to grid the plot
    def grid(self, val):
        self.axs[1].grid()
        self.fig.canvas.draw()

    #to show max and min points on the plot
    def points(self, val1):
        x_max, y_max = function().get_max_or_min(max, function.f)
        x_min, y_min = function().get_max_or_min(min, function.f)
        self.axs[1].plot(x_max, y_max, 'ro')
        self.axs[1].plot(x_min, y_min, 'ro')
        self.fig.canvas.draw()


    def my_plot(self):

        #table with tabulated values
        data = list(zip(*function().func(function.f)))
        cell_text = []
        for row in data:
            cell_text.append([x for x in row])


        collabel=("F(x)", "x")
        self.axs[0].axis('tight')
        self.axs[0].axis('off')
        the_table = self.axs[0].table(cellText=cell_text,colLabels=collabel,loc='center')


        #graph
        x_max, y_max = function().get_max_or_min(max, function.f)
        x_min, y_min = function().get_max_or_min(min, function.f)

        x = np.linspace(self.a, self.b, 100)
        y = function.f(x)
        pylab.style.use('ggplot')
        p, = self.axs[1].plot(x, y,color='black',label='Plot1')

        pylab.xlabel("Х", fontsize=10, fontweight="bold")
        pylab.ylabel("Y", fontsize=10, fontweight="bold")
        ax = pylab.gca()
        ax.axhline(y=0, color='k')
        ax.axvline(x=0, color='k')

        text(-30, 2.6, f"y max = {round(y_max, 3)}",{'color':'black','weight':'heavy','size':6})
        text(-38,2.6, f"x max = {round(x_max, 3)}",{'color':'red','weight':'heavy','size':6})
        text(-30,2.55, f"y min = {round(y_min, 3)}",{'color':'black','weight':'heavy','size':6})
        text(-38,2.55, f"x min = {round(x_min, 3)}",{'color':'red','weight':'heavy','size':6})
        pylab.title (f"Graphs\n x^(1/x)\n((t+1)^2)/4;((t-1)^2)/4", {'size':8})


        #Grid button
        ax_button1 = plt.axes([0.01, 0.3, 0.08, 0.05])
        grid_button1 = Button(ax_button1, 'Grid', color='white', hovercolor='grey')
        grid_button1.on_clicked(function().grid)


        #Points button
        ax_button1 = plt.axes([0.01, 0.2, 0.08, 0.05])
        grid_button = Button(ax_button1, 'Points', color='white', hovercolor='grey')
        grid_button.on_clicked(function().points)


        #to choose the plot you want show
        t=np.linspace(-1, 2, 100)

        p1, = self.axs[1].plot(((t+1)**2)/4,((t-1)**2)/4, color = 'red', label = 'Plot 2', visible = False)
        p2, = self.axs[1].plot(t, ((t+1)**2)/4, color = 'blue', label = 'x(t)', visible = False)
        p3, = self.axs[1].plot(t, ((t-1)**2)/4, color = 'yellow', label = 'y(t)', visible = False)
        plots =[p, p1, p2, p3]
        activated = [True, False, False, False]
        labels = ['Plot 1', 'Plot 2', 'x(t)', 'y(t)']
        ax_check = plt.axes([0.01, 0.05, 0.08, 0.1])
        plot_button = CheckButtons(ax_check,labels, activated)
        def select_plot(label):
            index = labels.index(label)
            plots[index].set_visible(not plots[index].get_visible())
            self.fig.canvas.draw()

        plot_button.on_clicked(select_plot)

        plt.savefig('Lab_2.png')# save fiqure
        plt.show()

f = function()
print(f'min_x, min_y-->{f.get_max_or_min(min, function.f)}')
print(f'max_x, max_y-->{f.get_max_or_min(max, function.f)}')

f.my_plot()
