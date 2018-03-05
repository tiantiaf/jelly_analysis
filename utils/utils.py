import datetime

def convert_timestamp_to_date_time(timestamp):
    date_time = datetime.datetime.fromtimestamp(timestamp / 1000)
    return date_time

def flatten_list(list_of_lists):
    flattened_list = []
    for x in list_of_lists:
        for y in x:
            flattened_list.append(y)
    return flattened_list
