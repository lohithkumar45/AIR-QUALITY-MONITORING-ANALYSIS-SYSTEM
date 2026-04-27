def validate_aqi(aqi):
    if aqi < 0:
        raise ValueError

try:
    name = input()
    aqi = int(input())
    validate_aqi(aqi)
    print(name, aqi)
except ValueError:
    print("Invalid AQI")
finally:
    print("Done")