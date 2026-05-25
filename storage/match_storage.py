from storage.database import get_connection


def save_match_state(

    match_id,
    player1,
    player2,
    tournament,
    status,
    set_score,
    game_score,
    final_result
):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT OR REPLACE INTO matches (

            match_id,
            player1,
            player2,
            tournament,
            status,
            set_score,
            game_score,
            final_result

        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            match_id,
            player1,
            player2,
            tournament,
            status,
            set_score,
            game_score,
            final_result
        )
    )

    connection.commit()

    connection.close()


def get_match_state(match_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            status,
            set_score,
            game_score,
            final_result

        FROM matches

        WHERE match_id = ?
        """,
        (match_id,)
    )

    result = cursor.fetchone()

    connection.close()

    return result