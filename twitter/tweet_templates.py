def format_match_start(player1, player2, tournament):

    return (
        f"🎾 {tournament}\n\n"
        f"{player1} vs {player2}\n\n"
        f"Match started."
    )


def format_set_update(player1, player2, set_score):

    return (
        f"🎾 LIVE UPDATE\n\n"
        f"{player1} vs {player2}\n"
        f"{set_score}"
    )


def format_final(player1, player2, score):

    return (
        f"🏆 FINAL\n\n"
        f"{player1} def. {player2}\n"
        f"{score}"
    )