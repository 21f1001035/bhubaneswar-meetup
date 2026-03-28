# Student Support Copilot - Case Study Instructions

## Audience
IITM BS workshop participants learning how to use LLMs with Python.

## Case study idea
Build a small **AI copilot for student support** using:
- a fictional program handbook
- a set of incoming student support tickets
- Python + an LLM API

## Why this is a good workshop case
This case is strong for a mixed cohort because it includes:
- **prompting** for beginners
- **structured JSON output** for applied thinking
- **retrieval** for grounded responses
- **evaluation** for intermediate learners

It also feels real without requiring a large backend or a complex framework.

---

## Learning objectives

By the end of the case study, students should be able to:

1. send a prompt from Python to an LLM
2. ask for structured outputs
3. retrieve relevant context from a document
4. draft a response grounded in policy text
5. identify when a human escalation is safer than auto-resolution

---

## Dataset files

### `data/program_handbook.md`
A fictional policy handbook with sections on:
- quiz windows
- late penalties
- regrading
- exam rescheduling
- fee refunds
- technical issues
- office hours
- academic integrity
- certificates
- accessibility and accommodations

### `data/student_support_tickets.jsonl`
A small support inbox with realistic student questions.

### `data/rag_questions.json`
Starter questions for the retrieval demo.

> Note: The dataset is fictional and meant only for classroom use.

---

## Recommended workflow for the session

### Part 1 - Warm-up (10-15 mins)
Run:
```bash
python 01_basic_prompting.py
python 02_prompt_patterns.py
python 03_structured_output.py
```

Discuss:
- what changed when the prompt became more specific
- why JSON output is easier for programs to use

### Part 2 - Retrieval demo (15-20 mins)
Run:
```bash
python 06_rag_simple.py
```

Discuss:
- why the handbook matters
- how retrieval reduces unsupported answers
- why "answer only from context" is useful but not perfect

### Part 3 - Main build (35-45 mins)
Run:
```bash
python 07_case_study_support_copilot.py
```

Students now have a baseline support copilot.

---

## Student task

For each ticket, build a system that produces:

1. `category`
2. `priority`
3. `needs_human_review`
4. `policy_basis`
5. `draft_reply`

### Good output characteristics
A good answer should:
- be polite
- mention the relevant policy
- avoid promising exceptions not in the handbook
- escalate when misconduct, accessibility, or exceptional approval is involved

---

## Beginner track

Beginners should focus on:
- running the scripts
- reading the prompts
- changing the user message
- changing the system instruction
- observing how the response changes

### Beginner success criteria
- They can make one successful LLM call
- They can produce valid JSON
- They can answer one handbook question using retrieval

---

## Intermediate track

Intermediate learners should extend the baseline.

### Suggested tasks
1. improve the prompt so the reply is shorter and more consistent
2. add validation checks after parsing JSON
3. attach chunk ids or short citations to the answer
4. compare two models on the same ticket
5. detect cases that should always go to a human reviewer
6. create a simple evaluation sheet for 5 tickets

### Intermediate success criteria
- They improve reliability, not just style
- They can explain why retrieval matters
- They can identify failure modes

---

## Suggested categories

You may use categories like:
- quiz issue
- assignment issue
- regrading
- exam reschedule
- refund
- technical issue
- academic integrity
- accessibility/accommodation
- routine doubt
- certificate/completion

Students do not need to use exactly these labels, but labels should be consistent.

---

## Suggested priority rubric

### Low
Routine question, no urgent loss or escalation risk

### Medium
Deadline impact or important learner action required

### High
Serious escalation, policy exception, academic integrity, accessibility, or missed exam with evidence

---

## Facilitator prompts for discussion

- If the LLM gives a polished answer that is not in policy, is that a good answer?
- Should a support bot answer academic integrity complaints automatically?
- When should an AI system stop and ask for human review?
- What is the difference between memory and retrieval here?

---

## Sample extension ideas

### Extension A - Add confidence
Ask the model to produce:
- confidence score
- reason for low confidence

### Extension B - Add evaluation
Create a small gold set with expected category + escalation decision.

### Extension C - Better retrieval
Swap TF-IDF retrieval with embeddings.

### Extension D - Frontend
Wrap the system in Streamlit.

---

## Common failure modes

1. **Hallucinated policy**
   - Fix: force answers to cite retrieved text

2. **Overconfident promises**
   - Fix: explicitly say "do not promise exceptions outside policy"

3. **Wrong routing**
   - Fix: add human-review rules for sensitive cases

4. **Inconsistent JSON**
   - Fix: validate and retry

5. **Weak retrieval**
   - Fix: tune chunk size and top-k

---

## Deliverable for student teams

Each team should submit:
- updated Python code
- one screenshot or terminal output
- 2 example tickets with outputs
- a short note on one limitation of their solution

---

## Closing message for participants

You did not just "call an API".
You combined:
- prompting
- output design
- retrieval
- policy grounding
- decision-making

That combination is what turns an LLM demo into a usable application.
