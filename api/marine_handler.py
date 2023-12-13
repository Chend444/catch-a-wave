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