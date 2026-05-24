from database.match_state import previous_matches


def format_set_scores(scores):

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


def parse_matches(data):

    if not data:
        print("No API response")
        return

    matches = data.get("result", [])

    if len(matches) == 0:
        print("No live WTA matches currently.")
        return

    for match in matches:

        match_id = match.get("event_key")

        player1 = match.get("event_first_player", "Unknown")
        player2 = match.get("event_second_player", "Unknown")

        tournament = match.get(
            "tournament_name",
            "Unknown Tournament"
        )

        status = match.get("event_status", "Unknown")

        game_result = match.get(
            "event_game_result",
            "0 - 0"
        )

        final_result = match.get(
            "event_final_result",
            "0 - 0"
        )

        scores = match.get("scores", [])

        formatted_set_score = format_set_scores(scores)

        current_state = {
            "game_result": game_result,
            "status": status,
            "final_result": final_result,
            "set_score": formatted_set_score
        }

        # NEW MATCH
        if match_id not in previous_matches:

            print("\n🟢 NEW LIVE MATCH")

            print(f"Tournament: {tournament}")

            print(f"{player1} vs {player2}")

            print(f"Set Score: {formatted_set_score}")

            print(f"Game Score: {game_result}")

            print(f"Status: {status}")

            previous_matches[match_id] = current_state

            continue

        previous_state = previous_matches[match_id]

        # SET SCORE CHANGED
        if (
            previous_state["set_score"]
            != formatted_set_score
        ):

            print("\n📈 SET SCORE UPDATE")

            print(f"{player1} vs {player2}")

            print(
                f"Old Set Score: "
                f"{previous_state['set_score']}"
            )

            print(
                f"New Set Score: "
                f"{formatted_set_score}"
            )

        # GAME SCORE CHANGED
        if (
            previous_state["game_result"]
            != game_result
        ):

            print("\n🎾 GAME UPDATE")

            print(f"{player1} vs {player2}")

            print(
                f"Old Game Score: "
                f"{previous_state['game_result']}"
            )

            print(
                f"New Game Score: "
                f"{game_result}"
            )

        # STATUS CHANGED
        if (
            previous_state["status"]
            != status
        ):

            print("\n📢 STATUS UPDATE")

            print(f"{player1} vs {player2}")

            print(
                f"Old Status: "
                f"{previous_state['status']}"
            )

            print(f"New Status: {status}")

        # MATCH FINISHED
        if (
            previous_state["status"] != "Finished"
            and status == "Finished"
        ):

            print("\n🏆 MATCH FINISHED")

            print(f"{player1} def. {player2}")

            print(
                f"Final Set Score: "
                f"{formatted_set_score}"
            )

        previous_matches[match_id] = current_state