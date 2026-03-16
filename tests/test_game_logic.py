from logic_utils import check_guess, update_score, parse_guess


# ---------------------------------------------------------------------------
# check_guess  (FIXME: "Logic breaks here" in app.py)
# The original bug: on TypeError it fell back to string comparison, so
# single-digit vs multi-digit comparisons like 9 vs 10 were wrong
# ("9" > "10" is True as strings → wrongly returned "Too High").
# ---------------------------------------------------------------------------

def test_check_guess_win():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_check_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_check_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_check_guess_string_comparison_bug():
    # Bug: old code compared str(9) > str(10) → "9" > "10" → True → "Too High" (wrong).
    # Correct integer comparison: 9 < 10 → "Too Low".
    outcome, _ = check_guess(9, 10)
    assert outcome == "Too Low"


# ---------------------------------------------------------------------------
# update_score  (FIXME: "The score was going negative" in app.py)
# The original bug: "Too High" on even attempt numbers awarded +5 instead
# of deducting -5, inconsistently rewarding wrong guesses.
# ---------------------------------------------------------------------------

def test_update_score_win_keeps_score():
    # Win should preserve the current score — not add a bonus on top.
    # Bug: old code did current_score + points, so 75 + 30 = 105 instead of 75.
    new_score = update_score(75, "Win", attempt_number=5)
    assert new_score == 75

def test_update_score_too_high_deducts():
    # Bug: even attempt numbers used to give +5 (score went UP on a wrong guess).
    # Fixed: always deducts 5 regardless of attempt parity.
    new_score = update_score(100, "Too High", attempt_number=2)  # even attempt
    assert new_score == 95

def test_update_score_too_low_deducts():
    new_score = update_score(100, "Too Low", attempt_number=1)
    assert new_score == 95

def test_update_score_too_high_odd_attempt_deducts():
    # Odd attempt should also deduct (was already deducting before the fix).
    new_score = update_score(100, "Too High", attempt_number=3)
    assert new_score == 95


# ---------------------------------------------------------------------------
# parse_guess  (robustness — supports the fixed check_guess downstream)
# ---------------------------------------------------------------------------

def test_parse_guess_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_guess_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None

def test_parse_guess_none():
    ok, value, err = parse_guess(None)
    assert ok is False

def test_parse_guess_non_number():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert "number" in err.lower()

def test_parse_guess_decimal_truncates():
    # "7.9" should parse as 7 (int truncation), not fail.
    ok, value, err = parse_guess("7.9")
    assert ok is True
    assert value == 7
