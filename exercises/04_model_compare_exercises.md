# Exercise 4 - Compare Models

## Goal
Observe differences across models.

## Tasks
1. Run with your default model:
   ```bash
   python 04_model_compare.py
   ```
2. Compare multiple models from your provider. Examples by provider:

   **Groq (free):**
   ```bash
   python 04_model_compare.py --models llama-3.3-70b-versatile llama-3.1-8b-instant gemma2-9b-it
   ```

   **Google AI Studio (free):**
   ```bash
   python 04_model_compare.py --models gemini-2.0-flash gemini-1.5-flash
   ```

   **GitHub Models (free):**
   ```bash
   python 04_model_compare.py --models gpt-4o-mini Mistral-small
   ```

   **OpenAI (paid):**
   ```bash
   python 04_model_compare.py --models gpt-4o-mini gpt-4o
   ```

3. Evaluate on:
   - clarity
   - length
   - helpfulness
   - accuracy to instructions

## Discussion
Bigger is not always better. When might a cheaper model be enough?
