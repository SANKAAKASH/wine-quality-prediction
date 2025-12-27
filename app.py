from flask import Flask, render_template, request
import numpy as np
import pickle
import cv2
from PIL import Image
import io

app = Flask(__name__)

# ================= LOAD MODEL =================
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# ================= IMAGE VALIDATION =================
def is_beverage_image(image_bytes):
    try:
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        img = np.array(image)
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        r, g, b = np.mean(img, axis=(0, 1))

        # Beverage-like color heuristic
        color_valid = (r > g and r > b) or (g > b)

        edges = cv2.Canny(gray, 100, 200)
        edge_density = np.mean(edges > 0)

        structure_valid = 0.02 < edge_density < 0.15

        return color_valid and structure_valid
    except:
        return False

# ================= IMAGE QUALITY ANALYSIS =================
def analyze_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img = np.array(image)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    color_score = np.mean(img) / 255
    clarity_score = min(cv2.Laplacian(gray, cv2.CV_64F).var() / 500, 1)

    score = (0.6 * color_score) + (0.4 * clarity_score)
    quality = int(3 + score * 5)

    return max(3, min(8, quality))

# ================= ROUTES =================
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data_quality = None
        image_quality = None
        mode = "Unknown"

        # -------- TABULAR DATA --------
        if request.form.get("fixed_acidity"):
            features = [
                float(request.form["fixed_acidity"]),
                float(request.form["volatile_acidity"]),
                float(request.form["citric_acid"]),
                float(request.form["residual_sugar"]),
                float(request.form["chlorides"]),
                float(request.form["free_sulfur_dioxide"]),
                float(request.form["total_sulfur_dioxide"]),
                float(request.form["density"]),
                float(request.form["pH"]),
                float(request.form["sulphates"]),
                float(request.form["alcohol"])
            ]

            data_quality = int(
                model.predict(np.array(features).reshape(1, -1))[0]
            )

        # -------- IMAGE --------
        if "image" in request.files and request.files["image"].filename != "":
            image_bytes = request.files["image"].read()

            if not is_beverage_image(image_bytes):
                return render_template(
                    "index.html",
                    error="Uploaded image is not a valid beer/wine image."
                )

            image_quality = analyze_image(image_bytes)

        # -------- FINAL QUALITY --------
        if data_quality is not None and image_quality is not None:
            final_quality = int(0.7 * data_quality + 0.3 * image_quality)
            mode = "Data + Image"
            confidence = 85
        elif data_quality is not None:
            final_quality = data_quality
            mode = "Data Only"
            confidence = 90
        elif image_quality is not None:
            final_quality = image_quality
            mode = "Image Only"
            confidence = 70
        else:
            return render_template(
                "index.html",
                error="Please enter data or upload an image."
            )

        # -------- LABEL --------
        if final_quality <= 4:
            label = "Low Quality"
            color = "danger"
        elif final_quality <= 6:
            label = "Average Quality"
            color = "warning"
        else:
            label = "High Quality"
            color = "success"

        return render_template(
            "index.html",
            quality=final_quality,
            label=label,
            color=color,
            mode=mode,
            confidence=confidence,
            data_quality=data_quality,
            image_quality=image_quality
        )

    except Exception as e:
        return render_template("index.html", error=str(e))


# ================= RUN =================
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
