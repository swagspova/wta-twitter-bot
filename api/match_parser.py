def parse_matches(data):

    if not data or "result" not in data:
        print("No matches found")
        return

    matches = data["result"]

    for match in matches:

        event = match.get("event_name", "Unknown Event")

        player1 = match.get("event_first_player", "Player 1")
        player2 = match.get("event_second_player", "Player 2")

        score = match.get("event_final_result", "No Score")

        status = match.get("event_status", "Unknown")

        print("\n🎾 LIVE WTA MATCH\n")
        print("=" * 40)
        print(f"Tournament: {event}")
        print(f"{player1} vs {player2}")
        print(f"Score: {score}")
        print(f"Status: {status}")