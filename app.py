from flask import Flask, request, render_template
from video_analysis import extract_video_data
from recommender import generate_recommendations
import os

import matplotlib
matplotlib.use("Agg")  # Required for server-side graph rendering
import matplotlib.pyplot as plt

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = []
    graph = None

    if request.method == "POST":
        video = request.files.get("video")

        if video and video.filename != "":
            file_path = os.path.join(UPLOAD_FOLDER, video.filename)
            video.save(file_path)

            # Extract video features
            data = extract_video_data(file_path)

            # Generate VFX recommendations
            recommendations = generate_recommendations(data)

            # Generate graph
            os.makedirs("static", exist_ok=True)
            graph_path = os.path.join("static", "graph.png")

            plt.figure(figsize=(8, 4))
            plt.plot(data["motion"], label="Motion Intensity")
            plt.plot(data["brightness"], label="Brightness Level")
            plt.xlabel("Frame Index")
            plt.ylabel("Normalized Value")
            plt.title("Video Feature Analysis")
            plt.legend()
            plt.tight_layout()

            plt.savefig(graph_path)
            plt.close()

            graph = graph_path

    return render_template(
        "index.html",
        recommendations=recommendations,
        graph=graph
    )


if __name__ == "__main__":
    app.run(debug=True)