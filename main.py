from video_analysis import extract_video_data
from recommender import generate_recommendations
import matplotlib.pyplot as plt

data = extract_video_data("sample.mp4")

recommendations = generate_recommendations(data)

print("\n=== VFX RECOMMENDATIONS ===")
for r in recommendations[:10]:  # show first 10
    print(r)

# Plot
plt.figure(figsize=(12,5))
plt.plot(data["timestamps"], data["motion"], label="Motion")
plt.plot(data["timestamps"], data["brightness"], label="Brightness")
plt.legend()
plt.xlabel("Time (seconds)")
plt.ylabel("Normalized Value")
plt.title("Motion & Brightness Analysis")
plt.show()