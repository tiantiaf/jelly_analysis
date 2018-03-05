import numpy as np
from utils.utils import convert_timestamp_to_date_time, flatten_list

def compute_night_day_interaction(timestamp_array):

    date = convert_timestamp_to_date_time(timestamp_array[0]).strftime('%Y-%m-%d')

    night_timestamp_array   = compute_file_array_during_period(timestamp_array, 0, 5)
    day_timestamp_array     = compute_file_array_during_period(timestamp_array, 6, 17)
    evening_timestamp_array = compute_file_array_during_period(timestamp_array, 18, 24)

    night_stat      = compute_start_end_duration(night_timestamp_array)
    day_stat        = compute_start_end_duration(day_timestamp_array)
    evening_stat    = compute_start_end_duration(evening_timestamp_array)

    return_array = [item for row in [[date], night_stat, day_stat, evening_stat] for item in row]

    return return_array

def compute_file_array_during_period(timestamp_array, start_hour, end_hour):
    return_timestamp_array = []
    for timestamp in timestamp_array:
        date_time = convert_timestamp_to_date_time(timestamp)
        if start_hour <= date_time.hour <= end_hour:
            return_timestamp_array.append(timestamp)
    return return_timestamp_array

def compute_start_end_duration(timestamp_array):

    if len(timestamp_array) > 2:
        timestamp_array = np.array(timestamp_array)
        start_date_time = convert_timestamp_to_date_time(timestamp_array.min())
        end_date_time = convert_timestamp_to_date_time(timestamp_array.max())

        duration = round((end_date_time.hour - start_date_time.hour - 1) \
                   + float(end_date_time.minute + 60 - start_date_time.minute) / 60, 2)

        count = len(timestamp_array)

        return [start_date_time.strftime('%H:%M:%S'),
                end_date_time.strftime('%H:%M:%S'),
                duration, count]
    else:
        return np.zeros(4)

def compute_condensed_stat_array(file_array):

    night_day_evening_stat = []
    number_of_files_array = []

    for user_idx in range(len(file_array)):
        # Number of files per day
        for date_idx in range(len(file_array[user_idx])):
            number_of_files_per_day = len(file_array[user_idx][date_idx])
            if 20 < number_of_files_per_day:

                # File Counts
                number_of_files_array = np.append(number_of_files_array, number_of_files_per_day)

                # File Start and End
                timestamp_array = []
                for file_name in file_array[user_idx][date_idx]:
                    timestamp = int(file_name.split("audio_")[1].split("_")[1].split(".csv")[0])
                    timestamp_array.append(timestamp)

                jellyID = file_array[user_idx][date_idx][0].split("audio_")[1].split("_")[0]

                night_day_evening_stat.append(flatten_list([[jellyID,
                                                             number_of_files_per_day],
                                                            compute_night_day_interaction(timestamp_array)]))
    return night_day_evening_stat
