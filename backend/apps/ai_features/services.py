from dataclasses import dataclass


@dataclass
class ModerationResult:
    is_toxic: bool
    score: float


def detect_toxic_text(text: str) -> ModerationResult:
    banned = {"abuse", "hate", "threat"}
    lowered = text.lower()
    hits = sum(1 for word in banned if word in lowered)
    score = min(1.0, hits * 0.35)
    return ModerationResult(is_toxic=score >= 0.7, score=score)


def compatibility_score(user_a_interests: list[str], user_b_interests: list[str]) -> float:
    if not user_a_interests or not user_b_interests:
        return 0.4
    a = set(user_a_interests)
    b = set(user_b_interests)
    overlap = len(a.intersection(b))
    return round(overlap / max(len(a.union(b)), 1), 2)
