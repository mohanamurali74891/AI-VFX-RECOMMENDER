def generate_recommendations(data):
    motion = data["motion"]
    brightness = data["brightness"]
    timestamps = data["timestamps"]

    highlight_scores = []

    for i in range(len(motion)):
        score = (0.7 * motion[i]) + (0.3 * brightness[i])
        highlight_scores.append((score, timestamps[i]))

    # Sort by highest score
    highlight_scores.sort(reverse=True)

    recommendations = []

    # Take top 5 moments
    for score, time in highlight_scores[:5]:

        if score > 0.8:
            effect = "Explosion / Cinematic Impact VFX"
        elif score > 0.65:
            effect = "Slow Motion + Dramatic Sound Effect"
        else:
            effect = "Color Grading Enhancement"

        recommendations.append(
            f"{effect} recommended at {round(time,2)} sec (Score: {round(score,2)})"
        )

    return recommendations