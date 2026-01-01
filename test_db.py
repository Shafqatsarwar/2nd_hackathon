import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = "postgresql://neondb_owner:npg_zhJvIP74aTle@ep-long-waterfall-abcwopjg-pooler.eu-west-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

def test_connection():
    print(f"Testing connection to: {DATABASE_URL.split('@')[-1]}")
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        result = cur.fetchone()
        print(f"✅ Connection successful! Result: {result}")
        cur.close()
        conn.close()
    except Exception as e:
        print(f"❌ Connection failed: {e}")

if __name__ == "__main__":
    test_connection()
