import time
import sys

# Original code with a dramatic countdown theme
i = 10
values = []
print("🚀 LAUNCH SEQUENCE INITIATED...")
print("=" * 20)
time.sleep(2)

while i >= 3:
    # Dramatic countdown effect
    progress = (10 - i) / 3  # 0 to 1 as we go from 7 to 4
    bar_length = int(progress * 20)
    bar = "█" * bar_length + "░" * (20 - bar_length)
    
    # Visual effect
    print(f"\rAltitude: {round(i, 3)} km | {bar} {int(progress * 100)}%", end="")
    
    values.append(round(i, 3))
    i -= 0.7
    time.sleep(0.3)

print("\n\n✨ LANDING SEQUENCE COMPLETE! ✨")
print("=" * 40)
print(f"📊 Altitude readings: {values}")
print(f"📈 Total readings: {len(values)}")
# print(f"🎯 Target reached: Below 4 km!")
# TODO@Belkau77
# Bonus: Create a simple ASCII chart
print("\n📉 ALTITUDE CHART:")
max_val = max(values)
for val in values:
    bar_length = int((val / 30) * 30)
    bar = "█" * bar_length
    print(f"{val:4.2f} |{bar}")

# Animated fireworks if you have the final value
if values[-1] < 3:
    print("\n🎆🎇 TOUCHDOWN! 🎇🎆")
    for _ in range(3):
        for pattern in ["✨  *  ✨", " * ✨ * ", "✨  *  ✨"]:
            print(f"\r{pattern}", end="")
            time.sleep(0.2)
    print() 