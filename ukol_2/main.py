import matplotlib.pyplot as plt
import requests

def get_historical_temps(start_date, end_date):
    """Stáhne průměrné denní teploty pro Brno z Open-Meteo API."""
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": 49.1951,
        "longitude": 16.6068,
        "start_date": start_date,
        "end_date": end_date,
        "daily": "temperature_2m_mean",
        "timezone": "Europe/Berlin"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    return data['daily']['temperature_2m_mean']

# Definice týdnů (pondělí - neděle) v roce 2024
# Leden: 8.1. - 14.1. 2024
# Červenec: 8.7. - 14.7. 2024
dny = ['Po', 'Út', 'St', 'Čt', 'Pá', 'So', 'Ne']

print("Stahuji reálná data z Open-Meteo API...")
leden_teploty = get_historical_temps("2024-01-08", "2024-01-14")
cervenec_teploty = get_historical_temps("2024-07-08", "2024-07-14")

# Výpočet rozdílu teplot
rozdily = [c - l for c, l in zip(cervenec_teploty, leden_teploty)]

# Inicializace grafu se dvěma subploty
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10), sharex=True)

# --- PRVNÍ GRAF (Srovnání) ---
ax1.axhspan(18, 24, color='gray', alpha=0.2, label='Komfortní zóna (18-24 °C)')
ax1.plot(dny, leden_teploty, label='Leden 2024 (reálná data)', color='blue', marker='o', linewidth=2)
ax1.plot(dny, cervenec_teploty, label='Červenec 2024 (reálná data)', color='red', marker='s', linewidth=2)

ax1.set_title('Reálné denní teploty v Brně (2024): Leden vs. Červenec', fontsize=14, fontweight='bold')
ax1.set_ylabel('Teplota (°C)', fontsize=12)
ax1.legend(loc='upper right', fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.axhline(0, color='black', linewidth=0.8, linestyle='--')

# Výpočet extrémů pro anotace
min_leden = min(leden_teploty)
den_min = dny[leden_teploty.index(min_leden)]
max_cervenec = max(cervenec_teploty)
den_max = dny[cervenec_teploty.index(max_cervenec)]

ax1.annotate(f'Min: {min_leden:.1f}°C', xy=(den_min, min_leden), xytext=(den_min, min_leden - 3),
             arrowprops=dict(facecolor='blue', shrink=0.05, width=2, headwidth=8),
             ha='center', fontsize=10, color='blue', fontweight='bold')

ax1.annotate(f'Max: {max_cervenec:.1f}°C', xy=(den_max, max_cervenec), xytext=(den_max, max_cervenec + 2),
             arrowprops=dict(facecolor='red', shrink=0.05, width=2, headwidth=8),
             ha='center', fontsize=10, color='red', fontweight='bold')

# --- DRUHÝ GRAF (Rozdíl) ---
bars = ax2.bar(dny, rozdily, color='orange', alpha=0.7, label='Rozdíl (Čv - Le)')
ax2.set_title('Denní rozdíl teplot (Červenec - Leden)', fontsize=13, fontweight='bold')
ax2.set_xlabel('Den v týdnu (8. - 14. dne v měsíci)', fontsize=12)
ax2.set_ylabel('Rozdíl (°C)', fontsize=12)
ax2.grid(True, axis='y', linestyle='--', alpha=0.7)

for bar in bars:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{yval:.1f}', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('teploty_brno_srovnani.png', dpi=300)

print(f"Data stažena: Leden: {leden_teploty}")
print(f"Data stažena: Červenec: {cervenec_teploty}")
print("Graf s reálnými daty byl úspěšně vygenerován.")
