# scripts/first_breath_cli.py
import json
import sys
from src.bridge.resonance_evaluator import analyze_conversation

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python first_breath_cli.py path/to/conversation.json")
        sys.exit(1)

    filepath = sys.argv[1]
    with open(filepath, "r", encoding="utf-8") as f:
        messages = json.load(f)

    evaluator = analyze_conversation(messages)
    result = evaluator.evaluate()
    print(json.dumps(result, indent=2))
