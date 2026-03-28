# Bonus Extensions

## Option A - Better support copilot
Improve `07_case_study_support_copilot.py` so it:
- adds confidence scores
- writes cleaner markdown reports
- flags policy gaps

## Option B - Small evaluator
Create 5 expected answers and compare model outputs manually.

## Option C - Mini UI
Build a simple Streamlit app:
- text input for student ticket
- model output on the right
- retrieved policy chunk shown below

## Option D - Embeddings version
Replace TF-IDF with embeddings + cosine similarity.

## Option E - Guardrails
Add validation so the reply must:
- mention policy
- avoid promises outside policy
- mention escalation when required
