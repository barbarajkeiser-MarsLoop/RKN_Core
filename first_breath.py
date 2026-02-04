"""
First Breath: Resonance Evaluator CLI / Library

From Resonance-Protocol — simplified starting point.
Run on conversation JSON to get a truth/resonance score.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class ResonanceEvaluator:
    """Core evaluator class — will grow with real NLP/embeddings later."""

    session_id: str = "first_breath"
    question_evolution: List[str] = field(default_factory=list)
    execution_evidence: List[str] = field(default_factory=list)
    concept_integration: List[str] = field(default_factory=list)
    challenges_extensions: List[str] = field(default_factory=list)
    transformation_markers: List[str] = field(default_factory=list)

    def evaluate(self) -> Dict[str, Any]:
        scores = {
            "question_evolution": 1 if len(self.question_evolution) >= 3 else 0,
            "execution_evidence": 1 if len(self.execution_evidence) > 0 else 0,
            "concept_integration": 1 if len(self.concept_integration) > 0 else 0,
            "challenge_extension": 1 if len(self.challenges_extensions) > 0 else 0,
            "transformation": 1 if len(self.transformation_markers) > 0 else 0,
        }

        total = sum(scores.values())

        interpretations = {
            0: "Consumption - No evidence of application",
            1: "Minimal Engagement",
            2: "Engagement - Building understanding",
            3: "Active Learning - Some integration",
            4: "Resonance - Learning + execution",
            5: "Deep Resonance - Transformation observable",
        }

        return {
            "session_id": self.session_id,
            "resonance_score": total,
            "breakdown": scores,
            "interpretation": interpretations.get(total, "Unknown score"),
            "qualifies_for_compensation": total >= 4,
        }


def analyze_conversation(messages: List[Dict[str, Any]]) -> ResonanceEvaluator:
    """
    Basic heuristic analysis — placeholder for future ML-enhanced version.
    Expects messages in format: [{'role': 'user'|'assistant', 'content': str}, ...]
    """
    evaluator = ResonanceEvaluator(session_id=f"analysis_{len(messages)}_msgs")

    # Question evolution
    questions = [m for m in messages if m.get("role") == "user" and "?" in m.get("content", "")]
    if len(questions) >= 3:
        evaluator.question_evolution = [f"Q{i+1}: {q['content'][:60]}..." for i, q in enumerate(questions[:5])]

    # Execution evidence (simple keyword match)
    execution_keywords = {"created", "built", "implemented", "tested", "deployed", "wrote", "coded", "made"}
    for m in messages:
        if m.get("role") == "user":
            content_lower = m.get("content", "").lower()
            if any(kw in content_lower for kw in execution_keywords):
                evaluator.execution_evidence.append(m["content"][:100] + ("..." if len(m["content"]) > 100 else ""))

    # Concept integration (placeholder — improve later)
    if len(messages) > 8:
        evaluator.concept_integration.append("Conversation length suggests potential integration")

    # Challenges / extensions
    challenge_keywords = {"but", "what if", "however", "alternatively", "disagree", "challenge"}
    for m in messages:
        if m.get("role") == "user":
            content_lower = m.get("content", "").lower()
            if any(kw in content_lower for kw in challenge_keywords):
                evaluator.challenges_extensions.append(m["content"][:100] + "...")

    # Transformation markers (placeholder)
    if len(messages) > 15:
        evaluator.transformation_markers.append("Extended interaction — potential before/after shift")

    return evaluator
