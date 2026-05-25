def format_match_start(
    player1,
    player2,
    tournament
):

    """
    Tweet format for match start.
    """

    return (
        f"🎾 {tournament}\n\n"
        f"{player1} vs {player2}\n\n"
        f"Match underway."
    )


def format_set_update(
    player1,
    player2,
    set_score,
    tournament
):

    """
    Tweet format for live set updates.
    """

    return (
        f"🎾 {tournament} — LIVE\n\n"
        f"{player1} vs {player2}\n\n"
        f"Set Score:\n"
        f"{set_score}"
    )


def format_game_update(
    player1,
    player2,
    set_score,
    game_score,
    tournament=None
):

    """
    Tweet format for point/game updates.
    """

    if tournament:

        return (
            f"🎾 {tournament} — LIVE\n\n"
            f"{player1} vs {player2}\n\n"
            f"Set Score: {set_score}\n"
            f"Game Score: {game_score}"
        )

    return (
        f"🎾 GAME UPDATE\n\n"
        f"{player1} vs {player2}\n\n"
        f"Set Score: {set_score}\n"
        f"Game Score: {game_score}"
    )


def format_final(
    player1,
    player2,
    final_score,
    tournament=None
):

    """
    Tweet format for completed matches.
    """

    if tournament:

        return (
            f"🏆 FINAL — {tournament}\n\n"
            f"{player1} def. {player2}\n\n"
            f"{final_score}"
        )

    return (
        f"🏆 FINAL\n\n"
        f"{player1} def. {player2}\n\n"
        f"{final_score}"
    )


def format_retirement(
    player1,
    player2,
    score,
    retired_player,
    tournament=None
):

    """
    Tweet format for retirements.
    """

    if tournament:

        return (
            f"⚠️ RETIREMENT — {tournament}\n\n"
            f"{player1} vs {player2}\n\n"
            f"{retired_player} retired.\n"
            f"Score: {score}"
        )

    return (
        f"⚠️ RETIREMENT\n\n"
        f"{player1} vs {player2}\n\n"
        f"{retired_player} retired.\n"
        f"Score: {score}"
    )


def format_walkover(
    player1,
    player2,
    winner,
    tournament=None
):

    """
    Tweet format for walkovers.
    """

    if tournament:

        return (
            f"🚫 WALKOVER — {tournament}\n\n"
            f"{winner} advances.\n\n"
            f"{player1} vs {player2}"
        )

    return (
        f"🚫 WALKOVER\n\n"
        f"{winner} advances.\n\n"
        f"{player1} vs {player2}"
    )


def format_rain_delay(
    player1,
    player2,
    tournament=None
):

    """
    Tweet format for delays/suspensions.
    """

    if tournament:

        return (
            f"🌧️ MATCH DELAY — {tournament}\n\n"
            f"{player1} vs {player2}\n\n"
            f"Play temporarily suspended."
        )

    return (
        f"🌧️ MATCH DELAY\n\n"
        f"{player1} vs {player2}\n\n"
        f"Play temporarily suspended."
    )