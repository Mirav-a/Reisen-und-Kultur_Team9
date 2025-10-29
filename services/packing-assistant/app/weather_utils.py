# weather_utils.py - Dummy Weather Formatter

def format_weather(weather_data):
    """
    Formatiert Wetterdaten in lesbaren Text für den AI-Prompt.

    :param weather_data: Dictionary mit keys: 'weather', 'temperature', 'season'
    :return: formatierter String
    """
    return f"{weather_data['weather']}, {weather_data['temperature']}°C, Saison: {weather_data['season']}"
