<!-- .github/copilot-instructions.md - Guidance for AI coding agents working on this repo -->
# Copilot / AI Agent Instructions — Wine-Quality-Prediction

Purpose: provide concise, actionable project knowledge so an AI coding agent can be productive immediately.

Quick summary
- Small Flask web app that loads a scikit-learn model (`model.pkl`) and exposes a single prediction endpoint (`/predict`).
- Training / model-generation happens in `Wine_Quality_Prediction_Notebook.ipynb` using `Raw_Data/winequality-red.csv`.

Run / developer workflows
- Install deps: `pip install -r requirements.txt` (use a virtualenv). Note: `requirements.txt` includes `streamlit` though app uses Flask.
- Run locally: `python app.py` (serves Flask app on default port 5000 with `debug=True`).
- Docker: `docker build -t winequality .` then `docker run -p 5000:5000 winequality` (Dockerfile runs `python app.py`).

Key files & responsibilities
- `app.py`: Flask app. Routes:
  - `/` — renders templates/index.html
  - `/predict` (POST) — reads 11 numeric form fields in a fixed order, builds a NumPy array, calls `model.predict(...)`, returns result in `index.html`.
  Example feature order used in code: `fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol`
- `model.pkl` (expected at repo root at runtime): pickled scikit-learn model. If missing, run the notebook to train and `pickle.dump()` the fitted model to this filename.
- `Wine_Quality_Prediction_Notebook.ipynb`: training and exploratory code. Use it to regenerate `model.pkl` and to confirm preprocessing.
- `templates/index.html` and `templates/error.html`: UI and basic error display. Form field names must match the names `app.py` expects.
- `Raw_Data/winequality-red.csv`: source dataset used in training.

Patterns and conventions (project-specific)
- The app expects form fields to be numeric strings; it converts them via `float(...)` in the exact order above. Preserve order when constructing feature arrays.
- The model is loaded with `pickle.load(open('model.pkl', 'rb'))` at module import time (singleton). Re-training requires re-saving `model.pkl` and redeploying/restarting the app.
- Minimal error handling: `predict()` wraps the whole flow in a broad `try/except` and returns the exception message to the template. Keep changes to error messaging consistent with this lightweight approach.

Integration points & external dependencies
- scikit-learn / numpy: ensure compatible versions. The repo's `requirements.txt` does not pin versions; training artifacts may depend on the scikit-learn/numpy versions used in the notebook. If you encounter pickling errors, try using scikit-learn and numpy versions used when the model was created.
- No external APIs used. All computation is local.

Examples
- Example `curl` to POST a prediction (replace values):

  curl -X POST \
    -F fixed_acidity=7.4 \
    -F volatile_acidity=0.70 \
    -F citric_acid=0.00 \
    -F residual_sugar=1.9 \
    -F chlorides=0.076 \
    -F free_sulfur_dioxide=11 \
    -F total_sulfur_dioxide=34 \
    -F density=0.9978 \
    -F pH=3.51 \
    -F sulphates=0.56 \
    -F alcohol=9.4 \
    http://localhost:5000/predict

What to look for when changing code
- If modifying the feature set/order: update `templates/index.html` form `name` attributes AND the features array construction in `app.py` together.
- If changing model serialization (e.g., switching to `joblib`), update both the code that loads the model and documentation; prefer `joblib.dump`/`joblib.load` for large numpy arrays but keep filename `model.pkl` for backward compatibility unless a migration plan is added.
- Avoid importing and loading the model inside the request handler (keeps current singleton pattern). If you need hot-reload for new models, implement a safe swap/reload mechanism and handle concurrency.

Troubleshooting notes (discoverable from repo)
- Missing `model.pkl` -> app will crash on import or throw when predicting. Regenerate by running the notebook to train and pickle the model.
- Pickle incompatibility errors -> check scikit-learn / numpy versions used to create the pickle.
- UI form mismatch -> ensure each `<input name="...">` in `templates/index.html` maps exactly to the feature order in `app.py`.

If you change anything non-trivial, add a short note in README.md describing how to run the changed flow (e.g., updated Docker ports, different model filename).

If anything above is unclear or you want stricter guardrails (tests, pinned deps, CI), tell me which area to expand and I will iterate.
