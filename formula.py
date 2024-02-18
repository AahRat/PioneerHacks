# wanted_temp=75
#
# wanted_humidity=40
#
# wanted_precipitation=0
#
# wanted_wind_speed=7
#
# wanted_cloud_cover=30
#
# wanted_visibility=10
#
#
#
#
# current_temp=58
#
# current_humidity=80
#
# current_precipitation=1
#
# current_wind_speed=10
#
# current_cloud_cover=100
#
# current_visibility=6
#
# current_AQI=28
#
# current_air_pressure=29.99
#
# current_UV=0
#
# index=100
#
#
#
# if current_temp<wanted_temp or current_temp>wanted_temp:
#     index-=((abs(current_temp-wanted_temp))*0.8)
#
# if current_humidity<wanted_humidity or current_humidity>wanted_humidity:
#     index-=((abs(current_humidity-wanted_humidity))/15)
#
# if current_precipitation!=wanted_precipitation:
#     index-=20
#
# if current_wind_speed>wanted_wind_speed or current_wind_speed<wanted_wind_speed:
#     index-=((abs(current_wind_speed-wanted_wind_speed)))
#
# if current_cloud_cover>wanted_cloud_cover or current_cloud_cover<wanted_cloud_cover:
#     index-=((abs(current_cloud_cover-wanted_cloud_cover))/20)
#
# if current_visibility<wanted_visibility:
#     index-=((abs(current_visibility-wanted_visibility)))
#
# if current_AQI>50 and current_AQI<=100:
#     index-=8
#
# if current_AQI>100 and current_AQI<=150:
#     index-=14
#
# if current_AQI>150 and current_AQI<=200:
#     index-=20
#
# if current_AQI>200 and current_AQI<=300:
#     index-=40
#
# if current_AQI>300 and current_AQI<=500:
#     index-=60
#
# if current_air_pressure<29.6 or current_air_pressure>30.2:
#     index-=5
#
#
# if current_UV>2 and current_UV<=5:
#     index-=5
#
# if current_UV>6:
#     index-=10
#
#
#
#
# print(round(index))


def weather_formula(preferences, real_data):
    index = 100
    if real_data[0] < preferences["Temperature"] or preferences["Temperature"] > real_data[0]:
        index -= ((abs(real_data[0] - preferences["Temperature"])) * 0.8)

    if real_data[1] < preferences["Humidity"] or preferences["Humidity"] > real_data[1]:
        index -= ((abs(real_data[1] - preferences["Humidity"])) / 15)

    wanted_precipitation = -1
    if preferences["Precipitation"] in ['None', 'none']:
        wanted_precipitation = 0
    elif preferences["Precipitation"] in ['Low', 'low']:
        wanted_precipitation = 1
    elif preferences["Precipitation"] in ['Moderate', 'moderate']:
        wanted_precipitation = 2
    elif preferences["Precipitation"] in ['High', 'high']:
        wanted_precipitation = 3

    if real_data[2] != wanted_precipitation:
        index -= 20

    if real_data[3] > preferences["Wind"] or real_data[3] < preferences["Wind"]:
        index -= ((abs(real_data[3] - preferences["Wind"])))

    if real_data[4] > preferences["Cloud Cover"] or real_data[4] < preferences["Cloud Cover"]:
        index -= ((abs(real_data[4] - preferences["Cloud Cover"])) / 20)

    if real_data[5] < preferences["Visibility"]:
        index -= ((abs(real_data[5] - preferences["Visibility"])))

    return int(index)
