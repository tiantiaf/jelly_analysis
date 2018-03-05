import csv
import datetime
import os
import numpy as np
from script.compute_stat import compute_stat_feature

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

		username_folder_index = username_folder_index + 1;

	return file_array

def compile_file_per_user(jelly_id_array, date_array, files_array):

	time_idx 		= 1
	is_turn_idx 	= 2
	intensity_idx 	= 3
	loudness_idx	= 4
	mfcc_idx		= 5
	lsp_idx			= 17
	zcr_idx			= 25
	voice_prob_idx	= 26
	pitch_idx		= 27
	env_idx			= 28

	header = ['timestamp(time since midnight)', 'isTurn', 'intensity', 'loudness',
				'mfcc0', 'mfcc1', 'mfcc2', 'mfcc3', 'mfcc4', 'mfcc5',
			   	'mfcc6', 'mfcc7', 'mfcc8', 'mfcc9', 'mfcc10', 'mfcc11',
				'lsp0', 'lsp1', 'lsp2', 'lsp3', 'lsp4', 'lsp5', 'lsp6', 'lsp7',
			   	'zcr', 'voice_prob', 'pitch', 'env']

	number_of_files_in_total 	= 0
	number_of_files_compiled	= 0

	for jelly_idx in range(len(files_array)):
		for date_idx in range(len(files_array[jelly_idx])):
			number_of_files_in_total = len(files_array[jelly_idx][date_idx]) + number_of_files_in_total

	for jelly_idx in range(len(files_array)):
		jelly_id = jelly_id_array[jelly_idx]
		print("Write to {}".format(jelly_id_array[jelly_idx]))

		if not os.path.isdir(''.join(["../compiled_data/", jelly_id])):
			os.makedirs(''.join(["../compiled_data/", jelly_id]))

		for date_idx in range(len(files_array[jelly_idx])):
			date_id = date_array[jelly_idx][date_idx]
			output_file = open(''.join(["../compiled_data/", jelly_id, "/" , date_id, ".csv"]), 'w')
			with output_file:
				output_writer = csv.writer(output_file, delimiter=',')
				output_writer.writerow(header)
				for file_idx in range(len(files_array[jelly_idx][date_idx])):
					number_of_files_compiled = number_of_files_compiled + 1

					timestamp_of_file = datetime.datetime.fromtimestamp(float(files_array[jelly_idx][date_idx][file_idx][11:24]) / 1000)
					time_elapsed = timestamp_of_file.hour * 3600 + timestamp_of_file.minute * 60 + timestamp_of_file.second
					file_path = ''.join(["../data/", jelly_id + "/", date_id + "/" + files_array[jelly_idx][date_idx][file_idx]])

					if os.path.isfile(file_path):
						with open(file_path) as csv_file:

							frames = csv.reader(csv_file, delimiter=';')
							for frame in frames:
								if 'frame' not in frame[0] and len(frame) > 40:
									frame_abs_time = time_elapsed + float(frame[time_idx])

									output_writer.writerow([str(frame_abs_time), frame[is_turn_idx],
												frame[intensity_idx], frame[loudness_idx],
												frame[mfcc_idx],
												frame[mfcc_idx + 1],
												frame[mfcc_idx + 2],
												frame[mfcc_idx + 3],
												frame[mfcc_idx + 4],
												frame[mfcc_idx + 5],
												frame[mfcc_idx + 6],
												frame[mfcc_idx + 7],
												frame[mfcc_idx + 8],
												frame[mfcc_idx + 9],
												frame[mfcc_idx + 10],
												frame[mfcc_idx + 11],
												frame[lsp_idx],
												frame[lsp_idx + 1],
												frame[lsp_idx + 2],
												frame[lsp_idx + 3],
												frame[lsp_idx + 4],
												frame[lsp_idx + 5],
												frame[lsp_idx + 6],
												frame[lsp_idx + 7],
												frame[zcr_idx], frame[voice_prob_idx],
												frame[pitch_idx], frame[env_idx]])

					print("{:.0%} have been compiled. File {} has been compiled.".
						  format(number_of_files_compiled / number_of_files_in_total,
						  ''.join(["../data/", jelly_id + "/", date_id + "/" + files_array[jelly_idx][date_idx][file_idx]])) )

def compile_all_files_per_user(jelly_id_array, date_array, files_array):

	time_idx 		= 1
	is_turn_idx 	= 2
	intensity_idx 	= 3
	loudness_idx	= 4
	mfcc_idx		= 5
	lsp_idx			= 17
	zcr_idx			= 25
	voice_prob_idx	= 26
	pitch_idx		= 27
	env_idx			= 28

	header = ['date', 'timestamp(time since midnight)', 'isTurn', 'intensity', 'loudness',
				'mfcc0', 'mfcc1', 'mfcc2', 'mfcc3', 'mfcc4', 'mfcc5',
			   	'mfcc6', 'mfcc7', 'mfcc8', 'mfcc9', 'mfcc10', 'mfcc11',
				'lsp0', 'lsp1', 'lsp2', 'lsp3', 'lsp4', 'lsp5', 'lsp6', 'lsp7',
			   	'zcr', 'voice_prob', 'pitch', 'env']

	number_of_files_in_total 	= 0
	number_of_files_compiled	= 0

	for jelly_idx in range(len(files_array)):
		for date_idx in range(len(files_array[jelly_idx])):
			number_of_files_in_total = len(files_array[jelly_idx][date_idx]) + number_of_files_in_total

	for jelly_idx in range(len(files_array)):
		jelly_id = jelly_id_array[jelly_idx]
		print("Write to {}".format(jelly_id_array[jelly_idx]))

		if not os.path.isdir(''.join(['../compiled_data/', jelly_id])):
			os.makedirs(''.join(['../compiled_data/', jelly_id]))

		for date_idx in range(len(files_array[jelly_idx])):
			date_id = date_array[jelly_idx][date_idx]
			save_date_id = date_id[5:7] + '-' + date_id[8:10] + '-' + date_id[0:4]

			output_file = open(''.join(['../compiled_data/', jelly_id, '/', jelly_id,
										'_', save_date_id, '.csv']), 'w')

			with output_file:
				output_writer = csv.writer(output_file, delimiter=',')

				for file_idx in range(len(files_array[jelly_idx][date_idx])):
					number_of_files_compiled = number_of_files_compiled + 1

					timestamp_of_file = datetime.datetime.fromtimestamp(float(files_array[jelly_idx][date_idx][file_idx][11:24]) / 1000)
					time_elapsed = timestamp_of_file.hour * 3600 + timestamp_of_file.minute * 60 + timestamp_of_file.second
					file_path = ''.join(["../data/", jelly_id + "/", date_id + "/" + files_array[jelly_idx][date_idx][file_idx]])

					if os.path.isfile(file_path):
						with open(file_path) as csv_file:

							frames = csv.reader(csv_file, delimiter=';')
							stat_frames = []
							for frame in frames:
								if 'frame' not in frame[0] and len(frame) > 40:
									frame_abs_time = time_elapsed + float(frame[time_idx])

									data = [save_date_id]

									for idx, col in enumerate(frame):
										if idx is not 0:
											if idx is 1:
												data.append(str(frame_abs_time))
											elif idx < 55:
												data.append(col)

									if len(stat_frames) is 0:
										stat_frames = data
									elif len(stat_frames) < 200:
										stat_frames = np.vstack((stat_frames, data))
									else:
										if float(frame[time_idx]).is_integer():
											print(float(frame[time_idx]))

										stat_frames = np.delete(stat_frames, 0, 0)
										stat_frames = np.vstack((stat_frames, data))

									output_writer.writerow(data)
								else:

									if file_idx is 0:
										frame_header = ['date', 'time', 'isTurn']

										for col in frame:
											if 'frameIndex' not in col:
												if 'sma' in col:
													frame_header.append(col)
										output_writer.writerow(frame_header)


					print("{:.0%} have been compiled. File {} has been compiled.".
						  format(number_of_files_compiled / number_of_files_in_total,
						  ''.join(["../data/", jelly_id + "/", date_id + "/" + files_array[jelly_idx][date_idx][file_idx]])))

def compile_stat_all_files_per_user(jelly_id_array, date_array, files_array):

	time_idx 		= 1

	number_of_files_in_total 	= 0
	number_of_files_compiled	= 0

	functionals = ['average', 'std', 'min', 'max',
				  'skew', 'kurtosis',
				  'percentile_1', 'percentile_99',
				  'linregress_slope', 'linregress_intercept',
				  'linregress_r', 'linregress_p',
				  'linregress_std_err']


	for jelly_idx in range(len(files_array)):
		for date_idx in range(len(files_array[jelly_idx])):
			number_of_files_in_total = len(files_array[jelly_idx][date_idx]) + number_of_files_in_total

	for jelly_idx in range(len(files_array)):
		jelly_id = jelly_id_array[jelly_idx]
		print("Write to {}".format(jelly_id_array[jelly_idx]))

		if not os.path.isdir(''.join(['../compiled_data/', jelly_id])):
			os.makedirs(''.join(['../compiled_data/', jelly_id]))

		for date_idx in range(len(files_array[jelly_idx])):
			date_id = date_array[jelly_idx][date_idx]
			save_date_id = date_id[5:7] + '-' + date_id[8:10] + '-' + date_id[0:4]

			output_file = open(''.join(['../compiled_data/', jelly_id, '/', jelly_id,
										'_', save_date_id, '.csv']), 'w')

			with output_file:
				output_writer = csv.writer(output_file, delimiter=',')

				for file_idx in range(len(files_array[jelly_idx][date_idx])):
					number_of_files_compiled = number_of_files_compiled + 1

					timestamp_of_file = datetime.datetime.fromtimestamp(int(float(files_array[jelly_idx][date_idx][file_idx][11:24]) / 1000))
					time_elapsed = timestamp_of_file.hour * 3600 + timestamp_of_file.minute * 60 + timestamp_of_file.second

					file_path = ''.join(["../data/", jelly_id + "/", date_id + "/" + files_array[jelly_idx][date_idx][file_idx]])

					if os.path.isfile(file_path):
						with open(file_path) as csv_file:

							frames = csv.reader(csv_file, delimiter=';')
							stat_frames = []
							for frame in frames:
								if 'frame' not in frame[0] and len(frame) > 40:
									frame_abs_time = time_elapsed + float(frame[time_idx])

									data = [save_date_id]

									for idx, col in enumerate(frame):
										if idx is not 0:
											if idx is 1:
												data.append(str(frame_abs_time))
											elif idx < 55:
												data.append(col)

									if len(stat_frames) is 0:
										stat_frames = data
									elif len(stat_frames) < 250:
										stat_frames = np.vstack((stat_frames, data))
									else:
										if (float(frame[time_idx])-2.5).is_integer() and float(frame[time_idx]) > 2:
											write_row = [timestamp_of_file.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]]
											time_delta = datetime.timedelta(seconds=1)
											timestamp_of_file = timestamp_of_file + time_delta

											stat_results = compute_stat_feature(functionals, stat_frames)
											for item in stat_results:
												write_row.append(item)

											output_writer.writerow(write_row)

										stat_frames = np.delete(stat_frames, 0, 0)
										stat_frames = np.vstack((stat_frames, data))

								else:

									if file_idx is 0:
										frame_header = ['TimeStamp', 'isTurn']

										for col in frame:
											if 'frameIndex' not in col:
												if 'sma' in col:
													for functional in functionals:
														frame_header.append(col + '_' + functional)
										output_writer.writerow(frame_header)


					print("{:.0%} have been compiled. File {} has been compiled.".
						  format(number_of_files_compiled / number_of_files_in_total,
						  ''.join(["../data/", jelly_id + "/", date_id + "/" + files_array[jelly_idx][date_idx][file_idx]])))

if __name__=='__main__':
	# Get name and date array
	jellyID = get_user_folder()
	dateArray = get_user_date_folder(jellyID)

	# Get file array
	allFilesArray = get_all_files_per_user(jellyID, dateArray)

	# Write Stat to File
	compile_stat_all_files_per_user(jellyID, dateArray, allFilesArray)

	# Write File
	# compile_all_files_per_user(jellyID, dateArray, allFilesArray)
















