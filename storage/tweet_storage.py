from storage.database import get_connection


def initialize_tweet_state(match_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT OR IGNORE INTO tweets (

            match_id,
            start_tweeted,
            final_tweeted,
            last_set_score

        ) VALUES (?, 0, 0, '')
        """,
        (match_id,)
    )

    connection.commit()

    connection.close()


def get_tweet_state(match_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            start_tweeted,
            final_tweeted,
            last_set_score

        FROM tweets

        WHERE match_id = ?
        """,
        (match_id,)
    )

    result = cursor.fetchone()

    connection.close()

    return result


def update_tweet_state(

    match_id,
    start_tweeted,
    final_tweeted,
    last_set_score
):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE tweets

        SET

            start_tweeted = ?,
            final_tweeted = ?,
            last_set_score = ?

        WHERE match_id = ?
        """,
        (
            start_tweeted,
            final_tweeted,
            last_set_score,
            match_id
        )
    )

    connection.commit()

    connection.close()