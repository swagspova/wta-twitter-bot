from database.match_state import previous_matches
from database.tweet_state import tweeted_events

from twitter.twitter_client import send_tweet

from twitter.tweet_templates import (
    format_match_start,
    format_set_update,
    format_final
)

import time


def format_set_scores(scores):

    """
    Convert API set-score array into readable format.

    Example:
    6-4 | 3-6 | 2-1
    """

    if not scores:
        return "No Set Scores"

    formatted_scores = []

    for set_data in scores:

        score_first = set_data.get("score_first", "0")
        score_second = set_data.get("score_second", "0")

        formatted_scores.append(
            f"{score_first}-{score_second}"
        )

    return " | ".join(formatted_scores)


def initialize_tweet_state(match_id):

    """
    Create initial tweet-tracking structure
    for each match.
    """

    if match_id not in tweeted_events:

        tweeted_events[match_id] = {
            "start": False,
            "final": False,
            "last_set": ""
        }


def print_match_header(title):

    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


def parse_matches(data):

    """
    Main monitoring + event detection engine.
    """

    if not data:

        print("No API response")
        return

    matches = data.get("result", [])

    if len(matches) == 0:

        print("No live WTA matches currently.")
        return

    for match in matches:

        try:

            # =========================================
            # MATCH DATA
            # =========================================

            match_id = str(
                match.get("event_key")
            )

            tournament = match.get(
                "tournament_name",
                "Unknown Tournament"
            )

            player1 = match.get(
                "event_first_player",
                "Unknown Player"
            )

            player2 = match.get(
                "event_second_player",
                "Unknown Player"
            )

            status = match.get(
                "event_status",
                "Unknown"
            )

            live = match.get(
                "event_live",
                "0"
            )

            game_result = match.get(
                "event_game_result",
                "0 - 0"
            )

            final_result = match.get(
                "event_final_result",
                "0 - 0"
            )

            scores = match.get(
                "scores",
                []
            )

            formatted_set_score = (
                format_set_scores(scores)
            )

            # =========================================
            # CURRENT MATCH STATE
            # =========================================

            current_state = {
                "game_result": game_result,
                "status": status,
                "final_result": final_result,
                "set_score": formatted_set_score
            }

            # =========================================
            # INITIALIZE TWEET TRACKING
            # =========================================

            initialize_tweet_state(match_id)

            # =========================================
            # NEW MATCH DETECTED
            # =========================================

            if match_id not in previous_matches:

                print_match_header(
                    "🟢 NEW LIVE MATCH"
                )

                print(
                    f"Tournament: {tournament}"
                )

                print(
                    f"{player1} vs {player2}"
                )

                print(
                    f"Set Score: "
                    f"{formatted_set_score}"
                )

                print(
                    f"Game Score: "
                    f"{game_result}"
                )

                print(
                    f"Status: {status}"
                )

                # -----------------------------
                # SEND MATCH START TWEET
                # -----------------------------

                if not tweeted_events[
                    match_id
                ]["start"]:

                    tweet = format_match_start(
                        player1,
                        player2,
                        tournament
                    )

                    response = send_tweet(
                        tweet
                    )

                    if response:

                        print(
                            "✅ Match start "
                            "tweet sent"
                        )

                        tweeted_events[
                            match_id
                        ]["start"] = True

                previous_matches[
                    match_id
                ] = current_state

                time.sleep(1)

                continue

            # =========================================
            # PREVIOUS STATE
            # =========================================

            previous_state = previous_matches[
                match_id
            ]

            # =========================================
            # SET SCORE UPDATE
            # =========================================

            if (
                previous_state["set_score"]
                != formatted_set_score
            ):

                print_match_header(
                    "📈 SET SCORE UPDATE"
                )

                print(
                    f"{player1} vs {player2}"
                )

                print(
                    "Old Set Score: "
                    f"{previous_state['set_score']}"
                )

                print(
                    "New Set Score: "
                    f"{formatted_set_score}"
                )

                # -----------------------------
                # SEND SET UPDATE TWEET
                # -----------------------------

                if (
                    tweeted_events[match_id][
                        "last_set"
                    ]
                    != formatted_set_score
                ):

                    tweet = format_set_update(
                        player1,
                        player2,
                        formatted_set_score
                    )

                    response = send_tweet(
                        tweet
                    )

                    if response:

                        print(
                            "✅ Set update "
                            "tweet sent"
                        )

                        tweeted_events[
                            match_id
                        ][
                            "last_set"
                        ] = (
                            formatted_set_score
                        )

            # =========================================
            # GAME SCORE UPDATE
            # =========================================

            if (
                previous_state["game_result"]
                != game_result
            ):

                print_match_header(
                    "🎾 GAME UPDATE"
                )

                print(
                    f"{player1} vs {player2}"
                )

                print(
                    "Old Game Score: "
                    f"{previous_state['game_result']}"
                )

                print(
                    "New Game Score: "
                    f"{game_result}"
                )

            # =========================================
            # STATUS UPDATE
            # =========================================

            if (
                previous_state["status"]
                != status
            ):

                print_match_header(
                    "📢 STATUS UPDATE"
                )

                print(
                    f"{player1} vs {player2}"
                )

                print(
                    "Old Status: "
                    f"{previous_state['status']}"
                )

                print(
                    f"New Status: {status}"
                )

            # =========================================
            # MATCH FINISHED
            # =========================================

            if (
                previous_state["status"]
                != "Finished"
                and status == "Finished"
                and not tweeted_events[
                    match_id
                ]["final"]
            ):

                print_match_header(
                    "🏆 MATCH FINISHED"
                )

                print(
                    f"{player1} def. {player2}"
                )

                print(
                    "Final Set Score: "
                    f"{formatted_set_score}"
                )

                # -----------------------------
                # SEND FINAL TWEET
                # -----------------------------

                tweet = format_final(
                    player1,
                    player2,
                    formatted_set_score
                )

                response = send_tweet(
                    tweet
                )

                if response:

                    print(
                        "✅ Final result "
                        "tweet sent"
                    )

                    tweeted_events[
                        match_id
                    ]["final"] = True

            # =========================================
            # SAVE UPDATED STATE
            # =========================================

            previous_matches[
                match_id
            ] = current_state

            # =========================================
            # RATE LIMIT SAFETY
            # =========================================

            time.sleep(1)

        except Exception as e:

            print(
                "❌ Error parsing match:"
            )

            print(e)