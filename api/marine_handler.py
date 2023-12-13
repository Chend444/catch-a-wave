import json
from api.waether_api.marine_api import get_city_data
from collections import defaultdict


def get_waves_peak_range(city_name):
    marine_data = get_city_data(city_name)
    waves = [float(hour['sig_ht_mt']) for hour in marine_data["forecast"]["forecastday"][0]["hour"]]

    max_wave_height = max(waves)
    max_ranges = []
    start = None

    for idx, wave_height in enumerate(waves):
        print(wave_height)
        if wave_height == max_wave_height:
            if start is None:
                start = marine_data["forecast"]["forecastday"][0]["hour"][idx]['time']
        elif start is not None:
            end = marine_data["forecast"]["forecastday"][0]["hour"][idx]['time']
            max_ranges.append([start, end])
            start = None

    if start is not None:
        # If the highest value persists until the end
        end = marine_data["forecast"]["forecastday"][0]["hour"][-1]['time']
        max_ranges.append([start, end])

    return int(max_wave_height * 100), max_ranges


def get_waves_peak_hours(city_name):
    marine_data = get_city_data(city_name)
    max_waves_height = 0
    waves_dict = defaultdict(list)
    for hour in marine_data["forecast"]["forecastday"][0]["hour"]:
        print(hour['sig_ht_mt'])
        parsed_date = hour['time'].split()

        if hour['sig_ht_mt'] > max_waves_height:
            max_waves_height = hour['sig_ht_mt']
            parsed_max_height = int(max_waves_height * 100)
            waves_dict.clear()
            waves_dict[parsed_max_height].append(parsed_date[1])

        elif hour['sig_ht_mt'] == max_waves_height:
            parsed_max_height = int(max_waves_height * 100)
            waves_dict[parsed_max_height].append(parsed_date[1])

    return waves_dict


def get_surfing_hourly_score(city_name):
    marine_data = get_city_data(city_name)
    swell_ht_mt_arr = []
    swell_dir_arr = []
    swell_period_secs_arr = []
    wind_kph_arr = []
    wind_degree_arr = []
    wind_dir_arr = []

    for hour in marine_data["forecast"]["forecastday"][0]["hour"]:
        swell_ht_mt_arr.append(hour['swell_ht_mt'])
        swell_dir_arr.append(hour['swell_dir'])
        swell_period_secs_arr.append(hour['swell_period_secs'])
        wind_kph_arr.append(hour['wind_kph'])
        wind_degree_arr.append(hour['wind_degree'])
        wind_dir_arr.append(hour['wind_dir'])

    normalized_swell_ht_mt = normalize_data_numbers(swell_ht_mt_arr)
    normalized_swell_dir = normalize_data_numbers(swell_dir_arr)
    normalized_swell_period_secs = normalize_data_numbers(swell_period_secs_arr)
    normalized_wind_kph = normalize_data_numbers(wind_kph_arr)
    normalized_wind_degree = normalize_data_numbers(wind_degree_arr)

    hourly_wave_score = calculate_surf_score(normalized_swell_ht_mt,normalized_swell_dir,normalized_swell_period_secs,normalized_wind_kph,normalized_wind_degree)

    return hourly_wave_score


def normalize_data_numbers(data):
    min_value = min(data)
    max_value = max(data)

    # Normalize the data
    normalized_data = [(val - min_value) / (max_value - min_value) for val in data]
    return normalized_data


def calculate_surf_score(swell_height, swell_direction, swell_period, wind_speed, wind_direction):
    # Define weights for each parameter
    weight_swell_height = 0.30
    weight_swell_period = 0.25
    weight_swell_direction = 0.15
    weight_wind_speed = 0.15
    weight_wind_direction = 0.15

    score_arr = []

    for i, (height, period, direction, speed, wind_dir) in enumerate(zip(swell_height, swell_period, swell_direction, wind_speed, wind_direction)):
        score = (height * weight_swell_height) + (period * weight_swell_period) + (direction * weight_swell_direction) + (speed * weight_wind_speed) + (wind_dir * weight_wind_direction)
        rounded_score = round(score*100)  # Round the score to two decimal places
        score_arr.append(rounded_score)

    score_dict = {}

    for i, score in enumerate(score_arr):
        hour_key = f"{i:02d}:00"  # Format the index as hours (00:00 format)
        score_dict[hour_key] = score

    return score_dict

