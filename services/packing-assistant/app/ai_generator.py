from app.weather_utils import format_weather
from app.travel_data_dummy import get_travel_data
import google.generativeai as genai

def generate_ai_packlist(destination: str, days: int, activities: list[str]) -> dict:
    weather_data = get_travel_data(destination)
    weather_text = format_weather(weather_data)

    prompt = (
        f"Erstelle eine Packliste für eine Reise nach {destination}.\n"
        f"Reisedauer: {days} Tage\n"
        f"Aktivitäten: {', '.join(activities) if activities else 'Keine'}\n"
        f"Wettervorhersage: {weather_text}\n\n"
        f"Packliste mit Begründung pro Item im Format:\n"
        f"- Sonnencreme: Schutz vor Sonnenbrand\n"
        f"- Wasserflasche: Wichtig bei Wanderung\n"
    )

    response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt)
    text = response.text.strip()

    # DEBUG-AUSGABE – nur zur Kontrolle
    print("---------- AI-RESPONSE START ----------")
    print(text)
    print("---------- AI-RESPONSE END   ----------")

    items = []

    for line in text.split("\n"):
        line = line.strip("- ").strip()
        if ":" in line:
            name, reason = line.split(":", 1)
            items.append({
                "name": name.strip(),
                "reason": reason.strip(),
                "qty": 1
            })

    return {
        "destination": destination,
        "summary": f"Packliste für {destination} ({days} Tage), Wetter: {weather_text}",
        "items": items
    }
