import matplotlib.pyplot as plt
import pandas as pd

def plot_files_stat(file_stat):

    jelly_id_array = []
    average = []
    std = []

    for row in file_stat:
        jelly_id_array.append(row[0])
        average.append(row[2])
        std.append(row[3])

    plt.errorbar(range(len(file_stat)), average, yerr=std, fmt='o',
			 markeredgewidth=2, elinewidth=2, capsize=5)

    plt.xticks(range(len(file_stat)), jelly_id_array)

    plt.xlabel('Participant ID', fontsize=12)
    plt.ylabel('Number Of Recordings', fontsize=12)
    plt.show()


def plot_file_distribution(file_distribution):
    jelly_id_array = []
    jelly_id_file_array = []

    for row in file_distribution:
        if row[0] not in jelly_id_array:
            jelly_id_array.append(row[0])

    number_of_jelly = int(len(jelly_id_array))

    number_of_subplot = 0
    for i in range(number_of_jelly):
        date_list = []
        data_list = []
        for row in file_distribution:
            if jelly_id_array[i] in row:
                date_list.append(row[1])
                data_list.append(row[2])
        if len(date_list) > 2:
            number_of_subplot += 1

    fig, axes = plt.subplots(nrows=number_of_subplot)

    number_of_subplot = 0
    imgplot = []

    for i in range(number_of_jelly):
        date_list = []
        data_list = []
        for row in file_distribution:
            if jelly_id_array[i] in row:
                date_list.append(row[1])
                data_list.append(row[2])

        if len(date_list) > 2:

            data_list = data_list[0:3]
            date_list = date_list[0:3]

            df = pd.DataFrame(columns=range(24))

            for idx, date in enumerate(date_list):
                df = df.append(pd.Series(data_list[idx], name=date, index=range(24)))

            imgplot = axes[number_of_subplot].imshow(data_list,
                                           aspect='auto',
                                           cmap=plt.cm.get_cmap('gist_heat', 80))
            axes[number_of_subplot].tick_params('both', length=0, width=0, which='major')
            axes[number_of_subplot].set_xlabel('Time(Hour)')

            y_label = []
            for j in range(len(date_list)):
                y_label.append('Day ' + str(j+1))

            axes[number_of_subplot].set_yticks(range(len(date_list)))
            axes[number_of_subplot].set_yticklabels(y_label)

            axes[number_of_subplot].set_title("Participant " + str(number_of_subplot+1))
            imgplot.set_clim(0, 80)

            number_of_subplot += 1

    #axes[number_of_subplot-1].set_xlabel('Time(Hour)')

    plt.tight_layout()
    fig.colorbar(imgplot, ax=axes.ravel().tolist(), pad=0.04, aspect = 30)
    plt.show()


def plot_file_distribution_temp(file_distribution):
    jelly_id_array = []
    jelly_id_file_array = []

    for row in file_distribution:
        if row[0] not in jelly_id_array:
            jelly_id_array.append(row[0])

    number_of_jelly = int(len(jelly_id_array))

    number_of_subplot = 0
    for i in range(number_of_jelly):
        date_list = []
        data_list = []
        for row in file_distribution:
            if jelly_id_array[i] in row:
                date_list.append(row[1])
                data_list.append(row[2])
        if len(date_list) > 2:
            number_of_subplot += 1

    fig, axes = plt.subplots(nrows=number_of_subplot)

    number_of_subplot = 0
    imgplot = []

    for i in range(number_of_jelly):
        date_list = []
        data_list = []
        for row in file_distribution:
            if jelly_id_array[i] in row:
                date_list.append(row[1])
                data_list.append(row[2])

        if len(date_list) > 2:

            data_list = data_list[0:3]
            date_list = date_list[0:3]

            df = pd.DataFrame(columns=range(24))

            for idx, date in enumerate(date_list):
                df = df.append(pd.Series(data_list[idx], name=date, index=range(24)))

            imgplot = axes[number_of_subplot].imshow(data_list,
                                                     aspect='auto',
                                                     cmap=plt.cm.get_cmap('gist_heat', 80))
            axes[number_of_subplot].tick_params('both', length=0, width=0, which='major')

            y_label = []
            for j in range(len(date_list)):
                y_label.append('Day ' + str(j + 1))

            axes[number_of_subplot].set_yticks(range(len(date_list)))
            axes[number_of_subplot].set_yticklabels(y_label)

            axes[number_of_subplot].set_title("Participant " + str(number_of_subplot + 1))
            imgplot.set_clim(0, 80)

            number_of_subplot += 1

    axes[number_of_subplot - 1].set_xlabel('Time(Hour)')

    fig.colorbar(imgplot, ax=axes.ravel().tolist())
    plt.show()








