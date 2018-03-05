import numpy as np
from scipy.stats import kurtosis
from scipy.stats import skew
from scipy import stats

def stat_average(final_feature_array):
    stat_result = np.average(final_feature_array)
    return stat_result

def stat_min(final_feature_array):
    stat_result = np.min(final_feature_array)
    return stat_result

def stat_max(final_feature_array):
    stat_result = np.max(final_feature_array)
    return stat_result

def stat_std(final_feature_array):
    stat_result = np.std(final_feature_array)
    return stat_result

def stat_skew(final_feature_array):
    stat_result = skew(final_feature_array)
    return stat_result

def stat_kurtosis(final_feature_array):
    stat_result = kurtosis(final_feature_array)
    return stat_result

def stat_percentile_1(final_feature_array):
    stat_result = np.percentile(final_feature_array, 1)
    return stat_result

def stat_percentile_99(final_feature_array):
    stat_result = np.percentile(final_feature_array, 99)
    return stat_result

def stat_linregress_slope(final_time_array, final_feature_array):
    linear_coeff = stats.linregress(final_time_array, final_feature_array)
    return linear_coeff[0]

def stat_linregress_intercept(final_time_array, final_feature_array):
    linear_coeff = stats.linregress(final_time_array, final_feature_array)
    return linear_coeff[1]

def stat_linregress_r(final_time_array, final_feature_array):
    linear_coeff = stats.linregress(final_time_array, final_feature_array)
    return linear_coeff[2]

def stat_linregress_p(final_time_array, final_feature_array):
    linear_coeff = stats.linregress(final_time_array, final_feature_array)
    return linear_coeff[3]

def stat_linregress_std_err(final_time_array, final_feature_array):
    linear_coeff = stats.linregress(final_time_array, final_feature_array)
    return linear_coeff[4]

def compute_stat_feature(row_header, stat_frames):

    stat_func = {
        'average': stat_average,
        'std': stat_std,
        'min': stat_min,
        'max': stat_max,
        'skew': stat_skew,
        'kurtosis': stat_kurtosis,
        'percentile_1': stat_percentile_1,
        'percentile_99': stat_percentile_99,
        'linregress_slope': stat_linregress_slope,
        'linregress_intercept': stat_linregress_intercept,
        'linregress_r': stat_linregress_r,
        'linregress_p': stat_linregress_p,
        'linregress_std_err': stat_linregress_std_err,
    }

    rows = np.array(stat_frames)

    vad = np.array(rows[:, 2], dtype=int)
    sum_vad = np.sum(vad)

    rows = np.delete(rows, [0, 1, 2], axis=1)
    rows = np.array(rows, dtype=float)

    stat_results = np.zeros(1 + (np.shape(rows)[1] * len(row_header)))
    stat_results[0] = sum_vad

    for i in range(0, np.shape(rows)[1], 1):
        feature_col = rows[:, i]

        final_feature_array = []
        final_time_array = []

        for j in range(len(feature_col)):

            if feature_col[j] != 0 and feature_col[j] > -90:
                final_feature_array = np.append(final_feature_array, feature_col[j])
                final_time_array = np.append(final_time_array, j * 0.01)

        stat_result = np.zeros(len(row_header))
        if len(final_feature_array) > 3:
            for idx, item in enumerate(row_header):
                for name, func in stat_func.items():
                    if item in name:
                        if 'linregress' in name:
                            stat_result[idx] = func(final_time_array, final_feature_array)
                        else:
                            stat_result[idx] = func(final_feature_array)
        stat_results[1 + i*len(row_header): 1 + (i+1)*len(row_header)] = stat_result

    return stat_results

