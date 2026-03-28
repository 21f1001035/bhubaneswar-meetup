# Exercise 3 - Structured Outputs

## Goal
Make the model return JSON that code can use directly.

## Tasks
1. Run `python 03_structured_output.py`
2. Modify the schema and add:
   - `urgency_reason`
   - `suggested_next_step`
3. Feed a different support ticket
4. Validate whether the JSON still parses

## Beginner version
Only change the ticket text and observe the output.

## Intermediate version
Add Python validation rules:
- `priority` must be one of `low`, `medium`, `high`
- `needs_human_review` must be boolean
