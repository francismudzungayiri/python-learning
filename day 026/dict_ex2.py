weather_c = {
    'Monday': 12,
    'Tuesday': 14,
    'Wednesday': 15,
    'Thursday': 14,
    'Friday': 21,
    'Saturday': 22,
    'Sunday': 24,
}

weather_in_forein = {
    day: (foreinheight*9/5) + 32 for (day, foreinheight) in weather_c.items()
}

print(weather_in_forein)