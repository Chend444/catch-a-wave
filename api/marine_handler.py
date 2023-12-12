import json
from api.waether_api.marine_api import get_city_data

def check_city_waves(cityName):
    marine_data = get_city_data(cityName)
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

    return max_wave_height, max_ranges


