import numpy as np
import matplotlib.pyplot as plt

def make_barchart_percentage(all_categories, categories_names, title, current_export_path, colors):

    percentage = []
    total = 0
    for i in all_categories:
        total = total + i
    
    for i in all_categories:
        percentage.append(float(i) / float(total) * 100)
    
    
    plt.rcdefaults()
    fig,ax = plt.subplots()
    y_pos = np.arange(len(all_categories))

    rects = ax.barh(y_pos, percentage, align='center', color=colors)
    i = 0
    for rect in rects:
        # Rectangle widths are already integer-valued but are floating
        # type, so it helps to remove the trailing decimal point and 0 by
        # converting width to int type
        width = int(rect.get_width())

        value = str(round(percentage[i], 2)) + '%'
        # Shift the text to the left side of the right edge
        xloc = -5
        # White on magenta
        clr = '#010a43'
        align = 'right'

        # Center the text vertically in the bar
        yloc = rect.get_y() + rect.get_height() / 2
        ax.annotate(str(all_categories[i]) + " - " + value, xy=(width, yloc), xytext=(xloc, 0),
                            textcoords="offset points",
                            ha=align, va='center',
                            color=clr, weight='bold', clip_on=True)
        i = i + 1

    ax.set_yticks(y_pos)
    ax.set_yticklabels(categories_names)
    ax.set_xlabel('Procentaj')
    

    ax.set_title(title)
    #ax.annotate

    plt.savefig(current_export_path)


def make_barchart_values(all_categories, categories_names, title, current_export_path, colors):
    
    
    plt.rcdefaults()
    fig,ax = plt.subplots()
    y_pos = np.arange(len(all_categories))

    rects = ax.barh(y_pos, all_categories, align='center', color=colors)
    i = 0
    for rect in rects:
        # Rectangle widths are already integer-valued but are floating
        # type, so it helps to remove the trailing decimal point and 0 by
        # converting width to int type
        width = int(rect.get_width())

        value = all_categories[i]
        # Shift the text to the left side of the right edge
        xloc = -5
        # White on magenta
        clr = '#010a43'
        align = 'right'

        # Center the text vertically in the bar
        yloc = rect.get_y() + rect.get_height() / 2
        ax.annotate(str(value) + "$", xy=(width, yloc), xytext=(xloc, 0),
                            textcoords="offset points",
                            ha=align, va='center',
                            color=clr, weight='bold', clip_on=True)
        i = i + 1

    ax.set_yticks(y_pos)
    ax.set_yticklabels(categories_names)
    ax.set_xlabel('Dollars $')


    ax.set_title(title)
    #ax.annotate

    plt.savefig(current_export_path)