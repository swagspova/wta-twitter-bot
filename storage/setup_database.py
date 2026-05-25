from storage.database import get_connection


def create_tables():

    connection = get_connection()

    cursor = connection.cursor()

    # =====================================
    # MATCH STATE TABLE
    # =====================================

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS matches (

            match_id TEXT PRIMARY KEY,

            player1 TEXT,
            player2 TEXT,

            tournament TEXT,

            status TEXT,

            set_score TEXT,

            game_score TEXT,

            final_result TEXT,

            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    # =====================================
    # TWEET TRACKING TABLE
    # =====================================

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tweets (

            match_id TEXT PRIMARY KEY,

            start_tweeted INTEGER DEFAULT 0,

            final_tweeted INTEGER DEFAULT 0,

            last_set_score TEXT
        )
        """
    )

    connection.commit()

    connection.close()

    print("✅ Database tables created")


if __name__ == "__main__":

    create_tables()