# Harnessing LLMs with Python - IITM BS Workshop

A hands-on workshop repo for a 2.5-3 hour session on using Large Language Models (LLMs) with Python.

This repo is designed for mixed-skill participants:
- **Beginners** can run and modify ready-made scripts.
- **Intermediate learners** can extend the scripts into a working mini application.

## What participants will learn

1. What an LLM is in practical terms
2. How to call an LLM from Python
3. How prompt design changes output quality
4. How to ask for structured JSON outputs
5. How chat memory works
6. How retrieval-augmented generation (RAG) works with a small knowledge base
7. How to build a simple **Student Support Copilot** case study

## Workshop flow

| Part | Focus | Files |
|---|---|---|
| 1 | First API call | `01_basic_prompting.py` |
| 2 | Prompt patterns | `02_prompt_patterns.py` |
| 3 | Structured outputs | `03_structured_output.py` |
| 4 | Compare models | `04_model_compare.py` |
| 5 | Chat memory | `05_chat_memory.py` |
| 6 | Simple RAG | `06_rag_simple.py` |
| 7 | Full case study | `07_case_study_support_copilot.py` |

## Repo structure

```text
21f1001035/
├── 01_basic_prompting.py
├── 02_prompt_patterns.py
├── 03_structured_output.py
├── 04_model_compare.py
├── 05_chat_memory.py
├── 06_rag_simple.py
├── 07_case_study_support_copilot.py
├── workshop_client.py
├── rag_utils.py
├── requirements.txt
├── .env.example
├── README.md
├── case_study/
│   ├── Student_Support_Copilot_Instructions.pdf
│   └── Student_Support_Copilot_Instructions.md
├── data/
│   ├── program_handbook.md
│   ├── student_support_tickets.jsonl
│   ├── rag_questions.json
│   └── sample_passage.txt
└── exercises/
    ├── 01_setup_and_first_call.md
    ├── 02_prompting_exercises.md
    ├── 03_structured_output_exercises.md
    ├── 04_model_compare_exercises.md
    ├── 05_chat_memory_exercises.md
    ├── 06_rag_case_study.md
    └── 07_bonus_extensions.md
```

## You do NOT need a paid API key

This workshop works with **free** LLM providers. No credit card required.

| Provider | Free? | Sign-up link | Models you get |
|----------|-------|-------------|----------------|
| **Groq** (recommended) | Yes | [console.groq.com](https://console.groq.com) | Llama 3.3 70B, Gemma 2, Mixtral |
| **Google AI Studio** | Yes | [aistudio.google.com/apikey](https://aistudio.google.com/apikey) | Gemini 2.0 Flash, Gemini 1.5 |
| **GitHub Models** | Yes | [github.com/settings/tokens](https://github.com/settings/tokens) | GPT-4o-mini, Llama, Mistral |
| **OpenRouter** | Partially | [openrouter.ai](https://openrouter.ai) | Various open-source models |
| **OpenAI** | No (paid) | [platform.openai.com](https://platform.openai.com) | GPT-4o, GPT-4o-mini |

All of these work with the same workshop code — you just change 2-3 lines in a config file.

## Quick start

### Step 1: Create a virtual environment

**On Mac/Linux:**
```bash
python -m venv .venv
source .venv/bin/activate
```

**On Windows PowerShell:**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Get a free API key

We recommend **Groq** — it is fast, free, and takes under a minute to set up:

1. Go to [console.groq.com](https://console.groq.com) and sign up (Google/GitHub login works)
2. Go to **API Keys** → **Create API Key**
3. Copy the key (starts with `gsk_`)

### Step 4: Create your `.env` file

```bash
cp .env.example .env
```

Open the `.env` file and replace the bottom section with your provider's values.

**Example `.env` for Groq (free):**
```
OPENAI_API_KEY=gsk_paste_your_groq_key_here
OPENAI_BASE_URL=https://api.groq.com/openai/v1
MODEL=llama-3.3-70b-versatile
TEMPERATURE=0.2
```

**Example `.env` for Google AI Studio (free):**
```
OPENAI_API_KEY=paste_your_google_ai_key_here
OPENAI_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/
MODEL=gemini-2.0-flash
TEMPERATURE=0.2
```

**Example `.env` for OpenAI (paid):**
```
OPENAI_API_KEY=sk-paste_your_openai_key_here
MODEL=gpt-4o-mini
TEMPERATURE=0.2
```

> **Tip:** The `.env.example` file has all provider configs with sign-up links. Just pick one.

### Step 5: Run the scripts

```bash
python 01_basic_prompting.py
python 02_prompt_patterns.py
python 03_structured_output.py
python 04_model_compare.py
python 05_chat_memory.py
python 06_rag_simple.py
python 07_case_study_support_copilot.py
```

## Suggested facilitation strategy

### For beginners
- Start from `01_basic_prompting.py`
- Let them change the prompt
- Then move to `03_structured_output.py`
- Then run `06_rag_simple.py`

### For intermediate learners
- Ask them to:
  - add error handling
  - improve the JSON schema
  - improve the retrieval strategy
  - compare multiple models
  - make the case study output more reliable

## Case study: Student Support Copilot

Participants act as builders for a fictional online program helpdesk assistant.

### Inputs
- A small **policy handbook**
- A set of incoming **student support tickets**

### Goal
For each ticket, build a copilot that:
1. identifies the issue category
2. assigns a priority
3. retrieves the relevant policy section
4. drafts a clear response
5. notes when human escalation is required

## Important note about the dataset

The dataset in this repo is **fictional and created for teaching purposes**. It is inspired by common online-learning support workflows, but it does **not** represent the real IITM BS program policies.

## Teaching notes

### Conceptual topics to explain briefly
- Tokens
- Context window
- Temperature
- System vs user messages
- Hallucinations
- Structured output
- Retrieval vs memory vs fine-tuning

### What not to overdo
- Transformer math
- Attention equations
- Too many frameworks at once
- Complex vector databases for a first workshop

## Minimal discussion prompts for the room

- When is an LLM enough by itself?
- When do we need retrieval?
- Why do structured outputs matter in real systems?
- Why is evaluation harder than the demo?

## Troubleshooting

### `401 Unauthorized`
Your API key is missing or invalid.

### `ModuleNotFoundError`
Run:

```bash
pip install -r requirements.txt
```

### Model not found
Set `MODEL` in `.env` to a model available on your provider.

## Stretch ideas

- Build a Streamlit UI
- Add confidence scores
- Log prompts and outputs
- Run a small evaluation set
- Swap TF-IDF retrieval with embeddings
- Add citations to the final answer

## License

You can adapt this repo freely for teaching and workshop use.
