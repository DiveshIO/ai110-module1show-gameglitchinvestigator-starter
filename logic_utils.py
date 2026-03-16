from __future__ import annotations

_DIFFICULTY_RANGES: dict[str, tuple[int, int]] = {
    "Easy": (1, 20),
    "Normal": (1, 100),
    "Hard": (1, 50),
}

_ATTEMPT_LIMITS: dict[str, int] = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}


def get_range_for_difficulty(difficulty: str) -> tuple[int, int]:
    """Return (low, high) inclusive range for a given difficulty."""
    return _DIFFICULTY_RANGES.get(difficulty, (1, 100))


def get_attempt_limit(difficulty: str) -> int:
    """Return max attempts allowed for a given difficulty."""
    return _ATTEMPT_LIMITS.get(difficulty, 8)


def parse_guess(raw: str) -> tuple[bool, int | None, str | None]:
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if not raw:
        return False, None, "Enter a guess."

    try:
        value = int(float(raw)) if "." in raw else int(raw)
    except (ValueError, TypeError):
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess: int, secret: int) -> tuple[str, str]:
    """
    Compare guess to secret and return (outcome, message).

    outcome: "Win" | "Too High" | "Too Low"

    Bug fixed: previous version fell back to string comparison on TypeError,
    causing incorrect ordering (e.g. "9" > "10" evaluates True as strings).
    Both values are now guaranteed int by the caller, so no fallback needed.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int) -> int:
    """
    Update score based on outcome and attempt number.

    Bug fixed: previous version awarded +5 points for "Too High" on even
    attempts, which rewarded wrong guesses inconsistently.
    """
    if outcome == "Win":
        return current_score

    if outcome in ("Too High", "Too Low"):
        return current_score - 5

    return current_score
