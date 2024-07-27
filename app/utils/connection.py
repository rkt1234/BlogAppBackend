import psycopg2

def connectToDB():
    print("Connecting to database........")
    USERNAME = "trail_owner"
    PASSWORD = "KC3FnYcO5xBp"

    try:
# Establish the connection
        conn = psycopg2.connect(
        dbname="sample",
        user=USERNAME,
        password=PASSWORD,
        host="ep-blue-scene-a5e7rn2t.us-east-2.aws.neon.tech",
        port="5432",
        sslmode="require"
        )
        print("Connection succeeded")
        return conn

    except Exception as error:
        print(f"Error connecting to the database: {error}")