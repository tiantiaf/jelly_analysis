import datetime
import os
import numpy as np
from utils.utils_plot import plot_files_stat, plot_file_distribution
from utils.compute_file_stat_utils import compute_condensed_stat_array
from utils.utils_csv import save_data_to_csv

def get_user_date_folder(username_array):

	date_array = []

	for userNameFolder in username_array:
		date_folders = os.listdir(''.join(["../data/", userNameFolder]))
		date_folders.sort()

		temp_date_folders = []

		for dateFolder in date_folders:
			if "2018-" in dateFolder:
				temp_date_folders.append(dateFolder)
		date_array.append(temp_date_folders)

	return date_array

def get_user_folder():
	username_folder_list = os.listdir('../data')
	username_folder_list.sort()

	username_array = []

	for userNameFolder in username_folder_list:
		if len(userNameFolder) < 5:
			username_array.append(userNameFolder)
	return username_array

def get_files_per_user(username_array, date_array):
	username_folder_index = 0
	file_array = []
	for userNameFolder in username_array:
		files_per_user = []
		for dateFolder in date_array[username_folder_index]:
			date_folder_abs = ''.join(["../data/", userNameFolder + "/", dateFolder])

			number_of_files_per_day = len(os.listdir(date_folder_abs))
			temp_file_array = os.listdir(date_folder_abs)
			temp_file_array.sort()
			if 50 < number_of_files_per_day < 500:
				files_per_user.append(temp_file_array)

		file_array.append(files_per_user)

		username_folder_index = username_folder_index + 1

	return file_array

def get_all_files_per_user(username_array, date_array):
	username_folder_index = 0
	file_array = []
	for userNameFolder in username_array:

		files_per_user = []
		for dateFolder in date_array[username_folder_index]:
			date_folder_abs = ''.join(["../data/", userNameFolder + "/", dateFolder])
			temp_file_array = os.listdir(date_folder_abs)
			temp_file_array.sort()
			files_per_user.append(temp_file_array)

		file_array.append(files_per_user)

		username_folder_index = username_folder_index + 1

	return file_array

def get_files_high_lvl_stat(condens_file_stat):

	jelly_id_array = []

	for row in condens_file_stat:
		if row[0] not in jelly_id_array:
			jelly_id_array.append(row[0])

	file_stat = []

	for jelly_id in jelly_id_array:
		file_counts = []
		valid_days = 0
		for row in condens_file_stat:
			if jelly_id in row:
				file_counts.append(int(row[1]))
				valid_days += 1

		file_counts = np.array(file_counts)
		file_stat.append([jelly_id, valid_days, round(file_counts.mean(), 2), round(file_counts.std(), 2)])

	return file_stat

def get_file_distribution_per_user(files_array):
	file_distribution = []

	for jelly_idx in range(len(files_array)):

		for date_idx in range(len(files_array[jelly_idx])):

			file_distribution_per_user = np.zeros(24)

			jelly_id 	= files_array[jelly_idx][date_idx][0].split("audio_")[1].split("_")[0]
			save_timestamp = int(files_array[jelly_idx][date_idx][0].split("audio_")[1].split("_")[1].split(".csv")[0])
			date_time = datetime.datetime.fromtimestamp(float(save_timestamp)/1000).strftime('%Y-%m-%d')

			for file_idx in range(len(files_array[jelly_idx][date_idx])):
				timestamp = datetime.datetime.fromtimestamp(float(files_array[jelly_idx][date_idx][file_idx][11:24]) / 1000)
				hour = timestamp.hour
				file_distribution_per_user[hour] = file_distribution_per_user[hour] + 1
			save_row = [jelly_id, date_time, file_distribution_per_user]

			file_distribution.append(save_row)

	return file_distribution


def filter_file_distribution(file_distribution):

	filtered_file_distribution = []

	for jelly_idx in range(len(file_distribution)):
		filter_file_distribution_per_user = np.zeros(24)
		for hour_idx in range(len(file_distribution[jelly_idx])):
			if hour_idx == 0:
				filter_file_distribution_per_user[hour_idx] = int((file_distribution[jelly_idx][hour_idx] +
																   file_distribution[jelly_idx][hour_idx+1]) / 2)
			elif hour_idx == 23:
				filter_file_distribution_per_user[hour_idx] = int((file_distribution[jelly_idx][hour_idx] +
																		file_distribution[jelly_idx][hour_idx - 1])/2)
			else:
				filter_file_distribution_per_user[hour_idx] = int((file_distribution[jelly_idx][hour_idx] +
																		file_distribution[jelly_idx][hour_idx - 1] +
																		file_distribution[jelly_idx][hour_idx + 1]) / 3)
		filtered_file_distribution.append(filter_file_distribution_per_user)
	print(filtered_file_distribution)
	return filtered_file_distribution

if __name__=='__main__':
	# Get name and date
	jellyID = get_user_folder()
	dateArray = get_user_date_folder(jellyID)

	# Get file array
	filesArray = get_files_per_user(jellyID, dateArray)

	# Get file stat
	condensFileStat 	= compute_condensed_stat_array(filesArray)
	high_lvl_file_stat 	= get_files_high_lvl_stat(condensFileStat)

	# Plot the High-Level File Stat
	# plot_files_stat(high_lvl_file_stat)

	header = ['jelly_id', 'valid_days', 'average file per day', 'std file per day']
	save_data_to_csv('high_lvl_file_stat', header, high_lvl_file_stat)

	# Get the File Distribution Per hour
	fileDistribution = get_file_distribution_per_user(filesArray)
	# fileDistribution = filter_file_distribution(fileDistribution)

	# Plot the Recordings per Hour/Distribution
	plot_file_distribution(fileDistribution)

	# Write File
















