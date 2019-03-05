import os
from abf import ABF
from bokeh.plotting import figure, output_file, show

DESKTOP = os.path.join(os.path.expanduser('~'),'Desktop')

f = r'C:\Users\jeakwon\Desktop\f1.abf'
abf = ABF(f)
# prepare some data
x = abf.sweepX
y = abf.sweepY

# output to static HTML file
output_file(os.path.join(DESKTOP, abf.abfID + '.html'))

# create a new plot with a title and axis labels
p = figure(
        plot_height     = 300,
        plot_width      = 800,
        title           = abf.abfFilePath, 
        x_axis_label    = abf.sweepLabelX, 
        y_axis_label    = abf.sweepLabelY,
    )

# add a line renderer with legend and line thickness
p.line(x, y, legend=abf.abfID, line_width=2)

# show the results
show(p)