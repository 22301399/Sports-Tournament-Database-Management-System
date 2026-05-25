"""
Sports Tournament Database Management System
DB Connection Configuration
"""

import psycopg2
import psycopg2.extras
import os

# ──────────────────────────────────────────────
# DATABASE CONFIGURATION
# Replace with your cloud DB credentials
# Supported: Railway, Render, Supabase, etc.
# ──────────────────────────────────────────────

DB_CONFIG = {
    "host":     os.getenv("DB_HOST",     "your-cloud-db-host.railway.app"),
    "port":     os.getenv("DB_PORT",     "5432"),
    "database": os.getenv("DB_NAME",     "sports_tournament"),
    "user":     os.getenv("DB_USER",     "postgres"),
    "password": os.getenv("DB_PASSWORD", "your_password_here"),
}


def get_connection():
    """Return a new database connection."""
    return psycopg2.connect(**DB_CONFIG)


def execute_query(query: str, params=None, fetch: bool = True):
    """
    Execute a SELECT query and return results as list of dicts.
    """
    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(query, params)
            if fetch:
                return [dict(row) for row in cur.fetchall()]
            conn.commit()
            return cur.rowcount
    finally:
        conn.close()


def execute_write(query: str, params=None):
    """
    Execute INSERT / UPDATE / DELETE.
    Returns the number of affected rows.
    """
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(query, params)
            conn.commit()
            return cur.rowcount
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()


def execute_returning(query: str, params=None):
    """
    Execute INSERT ... RETURNING id and return the new row id.
    """
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(query, params)
            result = cur.fetchone()
            conn.commit()
            return result[0] if result else None
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()
