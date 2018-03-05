import os
import csv
import matplotlib.pyplot as plt

if __name__=='__main__':

    data_folders = os.listdir(''.join(["../output/Battery"]))
    data_folders.sort()

    temp_date_folders = []
    lengend = []
    number_of_files = 1

    for dataFile in data_folders:
        if 'csv' in dataFile:
            print(dataFile)
            time_frame = []
            data_frame = []
            dataFile = ''.join(["../output/Battery/", dataFile])
            with open(dataFile) as csv_file:
                frames = csv.reader(csv_file, delimiter=',')

                lengend.append('Participant ' + str(number_of_files))
                for frame in frames:
                    if 'Time' not in frame:
                        time_frame.append(float(frame[0]))
                        data_frame.append(int(frame[1].strip('%')))

                plt.plot(time_frame, data_frame)
                plt.ylabel('Battery Percentage', fontsize=12)
                plt.xlabel('Time (hour)', fontsize=12)
                plt.xticks(fontsize=12)
                plt.yticks(fontsize=12)
            number_of_files += 1

    plt.legend(lengend)
    plt.xlim([0, 10])
    plt.ylim([0, 100])
    plt.show()
    plt.show()

