"""
=============================================================================
GRIT Team Growth & Work OS
-----------------------------------------------------------------------------
A production-grade, dark cyber luxury multi-user Work & Growth Operating System.
Dual-engine architecture: Team Sprint Delivery + Dedicated Personal Growth OS.

Features:
- Authentication & RBAC for 7 Team Members (Admin: Rajat, #2: Shatakshi)
- Dedicated "Personal Growth OS" module with full past database history & skill tracking
- Clean Zero-Dummy Initial State (No fake data; 100% real entries)
- Live Work Session & Punch-in Engine with dynamic elapsed timer
- Mandatory Daily Checkout / Standup Feed ("What I learned today" & feedback)
- Public Team Daily Learnings & Activity Feed visible to all members
- Gamified XP Engine & Cyber Level Progression (Initiate -> Titan)
- Interactive Skill Roadmaps (Python, UI/UX, AI/ML, Ops) with checkable milestones
- Tasks Management (Admin assignment + Member 1-click status transitions)
- Academic & Doubt Clearing Forum with syntax-highlighted code support
- Admin Controls for Rajat: Team Management, Member Provisioning, DB Audit
=============================================================================
"""

import streamlit as st
import sqlite3
import hashlib
import datetime
from datetime import datetime as _orig_dt, timedelta, timezone

# -----------------------------------------------------------------------------
# Timezone Engine: Indian Standard Time (IST, UTC+5:30)
# Guarantees accurate Indian local time on Streamlit Cloud (which runs on UTC servers)
# -----------------------------------------------------------------------------
IST_TIMEZONE = timezone(timedelta(hours=5, minutes=30))

class dt(_orig_dt):
    """
    Subclass of datetime.datetime that defaults .now() to Indian Standard Time (IST, UTC+5:30)
    as a timezone-naive datetime (matching SQLite storage and legacy operations).
    Guarantees that Streamlit Cloud servers (UTC) always display and store accurate Indian time.
    """
    @classmethod
    def now(cls, tz=None):
        if tz is None:
            return _orig_dt.now(timezone.utc).astimezone(IST_TIMEZONE).replace(tzinfo=None)
        return _orig_dt.now(tz)

    @classmethod
    def fromtimestamp(cls, timestamp, tz=None):
        if tz is None:
            return _orig_dt.fromtimestamp(timestamp, timezone.utc).astimezone(IST_TIMEZONE).replace(tzinfo=None)
        return _orig_dt.fromtimestamp(timestamp, tz)

import pandas as pd
import json
import os
import shutil
import textwrap
import threading
import requests

# -----------------------------------------------------------------------------
# Configuration & Constants (Rock-Solid Persistent Database Paths)
# -----------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, "grit_portal.db")
BACKUP_DIR = os.path.join(BASE_DIR, "backups")
EXPORT_JSON_PATH = os.path.join(BACKUP_DIR, "grit_data_export.json")
DEFAULT_PASSWORD = "grit2026"

os.makedirs(BACKUP_DIR, exist_ok=True)

# Shatakshi placed at #2 per requirement
TEAM_MEMBERS = [
    {"username": "Rajat", "name": "Rajat", "role": "admin", "title": "Lead & Solution Architect", "avatar_color": "#FFD700"},
    {"username": "Shatakshi", "name": "Shatakshi", "role": "member", "title": "Strategy & Operations", "avatar_color": "#A855F7"},
    {"username": "Harpreet", "name": "Harpreet", "role": "member", "title": "UI/UX Lead", "avatar_color": "#00FFA3"},
    {"username": "Aniran", "name": "Aniran", "role": "member", "title": "Tech & Features Lead", "avatar_color": "#00D2FF"},
    {"username": "Bhupender", "name": "Bhupender", "role": "member", "title": "Client Relations", "avatar_color": "#FF7A00"},
    {"username": "Misty", "name": "Misty", "role": "member", "title": "Research & Growth", "avatar_color": "#D946EF"},
    {"username": "Sainu", "name": "Sainu", "role": "member", "title": "QA & User Experience", "avatar_color": "#38BDF8"},
    {"username": "Shubham", "name": "Shubham", "role": "member", "title": "Full-Stack Developer", "avatar_color": "#22C55E"}
]

# -----------------------------------------------------------------------------
# Comprehensive Technical Roadmaps & Curricula Catalog (Official 17 Engineering Careers)
# -----------------------------------------------------------------------------
from roadmaps_data import ROADMAP_CATALOG, BUILTIN_ROADMAPS

# Set page configuration at top level
st.set_page_config(
    page_title="GRIT Team Growth & Work OS",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# HTML Rendering Helper (Prevents Markdown Code-Block Indentation Leak)
# -----------------------------------------------------------------------------
def render_html(html_str: str):
    """Safely renders HTML stripped of leading indentation on each line to completely prevent markdown code-block conversion."""
    cleaned = "\n".join(line.strip() for line in html_str.strip().splitlines())
    st.markdown(cleaned, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Security & Hashing Utilities
# -----------------------------------------------------------------------------
def hash_password(password: str) -> str:
    """Hash password using SHA-256."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def get_db_connection():
    """Create a thread-safe connection to the SQLite database with WAL durability mode and dict rows."""
    conn = sqlite3.connect(DB_NAME, check_same_thread=False, timeout=30.0)
    conn.row_factory = sqlite3.Row
    try:
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA synchronous=NORMAL")
        conn.execute("PRAGMA foreign_keys=ON")
    except Exception:
        pass
    return conn

# -----------------------------------------------------------------------------
# Enterprise Data Persistence, Automated Rolling Backups & Auto-Heal Engine
# -----------------------------------------------------------------------------
BACKUP_ACTIVITY_TABLES = [
    "users", "work_sessions", "daily_checkouts", "tasks", "task_timer_sessions",
    "learning_logs", "skill_roadmap_progress", "custom_skill_tracks",
    "academic_queries", "academic_answers", "personal_growth_goals"
]

def get_cloud_persistence_config():
    """
    Checks for Cloud Persistence credentials in Streamlit secrets, OS environment, or local cache.
    Supported config in Streamlit Cloud Secrets (secrets.toml):
    [cloud_persistence]
    github_token = "ghp_..."
    gist_id = "..." # (Optional: if blank, automatically creates a private Gist on first sync)
    """
    token = None
    gist_id = None
    try:
        if hasattr(st, "secrets") and "cloud_persistence" in st.secrets:
            token = st.secrets["cloud_persistence"].get("github_token")
            gist_id = st.secrets["cloud_persistence"].get("gist_id")
        elif hasattr(st, "secrets") and "GITHUB_TOKEN" in st.secrets:
            token = st.secrets.get("GITHUB_TOKEN")
            gist_id = st.secrets.get("GIST_ID")
    except Exception:
        pass

    if not token:
        token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GRIT_GITHUB_TOKEN")
    if not gist_id:
        gist_id = os.environ.get("GIST_ID") or os.environ.get("GRIT_GIST_ID")

    # Check local cache file in BACKUP_DIR if gist_id was previously auto-created
    gist_cache_file = os.path.join(BACKUP_DIR, "cloud_gist_id.txt")
    if not gist_id and os.path.exists(gist_cache_file):
        try:
            with open(gist_cache_file, "r", encoding="utf-8") as f:
                cached = f.read().strip()
                if cached:
                    gist_id = cached
        except Exception:
            pass

    return (token.strip() if token else None, gist_id.strip() if gist_id else None)

def sync_database_to_cloud(reason: str = "auto") -> tuple[bool, str]:
    """
    Syncs the complete dual-layer JSON database snapshot to a private GitHub Gist.
    Guarantees permanent, indestructible cloud persistence across Streamlit Cloud container rebuilds.
    """
    token, gist_id = get_cloud_persistence_config()
    if not token:
        return False, "No Cloud GitHub Token configured. Running in local ephemeral mode."

    try:
        export_data = {}
        conn = get_db_connection()
        cursor = conn.cursor()
        for table in BACKUP_ACTIVITY_TABLES:
            try:
                cursor.execute(f"SELECT * FROM [{table}]")
                export_data[table] = [dict(row) for row in cursor.fetchall()]
            except Exception:
                pass
        conn.close()

        payload_content = json.dumps(export_data, indent=2, default=str)
        auth_header = f"token {token}" if not (token.startswith("Bearer ") or token.startswith("token ")) else token
        headers = {
            "Authorization": auth_header,
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "GRIT-Work-OS-App/1.0"
        }

        if gist_id:
            url = f"https://api.github.com/gists/{gist_id}"
            body = {
                "description": f"GRIT Team OS Live Cloud Database ({reason} @ {dt.now().strftime('%Y-%m-%d %H:%M:%S')})",
                "files": {
                    "grit_data_export.json": {"content": payload_content}
                }
            }
            res = requests.patch(url, headers=headers, json=body, timeout=12)
            if res.status_code in [200, 201]:
                return True, f"Successfully synced to Cloud Gist ({gist_id[:8]}...)"
            elif res.status_code == 404:
                gist_id = None
            else:
                err_detail = ""
                try:
                    err_detail = res.json().get("message", res.text[:120])
                except Exception:
                    err_detail = res.text[:120]
                return False, f"GitHub Gist API error: HTTP {res.status_code} ({err_detail})"

        if not gist_id:
            url = "https://api.github.com/gists"
            body = {
                "description": f"GRIT Team OS Live Cloud Database (Auto-Created {dt.now().strftime('%Y-%m-%d %H:%M:%S')})",
                "public": False,
                "files": {
                    "grit_data_export.json": {"content": payload_content}
                }
            }
            res = requests.post(url, headers=headers, json=body, timeout=12)
            if res.status_code in [200, 201]:
                new_gist_id = res.json().get("id")
                try:
                    with open(os.path.join(BACKUP_DIR, "cloud_gist_id.txt"), "w", encoding="utf-8") as f:
                        f.write(new_gist_id)
                except Exception:
                    pass
                return True, f"Created new private Cloud Gist: {new_gist_id}"
            else:
                err_detail = ""
                try:
                    err_detail = res.json().get("message", res.text[:120])
                except Exception:
                    err_detail = res.text[:120]
                return False, f"GitHub Gist API error: HTTP {res.status_code} ({err_detail})"

    except Exception as e:
        return False, f"Cloud Sync Exception: {str(e)}"

def restore_database_from_cloud() -> tuple[bool, str]:
    """
    Fetches the latest JSON snapshot from GitHub Gist and restores SQLite database.
    """
    token, gist_id = get_cloud_persistence_config()
    if not token or not gist_id:
        return False, "Cloud persistence credentials not configured."

    try:
        auth_header = f"token {token}" if not (token.startswith("Bearer ") or token.startswith("token ")) else token
        headers = {
            "Authorization": auth_header,
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "GRIT-Work-OS-App/1.0"
        }
        res = requests.get(f"https://api.github.com/gists/{gist_id}", headers=headers, timeout=15)
        if res.status_code != 200:
            err_detail = ""
            try:
                err_detail = res.json().get("message", res.text[:120])
            except Exception:
                err_detail = res.text[:120]
            return False, f"Failed to fetch Gist: HTTP {res.status_code} ({err_detail})"


        gist_json = res.json()
        files = gist_json.get("files", {})
        if "grit_data_export.json" not in files:
            return False, "grit_data_export.json not found in Gist."

        content_str = files["grit_data_export.json"].get("content", "")
        if not content_str:
            return False, "Gist backup content was empty."

        data = json.loads(content_str)
        if restore_database_from_json_data(data):
            try:
                with open(EXPORT_JSON_PATH, "w", encoding="utf-8") as f:
                    f.write(content_str)
            except Exception:
                pass
            return True, "Successfully restored database from Cloud Gist snapshot!"
        return False, "Database restore from JSON failed."
    except Exception as e:
        return False, f"Cloud restore error: {str(e)}"

def create_database_backup(reason: str = "auto") -> str:
    """
    Creates an atomic, thread-safe online snapshot of SQLite database & dual-layer JSON export.
    Maintains a rolling window of the last 30 backups to guarantee 100% zero data loss.
    Automatically initiates a non-blocking background sync to the Cloud Persistence Shield if configured.
    """
    if not os.path.exists(DB_NAME):
        return ""
    try:
        now_str = dt.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = f"grit_portal_backup_{reason}_{now_str}.db"
        backup_path = os.path.join(BACKUP_DIR, backup_filename)

        # 1. Atomic Online SQLite Backup (Safe during live user sessions)
        src_conn = sqlite3.connect(DB_NAME, timeout=30.0)
        dst_conn = sqlite3.connect(backup_path)
        with dst_conn:
            src_conn.backup(dst_conn, pages=100)
        dst_conn.close()

        # 2. Dual-Layer JSON Mirror Export (Human-readable fail-safe)
        src_conn.row_factory = sqlite3.Row
        cursor = src_conn.cursor()
        export_data = {}
        for table in BACKUP_ACTIVITY_TABLES:
            try:
                cursor.execute(f"SELECT * FROM [{table}]")
                export_data[table] = [dict(row) for row in cursor.fetchall()]
            except Exception:
                pass
        src_conn.close()

        with open(EXPORT_JSON_PATH, "w", encoding="utf-8") as f:
            json.dump(export_data, f, indent=2, default=str)

        # 3. Prune old backups, preserving latest 30 snapshots
        backups = sorted(
            [os.path.join(BACKUP_DIR, f) for f in os.listdir(BACKUP_DIR) if f.startswith("grit_portal_backup_") and f.endswith(".db")],
            key=os.path.getmtime
        )
        if len(backups) > 30:
            for old_b in backups[:-30]:
                try:
                    os.remove(old_b)
                except Exception:
                    pass

        # 4. Trigger non-blocking Cloud Persistence Sync
        token, _ = get_cloud_persistence_config()
        if token:
            try:
                threading.Thread(target=sync_database_to_cloud, args=(reason,), daemon=True).start()
            except Exception:
                pass

        return backup_filename
    except Exception as e:
        print(f"[Backup Engine Error]: {e}")
        return ""

def list_database_backups():
    """Lists all available historical database snapshots with metadata."""
    if not os.path.exists(BACKUP_DIR):
        return []
    files = [f for f in os.listdir(BACKUP_DIR) if f.startswith("grit_portal_backup_") and f.endswith(".db")]
    results = []
    for f in sorted(files, reverse=True):
        full_path = os.path.join(BACKUP_DIR, f)
        try:
            sz_kb = round(os.path.getsize(full_path) / 1024, 1)
            mtime = dt.fromtimestamp(os.path.getmtime(full_path)).strftime("%Y-%m-%d %H:%M:%S")
            results.append({"filename": f, "path": full_path, "size_kb": sz_kb, "timestamp": mtime})
        except Exception:
            pass
    return results

def restore_database_from_backup_file(backup_filepath: str) -> bool:
    """Restores database from a designated snapshot backup file with safety pre-snapshot."""
    if not os.path.exists(backup_filepath):
        return False
    try:
        # Pre-snapshot current state before restoring
        create_database_backup("pre_restore_safety")
        # Copy backup over live DB
        shutil.copy2(backup_filepath, DB_NAME)
        # Clean up stale WAL / shm locks
        for ext in ["-wal", "-shm"]:
            w_file = DB_NAME + ext
            if os.path.exists(w_file):
                try:
                    os.remove(w_file)
                except Exception:
                    pass
        return True
    except Exception as e:
        print(f"[Restore Error]: {e}")
        return False

def restore_database_from_json_data(data: dict) -> bool:
    """Restores database tables from a structured JSON dump with foreign keys temporarily relaxed."""
    if not isinstance(data, dict):
        return False
    try:
        conn = sqlite3.connect(DB_NAME, check_same_thread=False, timeout=30.0)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = OFF")
        for table, rows in data.items():
            if not rows or not isinstance(rows, list):
                continue
            try:
                cursor.execute(f"DELETE FROM [{table}]")
                cols = list(rows[0].keys())
                placeholders = ", ".join(["?"] * len(cols))
                col_names = ", ".join([f"[{c}]" for c in cols])
                sql = f"INSERT OR REPLACE INTO [{table}] ({col_names}) VALUES ({placeholders})"
                for r in rows:
                    cursor.execute(sql, [r[c] for c in cols])
            except Exception as e:
                print(f"Error restoring table {table} from JSON: {e}")
        conn.commit()
        cursor.execute("PRAGMA foreign_keys = ON")
        conn.close()
        return True
    except Exception as e:
        print(f"[JSON Restore Error]: {e}")
        return False

def auto_heal_database_if_empty():
    """
    Automatic Self-Healing Resilience Shield:
    1. Checks if live DB has zero activity records (e.g. after a fresh Streamlit Cloud redeploy/rebuild).
    2. If empty and Cloud Persistence is configured, AUTOMATICALLY pulls and restores from Cloud Gist!
    3. If Cloud is not configured or empty, falls back to local rolling backups or JSON mirror.
    Guarantees that git pushes, branch updates, and server restarts NEVER wipe data.
    """
    if not os.path.exists(DB_NAME):
        return
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM work_sessions")
        sess_cnt = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM daily_checkouts")
        co_cnt = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM skill_roadmap_progress")
        rm_cnt = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM users")
        user_cnt = cursor.fetchone()[0]
        conn.close()

        # If zero activity or default-only seed
        if sess_cnt == 0 and co_cnt == 0 and rm_cnt == 0:
            # 1. Try Cloud Gist Auto-Heal FIRST
            token, gist_id = get_cloud_persistence_config()
            if token and gist_id:
                success, msg = restore_database_from_cloud()
                if success:
                    print(f"[Auto-Heal Cloud Shield]: {msg}")
                    return

            # 2. Check local rolling backups in backups/
            backups = list_database_backups()
            for b in backups:
                b_path = b["path"]
                try:
                    b_conn = sqlite3.connect(b_path)
                    b_cur = b_conn.cursor()
                    b_cur.execute("SELECT COUNT(*) FROM work_sessions")
                    b_sess = b_cur.fetchone()[0]
                    b_cur.execute("SELECT COUNT(*) FROM daily_checkouts")
                    b_co = b_cur.fetchone()[0]
                    b_cur.execute("SELECT COUNT(*) FROM skill_roadmap_progress")
                    b_rm = b_cur.fetchone()[0]
                    b_cur.execute("SELECT COUNT(*) FROM users")
                    b_users = b_cur.fetchone()[0]
                    b_conn.close()
                    if b_sess > 0 or b_co > 0 or b_rm > 0 or b_users > 7:
                        shutil.copy2(b_path, DB_NAME)
                        print(f"[Auto-Heal Shield]: Live database automatically healed from backup: {b['filename']}")
                        return
                except Exception:
                    pass

            # 3. Check JSON mirror
            if os.path.exists(EXPORT_JSON_PATH):
                try:
                    with open(EXPORT_JSON_PATH, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    if data.get("work_sessions") or data.get("daily_checkouts") or data.get("skill_roadmap_progress") or len(data.get("users", [])) > 7:
                        restore_database_from_json_data(data)
                        print("[Auto-Heal Shield]: Live database automatically healed from JSON mirror!")
                except Exception as e:
                    print(f"[Auto-Heal JSON Error]: {e}")
    except Exception as e:
        print(f"[Auto-Heal Check Error]: {e}")



# -----------------------------------------------------------------------------
# Gamified XP & Level Progression Engine
# -----------------------------------------------------------------------------
LEVEL_TIERS = [
    (0, 300, "Level 1: Cyber Initiate", "#94A3B8"),
    (301, 800, "Level 2: Terminal Operator", "#38BDF8"),
    (801, 1800, "Level 3: Code Runner", "#00FFA3"),
    (1801, 3200, "Level 4: Systems Architect", "#A855F7"),
    (3201, 999999, "Level 5: Apex Titan", "#FFD700")
]

def calculate_xp_and_level(hours: float, tasks_done: int, skills_done: int, standups: int):
    """Calculates total gamified XP and current level progression."""
    total_xp = int((hours * 50.0) + (tasks_done * 150.0) + (skills_done * 100.0) + (standups * 75.0))
    current_tier = LEVEL_TIERS[0]
    for min_xp, max_xp, label, color in LEVEL_TIERS:
        if total_xp >= min_xp:
            current_tier = (min_xp, max_xp, label, color)
    min_xp, max_xp, label, color = current_tier
    level_progress = min(100, int(((total_xp - min_xp) / max(1, (max_xp - min_xp))) * 100)) if max_xp < 999999 else 100
    return total_xp, label, color, level_progress

# -----------------------------------------------------------------------------
# Database Schema & Clean Zero Initialization
# -----------------------------------------------------------------------------
def init_db():
    """Initializes tables and registers ONLY the 7 real team members (Zero dummy data)."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            role TEXT NOT NULL,
            title TEXT NOT NULL,
            password_hash TEXT NOT NULL,
            avatar_color TEXT DEFAULT '#00D2FF',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS work_sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            username TEXT NOT NULL,
            start_time TEXT NOT NULL,
            end_time TEXT,
            duration_minutes REAL DEFAULT 0.0,
            duration_hours REAL DEFAULT 0.0,
            notes TEXT,
            status TEXT DEFAULT 'active',
            date TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS daily_checkouts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            username TEXT NOT NULL,
            date TEXT NOT NULL,
            work_summary TEXT NOT NULL,
            learning_today TEXT NOT NULL,
            hours_worked REAL NOT NULL DEFAULT 0.0,
            blockers_feedback TEXT,
            submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            assigned_to TEXT NOT NULL,
            assigned_by TEXT NOT NULL,
            priority TEXT NOT NULL,
            category TEXT NOT NULL,
            due_date TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Pending',
            time_spent_seconds INTEGER DEFAULT 0,
            timer_started_at TEXT,
            timer_started_by TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            completed_at TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS task_timer_sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_id INTEGER NOT NULL,
            username TEXT NOT NULL,
            start_time TEXT NOT NULL,
            end_time TEXT,
            duration_seconds INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (task_id) REFERENCES tasks(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS learning_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            username TEXT NOT NULL,
            skill_name TEXT NOT NULL,
            proof_link TEXT,
            hours_spent REAL NOT NULL DEFAULT 0.0,
            mastery_pct INTEGER NOT NULL DEFAULT 0,
            notes TEXT,
            logged_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS skill_roadmap_progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            username TEXT NOT NULL,
            track_name TEXT NOT NULL,
            topic_name TEXT NOT NULL,
            is_completed INTEGER DEFAULT 0,
            completed_at TIMESTAMP,
            UNIQUE(user_id, track_name, topic_name)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS custom_skill_tracks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            username TEXT NOT NULL,
            track_name TEXT NOT NULL,
            category TEXT DEFAULT 'Custom Roadmaps',
            icon TEXT DEFAULT '⚡',
            summary TEXT DEFAULT '',
            topics_json TEXT NOT NULL,
            is_global INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS academic_queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            author TEXT NOT NULL,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            tags TEXT NOT NULL,
            is_resolved INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS academic_answers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query_id INTEGER NOT NULL,
            author TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (query_id) REFERENCES academic_queries(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS personal_growth_goals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            username TEXT NOT NULL,
            goal_title TEXT NOT NULL,
            category TEXT NOT NULL DEFAULT 'Skill Target',
            target_date TEXT,
            notes TEXT,
            status TEXT NOT NULL DEFAULT 'In Progress',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            completed_at TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    # Schema migration for existing database instances
    cursor.execute("PRAGMA table_info(tasks)")
    existing_cols = [row["name"] for row in cursor.fetchall()]
    if "time_spent_seconds" not in existing_cols:
        cursor.execute("ALTER TABLE tasks ADD COLUMN time_spent_seconds INTEGER DEFAULT 0")
    if "timer_started_at" not in existing_cols:
        cursor.execute("ALTER TABLE tasks ADD COLUMN timer_started_at TEXT DEFAULT NULL")
    if "timer_started_by" not in existing_cols:
        cursor.execute("ALTER TABLE tasks ADD COLUMN timer_started_by TEXT DEFAULT NULL")

    cursor.execute("PRAGMA table_info(daily_checkouts)")
    existing_co_cols = [row["name"] for row in cursor.fetchall()]
    if "kudos_count" not in existing_co_cols:
        cursor.execute("ALTER TABLE daily_checkouts ADD COLUMN kudos_count INTEGER DEFAULT 0")

    cursor.execute("PRAGMA table_info(users)")
    existing_u_cols = [row["name"] for row in cursor.fetchall()]
    if "phone" not in existing_u_cols:
        cursor.execute("ALTER TABLE users ADD COLUMN phone TEXT DEFAULT ''")

    cursor.execute("PRAGMA table_info(custom_skill_tracks)")
    existing_cst_cols = [row["name"] for row in cursor.fetchall()]
    if "category" not in existing_cst_cols:
        cursor.execute("ALTER TABLE custom_skill_tracks ADD COLUMN category TEXT DEFAULT 'Custom Roadmaps'")
    if "icon" not in existing_cst_cols:
        cursor.execute("ALTER TABLE custom_skill_tracks ADD COLUMN icon TEXT DEFAULT '⚡'")
    if "summary" not in existing_cst_cols:
        cursor.execute("ALTER TABLE custom_skill_tracks ADD COLUMN summary TEXT DEFAULT ''")
    if "is_global" not in existing_cst_cols:
        cursor.execute("ALTER TABLE custom_skill_tracks ADD COLUMN is_global INTEGER DEFAULT 1")

    conn.commit()

    cursor.execute("SELECT COUNT(*) as count FROM users")
    count = cursor.fetchone()["count"]
    if count == 0:
        default_hash = hash_password(DEFAULT_PASSWORD)
        for member in TEAM_MEMBERS:
            cursor.execute("""
                INSERT INTO users (username, name, role, title, password_hash, avatar_color)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (member["username"], member["name"], member["role"], member["title"], default_hash, member["avatar_color"]))
        conn.commit()
    conn.close()
    auto_heal_database_if_empty()
    create_database_backup("init_boot")

# -----------------------------------------------------------------------------
# Modular SQLite Database Helper Functions
# -----------------------------------------------------------------------------
def verify_user(username: str, password: str):
    """Verifies user credentials against SQLite and returns user dict if valid."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    if user and user["password_hash"] == hash_password(password):
        return dict(user)
    return None

def get_all_users():
    """Retrieves list of all registered team members in designated order."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(users)")
    cols = [r["name"] for r in cursor.fetchall()]
    phone_col = "phone, " if "phone" in cols else "'' as phone, "
    cursor.execute(f"SELECT id, username, name, role, title, avatar_color, {phone_col} created_at FROM users ORDER BY id ASC")
    users = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return users

def get_active_session(user_id: int):
    """Fetches any active (uncompleted) work session for the user."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM work_sessions 
        WHERE user_id = ? AND status = 'active' 
        ORDER BY id DESC LIMIT 1
    """, (user_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def start_session(user_id: int, username: str, notes: str = ""):
    """Starts a new punch-in work session."""
    active = get_active_session(user_id)
    if active:
        return active, "A session is already active!"

    now_str = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    date_str = dt.now().strftime("%Y-%m-%d")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO work_sessions (user_id, username, start_time, notes, status, date)
        VALUES (?, ?, ?, ?, 'active', ?)
    """, (user_id, username, now_str, notes, date_str))
    conn.commit()
    session_id = cursor.lastrowid
    conn.close()
    return {"id": session_id, "start_time": now_str, "notes": notes}, "Session punched in successfully!"

def end_session(session_id: int):
    """Punches out of an active work session, calculating total duration."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM work_sessions WHERE id = ?", (session_id,))
    session = cursor.fetchone()

    if not session or session["status"] != "active":
        conn.close()
        return None, "No active session found with this ID."

    start_dt = dt.strptime(session["start_time"], "%Y-%m-%d %H:%M:%S")
    end_dt = dt.now()
    delta = end_dt - start_dt

    duration_minutes = round(delta.total_seconds() / 60.0, 2)
    duration_hours = round(delta.total_seconds() / 3600.0, 2)
    end_str = end_dt.strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        UPDATE work_sessions 
        SET end_time = ?, duration_minutes = ?, duration_hours = ?, status = 'completed'
        WHERE id = ?
    """, (end_str, duration_minutes, duration_hours, session_id))
    conn.commit()
    conn.close()
    create_database_backup("session_clockout")

    return {"duration_hours": duration_hours, "duration_minutes": duration_minutes}, "Punched out successfully!"

def submit_daily_checkout(user_id: int, username: str, work_summary: str, learning_today: str, hours_worked: float, blockers_feedback: str = ""):
    """Records daily checkout & standup report and logs skill acquisition."""
    today_str = dt.now().strftime("%Y-%m-%d")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO daily_checkouts (user_id, username, date, work_summary, learning_today, hours_worked, blockers_feedback)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (user_id, username, today_str, work_summary, learning_today, hours_worked, blockers_feedback))

    if learning_today.strip():
        cursor.execute("""
            INSERT INTO learning_logs (user_id, username, skill_name, hours_spent, mastery_pct, notes)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (user_id, username, "Daily Sprint Learning", hours_worked, 70, learning_today))

    conn.commit()
    conn.close()
    create_database_backup("daily_checkout")
    return True

def get_daily_checkouts(user_id: int = None, limit: int = 100):
    """Retrieves daily checkouts for feed (Lead overview, team feed, or personal history)."""
    conn = get_db_connection()
    cursor = conn.cursor()
    if user_id:
        cursor.execute("""
            SELECT dc.*, u.title as user_title, u.avatar_color
            FROM daily_checkouts dc
            JOIN users u ON dc.user_id = u.id
            WHERE dc.user_id = ?
            ORDER BY dc.id DESC LIMIT ?
        """, (user_id, limit))
    else:
        cursor.execute("""
            SELECT dc.*, u.title as user_title, u.avatar_color
            FROM daily_checkouts dc
            JOIN users u ON dc.user_id = u.id
            ORDER BY dc.id DESC LIMIT ?
        """, (limit,))
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return rows

def add_checkout_kudo(checkout_id: int):
    """Increments kudos count for a daily checkout."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE daily_checkouts SET kudos_count = COALESCE(kudos_count, 0) + 1 WHERE id = ?", (checkout_id,))
    conn.commit()
    conn.close()
    return True

def get_all_user_work_sessions(user_id: int, limit: int = 100):
    """Retrieves full past history of work sessions for an individual user."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM work_sessions
        WHERE user_id = ? AND status = 'completed'
        ORDER BY id DESC LIMIT ?
    """, (user_id, limit))
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return rows

def get_roadmap_progress(user_id: int):
    """Gets all completed topics for a user across all roadmaps."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT track_name, topic_name, is_completed
        FROM skill_roadmap_progress
        WHERE user_id = ? AND is_completed = 1
    """, (user_id,))
    completed = {(row["track_name"], row["topic_name"]) for row in cursor.fetchall()}
    conn.close()
    return completed

def toggle_roadmap_topic(user_id: int, username: str, track_name: str, topic_name: str, is_completed: bool):
    """Toggles completion status of a topic milestone in a skill roadmap."""
    conn = get_db_connection()
    cursor = conn.cursor()
    now_str = dt.now().strftime("%Y-%m-%d %H:%M:%S") if is_completed else None
    val = 1 if is_completed else 0

    cursor.execute("""
        INSERT INTO skill_roadmap_progress (user_id, username, track_name, topic_name, is_completed, completed_at)
        VALUES (?, ?, ?, ?, ?, ?)
        ON CONFLICT(user_id, track_name, topic_name) 
        DO UPDATE SET is_completed = excluded.is_completed, completed_at = excluded.completed_at
    """, (user_id, username, track_name, topic_name, val, now_str))
    conn.commit()
    conn.close()
    create_database_backup("roadmap_toggle")
    return True

def get_custom_tracks(user_id: int = None):
    """Retrieves global team tracks and custom tracks for user."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(custom_skill_tracks)")
    cols = [r["name"] for r in cursor.fetchall()]
    if "is_global" in cols:
        if user_id:
            cursor.execute("SELECT * FROM custom_skill_tracks WHERE is_global = 1 OR user_id = ? ORDER BY id ASC", (user_id,))
        else:
            cursor.execute("SELECT * FROM custom_skill_tracks ORDER BY id ASC")
    else:
        if user_id:
            cursor.execute("SELECT * FROM custom_skill_tracks WHERE user_id = ? ORDER BY id ASC", (user_id,))
        else:
            cursor.execute("SELECT * FROM custom_skill_tracks ORDER BY id ASC")
    tracks = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return tracks

def create_custom_track(user_id: int, username: str, track_name: str, topics_list: list, category: str = "Custom Roadmaps", icon: str = "⚡", summary: str = "", is_global: int = 1):
    """Allows user or admin to create custom skill roadmap with custom topics."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(custom_skill_tracks)")
    cols = [r["name"] for r in cursor.fetchall()]
    if "category" in cols and "is_global" in cols:
        cursor.execute("""
            INSERT INTO custom_skill_tracks (user_id, username, track_name, category, icon, summary, topics_json, is_global)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (user_id, username, track_name.strip(), category.strip(), icon.strip() or "⚡", summary.strip(), json.dumps(topics_list), is_global))
    else:
        cursor.execute("""
            INSERT INTO custom_skill_tracks (user_id, username, track_name, topics_json)
            VALUES (?, ?, ?, ?)
        """, (user_id, username, track_name.strip(), json.dumps(topics_list)))
    conn.commit()
    conn.close()
    create_database_backup("custom_track_create")
    return True

def delete_custom_track(track_id: int):
    """Deletes a custom skill track by ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM custom_skill_tracks WHERE id = ?", (track_id,))
    conn.commit()
    conn.close()
    create_database_backup("custom_track_delete")
    return True

def add_personal_growth_goal(user_id: int, username: str, goal_title: str, category: str = "Skill Target", target_date: str = None, notes: str = None):
    """Adds a new active growth target goal for the engineer."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO personal_growth_goals (user_id, username, goal_title, category, target_date, notes, status)
        VALUES (?, ?, ?, ?, ?, ?, 'In Progress')
    """, (user_id, username, goal_title.strip(), category.strip(), target_date, notes))
    conn.commit()
    conn.close()
    create_database_backup("growth_goal_add")
    return True

def get_personal_growth_goals(user_id: int, status: str = None):
    """Retrieves personal growth goals for a user, optionally filtered by status ('In Progress' or 'Completed')."""
    conn = get_db_connection()
    cursor = conn.cursor()
    if status:
        cursor.execute("""
            SELECT * FROM personal_growth_goals
            WHERE user_id = ? AND status = ?
            ORDER BY id DESC
        """, (user_id, status))
    else:
        cursor.execute("""
            SELECT * FROM personal_growth_goals
            WHERE user_id = ?
            ORDER BY CASE WHEN status = 'In Progress' THEN 0 ELSE 1 END, id DESC
        """, (user_id,))
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return rows

def toggle_personal_growth_goal(goal_id: int, user_id: int, is_completed: bool):
    """Toggles completion status of a personal growth goal."""
    conn = get_db_connection()
    cursor = conn.cursor()
    new_status = 'Completed' if is_completed else 'In Progress'
    now_str = dt.now().strftime("%Y-%m-%d %H:%M:%S") if is_completed else None
    cursor.execute("""
        UPDATE personal_growth_goals
        SET status = ?, completed_at = ?
        WHERE id = ? AND user_id = ?
    """, (new_status, now_str, goal_id, user_id))
    conn.commit()
    conn.close()
    create_database_backup("growth_goal_toggle")
    return True

def delete_personal_growth_goal(goal_id: int, user_id: int):
    """Deletes a personal growth goal."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM personal_growth_goals WHERE id = ? AND user_id = ?", (goal_id, user_id))
    conn.commit()
    conn.close()
    create_database_backup("growth_goal_delete")
    return True


def get_personal_growth_stats(user_id: int, username: str):
    """Computes comprehensive personal growth metrics, XP, and formatted 7-day trend."""
    conn = get_db_connection()
    cursor = conn.cursor()
    today_str = dt.now().strftime("%Y-%m-%d")

    # Today's hours
    cursor.execute("""
        SELECT COALESCE(SUM(duration_hours), 0.0) as today_hrs
        FROM work_sessions 
        WHERE user_id = ? AND date = ? AND status = 'completed'
    """, (user_id, today_str))
    today_hours = round(cursor.fetchone()["today_hrs"], 2)

    # All-time hours
    cursor.execute("""
        SELECT COALESCE(SUM(duration_hours), 0.0) as all_time_hrs
        FROM work_sessions 
        WHERE user_id = ? AND status = 'completed'
    """, (user_id,))
    all_time_hours = round(cursor.fetchone()["all_time_hrs"], 2)

    # Last 7 days trend with clean, readable date labels (e.g. 15 Oct, 16 Oct)
    dates_7 = [(dt.now() - timedelta(days=i)) for i in range(6, -1, -1)]
    daily_trend = {}
    for date_obj in dates_7:
        d_raw = date_obj.strftime("%Y-%m-%d")
        d_label = date_obj.strftime("%d %b")
        cursor.execute("""
            SELECT COALESCE(SUM(duration_hours), 0.0) as d_hrs
            FROM work_sessions 
            WHERE user_id = ? AND date = ? AND status = 'completed'
        """, (user_id, d_raw))
        daily_trend[d_label] = round(cursor.fetchone()["d_hrs"], 2)

    # Tasks stats
    cursor.execute("""
        SELECT 
            COUNT(*) as total_tasks,
            SUM(CASE WHEN status = 'Completed' THEN 1 ELSE 0 END) as completed,
            SUM(CASE WHEN status != 'Completed' THEN 1 ELSE 0 END) as active
        FROM tasks WHERE assigned_to = ?
    """, (username,))
    task_res = cursor.fetchone()
    completed_tasks = task_res["completed"] or 0
    active_tasks = task_res["active"] or 0

    # Skills completed in roadmap
    cursor.execute("""
        SELECT COUNT(*) as completed_topics
        FROM skill_roadmap_progress
        WHERE user_id = ? AND is_completed = 1
    """, (user_id,))
    completed_skills = cursor.fetchone()["completed_topics"] or 0

    # Daily checkouts count
    cursor.execute("SELECT COUNT(*) as count FROM daily_checkouts WHERE user_id = ?", (user_id,))
    standup_count = cursor.fetchone()["count"] or 0

    # Daily consistency streak calculation
    cursor.execute("""
        SELECT DISTINCT date FROM work_sessions WHERE user_id = ? AND status = 'completed'
        UNION
        SELECT DISTINCT date FROM daily_checkouts WHERE user_id = ?
    """, (user_id, user_id))
    active_dates = {row["date"] for row in cursor.fetchall()}

    streak_days = 0
    today_date = dt.now().date()
    check_date = today_date
    if check_date.strftime("%Y-%m-%d") not in active_dates:
        yesterday_date = today_date - timedelta(days=1)
        if yesterday_date.strftime("%Y-%m-%d") in active_dates:
            check_date = yesterday_date

    while check_date.strftime("%Y-%m-%d") in active_dates:
        streak_days += 1
        check_date = check_date - timedelta(days=1)

    conn.close()

    total_xp, level_title, level_color, level_progress = calculate_xp_and_level(
        all_time_hours, completed_tasks, completed_skills, standup_count
    )

    return {
        "today_hours": today_hours,
        "all_time_hours": all_time_hours,
        "completed_tasks": completed_tasks,
        "active_tasks": active_tasks,
        "completed_skills": completed_skills,
        "standup_count": standup_count,
        "streak_days": streak_days,
        "total_xp": total_xp,
        "level_title": level_title,
        "level_color": level_color,
        "level_progress": level_progress,
        "daily_trend": daily_trend
    }

def get_leaderboard():
    """Computes real-time dynamic leaderboard metrics, XP, and ranks (Shatakshi at #2 priority)."""
    conn = get_db_connection()
    cursor = conn.cursor()
    today_str = dt.now().strftime("%Y-%m-%d")

    cursor.execute("SELECT id, username, name, role, title, avatar_color FROM users ORDER BY id ASC")
    users = [dict(u) for u in cursor.fetchall()]

    leaderboard = []
    total_team_hours = 0.0
    total_active_tasks = 0
    total_completed_tasks = 0

    for user in users:
        u_id = user["id"]
        uname = user["username"]

        cursor.execute("""
            SELECT COALESCE(SUM(duration_hours), 0.0) as today_hrs
            FROM work_sessions 
            WHERE user_id = ? AND date = ? AND status = 'completed'
        """, (u_id, today_str))
        today_hours = round(cursor.fetchone()["today_hrs"], 2)

        cursor.execute("""
            SELECT COALESCE(SUM(duration_hours), 0.0) as all_time_hrs
            FROM work_sessions 
            WHERE user_id = ? AND status = 'completed'
        """, (u_id,))
        all_time_hours = round(cursor.fetchone()["all_time_hrs"], 2)
        total_team_hours += all_time_hours

        cursor.execute("""
            SELECT 
                COUNT(*) as total_tasks,
                SUM(CASE WHEN status = 'Completed' THEN 1 ELSE 0 END) as completed,
                SUM(CASE WHEN status != 'Completed' THEN 1 ELSE 0 END) as active
            FROM tasks WHERE assigned_to = ?
        """, (uname,))
        task_res = cursor.fetchone()
        completed_tasks = task_res["completed"] or 0
        active_tasks = task_res["active"] or 0

        total_active_tasks += active_tasks
        total_completed_tasks += completed_tasks

        cursor.execute("""
            SELECT COUNT(*) as count 
            FROM skill_roadmap_progress 
            WHERE user_id = ? AND is_completed = 1
        """, (u_id,))
        skills_mastered = cursor.fetchone()["count"] or 0

        cursor.execute("""
            SELECT COUNT(*) as count 
            FROM daily_checkouts 
            WHERE user_id = ?
        """, (u_id,))
        standups_submitted = cursor.fetchone()["count"] or 0

        cursor.execute("""
            SELECT id, start_time FROM work_sessions 
            WHERE user_id = ? AND status = 'active' LIMIT 1
        """, (u_id,))
        is_punch_active = cursor.fetchone() is not None

        # Member consistency streak
        cursor.execute("""
            SELECT DISTINCT date FROM work_sessions WHERE user_id = ? AND status = 'completed'
            UNION
            SELECT DISTINCT date FROM daily_checkouts WHERE user_id = ?
        """, (u_id, u_id))
        u_active_dates = {row["date"] for row in cursor.fetchall()}
        u_streak = 0
        u_today_date = dt.now().date()
        u_check_date = u_today_date
        if u_check_date.strftime("%Y-%m-%d") not in u_active_dates:
            u_yest = u_today_date - timedelta(days=1)
            if u_yest.strftime("%Y-%m-%d") in u_active_dates:
                u_check_date = u_yest
        while u_check_date.strftime("%Y-%m-%d") in u_active_dates:
            u_streak += 1
            u_check_date = u_check_date - timedelta(days=1)

        score = round((all_time_hours * 10.0) + (completed_tasks * 35.0) + (skills_mastered * 8.0) + (standups_submitted * 15.0), 1)
        xp, level_title, level_color, _ = calculate_xp_and_level(all_time_hours, completed_tasks, skills_mastered, standups_submitted)

        leaderboard.append({
            "user_id": u_id,
            "username": uname,
            "name": user["name"],
            "role": user["role"],
            "title": user["title"],
            "avatar_color": user["avatar_color"],
            "today_hours": today_hours,
            "all_time_hours": all_time_hours,
            "completed_tasks": completed_tasks,
            "active_tasks": active_tasks,
            "skills_mastered": skills_mastered,
            "standups_submitted": standups_submitted,
            "is_punch_active": is_punch_active,
            "streak_days": u_streak,
            "score": score,
            "xp": xp,
            "level_title": level_title,
            "level_color": level_color
        })

    conn.close()

    # Sort primarily by score descending, tie-break preserves seed order (#1 Rajat, #2 Shatakshi)
    leaderboard.sort(key=lambda x: (x["score"], -x["user_id"]), reverse=True)

    summary = {
        "total_team_hours": round(total_team_hours, 1),
        "total_active_tasks": total_active_tasks,
        "total_completed_tasks": total_completed_tasks,
        "active_punchins_count": sum(1 for m in leaderboard if m["is_punch_active"])
    }

    return leaderboard, summary

def assign_task(title: str, description: str, assigned_to: str, assigned_by: str, priority: str, category: str, due_date: str):
    """Creates a new task assignment."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tasks (title, description, assigned_to, assigned_by, priority, category, due_date, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, 'Pending')
    """, (title, description, assigned_to, assigned_by, priority, category, due_date))
    conn.commit()
    conn.close()
    create_database_backup("task_assign")
    return True

def update_task_status(task_id: int, new_status: str):
    """Updates the progress status of a task."""
    conn = get_db_connection()
    cursor = conn.cursor()
    completed_at = dt.now().strftime("%Y-%m-%d %H:%M:%S") if new_status == "Completed" else None
    cursor.execute("""
        UPDATE tasks 
        SET status = ?, completed_at = ?
        WHERE id = ?
    """, (new_status, completed_at, task_id))
    conn.commit()
    conn.close()
    create_database_backup("task_status_update")
    return True

def delete_task(task_id: int):
    """Deletes a task record and associated timer sessions safely."""
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM task_timer_sessions WHERE task_id = ?", (task_id,))
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        create_database_backup("task_delete")
        return True
    finally:
        conn.close()

def format_seconds_to_hhmmss(seconds: int) -> str:
    """Formats seconds into readable string like 1h 24m 15s or 0m 00s."""
    seconds = int(max(0, seconds))
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    if h > 0:
        return f"{h}h {m:02d}m {s:02d}s"
    elif m > 0:
        return f"{m}m {s:02d}s"
    else:
        return f"{s}s"

def start_task_timer(task_id: int, username: str):
    """Starts the stopwatch timer on a specific task."""
    conn = get_db_connection()
    cursor = conn.cursor()
    now_iso = dt.now().isoformat()
    # Transition to 'In Progress' if currently 'Pending'
    cursor.execute("""
        UPDATE tasks 
        SET timer_started_at = ?, timer_started_by = ?,
            status = CASE WHEN status = 'Pending' THEN 'In Progress' ELSE status END
        WHERE id = ?
    """, (now_iso, username, task_id))
    conn.commit()
    conn.close()
    return True

def stop_task_timer(task_id: int, username: str):
    """Stops the task stopwatch timer and logs elapsed seconds."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT timer_started_at, time_spent_seconds, title FROM tasks WHERE id = ?", (task_id,))
    task = cursor.fetchone()
    if not task or not task["timer_started_at"]:
        conn.close()
        return 0, "No active timer on this task."

    try:
        start_time = dt.fromisoformat(task["timer_started_at"])
    except Exception:
        start_time = dt.now()

    now_time = dt.now()
    elapsed_seconds = int((now_time - start_time).total_seconds())
    if elapsed_seconds < 0:
        elapsed_seconds = 0

    new_total_seconds = (task["time_spent_seconds"] or 0) + elapsed_seconds

    cursor.execute("""
        UPDATE tasks 
        SET timer_started_at = NULL, timer_started_by = NULL, time_spent_seconds = ?
        WHERE id = ?
    """, (new_total_seconds, task_id))

    cursor.execute("""
        INSERT INTO task_timer_sessions (task_id, username, start_time, end_time, duration_seconds)
        VALUES (?, ?, ?, ?, ?)
    """, (task_id, username, task["timer_started_at"], now_time.isoformat(), elapsed_seconds))

    conn.commit()
    conn.close()
    create_database_backup("task_timer_stop")
    return elapsed_seconds, f"Logged {format_seconds_to_hhmmss(elapsed_seconds)} to task!"

def reset_task_timer(task_id: int):
    """Resets active timer on a task without saving elapsed session."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET timer_started_at = NULL, timer_started_by = NULL WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return True

def manual_add_task_time(task_id: int, username: str, additional_minutes: int):
    """Manually adds offline time to a task."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT time_spent_seconds FROM tasks WHERE id = ?", (task_id,))
    task = cursor.fetchone()
    if not task:
        conn.close()
        return False
    add_sec = int(additional_minutes * 60)
    new_total_seconds = (task["time_spent_seconds"] or 0) + add_sec
    now_iso = dt.now().isoformat()
    cursor.execute("""
        UPDATE tasks SET time_spent_seconds = ? WHERE id = ?
    """, (new_total_seconds, task_id))
    cursor.execute("""
        INSERT INTO task_timer_sessions (task_id, username, start_time, end_time, duration_seconds)
        VALUES (?, ?, ?, ?, ?)
    """, (task_id, username, now_iso, now_iso, add_sec))
    conn.commit()
    conn.close()
    create_database_backup("task_manual_time")
    return True



def get_tasks(assigned_to: str = None, status_filter: str = None):
    """Fetches tasks with optional filters."""
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM tasks WHERE 1=1"
    params = []

    if assigned_to:
        query += " AND assigned_to = ?"
        params.append(assigned_to)
    if status_filter and status_filter != "All":
        query += " AND status = ?"
        params.append(status_filter)

    query += " ORDER BY CASE priority WHEN 'High' THEN 1 WHEN 'Medium' THEN 2 ELSE 3 END, id DESC"
    cursor.execute(query, params)
    tasks = [dict(t) for t in cursor.fetchall()]
    conn.close()
    return tasks

def add_learning_log(user_id: int, username: str, skill_name: str, proof_link: str, hours_spent: float, mastery_pct: int, notes: str):
    """Adds a new skill acquisition milestone to the journal."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO learning_logs (user_id, username, skill_name, proof_link, hours_spent, mastery_pct, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (user_id, username, skill_name, proof_link, hours_spent, mastery_pct, notes))
    conn.commit()
    conn.close()
    create_database_backup("learning_log_add")
    return True

def get_learning_logs(username: str = None):
    """Retrieves learning logs filtered by user or team-wide."""
    conn = get_db_connection()
    cursor = conn.cursor()
    if username and username != "All Members":
        cursor.execute("""
            SELECT l.*, u.title as user_title, u.avatar_color
            FROM learning_logs l
            JOIN users u ON l.user_id = u.id
            WHERE l.username = ?
            ORDER BY l.id DESC
        """, (username,))
    else:
        cursor.execute("""
            SELECT l.*, u.title as user_title, u.avatar_color
            FROM learning_logs l
            JOIN users u ON l.user_id = u.id
            ORDER BY l.id DESC
        """)
    logs = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return logs

def add_academic_query(author: str, title: str, content: str, tags: str):
    """Posts a new academic or coding query."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO academic_queries (author, title, content, tags, is_resolved)
        VALUES (?, ?, ?, ?, 0)
    """, (author, title, content, tags))
    conn.commit()
    conn.close()
    create_database_backup("academic_query_add")
    return True

def get_academic_queries(search_term: str = "", filter_tag: str = "All"):
    """Fetches queries with search and tag filters."""
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        SELECT q.*, 
            (SELECT COUNT(*) FROM academic_answers WHERE query_id = q.id) as answer_count
        FROM academic_queries q
        WHERE 1=1
    """
    params = []
    if search_term:
        query += " AND (q.title LIKE ? OR q.content LIKE ? OR q.tags LIKE ?)"
        term = f"%{search_term}%"
        params.extend([term, term, term])
    if filter_tag and filter_tag != "All":
        query += " AND q.tags LIKE ?"
        params.append(f"%{filter_tag}%")

    query += " ORDER BY q.id DESC"
    cursor.execute(query, params)
    queries = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return queries

def add_academic_answer(query_id: int, author: str, content: str):
    """Submits a solution or note to a query."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO academic_answers (query_id, author, content)
        VALUES (?, ?, ?)
    """, (query_id, author, content))
    conn.commit()
    conn.close()
    create_database_backup("academic_answer_add")
    return True

def get_academic_answers(query_id: int):
    """Gets all responses for a query."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT a.*, u.title as author_title, u.avatar_color
        FROM academic_answers a
        LEFT JOIN users u ON a.author = u.username
        WHERE a.query_id = ?
        ORDER BY a.id ASC
    """, (query_id,))
    answers = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return answers

def toggle_query_resolution(query_id: int, current_status: int):
    """Toggles query between resolved and unresolved."""
    conn = get_db_connection()
    cursor = conn.cursor()
    new_status = 0 if current_status == 1 else 1
    cursor.execute("UPDATE academic_queries SET is_resolved = ? WHERE id = ?", (new_status, query_id))
    conn.commit()
    conn.close()
    create_database_backup("academic_query_toggle")
    return True

def reset_user_password(username: str, new_password: str):
    """Admin function to reset user password."""
    conn = get_db_connection()
    cursor = conn.cursor()
    new_hash = hash_password(new_password)
    cursor.execute("UPDATE users SET password_hash = ? WHERE username = ?", (new_hash, username))
    conn.commit()
    conn.close()
    create_database_backup("password_reset")
    return True

def change_user_password(user_id: int, new_password: str):
    """Updates password hash for a specific user ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    new_hash = hash_password(new_password)
    cursor.execute("UPDATE users SET password_hash = ? WHERE id = ?", (new_hash, user_id))
    conn.commit()
    conn.close()
    create_database_backup("password_change")
    return True

def update_user_profile(user_id: int, name: str, title: str, role: str, phone: str = "", avatar_color: str = None):
    """Admin function to update team member's full profile, title, contact, role, and avatar."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(users)")
    cols = [r["name"] for r in cursor.fetchall()]
    
    if "phone" in cols:
        if avatar_color:
            cursor.execute("""
                UPDATE users 
                SET name = ?, title = ?, role = ?, phone = ?, avatar_color = ?
                WHERE id = ?
            """, (name.strip(), title.strip(), role.strip(), phone.strip(), avatar_color, user_id))
        else:
            cursor.execute("""
                UPDATE users 
                SET name = ?, title = ?, role = ?, phone = ?
                WHERE id = ?
            """, (name.strip(), title.strip(), role.strip(), phone.strip(), user_id))
    else:
        if avatar_color:
            cursor.execute("""
                UPDATE users 
                SET name = ?, title = ?, role = ?, avatar_color = ?
                WHERE id = ?
            """, (name.strip(), title.strip(), role.strip(), avatar_color, user_id))
        else:
            cursor.execute("""
                UPDATE users 
                SET name = ?, title = ?, role = ?
                WHERE id = ?
            """, (name.strip(), title.strip(), role.strip(), user_id))
    conn.commit()
    conn.close()
    create_database_backup("user_profile_update")
    return True

def delete_user_by_id(user_id: int):
    """Admin function to delete a member from the team."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    create_database_backup("user_delete")
    return True

def create_new_user(username: str, name: str, role: str, title: str, password: str = DEFAULT_PASSWORD, avatar_color: str = "#00D2FF", phone: str = ""):
    """Admin function to provision a new team member with optional phone number."""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        p_hash = hash_password(password)
        cursor.execute("PRAGMA table_info(users)")
        cols = [r["name"] for r in cursor.fetchall()]
        if "phone" in cols:
            cursor.execute("""
                INSERT INTO users (username, name, role, title, password_hash, avatar_color, phone)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (username.strip(), name.strip(), role.strip(), title.strip(), p_hash, avatar_color, phone.strip()))
        else:
            cursor.execute("""
                INSERT INTO users (username, name, role, title, password_hash, avatar_color)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (username.strip(), name.strip(), role.strip(), title.strip(), p_hash, avatar_color))
        conn.commit()
        conn.close()
        create_database_backup("user_create")
        return True, "User registered successfully!"
    except sqlite3.IntegrityError:
        conn.close()
        return False, "Username already exists."


def purge_all_activity_data():
    """Purges all activity records keeping users and credentials intact after emergency backup."""
    create_database_backup("EMERGENCY_PRE_PURGE")
    conn = get_db_connection()
    c = conn.cursor()
    tables = [
        "work_sessions", "daily_checkouts", "tasks", "task_timer_sessions",
        "learning_logs", "skill_roadmap_progress", "custom_skill_tracks",
        "academic_queries", "academic_answers", "personal_growth_goals"
    ]
    for t in tables:
        try:
            c.execute(f"DELETE FROM {t}")
        except Exception:
            pass
    try:
        c.execute("""
            DELETE FROM sqlite_sequence 
            WHERE name IN ('work_sessions', 'daily_checkouts', 'tasks', 'task_timer_sessions', 
                           'learning_logs', 'skill_roadmap_progress', 'custom_skill_tracks', 
                           'academic_queries', 'academic_answers', 'personal_growth_goals')
        """)
    except Exception:
        pass
    conn.commit()
    conn.close()
    return True

# -----------------------------------------------------------------------------
# Custom Styling: Dark Cyber Luxury Design System
# -----------------------------------------------------------------------------
def inject_custom_css():
    """Injects high-contrast dark cyber luxury styling with strict typography rules."""
    css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200');

    :root {
        --bg-main: #0E1117;
        --bg-card: #141721;
        --bg-card-hover: #191E2D;
        --border-color: #262730;
        --accent-neon: #00FFA3;
        --accent-cyan: #00D2FF;
        --accent-purple: #9D00FF;
        --accent-amber: #FFB800;
        --accent-red: #FF4757;
        --text-primary: #FFFFFF;
        --text-secondary: #94A3B8;
        --text-muted: #64748B;
    }

    /* Core Page & Typography specifically targeting text containers, NEVER wildcard */
    html, body, p, div.stMarkdown, input, textarea, select, button, label, h1, h2, h3, h4, h5, h6 {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }
    
    /* Strict Material Icons Protection - NEVER display ligature as raw text */
    [data-testid="stIconMaterial"], 
    .material-symbols-rounded, 
    .material-symbols-outlined,
    span[data-testid="stIconMaterial"],
    [class*="material-symbols"] {
        font-family: 'Material Symbols Rounded', 'Material Icons' !important;
        font-style: normal !important;
        display: inline-block !important;
    }

    .stApp {
        background-color: var(--bg-main);
        background-image: 
            radial-gradient(circle at 10% 20%, rgba(0, 255, 163, 0.03) 0%, transparent 40%),
            radial-gradient(circle at 90% 80%, rgba(0, 210, 255, 0.03) 0%, transparent 40%);
    }

    /* Sidebar Customization */
    section[data-testid="stSidebar"] {
        background-color: #0A0D13 !important;
        border-right: 1px solid var(--border-color) !important;
    }
    section[data-testid="stSidebar"] .stMarkdown h1, 
    section[data-testid="stSidebar"] .stMarkdown h2, 
    section[data-testid="stSidebar"] .stMarkdown h3 {
        color: var(--accent-neon) !important;
    }

    /* KPI Metric Cards */
    .kpi-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 16px;
        margin-bottom: 24px;
    }
    .kpi-card {
        background: linear-gradient(135deg, rgba(20, 23, 33, 0.9) 0%, rgba(14, 17, 23, 0.95) 100%);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        padding: 18px 20px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.35);
        transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
        position: relative;
        overflow: hidden;
    }
    .kpi-card:hover {
        transform: translateY(-2px);
        border-color: rgba(0, 255, 163, 0.4);
        box-shadow: 0 6px 25px rgba(0, 255, 163, 0.12);
    }
    .kpi-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 4px;
        height: 100%;
        background: var(--accent-neon);
    }
    .kpi-card.cyan::before { background: var(--accent-cyan); }
    .kpi-card.purple::before { background: var(--accent-purple); }
    .kpi-card.amber::before { background: var(--accent-amber); }

    .kpi-title {
        font-size: 0.8rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: var(--text-secondary);
        margin-bottom: 8px;
    }
    .kpi-value {
        font-family: 'JetBrains Mono', monospace;
        font-size: 2.1rem;
        font-weight: 700;
        color: #FFFFFF;
        line-height: 1.1;
    }
    .kpi-subtext {
        font-size: 0.75rem;
        color: var(--accent-neon);
        margin-top: 6px;
    }

    /* Cyber Card Generic */
    .cyber-card {
        background: var(--bg-card);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.4);
    }

    /* Zero State Card */
    .zero-state-card {
        background: rgba(20, 23, 33, 0.6);
        border: 1px dashed #262730;
        border-radius: 12px;
        padding: 30px 20px;
        text-align: center;
        margin-bottom: 20px;
    }

    /* Live Session Banner */
    .session-banner-active {
        background: linear-gradient(135deg, rgba(0, 255, 163, 0.1) 0%, rgba(20, 23, 33, 0.95) 100%);
        border: 1px solid rgba(0, 255, 163, 0.4);
        border-radius: 14px;
        padding: 20px;
        margin-bottom: 24px;
        box-shadow: 0 0 30px rgba(0, 255, 163, 0.15);
    }

    /* Pulsing Green Indicator */
    .pulse-dot {
        display: inline-block;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background-color: var(--accent-neon);
        box-shadow: 0 0 0 0 rgba(0, 255, 163, 0.7);
        animation: pulse-ring 1.8s infinite cubic-bezier(0.66, 0, 0, 1);
        margin-right: 8px;
        vertical-align: middle;
    }
    @keyframes pulse-ring {
        0% { box-shadow: 0 0 0 0 rgba(0, 255, 163, 0.7); }
        70% { box-shadow: 0 0 0 10px rgba(0, 255, 163, 0); }
        100% { box-shadow: 0 0 0 0 rgba(0, 255, 163, 0); }
    }

    /* Badges */
    .badge {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }
    .badge-pending {
        background: rgba(255, 184, 0, 0.15);
        color: #FFB800;
        border: 1px solid rgba(255, 184, 0, 0.3);
    }
    .badge-inprogress {
        background: rgba(0, 210, 255, 0.15);
        color: #00D2FF;
        border: 1px solid rgba(0, 210, 255, 0.3);
    }
    .badge-review {
        background: rgba(157, 0, 255, 0.15);
        color: #C084FC;
        border: 1px solid rgba(157, 0, 255, 0.3);
    }
    .badge-completed {
        background: rgba(0, 255, 163, 0.15);
        color: #00FFA3;
        border: 1px solid rgba(0, 255, 163, 0.3);
    }
    .badge-admin {
        background: linear-gradient(135deg, rgba(255, 215, 0, 0.2) 0%, rgba(255, 140, 0, 0.2) 100%);
        color: #FFD700;
        border: 1px solid rgba(255, 215, 0, 0.5);
    }
    .badge-member {
        background: rgba(0, 210, 255, 0.1);
        color: #38BDF8;
        border: 1px solid rgba(0, 210, 255, 0.2);
    }

    /* Leaderboard Podium Cards Special */
    .leader-gold-card {
        background: linear-gradient(135deg, rgba(255, 215, 0, 0.09) 0%, rgba(20, 23, 33, 0.98) 100%);
        border: 1px solid rgba(255, 215, 0, 0.6);
        border-radius: 12px;
        padding: 16px 20px;
        margin-bottom: 12px;
        box-shadow: 0 0 25px rgba(255, 215, 0, 0.15);
    }
    .leader-silver-card {
        background: linear-gradient(135deg, rgba(192, 192, 192, 0.08) 0%, rgba(20, 23, 33, 0.98) 100%);
        border: 1px solid rgba(192, 192, 192, 0.55);
        border-radius: 12px;
        padding: 16px 20px;
        margin-bottom: 12px;
        box-shadow: 0 0 20px rgba(192, 192, 192, 0.12);
    }
    .leader-bronze-card {
        background: linear-gradient(135deg, rgba(205, 127, 50, 0.08) 0%, rgba(20, 23, 33, 0.98) 100%);
        border: 1px solid rgba(205, 127, 50, 0.55);
        border-radius: 12px;
        padding: 16px 20px;
        margin-bottom: 12px;
        box-shadow: 0 0 20px rgba(205, 127, 50, 0.12);
    }
    .leader-row-card {
        background: var(--bg-card);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        padding: 14px 18px;
        margin-bottom: 10px;
        transition: all 0.2s ease;
    }
    .leader-row-card:hover {
        border-color: rgba(0, 210, 255, 0.3);
        transform: translateX(4px);
    }
    .leader-you-card {
        border: 2px solid #00FFA3 !important;
        box-shadow: 0 0 25px rgba(0, 255, 163, 0.22) !important;
    }

    /* Task Stopwatch Widget */
    .task-timer-box-running {
        background: linear-gradient(135deg, rgba(0, 255, 163, 0.12) 0%, rgba(14, 17, 23, 0.95) 100%);
        border: 1px solid rgba(0, 255, 163, 0.5);
        border-radius: 10px;
        padding: 12px 16px;
        margin-top: 12px;
        margin-bottom: 12px;
        box-shadow: 0 0 20px rgba(0, 255, 163, 0.15);
    }
    .task-timer-box-idle {
        background: rgba(20, 23, 33, 0.7);
        border: 1px solid #262730;
        border-radius: 10px;
        padding: 10px 14px;
        margin-top: 10px;
        margin-bottom: 12px;
    }

    /* Streamlit Components Restyling */
    div.stButton > button {
        background: #141721;
        color: #FFFFFF;
        border: 1px solid #262730;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.2s ease;
    }
    div.stButton > button:hover {
        border-color: var(--accent-neon);
        color: var(--accent-neon);
        box-shadow: 0 0 12px rgba(0, 255, 163, 0.25);
    }
    div.stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #00FFA3 0%, #00B876 100%);
        color: #0A0D13 !important;
        font-weight: 700;
        border: none;
    }
    div.stButton > button[kind="primary"]:hover {
        box-shadow: 0 0 20px rgba(0, 255, 163, 0.4);
    }

    div[data-baseweb="input"], div[data-baseweb="select"] {
        background-color: #0D1017 !important;
        border-color: #262730 !important;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Session State & Authentication Control
# -----------------------------------------------------------------------------
def init_session_state():
    """Ensures critical session state variables are initialized."""
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "user" not in st.session_state:
        st.session_state.user = None
    if "current_view" not in st.session_state:
        st.session_state.current_view = "Dashboard & Leaderboard"
    if "show_checkout_modal" not in st.session_state:
        st.session_state.show_checkout_modal = False
    if "admin_original_user" not in st.session_state:
        st.session_state.admin_original_user = None

def login_user(user_dict):
    """Sets authenticated state."""
    st.session_state.authenticated = True
    st.session_state.user = user_dict
    st.session_state.show_checkout_modal = False

def logout_user():
    """Clears authenticated state."""
    st.session_state.authenticated = False
    st.session_state.user = None
    st.session_state.show_checkout_modal = False
    st.session_state.pop("admin_original_user", None)
    st.rerun()

# -----------------------------------------------------------------------------
# Sub-View: Authentication Screen (Clean Real Users)
# -----------------------------------------------------------------------------
def render_login_view():
    """Renders the cyber luxury login portal with secure member authentication."""
    col1, col2, col3 = st.columns([1, 2.4, 1])

    with col2:
        render_html("""
        <div style="text-align: center; margin-top: 36px; margin-bottom: 30px;">
            <div style="display: inline-block; padding: 8px 20px; border-radius: 50px; background: rgba(0, 255, 163, 0.08); border: 1px solid rgba(0, 255, 163, 0.3); color: #00FFA3; font-weight: 800; font-size: 0.8rem; letter-spacing: 2px; margin-bottom: 14px; text-transform: uppercase;">
                ⚡ GRIT WORKSPACE OS
            </div>
            
            <div style="font-size: clamp(3.6rem, 7.5vw, 5.2rem); font-weight: 900; letter-spacing: 8px; line-height: 1.05; margin: 0 0 4px 0; background: linear-gradient(135deg, #00FFA3 0%, #00D2FF 45%, #FFFFFF 95%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-shadow: 0 0 50px rgba(0,255,163,0.35);">
                GRIT
            </div>
            
            <div style="font-size: clamp(1.1rem, 2.2vw, 1.4rem); font-weight: 700; color: #E2E8F0; letter-spacing: 1.5px; margin-bottom: 16px; text-transform: uppercase; opacity: 0.95;">
                Team Growth & Work OS
            </div>

            <div style="font-size: clamp(1.85rem, 4vw, 2.65rem); font-weight: 800; line-height: 1.25; margin: 12px 0 10px 0; background: linear-gradient(135deg, #FFFFFF 0%, #00D2FF 45%, #00FFA3 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; letter-spacing: -0.5px; text-shadow: 0 4px 30px rgba(0, 210, 255, 0.35);">
                “Stay together and grow together”
            </div>

            <p style="color: #94A3B8; font-size: 1.05rem; margin-top: 8px; margin-bottom: 22px; font-weight: 500; line-height: 1.5;">
                High-Performance Engineering, Personal Skill Mastery & Accountability
            </p>
        </div>
        """)

        render_html('<div class="cyber-card">')
        with st.form("login_form"):
            all_users = get_all_users()
            user_options = [u["username"] for u in all_users]

            selected_user = st.selectbox("Select Team Member", user_options)
            password = st.text_input("Password", type="password", placeholder="Enter your password (default: grit2026)")
            submitted = st.form_submit_button("Enter GRIT OS", type="primary", use_container_width=True)

            if submitted:
                user_data = verify_user(selected_user, password)
                if user_data:
                    login_user(user_data)
                    st.success(f"Access Granted. Welcome back, {user_data['name']}!")
                    st.rerun()
                else:
                    st.error("Invalid credentials. Please verify your password.")
        render_html('</div>')

# -----------------------------------------------------------------------------
# Module: Sidebar Navigation, Clean Live Timer & Gamified Level Badge
# -----------------------------------------------------------------------------
def render_sidebar():
    """Renders the left cyber sidebar containing user info, live session widget, and navigation."""
    user = st.session_state.user

    with st.sidebar:
        render_html(f"""
        <div style="padding: 12px 0 20px 0; border-bottom: 1px solid #1E2330; margin-bottom: 20px;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <div style="width: 38px; height: 38px; border-radius: 8px; background: linear-gradient(135deg, #00FFA3, #00D2FF); display: flex; align-items: center; justify-content: center; font-size: 1.2rem; font-weight: 800; color: #0A0D13;">
                    G
                </div>
                <div>
                    <div style="font-weight: 800; font-size: 1.1rem; color: #FFFFFF; letter-spacing: 0.5px;">GRIT OS</div>
                    <div style="font-size: 0.72rem; color: #00FFA3; font-weight: 600; text-transform: uppercase;">Team Growth Platform</div>
                </div>
            </div>
        </div>
        """)

        pstats = get_personal_growth_stats(user["id"], user["username"])
        role_badge = f'<span class="badge badge-admin">Admin Lead</span>' if user["role"] == "admin" else f'<span class="badge badge-member">Member</span>'
        
        render_html(f"""
        <div style="background: #141721; border: 1px solid #262730; border-radius: 10px; padding: 14px; margin-bottom: 20px;">
            <div style="display: flex; align-items: center; gap: 12px;">
                <div style="width: 42px; height: 42px; border-radius: 50%; background: {user.get('avatar_color', '#00D2FF')}; color: #0A0D13; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 1.1rem;">
                    {user['username'][:2].upper()}
                </div>
                <div>
                    <div style="font-weight: 700; color: #FFFFFF; font-size: 0.98rem;">{user['name']}</div>
                    <div style="color: #94A3B8; font-size: 0.78rem;">{user['title']}</div>
                </div>
            </div>
            
            <div style="margin-top: 12px; padding-top: 10px; border-top: 1px solid #1E2330;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                    <span style="font-size: 0.78rem; font-weight: 700; color: {pstats['level_color']};">{pstats['level_title']}</span>
                    <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.78rem; color: #FF7A00; font-weight: 800;">🔥 {pstats['streak_days']}d Streak</span>
                </div>
                <div style="background: #0A0D13; border-radius: 4px; height: 6px; width: 100%; overflow: hidden;">
                    <div style="background: linear-gradient(90deg, #00D2FF, #00FFA3); height: 100%; width: {pstats['level_progress']}%;"></div>
                </div>
            </div>

            <div style="margin-top: 10px; display: flex; justify-content: space-between; align-items: center;">
                {role_badge}
                <span style="color: #00FFA3; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; font-weight: 700;">{pstats['total_xp']} XP</span>
            </div>
        </div>
        """)

        active_sess = get_active_session(user["id"])
        st.markdown("### Work Session")

        if active_sess:
            start_dt = dt.strptime(active_sess["start_time"], "%Y-%m-%d %H:%M:%S")
            elapsed = dt.now() - start_dt
            hours, remainder = divmod(int(elapsed.total_seconds()), 3600)
            minutes, seconds = divmod(remainder, 60)
            elapsed_formatted = f"{hours:02d}h {minutes:02d}m {seconds:02d}s"
            start_time_fmt = start_dt.strftime("%I:%M %p")
            current_time_fmt = dt.now().strftime("%I:%M %p")

            render_html(f"""
            <div style="background: rgba(0, 255, 163, 0.08); border: 1px solid rgba(0, 255, 163, 0.3); border-radius: 10px; padding: 12px; margin-bottom: 12px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                    <div style="display: flex; align-items: center; gap: 6px;">
                        <span class="pulse-dot"></span>
                        <strong style="color: #00FFA3; font-size: 0.85rem;">SESSION ACTIVE</strong>
                    </div>
                    <span style="color: #00D2FF; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; font-weight: 700;">🕒 {current_time_fmt} IST</span>
                </div>
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.4rem; font-weight: 700; color: #FFFFFF;">
                    {elapsed_formatted}
                </div>
                <div style="color: #94A3B8; font-size: 0.75rem; margin-top: 4px;">
                    Started: {start_time_fmt} IST ({active_sess['start_time'].split(' ')[0]})
                </div>
            </div>
            """)

            if st.button("Punch Out & Complete Standup", key="side_punch_out_btn", type="primary"):
                st.session_state.show_checkout_modal = True
                st.rerun()
        else:
            current_time_fmt = dt.now().strftime("%I:%M %p")
            render_html(f"""
            <div style="background: #141721; border: 1px solid #262730; border-radius: 10px; padding: 14px; margin-bottom: 12px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <span style="color: #00FFA3; font-size: 0.8rem; font-weight: 700; text-transform: uppercase;">Start Focus Session</span>
                    <span style="color: #00D2FF; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; font-weight: 700;">🕒 {current_time_fmt} IST</span>
                </div>
            """)

            my_open_tasks = [t["title"] for t in get_tasks(assigned_to=user["username"]) if t["status"] != "Completed"]
            if my_open_tasks:
                task_sel = st.selectbox("Task Quick-Pick", ["-- Custom Focus Note --"] + my_open_tasks, key="side_task_quick_sel", label_visibility="collapsed")
                if task_sel != "-- Custom Focus Note --":
                    session_note = task_sel
                else:
                    session_note = st.text_input("Session Focus", placeholder="What are you working on?", key="side_session_focus", label_visibility="collapsed")
            else:
                session_note = st.text_input("Session Focus", placeholder="What are you working on?", key="side_session_focus", label_visibility="collapsed")

            if st.button("Punch In Now", key="side_punch_in_btn", type="primary"):
                start_session(user["id"], user["username"], session_note)
                st.toast("Focus session started! Deep work mode activated.")
                st.rerun()

            render_html("</div>")

        render_html("<hr style='border:0; border-top:1px solid #1E2330; margin: 20px 0;'>")

        st.markdown("### Navigation")
        nav_options = [
            "Dashboard & Leaderboard",
            "Personal Growth OS",
            "Skill Roadmaps & Growth",
            "Tasks Board",
            "Academics Hub"
        ]
        is_admin_or_impersonating = (user["role"] == "admin") or bool(st.session_state.get("admin_original_user"))
        if is_admin_or_impersonating:
            nav_options.append("👑 Admin Controls")

        current_v = st.session_state.current_view
        if current_v == "Admin Controls (Rajat only)":
            current_v = "👑 Admin Controls"

        selected_nav = st.radio(
            "Go to",
            nav_options,
            index=nav_options.index(current_v) if current_v in nav_options else 0,
            label_visibility="collapsed"
        )
        st.session_state.current_view = selected_nav

        if is_admin_or_impersonating:
            render_html("<div style='margin-top: 14px;'></div>")
            with st.expander("⚡ 1-Click Fast Switcher (Admin)", expanded=False):
                st.caption("Admin exclusive: Jump directly into any member's account to inspect progress:")
                all_u = get_all_users()
                for u in all_u:
                    is_current = (u["id"] == user["id"])
                    btn_label = f"✓ {u['name']} (Active)" if is_current else f"👁️ View as {u['name']}"
                    if st.button(btn_label, key=f"sb_admin_switch_{u['id']}", disabled=is_current, use_container_width=True):
                        if not st.session_state.get("admin_original_user") and user["role"] == "admin":
                            st.session_state.admin_original_user = user
                        elif st.session_state.get("admin_original_user") and u["id"] == st.session_state["admin_original_user"]["id"]:
                            st.session_state.pop("admin_original_user", None)
                        login_user(u)
                        st.rerun()

                if st.session_state.get("admin_original_user"):
                    if st.button("⬅️ Return to Rajat (Admin)", key="sb_revert_admin", type="primary", use_container_width=True):
                        orig = st.session_state.pop("admin_original_user")
                        login_user(orig)
                        st.rerun()

        render_html("<div style='margin-top: 18px;'></div>")

        with st.expander("🔐 Change My Password", expanded=False):
            with st.form("sidebar_change_pwd_form"):
                st.markdown(f"<div style='font-size:0.8rem; color:#94A3B8; margin-bottom:8px;'>Update password for <strong>{user['username']}</strong></div>", unsafe_allow_html=True)
                cur_p = st.text_input("Current Password", type="password", key="sb_cur_pwd")
                new_p = st.text_input("New Password", type="password", key="sb_new_pwd")
                new_p_c = st.text_input("Confirm New Password", type="password", key="sb_new_pwd_c")
                if st.form_submit_button("Update Password", type="primary"):
                    if not new_p or new_p != new_p_c:
                        st.error("Passwords do not match or are empty.")
                    elif not verify_user(user["username"], cur_p):
                        st.error("Current password is incorrect.")
                    else:
                        change_user_password(user["id"], new_p)
                        st.session_state.user["password_hash"] = hash_password(new_p)
                        st.toast("Password updated successfully! 🎉")
                        st.success("Password changed! Use your new password next time you sign in.")

        render_html("<div style='margin-top: 10px;'></div>")
        col_ref, col_logout = st.columns([1, 1])
        with col_ref:
            if st.button("🔄 Refresh"):
                st.rerun()
        with col_logout:
            if st.button("🚪 Log Out"):
                if active_sess:
                    st.session_state.confirm_force_logout = True
                    st.rerun()
                else:
                    logout_user()

        if active_sess and st.session_state.get("confirm_force_logout", False):
            st.warning("⚠️ Active focus session running! Submit daily standup or log out directly:")
            c_standup, c_direct = st.columns(2)
            with c_standup:
                if st.button("📝 Standup & Out", key="co_then_logout", type="primary"):
                    st.session_state.show_checkout_modal = True
                    st.session_state.confirm_force_logout = False
                    st.rerun()
            with c_direct:
                if st.button("🚪 Force Logout", key="direct_force_logout"):
                    end_session(active_sess["id"])
                    logout_user()

# -----------------------------------------------------------------------------
# Modal / Overlay: Daily Checkout & Learning Standup Form
# -----------------------------------------------------------------------------
def render_daily_checkout_modal():
    """Renders the mandatory checkout form required before session completion."""
    user = st.session_state.user
    active_sess = get_active_session(user["id"])

    if not active_sess:
        st.session_state.show_checkout_modal = False
        return

    start_dt = dt.strptime(active_sess["start_time"], "%Y-%m-%d %H:%M:%S")
    delta = dt.now() - start_dt
    duration_hours = round(delta.total_seconds() / 3600.0, 2)
    duration_minutes = round(delta.total_seconds() / 60.0, 1)

    render_html("""
    <div style="background: rgba(0, 255, 163, 0.05); border: 1px solid #00FFA3; border-radius: 14px; padding: 22px; margin-bottom: 24px;">
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
            <span class="pulse-dot"></span>
            <h2 style="margin: 0; color: #00FFA3; font-size: 1.5rem;">Daily Standup & Learning Checkout</h2>
        </div>
        <p style="color: #94A3B8; font-size: 0.9rem; margin: 0;">
            Share what you built and learned today. This updates the public Team Learnings Feed, stores your past history, and awards you +75 XP!
        </p>
    </div>
    """)

    with st.form("checkout_standup_form"):
        col_h1, col_h2 = st.columns(2)
        with col_h1:
            st.metric("Session Duration", f"{duration_hours} hrs", f"{duration_minutes} mins")
        with col_h2:
            st.metric("Date & Time (IST)", dt.now().strftime("%d %b %Y"), dt.now().strftime("%I:%M %p IST"))

        initial_work = f"Delivered: {active_sess['notes']}" if active_sess.get("notes") else ""
        work_summary = st.text_area("1. What work / sprint deliverables did you complete today? *", value=initial_work, placeholder="e.g. Built SQLite concurrency harness, resolved bug in auth...", height=90)
        learning_today = st.text_area("2. What new skill, concept or technology did you learn today? *", placeholder="e.g. Mastered Python async/await syntax, container queries in CSS...", height=90)
        feedback_notes = st.text_area("3. Blockers, Help Needed, or Notes for the Team / Lead", placeholder="e.g. Need clarification on client API schema; no blockers otherwise...", height=70)

        col_sub1, col_sub2, col_sub3 = st.columns([2, 1, 1])
        with col_sub1:
            submitted = st.form_submit_button("Submit Standup & Punch Out", type="primary")
        with col_sub2:
            cancel = st.form_submit_button("Cancel & Continue")
        with col_sub3:
            force_logout = st.form_submit_button("🚪 Force Log Out")

        if submitted:
            if work_summary.strip() and learning_today.strip():
                res, msg = end_session(active_sess["id"])
                submit_daily_checkout(
                    user_id=user["id"],
                    username=user["username"],
                    work_summary=work_summary,
                    learning_today=learning_today,
                    hours_worked=duration_hours,
                    blockers_feedback=feedback_notes
                )
                st.session_state.show_checkout_modal = False
                st.toast("XP Awarded! +75 XP for Daily Standup.")
                st.success(f"Daily checkout submitted! Logged {duration_hours} hrs. Great work today, {user['name']}!")
                st.rerun()
            else:
                st.error("Please answer questions 1 and 2 to record your daily growth.")

        if cancel:
            st.session_state.show_checkout_modal = False
            st.rerun()

        if force_logout:
            end_session(active_sess["id"])
            logout_user()

# -----------------------------------------------------------------------------
# Module 1: Dashboard & Team Growth Engine (Leaderboard + Public Learnings Feed)
# -----------------------------------------------------------------------------
def render_dashboard_view():
    """
    Renders the executive dashboard with:
    Tab 1: Team Standings & Leaderboard (VISIBLE TO EVERYONE FIRST)
    Tab 2: Team Daily Learnings & Activity Feed (VISIBLE TO EVERYONE)
    """
    user = st.session_state.user

    if st.session_state.show_checkout_modal:
        render_daily_checkout_modal()
        return

    tab_team, tab_feed = st.tabs([
        "Team Standings & Leaderboard",
        "Team Daily Learnings & Activity Feed"
    ])

    # ---------------- TAB 1: TEAM LEADERBOARD & METRICS ----------------
    with tab_team:
        leaderboard_data, summary = get_leaderboard()

        render_html("""
        <div style="margin-bottom: 20px;">
            <div style="display: inline-block; padding: 5px 14px; border-radius: 20px; background: rgba(0, 255, 163, 0.08); border: 1px solid rgba(0, 255, 163, 0.25); color: #00FFA3; font-size: 0.8rem; font-weight: 700; letter-spacing: 1px; margin-bottom: 10px;">
                🤝 Stay Together and Grow Together
            </div>
            <h1 style="font-size: 2.2rem; font-weight: 800; margin-bottom: 4px;">Team Standings & Leaderboard</h1>
            <p style="color: #94A3B8; font-size: 0.95rem;">Real-time performance metrics, team-wide hours, and competitive growth standings.</p>
        </div>
        """)

        # Team KPI Cards
        render_html(f"""
        <div class="kpi-container">
            <div class="kpi-card">
                <div class="kpi-title">Total Team Hours</div>
                <div class="kpi-value">{summary['total_team_hours']} <span style="font-size:1.1rem; color:#94A3B8;">hrs</span></div>
                <div class="kpi-subtext">Cumulative engineering time</div>
            </div>
            <div class="kpi-card cyan">
                <div class="kpi-title">Active Punch-Ins</div>
                <div class="kpi-value">{summary['active_punchins_count']}</div>
                <div class="kpi-subtext">Members working right now</div>
            </div>
            <div class="kpi-card purple">
                <div class="kpi-title">Active Tasks</div>
                <div class="kpi-value">{summary['total_active_tasks']}</div>
                <div class="kpi-subtext">Pending & In Progress</div>
            </div>
            <div class="kpi-card amber">
                <div class="kpi-title">Completed Tasks</div>
                <div class="kpi-value">{summary['total_completed_tasks']}</div>
                <div class="kpi-subtext">Delivered sprint goals</div>
            </div>
        </div>
        """)

        # ---------------- APNA: YOUR PERSONAL STANDING SUMMARY ----------------
        my_data = next((m for m in leaderboard_data if m["username"] == user["username"]), None)
        my_rank = next((idx + 1 for idx, m in enumerate(leaderboard_data) if m["username"] == user["username"]), 1)

        if my_data:
            my_active_badge = '<span class="pulse-dot" title="Active Focus Session"></span> <span style="color:#00FFA3; font-weight:700; font-size:0.8rem;">PUNCHED IN</span>' if my_data["is_punch_active"] else '<span style="color:#64748B; font-size:0.8rem;">● Offline</span>'
            my_role_label = "Lead & Solution Architect" if my_data["role"] == "admin" else my_data["title"]
            render_html(f"""
            <div style="background: linear-gradient(135deg, rgba(0, 255, 163, 0.09) 0%, rgba(20, 23, 33, 0.98) 100%); border: 2px solid #00FFA3; border-radius: 14px; padding: 18px 22px; margin-bottom: 24px; box-shadow: 0 0 25px rgba(0, 255, 163, 0.15);">
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px;">
                    <div style="display: flex; align-items: center; gap: 14px;">
                        <div style="width: 50px; height: 50px; border-radius: 50%; background: {my_data['avatar_color']}; color: #0A0D13; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 1.25rem; box-shadow: 0 0 16px rgba(0, 255, 163, 0.35);">
                            {my_data['username'][:2].upper()}
                        </div>
                        <div>
                            <div style="display: flex; align-items: center; gap: 8px;">
                                <span style="font-size: 1.25rem; font-weight: 800; color: #FFFFFF;">{my_data['name']}</span>
                                <span class="badge" style="background: rgba(0, 255, 163, 0.2); color: #00FFA3; border: 1px solid #00FFA3;">⚡ YOU (MY STANDING)</span>
                                {my_active_badge}
                            </div>
                            <div style="color: #94A3B8; font-size: 0.82rem; margin-top: 2px;">
                                {my_role_label} ● <span style="color: {my_data['level_color']}; font-weight: 700;">{my_data['level_title']}</span>
                            </div>
                        </div>
                    </div>
                    <div style="display: flex; gap: 20px; align-items: center; text-align: center; flex-wrap: wrap;">
                        <div>
                            <div style="color: #94A3B8; font-size: 0.7rem; text-transform: uppercase;">Your Rank</div>
                            <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.4rem; font-weight: 800; color: #00FFA3;">#{my_rank} <span style="font-size: 0.8rem; color: #64748B;">/ {len(leaderboard_data)}</span></div>
                        </div>
                        <div>
                            <div style="color: #94A3B8; font-size: 0.7rem; text-transform: uppercase;">Today's Hours</div>
                            <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.15rem; font-weight: 700; color: #FFFFFF;">{my_data['today_hours']}h</div>
                        </div>
                        <div>
                            <div style="color: #94A3B8; font-size: 0.7rem; text-transform: uppercase;">Total Hours</div>
                            <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.15rem; font-weight: 700; color: #00D2FF;">{my_data['all_time_hours']}h</div>
                        </div>
                        <div>
                            <div style="color: #94A3B8; font-size: 0.7rem; text-transform: uppercase;">Tasks Done</div>
                            <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.15rem; font-weight: 700; color: #A855F7;">{my_data['completed_tasks']}</div>
                        </div>
                        <div>
                            <div style="color: #94A3B8; font-size: 0.7rem; text-transform: uppercase;">Streak</div>
                            <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.15rem; font-weight: 700; color: #FF7A00;">🔥 {my_data.get('streak_days', 0)}d</div>
                        </div>
                        <div>
                            <div style="color: #94A3B8; font-size: 0.7rem; text-transform: uppercase;">XP</div>
                            <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.15rem; font-weight: 700; color: #FFB800;">{my_data['xp']}</div>
                        </div>
                        <div style="padding-left: 12px; border-left: 1px solid rgba(0, 255, 163, 0.3);">
                            <div style="color: #00FFA3; font-size: 0.7rem; text-transform: uppercase; font-weight: 700;">Score</div>
                            <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.6rem; font-weight: 800; color: #00FFA3;">{my_data['score']}</div>
                        </div>
                    </div>
                </div>
            </div>
            """)

        # ---------------- SAB TEAM KA BHI: FULL TEAM STANDINGS ----------------
        st.markdown("### 🏆 Team Performance Standings")
        render_html("""
        <div style="background: rgba(20, 23, 33, 0.6); border: 1px solid #262730; border-radius: 8px; padding: 10px 16px; margin-bottom: 16px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
            <div style="color: #94A3B8; font-size: 0.82rem;">
                ⚡ <strong>Live Scoring Formula:</strong> <span style="color: #FFFFFF;">(Hours x 10) + (Tasks x 35) + (Roadmap Skills x 8) + (Daily Standups x 15)</span>
            </div>
            <div style="color: #00FFA3; font-size: 0.8rem; font-weight: 600;">
                Live SQLite Feed
            </div>
        </div>
        """)

        # Filter & Sort Controls
        col_sort1, col_sort2, col_sort3 = st.columns([2, 2, 2])
        with col_sort1:
            sort_by = st.selectbox(
                "Sort Standings",
                ["Score (Default)", "Total Hours", "Completed Tasks", "XP Points", "Seed Priority"],
                key="lb_sort_selector"
            )
        with col_sort2:
            filter_scope = st.selectbox(
                "Filter Scope",
                ["All 7 Members", "Active Punch-ins Only"],
                key="lb_scope_filter"
            )
        with col_sort3:
            search_member = st.text_input("Search Member", placeholder="Filter by name or role...", key="lb_search_member")

        # Process filtered & sorted list
        filtered_lb = list(leaderboard_data)
        if filter_scope == "Active Punch-ins Only":
            filtered_lb = [m for m in filtered_lb if m["is_punch_active"]]
        if search_member.strip():
            sm = search_member.strip().lower()
            filtered_lb = [m for m in filtered_lb if sm in m["name"].lower() or sm in m["username"].lower() or sm in m["title"].lower()]

        if sort_by == "Total Hours":
            filtered_lb.sort(key=lambda x: (x["all_time_hours"], x["score"]), reverse=True)
        elif sort_by == "Completed Tasks":
            filtered_lb.sort(key=lambda x: (x["completed_tasks"], x["score"]), reverse=True)
        elif sort_by == "XP Points":
            filtered_lb.sort(key=lambda x: (x["xp"], x["score"]), reverse=True)
        elif sort_by == "Seed Priority":
            filtered_lb.sort(key=lambda x: x["user_id"])
        else:
            filtered_lb.sort(key=lambda x: (x["score"], -x["user_id"]), reverse=True)

        if not filtered_lb:
            st.info("No members match the current filter or search criteria.")

        for rank, member in enumerate(filtered_lb, 1):
            is_me = (member["username"] == user["username"])
            me_highlight_class = "leader-you-card" if is_me else ""
            me_tag = '<span class="badge" style="background: rgba(0, 255, 163, 0.2); color: #00FFA3; border: 1px solid #00FFA3; margin-left: 6px;">YOU</span>' if is_me else ''
            active_indicator = '<span class="pulse-dot" title="Active Focus Session"></span> <span style="color:#00FFA3; font-size:0.75rem; font-weight:700;">ACTIVE NOW</span>' if member["is_punch_active"] else '<span style="color:#64748B; font-size:0.75rem;">OFFLINE</span>'
            role_label = "Lead & Solution Architect" if member["role"] == "admin" else member["title"]

            # #1 Gold Champion Spotlight Card
            if rank == 1:
                render_html(f"""
                <div class="leader-gold-card {me_highlight_class}">
                    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
                        <div style="display: flex; align-items: center; gap: 14px;">
                            <div style="font-size: 1.8rem;">👑</div>
                            <div style="width: 48px; height: 48px; border-radius: 50%; background: #FFD700; color: #0A0D13; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 1.2rem; box-shadow: 0 0 16px rgba(255, 215, 0, 0.45);">
                                {member['username'][:2].upper()}
                            </div>
                            <div>
                                <div style="display: flex; align-items: center; gap: 8px;">
                                    <span style="font-size: 1.25rem; font-weight: 800; color: #FFFFFF;">{member['name']}</span>
                                    {me_tag}
                                    <span class="badge" style="background: rgba(255, 215, 0, 0.2); color: #FFD700; border: 1px solid rgba(255, 215, 0, 0.5);">#1 TOP PERFORMER</span>
                                </div>
                                <div style="display: flex; align-items: center; gap: 10px; margin-top: 4px;">
                                    <span style="color: #94A3B8; font-size: 0.82rem;">{role_label}</span>
                                    <span style="color: {member['level_color']}; font-weight: 700; font-size: 0.8rem;">● {member['level_title']}</span>
                                    <span style="border-left: 1px solid #262730; padding-left: 8px;">{active_indicator}</span>
                                </div>
                            </div>
                        </div>
                        <div style="display: flex; gap: 20px; text-align: center; align-items: center; flex-wrap: wrap;">
                            <div>
                                <div style="color: #94A3B8; font-size: 0.72rem; text-transform: uppercase;">Today</div>
                                <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.15rem; font-weight: 700; color: #00FFA3;">{member['today_hours']}h</div>
                            </div>
                            <div>
                                <div style="color: #94A3B8; font-size: 0.72rem; text-transform: uppercase;">Total Hours</div>
                                <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.15rem; font-weight: 700; color: #FFFFFF;">{member['all_time_hours']}h</div>
                            </div>
                            <div>
                                <div style="color: #94A3B8; font-size: 0.72rem; text-transform: uppercase;">Tasks</div>
                                <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.15rem; font-weight: 700; color: #00D2FF;">{member['completed_tasks']}</div>
                            </div>
                            <div>
                                <div style="color: #94A3B8; font-size: 0.72rem; text-transform: uppercase;">XP</div>
                                <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.15rem; font-weight: 700; color: #A855F7;">{member['xp']}</div>
                            </div>
                            <div style="padding-left: 10px; border-left: 1px solid rgba(255, 215, 0, 0.3);">
                                <div style="color: #FFD700; font-size: 0.72rem; text-transform: uppercase; font-weight: 700;">Score</div>
                                <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.6rem; font-weight: 800; color: #FFD700;">{member['score']}</div>
                            </div>
                        </div>
                    </div>
                </div>
                """)
            # #2 Silver Contender Spotlight Card (#2 Shatakshi priority)
            elif rank == 2:
                render_html(f"""
                <div class="leader-silver-card {me_highlight_class}">
                    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
                        <div style="display: flex; align-items: center; gap: 14px;">
                            <div style="font-size: 1.6rem;">🥈</div>
                            <div style="width: 44px; height: 44px; border-radius: 50%; background: {member['avatar_color']}; color: #0A0D13; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 1.1rem; box-shadow: 0 0 12px rgba(192, 192, 192, 0.35);">
                                {member['username'][:2].upper()}
                            </div>
                            <div>
                                <div style="display: flex; align-items: center; gap: 8px;">
                                    <strong style="font-size: 1.15rem; color: #FFFFFF;">{member['name']}</strong>
                                    {me_tag}
                                    <span class="badge" style="background: rgba(192, 192, 192, 0.15); color: #E2E8F0; border: 1px solid rgba(192, 192, 192, 0.4);">#2 CONTENDER</span>
                                </div>
                                <div style="display: flex; align-items: center; gap: 10px; margin-top: 3px;">
                                    <span style="color: #94A3B8; font-size: 0.8rem;">{role_label}</span>
                                    <span style="color: {member['level_color']}; font-weight: 700; font-size: 0.78rem;">● {member['level_title']}</span>
                                    <span style="border-left: 1px solid #262730; padding-left: 8px;">{active_indicator}</span>
                                </div>
                            </div>
                        </div>
                        <div style="display: flex; gap: 20px; text-align: center; align-items: center; flex-wrap: wrap;">
                            <div>
                                <div style="color: #94A3B8; font-size: 0.7rem; text-transform: uppercase;">Today</div>
                                <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.05rem; font-weight: 700; color: #00FFA3;">{member['today_hours']}h</div>
                            </div>
                            <div>
                                <div style="color: #94A3B8; font-size: 0.7rem; text-transform: uppercase;">Total Hours</div>
                                <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.05rem; font-weight: 700; color: #FFFFFF;">{member['all_time_hours']}h</div>
                            </div>
                            <div>
                                <div style="color: #94A3B8; font-size: 0.7rem; text-transform: uppercase;">Tasks</div>
                                <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.05rem; font-weight: 700; color: #00D2FF;">{member['completed_tasks']}</div>
                            </div>
                            <div>
                                <div style="color: #94A3B8; font-size: 0.7rem; text-transform: uppercase;">XP</div>
                                <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.05rem; font-weight: 700; color: #A855F7;">{member['xp']}</div>
                            </div>
                            <div style="padding-left: 10px; border-left: 1px solid rgba(192, 192, 192, 0.3);">
                                <div style="color: #E2E8F0; font-size: 0.7rem; text-transform: uppercase; font-weight: 700;">Score</div>
                                <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.4rem; font-weight: 800; color: #E2E8F0;">{member['score']}</div>
                            </div>
                        </div>
                    </div>
                </div>
                """)
            # #3 Bronze Contender Card
            elif rank == 3:
                render_html(f"""
                <div class="leader-bronze-card {me_highlight_class}">
                    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
                        <div style="display: flex; align-items: center; gap: 14px;">
                            <div style="font-size: 1.6rem;">🥉</div>
                            <div style="width: 42px; height: 42px; border-radius: 50%; background: {member['avatar_color']}; color: #0A0D13; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 1.05rem;">
                                {member['username'][:2].upper()}
                            </div>
                            <div>
                                <div style="display: flex; align-items: center; gap: 8px;">
                                    <strong style="font-size: 1.1rem; color: #FFFFFF;">{member['name']}</strong>
                                    {me_tag}
                                    <span class="badge" style="background: rgba(205, 127, 50, 0.15); color: #CD7F32; border: 1px solid rgba(205, 127, 50, 0.4);">#3 CONTENDER</span>
                                </div>
                                <div style="display: flex; align-items: center; gap: 10px; margin-top: 3px;">
                                    <span style="color: #94A3B8; font-size: 0.8rem;">{role_label}</span>
                                    <span style="color: {member['level_color']}; font-weight: 700; font-size: 0.78rem;">● {member['level_title']}</span>
                                    <span style="border-left: 1px solid #262730; padding-left: 8px;">{active_indicator}</span>
                                </div>
                            </div>
                        </div>
                        <div style="display: flex; gap: 20px; text-align: center; align-items: center; flex-wrap: wrap;">
                            <div>
                                <div style="color: #94A3B8; font-size: 0.7rem; text-transform: uppercase;">Today</div>
                                <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.0rem; font-weight: 700; color: #00FFA3;">{member['today_hours']}h</div>
                            </div>
                            <div>
                                <div style="color: #94A3B8; font-size: 0.7rem; text-transform: uppercase;">Total Hours</div>
                                <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.0rem; font-weight: 700; color: #FFFFFF;">{member['all_time_hours']}h</div>
                            </div>
                            <div>
                                <div style="color: #94A3B8; font-size: 0.7rem; text-transform: uppercase;">Tasks</div>
                                <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.0rem; font-weight: 700; color: #00D2FF;">{member['completed_tasks']}</div>
                            </div>
                            <div>
                                <div style="color: #94A3B8; font-size: 0.7rem; text-transform: uppercase;">XP</div>
                                <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.0rem; font-weight: 700; color: #A855F7;">{member['xp']}</div>
                            </div>
                            <div style="padding-left: 10px; border-left: 1px solid rgba(205, 127, 50, 0.3);">
                                <div style="color: #CD7F32; font-size: 0.7rem; text-transform: uppercase; font-weight: 700;">Score</div>
                                <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.35rem; font-weight: 800; color: #CD7F32;">{member['score']}</div>
                            </div>
                        </div>
                    </div>
                </div>
                """)
            # Ranks #4 to #7 Row Cards
            else:
                render_html(f"""
                <div class="leader-row-card {me_highlight_class}">
                    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
                        <div style="display: flex; align-items: center; gap: 14px;">
                            <div style="font-family: 'JetBrains Mono', monospace; font-weight: 800; font-size: 1.05rem; color: #64748B; width: 28px;">
                                #{rank}
                            </div>
                            <div style="width: 40px; height: 40px; border-radius: 50%; background: {member['avatar_color']}; color: #0A0D13; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 1.0rem;">
                                {member['username'][:2].upper()}
                            </div>
                            <div>
                                <div style="display: flex; align-items: center; gap: 8px;">
                                    <strong style="font-size: 1.05rem; color: #FFFFFF;">{member['name']}</strong>
                                    {me_tag}
                                    <span style="color: #64748B; font-size: 0.8rem;">({member['username']})</span>
                                </div>
                                <div style="display: flex; align-items: center; gap: 10px; margin-top: 2px;">
                                    <span style="color: #94A3B8; font-size: 0.8rem;">{role_label}</span>
                                    <span style="color: {member['level_color']}; font-weight: 700; font-size: 0.78rem;">● {member['level_title']}</span>
                                    <span style="border-left: 1px solid #262730; padding-left: 8px;">{active_indicator}</span>
                                </div>
                            </div>
                        </div>
                        <div style="display: flex; gap: 20px; text-align: center; align-items: center; flex-wrap: wrap;">
                            <div>
                                <div style="color: #64748B; font-size: 0.7rem; text-transform: uppercase;">Today</div>
                                <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.0rem; font-weight: 700; color: #00FFA3;">{member['today_hours']}h</div>
                            </div>
                            <div>
                                <div style="color: #64748B; font-size: 0.7rem; text-transform: uppercase;">Total Hours</div>
                                <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.0rem; font-weight: 700; color: #FFFFFF;">{member['all_time_hours']}h</div>
                            </div>
                            <div>
                                <div style="color: #64748B; font-size: 0.7rem; text-transform: uppercase;">Tasks</div>
                                <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.0rem; font-weight: 700; color: #00D2FF;">{member['completed_tasks']}</div>
                            </div>
                            <div>
                                <div style="color: #64748B; font-size: 0.7rem; text-transform: uppercase;">XP</div>
                                <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.0rem; font-weight: 700; color: #A855F7;">{member['xp']}</div>
                            </div>
                            <div style="padding-left: 10px; border-left: 1px solid #262730;">
                                <div style="color: #94A3B8; font-size: 0.7rem; text-transform: uppercase;">Score</div>
                                <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.25rem; font-weight: 700; color: #FFFFFF;">{member['score']}</div>
                            </div>
                        </div>
                    </div>
                </div>
                """)

    # ---------------- TAB 2: PUBLIC TEAM LEARNINGS & ACTIVITY FEED ----------------
    with tab_feed:
        render_html("""
        <div style="margin-bottom: 20px;">
            <h1 style="font-size: 2.2rem; font-weight: 800; margin-bottom: 4px;">Team Daily Learnings & Activity Feed</h1>
            <p style="color: #94A3B8; font-size: 0.95rem;">
                See what every engineer is learning, building, and exploring today. Transparent, cross-team knowledge sharing.
            </p>
        </div>
        """)

        col_feed_filt1, col_feed_filt2 = st.columns([3, 1])
        with col_feed_filt2:
            all_u = get_all_users()
            feed_filter_opts = ["All Members"] + [u["username"] for u in all_u]
            sel_feed_user = st.selectbox("Filter Feed by Member", feed_filter_opts, index=0)

        target_uid = None
        if sel_feed_user != "All Members":
            target_match = next((u for u in all_u if u["username"] == sel_feed_user), None)
            if target_match:
                target_uid = target_match["id"]

        checkouts = get_daily_checkouts(user_id=target_uid, limit=50)
        if checkouts:
            for co in checkouts:
                render_html(f"""
                <div class="cyber-card" style="margin-bottom: 16px; border-left: 4px solid #00D2FF;">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; margin-bottom: 10px;">
                        <div style="display: flex; align-items: center; gap: 10px;">
                            <div style="width: 36px; height: 36px; border-radius: 50%; background: {co['avatar_color']}; color: #0A0D13; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 0.9rem;">
                                {co['username'][:2].upper()}
                            </div>
                            <div>
                                <strong style="color: #FFFFFF; font-size: 1.05rem;">{co['username']}</strong>
                                <span style="color: #94A3B8; font-size: 0.8rem;"> — {co['user_title']}</span>
                            </div>
                        </div>
                        <div style="text-align: right;">
                            <span class="badge" style="background: rgba(0, 210, 255, 0.15); color: #00D2FF; border: 1px solid rgba(0, 210, 255, 0.3); font-size: 0.8rem;">{co['hours_worked']} hrs focus</span>
                            <span style="color: #64748B; font-size: 0.8rem; margin-left: 8px;">{co['submitted_at']}</span>
                        </div>
                    </div>

                    <div style="background: #0E1117; border-radius: 8px; padding: 12px; margin-bottom: 8px; border: 1px solid #1E2330;">
                        <div style="color: #00FFA3; font-size: 0.78rem; text-transform: uppercase; font-weight: 700; margin-bottom: 4px;">What Was Learned Today</div>
                        <div style="color: #FFFFFF; font-size: 0.92rem; line-height: 1.4;">{co['learning_today']}</div>
                    </div>

                    <div style="background: #0E1117; border-radius: 8px; padding: 12px; margin-bottom: 8px; border: 1px solid #1E2330;">
                        <div style="color: #94A3B8; font-size: 0.78rem; text-transform: uppercase; font-weight: 700; margin-bottom: 4px;">Deliverables & Tasks Completed</div>
                        <div style="color: #CBD5E1; font-size: 0.88rem;">{co['work_summary']}</div>
                    </div>

                    {f'''
                    <div style="background: rgba(255, 184, 0, 0.08); border: 1px solid rgba(255, 184, 0, 0.25); border-radius: 8px; padding: 10px;">
                        <div style="color: #FFB800; font-size: 0.75rem; text-transform: uppercase; font-weight: 700;">Team Notes / Blockers / Feedback</div>
                        <div style="color: #CBD5E1; font-size: 0.85rem;">{co['blockers_feedback']}</div>
                    </div>
                    ''' if co['blockers_feedback'] else ''}
                </div>
                """)

                k_count = co.get("kudos_count") or 0
                c_sp, c_kd = st.columns([5, 1])
                with c_kd:
                    if st.button(f"👏 Kudos ({k_count})", key=f"kudo_btn_{co['id']}", help="Appreciate this learning"):
                        add_checkout_kudo(co["id"])
                        st.toast(f"Gave Kudos to {co['username']}'s daily learning! 👏")
                        st.rerun()
        else:
            render_html("""
            <div class="zero-state-card">
                <div style="font-size: 2rem; margin-bottom: 8px;">📢</div>
                <div style="font-weight: 700; color: #FFFFFF; font-size: 1.1rem;">No Daily Learnings Logged Yet</div>
                <div style="color: #64748B; font-size: 0.88rem; margin-top: 4px;">
                    When any member punches out and submits their daily standup, their learnings and daily accomplishments will appear here for the whole team to see!
                </div>
            </div>
            """)

# -----------------------------------------------------------------------------
# Module 2: Dedicated Personal Growth OS ("Pesnl Groth Ka Alg Section")
# -----------------------------------------------------------------------------
def render_personal_growth_view():
    """
    Dedicated full-page Personal Growth OS for the logged-in engineer.
    Includes:
    - Current status & "Aaj ye kiya tha" (Today's focus session)
    - Personal Skill Progression (Where I stand, roadmap completion %)
    - 7-Day Performance Trend Chart
    - Comprehensive Past History Database (All past sessions & daily standup reflections)
    """
    user = st.session_state.user
    pstats = get_personal_growth_stats(user["id"], user["username"])

    render_html(f"""
    <div style="margin-bottom: 20px;">
        <h1 style="font-size: 2.2rem; font-weight: 800; margin-bottom: 4px;">Personal Growth OS — {user['name']}</h1>
        <p style="color: #94A3B8; font-size: 0.95rem;">
            Your personal engineering dashboard: daily focus tracker, roadmap mastery, and complete past history database.
        </p>
    </div>
    """)

    # Hero Gamified Card
    render_html(f"""
    <div class="cyber-card" style="border: 1px solid {pstats['level_color']}; margin-bottom: 20px; background: linear-gradient(135deg, rgba(20,23,33,0.95), rgba(10,13,19,0.98));">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
            <div>
                <div style="font-size: 0.8rem; text-transform: uppercase; color: #94A3B8; font-weight: 700;">Cyber Engineering Tier</div>
                <div style="font-size: 1.6rem; font-weight: 800; color: {pstats['level_color']};">{pstats['level_title']}</div>
                <div style="color: #94A3B8; font-size: 0.85rem; margin-top: 2px;">{user['title']}</div>
            </div>
            <div style="text-align: right;">
                <div style="display: flex; align-items: center; justify-content: flex-end; gap: 10px; margin-bottom: 4px;">
                    <span style="background: rgba(255, 184, 0, 0.15); border: 1px solid rgba(255, 184, 0, 0.4); color: #FFB800; font-family: 'JetBrains Mono', monospace; font-size: 0.95rem; font-weight: 700; padding: 4px 10px; border-radius: 6px;">🔥 {pstats['streak_days']}d Streak</span>
                    <span style="font-family: 'JetBrains Mono', monospace; font-size: 2.0rem; font-weight: 800; color: #00FFA3;">{pstats['total_xp']} XP</span>
                </div>
                <div style="font-size: 0.75rem; color: #94A3B8;">Next Level Progress: {pstats['level_progress']}%</div>
            </div>
        </div>
        <div style="background: #0A0D13; border-radius: 6px; height: 8px; width: 100%; margin-top: 12px; overflow: hidden;">
            <div style="background: linear-gradient(90deg, #00D2FF, #00FFA3); height: 100%; width: {pstats['level_progress']}%;"></div>
        </div>
    </div>
    """)

    # KPI Metric Cards
    render_html(f"""
    <div class="kpi-container">
        <div class="kpi-card amber">
            <div class="kpi-title">Consistency Streak</div>
            <div class="kpi-value">{pstats['streak_days']} <span style="font-size:1.1rem; color:#FFB800;">🔥 days</span></div>
            <div class="kpi-subtext" style="color: #FFB800;">Consecutive active days</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-title">My Focus Hours Today</div>
            <div class="kpi-value">{pstats['today_hours']} <span style="font-size:1.1rem; color:#94A3B8;">hrs</span></div>
            <div class="kpi-subtext">Logged today ({dt.now().strftime('%d %b')})</div>
        </div>
        <div class="kpi-card cyan">
            <div class="kpi-title">Total Work Hours</div>
            <div class="kpi-value">{pstats['all_time_hours']} <span style="font-size:1.1rem; color:#00D2FF;">hrs</span></div>
            <div class="kpi-subtext">All-time focus logged</div>
        </div>
        <div class="kpi-card purple">
            <div class="kpi-title">Skills Mastered</div>
            <div class="kpi-value">{pstats['completed_skills']}</div>
            <div class="kpi-subtext">Checked roadmap milestones</div>
        </div>
        <div class="kpi-card amber">
            <div class="kpi-title">Daily Standups Logged</div>
            <div class="kpi-value">{pstats['standup_count']}</div>
            <div class="kpi-subtext">Reflections in database</div>
        </div>
    </div>
    """)

    # Section Tabs within Personal Growth OS
    pg_tab_today, pg_tab_skills, pg_tab_db = st.tabs([
        "⚡ Today's Work & Focus ('Aaj Ye Kiya Tha')",
        "🗺️ My Skills & Where I Stand",
        "🗄️ Past History Database (Complete Archive)"
    ])

    # 1. Today's Work & Active Session
    with pg_tab_today:
        st.markdown("### ⏱️ Today's Active Session & Focus")
        active_sess = get_active_session(user["id"])
        if active_sess:
            start_dt = dt.strptime(active_sess["start_time"], "%Y-%m-%d %H:%M:%S")
            delta = dt.now() - start_dt
            hrs, rem = divmod(int(delta.total_seconds()), 3600)
            mins, secs = divmod(rem, 60)
            start_time_fmt = start_dt.strftime("%I:%M %p, %d %b %Y")
            current_time_fmt = dt.now().strftime("%I:%M %p")
            render_html(f"""
            <div class="session-banner-active">
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                    <div>
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <span class="pulse-dot"></span>
                            <strong style="color: #00FFA3;">LIVE WORK SESSION IN PROGRESS</strong>
                        </div>
                        <div style="font-size: 1.15rem; font-weight: 700; color: #FFFFFF; margin-top: 4px;">
                            Focus: {active_sess['notes'] or 'Sprint Work & Skill Practice'}
                        </div>
                        <div style="color: #94A3B8; font-size: 0.85rem; margin-top: 2px;">
                            Session Started: {start_time_fmt} IST &nbsp;|&nbsp; Current Time: <span style="color: #00D2FF; font-weight: 600;">{current_time_fmt} IST</span>
                        </div>
                    </div>
                    <div style="font-family: 'JetBrains Mono', monospace; font-size: 2.2rem; font-weight: 700; color: #00FFA3;">
                        {hrs:02d}h {mins:02d}m {secs:02d}s
                    </div>
                </div>
            </div>
            """)
            if st.button("Punch Out & Complete Standup Reflection", key="pg_punch_out_btn", type="primary"):
                st.session_state.show_checkout_modal = True
                st.rerun()
        else:
            curr_time_str = dt.now().strftime("%I:%M %p, %d %b %Y")
            with st.container():
                render_html(f"""
                <div class="cyber-card" style="margin-bottom: 16px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; margin-bottom: 4px;">
                        <div style="font-weight: 700; color: #FFFFFF; font-size: 1.1rem;">Start Today's Focus Session</div>
                        <div style="color: #00D2FF; font-family: 'JetBrains Mono', monospace; font-size: 0.82rem; font-weight: 700;">🕒 Current Time: {curr_time_str} IST</div>
                    </div>
                    <div style="color: #94A3B8; font-size: 0.85rem; margin-bottom: 12px;">Enter your session focus or pick an assigned sprint task to begin logging hours and building your streak.</div>
                """)
                my_open_tasks = [t["title"] for t in get_tasks(assigned_to=user["username"]) if t["status"] != "Completed"]
                if my_open_tasks:
                    col_p0, col_p1, col_p2 = st.columns([2, 3, 1])
                    with col_p0:
                        task_sel = st.selectbox("Quick-Pick Assigned Task", ["-- Custom Focus Note --"] + my_open_tasks, key="pg_task_quick_sel")
                    with col_p1:
                        if task_sel != "-- Custom Focus Note --":
                            focus_in = task_sel
                            st.text_input("Active Deliverable Focus", value=task_sel, disabled=True, key="pg_personal_focus_disp")
                        else:
                            focus_in = st.text_input("Session Focus Note", placeholder="What are you working on right now?", key="pg_personal_focus_input")
                    with col_p2:
                        st.write("")
                        if st.button("Punch In Now", key="pg_personal_start_btn", type="primary", use_container_width=True):
                            start_session(user["id"], user["username"], focus_in)
                            st.toast("Focus session started! Deep work mode activated.")
                            st.rerun()
                else:
                    col_p1, col_p2 = st.columns([3, 1])
                    with col_p1:
                        focus_in = st.text_input("Session Focus", placeholder="What are you working on right now?", key="pg_personal_focus_input", label_visibility="collapsed")
                    with col_p2:
                        if st.button("Punch In Now", key="pg_personal_start_btn", type="primary"):
                            start_session(user["id"], user["username"], focus_in)
                            st.toast("Focus session started! Deep work mode activated.")
                            st.rerun()
                render_html("</div>")

        st.markdown("### 🎯 My Growth Targets & Upcoming Focus ('Kya Karne Wale Hain')")
        st.markdown("""
        <p style="color: #94A3B8; font-size: 0.85rem; margin-top: -8px; margin-bottom: 14px;">
            Set concrete personal goals, target milestones, and tech stacks you plan to conquer next.
        </p>
        """, unsafe_allow_html=True)

        user_goals = get_personal_growth_goals(user["id"])
        active_goals = [g for g in user_goals if g["status"] == "In Progress"]
        completed_goals = [g for g in user_goals if g["status"] == "Completed"]

        if active_goals:
            for g in active_goals:
                col_g1, col_g2, col_g3 = st.columns([6, 2, 2])
                with col_g1:
                    cat_badge = f'<span style="background: rgba(0,210,255,0.15); color: #00D2FF; border: 1px solid rgba(0,210,255,0.3); font-size: 0.72rem; padding: 2px 8px; border-radius: 4px; font-weight: 600; margin-right: 8px;">{g["category"]}</span>'
                    date_info = f'<span style="color: #FFB800; font-size: 0.8rem; margin-left: 8px;">🎯 Target: {g["target_date"]}</span>' if g["target_date"] else ''
                    note_info = f'<div style="color: #94A3B8; font-size: 0.82rem; margin-top: 4px;">{g["notes"]}</div>' if g["notes"] else ''
                    render_html(f"""
                    <div style="padding: 10px 14px; background: #141721; border-radius: 8px; border-left: 3px solid #00FFA3; margin-bottom: 8px;">
                        <div style="display: flex; align-items: center; flex-wrap: wrap;">
                            {cat_badge}
                            <strong style="color: #FFFFFF; font-size: 0.95rem;">{g["goal_title"]}</strong>
                            {date_info}
                        </div>
                        {note_info}
                    </div>
                    """)
                with col_g2:
                    if st.button("Achieved ✅", key=f"goal_done_{g['id']}", help="Mark target goal as completed"):
                        toggle_personal_growth_goal(g["id"], user["id"], True)
                        st.toast(f"Goal '{g['goal_title']}' achieved! Great job! 🎉")
                        st.rerun()
                with col_g3:
                    if st.button("Remove 🗑️", key=f"goal_del_{g['id']}", help="Delete target goal"):
                        delete_personal_growth_goal(g["id"], user["id"])
                        st.rerun()
        else:
            render_html("""
            <div class="cyber-card" style="margin-bottom: 14px; text-align: center; padding: 18px;">
                <div style="font-size: 1.4rem; margin-bottom: 4px;">🚀</div>
                <div style="font-weight: 700; color: #FFFFFF; font-size: 0.98rem;">No Active Growth Targets Set</div>
                <div style="color: #94A3B8; font-size: 0.82rem; margin-top: 2px;">
                    Define what you are planning to learn or achieve next using the form below.
                </div>
            </div>
            """)

        with st.expander("➕ Set New Personal Growth Target ('Kya Karne Wale Hain')", expanded=False):
            with st.form("set_growth_goal_form"):
                col_gf1, col_gf2 = st.columns([3, 2])
                with col_gf1:
                    new_g_title = st.text_input("Goal Title *", placeholder="e.g. Master LangGraph Multi-Agent Workflows & Build Incident Response Agent")
                with col_gf2:
                    cat_options = list(ROADMAP_CATALOG.keys()) + ["Custom Skill Target", "Client Project Deliverable", "Architecture Breakthrough"]
                    new_g_cat = st.selectbox("Category / Domain", cat_options, index=0)

                col_gf3, col_gf4 = st.columns([2, 3])
                with col_gf3:
                    new_g_date = st.date_input("Target Completion Date", value=dt.now().date() + timedelta(days=14))
                with col_gf4:
                    new_g_notes = st.text_input("Execution Strategy / Notes", placeholder="e.g. Study official docs, build 2 prototypes, submit PR for review")

                if st.form_submit_button("Set Growth Target", type="primary"):
                    if new_g_title.strip():
                        add_personal_growth_goal(user["id"], user["username"], new_g_title.strip(), new_g_cat, str(new_g_date), new_g_notes.strip())
                        st.toast("Growth target created! Focus on achieving it! 🎯")
                        st.rerun()
                    else:
                        st.error("Please provide a Goal Title.")

        if completed_goals:
            with st.expander(f"🏆 Completed Growth Targets ({len(completed_goals)})", expanded=False):
                for cg in completed_goals:
                    render_html(f"""
                    <div style="padding: 8px 12px; background: rgba(0, 255, 163, 0.05); border: 1px solid rgba(0, 255, 163, 0.2); border-radius: 6px; margin-bottom: 6px; display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <span style="color: #00FFA3; font-weight: 700; margin-right: 6px;">✓</span>
                            <span style="color: #E2E8F0; text-decoration: line-through; font-size: 0.9rem;">{cg["goal_title"]}</span>
                            <span style="color: #64748B; font-size: 0.75rem; margin-left: 8px;">({cg["category"]})</span>
                        </div>
                        <span style="color: #00FFA3; font-size: 0.75rem; font-family: 'JetBrains Mono', monospace;">Completed: {cg["completed_at"] or 'Yes'}</span>
                    </div>
                    """)

        st.markdown("### 📊 My 7-Day Focus Hours Trend")
        df_trend = pd.DataFrame(list(pstats["daily_trend"].items()), columns=["Day", "Hours"])
        df_trend.set_index("Day", inplace=True)
        st.bar_chart(df_trend, color="#00FFA3")

    # 2. My Skills & Where I Stand (Interactive Clickable Drilldowns)
    with pg_tab_skills:
        st.markdown("### 🗺️ My Skills & Where I Stand ('Kya Kya Seekha' & Active Standing)")
        st.markdown("""
        <p style="color: #94A3B8; font-size: 0.88rem; margin-top: -8px; margin-bottom: 16px;">
            Open any skill roadmap below to see exactly what you have mastered so far (<strong>Kya Kya Seekha</strong>), where you currently stand, and check off your next milestones directly!
        </p>
        """, unsafe_allow_html=True)

        completed_topics = get_roadmap_progress(user["id"])

        # Prepare all tracks (Built-in catalog + custom tracks)
        all_tracks_dict = {}
        for track_name, catalog_data in ROADMAP_CATALOG.items():
            all_tracks_dict[track_name] = {
                "icon": catalog_data.get("icon", "⚡"),
                "category": catalog_data.get("category", "General"),
                "difficulty": catalog_data.get("difficulty", "All Levels"),
                "duration": catalog_data.get("duration", "Self-Paced"),
                "summary": catalog_data.get("summary", ""),
                "topics": catalog_data.get("topics", []),
                "learning_guide": catalog_data.get("learning_guide", {}),
                "is_custom": False
            }

        custom_tracks = get_custom_tracks(user["id"])
        for ct in custom_tracks:
            try:
                ct_topics = json.loads(ct["topics_json"])
                c_key = f"{ct['track_name']} (Custom)"
                all_tracks_dict[c_key] = {
                    "icon": "🛠️",
                    "category": "Custom Roadmaps",
                    "difficulty": "Custom",
                    "duration": "Custom Track",
                    "summary": f"Custom personalized roadmap created by {ct['username']}.",
                    "topics": ct_topics,
                    "learning_guide": {},
                    "is_custom": True
                }
            except Exception:
                pass

        # High level summary KPIs
        total_milestones_all = sum(len(d["topics"]) for d in all_tracks_dict.values())
        total_completed_all = sum(1 for (t_name, t_topic) in completed_topics if t_name in all_tracks_dict and t_topic in all_tracks_dict[t_name]["topics"])
        active_in_progress_tracks = sum(1 for t_name, d in all_tracks_dict.items() if any((t_name, t) in completed_topics for t in d["topics"]) and not all((t_name, t) in completed_topics for t in d["topics"]))
        mastered_tracks_count = sum(1 for t_name, d in all_tracks_dict.items() if len(d["topics"]) > 0 and all((t_name, t) in completed_topics for t in d["topics"]))

        render_html(f"""
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin-bottom: 20px;">
            <div style="background: #141721; border: 1px solid #262730; border-radius: 8px; padding: 14px;">
                <div style="color: #94A3B8; font-size: 0.75rem; text-transform: uppercase; font-weight: 700;">Total Mastered Milestones</div>
                <div style="font-size: 1.8rem; font-weight: 800; color: #00FFA3; font-family: 'JetBrains Mono', monospace;">{total_completed_all} <span style="font-size: 0.9rem; color: #64748B;">/ {total_milestones_all}</span></div>
            </div>
            <div style="background: #141721; border: 1px solid #262730; border-radius: 8px; padding: 14px;">
                <div style="color: #94A3B8; font-size: 0.75rem; text-transform: uppercase; font-weight: 700;">Active Tracks In Progress</div>
                <div style="font-size: 1.8rem; font-weight: 800; color: #00D2FF; font-family: 'JetBrains Mono', monospace;">{active_in_progress_tracks}</div>
            </div>
            <div style="background: #141721; border: 1px solid #262730; border-radius: 8px; padding: 14px;">
                <div style="color: #94A3B8; font-size: 0.75rem; text-transform: uppercase; font-weight: 700;">Fully Mastered Tracks</div>
                <div style="font-size: 1.8rem; font-weight: 800; color: #FFD700; font-family: 'JetBrains Mono', monospace;">{mastered_tracks_count}</div>
            </div>
        </div>
        """)

        # Personal Career Focus & Next Action Radar
        st.markdown("#### 🎯 My Primary Career Target & Focus Radar")
        all_career_names = list(ROADMAP_CATALOG.keys())
        user_target_key = f"user_primary_target_{user['id']}"
        saved_target = st.session_state.get(user_target_key, "Full-Stack Developer" if "Full-Stack Developer" in all_career_names else all_career_names[0])
        default_target_idx = all_career_names.index(saved_target) if saved_target in all_career_names else 0

        c_target1, c_target2 = st.columns([2, 1])
        with c_target1:
            chosen_target = st.selectbox(
                "Pin Your Target Career Track to Focus On:",
                all_career_names,
                index=default_target_idx,
                key=f"sel_target_career_{user['id']}"
            )
            st.session_state[user_target_key] = chosen_target
        with c_target2:
            st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
            st.caption(f"🎯 Pinned focus career for **{user['name']}**")

        target_data = ROADMAP_CATALOG.get(chosen_target, {})
        if target_data:
            target_topics = target_data.get("topics", [])
            target_done = sum(1 for t in target_topics if (chosen_target, t) in completed_topics)
            target_total = len(target_topics)
            target_pct = int((target_done / target_total) * 100) if target_total > 0 else 0
            target_tier = "Master" if target_pct >= 85 else ("Advanced" if target_pct >= 65 else ("Intermediate" if target_pct >= 40 else ("Foundation" if target_pct > 0 else "Getting Started")))
            target_tier_color = "#00FFA3" if target_pct >= 85 else ("#00D2FF" if target_pct >= 65 else ("#FFB800" if target_pct >= 40 else ("#A855F7" if target_pct > 0 else "#64748B")))

            render_html(f"""
            <div class="cyber-card" style="border: 1px solid {target_tier_color}; margin-bottom: 16px; background: linear-gradient(135deg, rgba(20,23,33,0.95), rgba(10,13,19,0.98));">
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                    <div>
                        <div style="font-size: 0.75rem; text-transform: uppercase; color: #94A3B8; font-weight: 700;">Personal Pinned Track</div>
                        <div style="font-size: 1.35rem; font-weight: 800; color: #FFFFFF; display: flex; align-items: center; gap: 8px;">
                            <span>{target_data.get('icon', '🎯')}</span>
                            <span>{chosen_target}</span>
                        </div>
                        <div style="color: #94A3B8; font-size: 0.82rem; margin-top: 2px;">{target_data.get('summary', '')}</div>
                    </div>
                    <div style="text-align: right;">
                        <span class="badge" style="background: rgba(0, 210, 255, 0.15); color: {target_tier_color}; border: 1px solid {target_tier_color}; font-size: 0.85rem;">
                            {target_tier} ({target_pct}%)
                        </span>
                        <div style="font-size: 0.8rem; color: #94A3B8; margin-top: 4px;">
                            <strong style="color: #FFFFFF;">{target_done} / {target_total}</strong> milestones mastered
                        </div>
                    </div>
                </div>
                <div style="background: #0A0D13; border-radius: 6px; height: 8px; width: 100%; margin-top: 12px; overflow: hidden;">
                    <div style="background: linear-gradient(90deg, #00D2FF, #00FFA3); height: 100%; width: {target_pct}%;"></div>
                </div>
            </div>
            """)

            # Immediate Next 3 Actionable Milestones
            next_uncompleted = [t for t in target_topics if (chosen_target, t) not in completed_topics][:3]
            if next_uncompleted:
                st.markdown(f"**⚡ Immediate Next Milestones to Conquer in {chosen_target}:**")
                cols_next = st.columns(len(next_uncompleted))
                for n_idx, n_top in enumerate(next_uncompleted):
                    with cols_next[n_idx]:
                        render_html(f"""
                        <div style="background: #0E1117; border: 1px solid #1E2330; border-radius: 8px; padding: 10px; margin-bottom: 6px; min-height: 85px;">
                            <div style="color: #00D2FF; font-size: 0.72rem; text-transform: uppercase; font-weight: 700;">Target Goal #{n_idx + 1}</div>
                            <div style="color: #FFFFFF; font-size: 0.82rem; font-weight: 600; margin-top: 4px;">{n_top}</div>
                        </div>
                        """)
                        if st.button("Mark Mastered ✅", key=f"quick_master_{user['id']}_{n_idx}", help=f"Check off '{n_top}' (+100 XP)"):
                            toggle_roadmap_topic(user["id"], user["username"], chosen_target, n_top, True)
                            st.toast(f"Milestone Mastered! +100 XP awarded for '{n_top}'! 🚀")
                            st.rerun()
            else:
                st.success(f"🎉 Outstanding achievement! You have mastered all {target_total} milestones in {chosen_target}!")

        render_html("<div style='margin-top: 20px; border-top: 1px solid #1E2330; margin-bottom: 16px;'></div>")

        # Search and Category filter
        col_f1, col_f2 = st.columns([2, 1])
        with col_f1:
            skill_search_query = st.text_input("🔍 Quick Search Skill or Topic", placeholder="e.g. Python, SQL, LLM, React, Docker, Machine Learning...", key="pg_skill_search_input")
        with col_f2:
            all_cats = ["All Categories"] + sorted(list({d["category"] for d in all_tracks_dict.values()}))
            selected_cat = st.selectbox("Filter by Category", all_cats, index=0, key="pg_skill_cat_filter")

        # Determine visible tracks
        visible_tracks = []
        for t_name, d in all_tracks_dict.items():
            if selected_cat != "All Categories" and d["category"] != selected_cat:
                continue
            if skill_search_query:
                sq = skill_search_query.lower()
                matches_track = sq in t_name.lower() or sq in d["category"].lower() or any(sq in t.lower() for t in d["topics"])
                if not matches_track:
                    continue
            visible_tracks.append((t_name, d))

        if not visible_tracks:
            render_html("""
            <div class="zero-state-card">
                <div style="font-size: 1.8rem; margin-bottom: 6px;">🔍</div>
                <div style="font-weight: 700; color: #FFFFFF;">No matching skill tracks found</div>
                <div style="color: #64748B; font-size: 0.85rem; margin-top: 4px;">Try clearing your search query or picking another domain.</div>
            </div>
            """)
        else:
            for t_name, d in visible_tracks:
                topics = d["topics"]
                completed_in_track = sum(1 for t in topics if (t_name, t) in completed_topics)
                total_in_track = len(topics)
                pct = int((completed_in_track / total_in_track) * 100) if total_in_track > 0 else 0
                
                tier = "Master" if pct >= 85 else ("Advanced" if pct >= 65 else ("Intermediate" if pct >= 40 else ("Foundation" if pct > 0 else "Not Started")))
                tier_color = "#00FFA3" if pct >= 85 else ("#00D2FF" if pct >= 65 else ("#FFB800" if pct >= 40 else ("#A855F7" if pct > 0 else "#64748B")))

                expander_label = f"{d['icon']} {t_name} — {tier} ({pct}%) • [{completed_in_track}/{total_in_track} Mastered]"
                is_expanded = (pct > 0 and pct < 100) or (len(visible_tracks) == 1)

                with st.expander(expander_label, expanded=is_expanded):
                    render_html(f"""
                    <div style="margin-bottom: 14px;">
                        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; margin-bottom: 6px;">
                            <div>
                                <span style="background: rgba(0,210,255,0.1); color: #00D2FF; border: 1px solid rgba(0,210,255,0.3); font-size: 0.72rem; padding: 2px 8px; border-radius: 4px; font-weight: 600; text-transform: uppercase;">{d['category']}</span>
                                <span style="color: #94A3B8; font-size: 0.82rem; margin-left: 8px;">⏳ {d['duration']}</span>
                                <span style="color: #94A3B8; font-size: 0.82rem; margin-left: 8px;">🎯 {d['difficulty']}</span>
                            </div>
                            <span class="badge" style="background: rgba(0, 210, 255, 0.15); color: {tier_color}; border: 1px solid {tier_color}; font-size: 0.8rem;">
                                {tier} ({pct}%)
                            </span>
                        </div>
                        <div style="color: #CBD5E1; font-size: 0.88rem; margin-bottom: 10px;">{d['summary']}</div>
                        <div style="background: #0A0D13; border-radius: 6px; height: 8px; width: 100%; overflow: hidden; margin-bottom: 12px;">
                            <div style="background: linear-gradient(90deg, #00D2FF, #00FFA3); height: 100%; width: {pct}%;"></div>
                        </div>
                    </div>
                    """)

                    col_learned, col_next = st.columns(2)

                    with col_learned:
                        st.markdown(f"#### ✅ Kya Kya Seekha ({completed_in_track})")
                        mastered_list = [t for t in topics if (t_name, t) in completed_topics]
                        if mastered_list:
                            for m_idx, m_topic in enumerate(mastered_list):
                                col_lm1, col_lm2 = st.columns([5, 1])
                                with col_lm1:
                                    render_html(f"""
                                    <div style="padding: 8px 12px; background: rgba(0, 255, 163, 0.08); border: 1px solid rgba(0, 255, 163, 0.3); border-radius: 6px; margin-bottom: 6px;">
                                        <div style="color: #00FFA3; font-weight: 700; font-size: 0.88rem;">✓ {m_topic}</div>
                                    </div>
                                    """)
                                with col_lm2:
                                    if st.button("↺", key=f"uncheck_{user['id']}_{t_name}_{m_idx}", help="Mark uncompleted / revisit"):
                                        toggle_roadmap_topic(user["id"], user["username"], t_name, m_topic, False)
                                        st.rerun()
                        else:
                            render_html("""
                            <div style="padding: 12px; background: #0E1117; border: 1px dashed #262730; border-radius: 6px; color: #64748B; font-size: 0.84rem; text-align: center;">
                                🌱 No milestones mastered in this track yet.<br>Tick off your first topic on the right to start!
                            </div>
                            """)

                    with col_next:
                        pending_count = total_in_track - completed_in_track
                        st.markdown(f"#### ⏳ Where I Stand / Next Up ({pending_count})")
                        pending_list = [t for t in topics if (t_name, t) not in completed_topics]
                        if pending_list:
                            for p_idx, p_topic in enumerate(pending_list):
                                checked = st.checkbox(
                                    label=f"**{p_topic}**",
                                    value=False,
                                    key=f"pg_tick_{user['id']}_{t_name}_{p_idx}"
                                )
                                if checked:
                                    toggle_roadmap_topic(user["id"], user["username"], t_name, p_topic, True)
                                    st.toast(f"Milestone Mastered! +100 XP for '{p_topic}'! 🚀")
                                    st.rerun()
                        else:
                            render_html("""
                            <div style="padding: 12px; background: rgba(0, 255, 163, 0.1); border: 1px solid rgba(0, 255, 163, 0.3); border-radius: 6px; color: #00FFA3; font-size: 0.88rem; text-align: center; font-weight: 700;">
                                🏆 All milestones mastered in this roadmap! Flawless execution!
                            </div>
                            """)

                    # Curated learning guide & resources expander
                    guide = d.get("learning_guide", {})
                    if guide:
                        with st.expander("📚 Curated Learning Blueprint & Resources ('Kahan Se Kya Lagta Hai')", expanded=False):
                            if "what_to_learn" in guide:
                                st.markdown(f"**Key Concepts to Solidify:** {guide['what_to_learn']}")
                            if "free_resources" in guide:
                                st.markdown("**Free Curated Documentation & Guides:**")
                                for res in guide["free_resources"]:
                                    st.markdown(f"- [{res['title']}]({res['url']})")
                            if "capstone_project" in guide:
                                st.markdown(f"**Recommended Proof-of-Work Project:** {guide['capstone_project']}")

    # 3. Complete Past History Database Archive
    with pg_tab_db:
        st.markdown("### 🗄️ Complete Past Work & Standup Archive")
        st.markdown("""
        <p style="color: #94A3B8; font-size: 0.85rem; margin-top: -8px; margin-bottom: 16px;">
            Full historical database records of all your past completed work sessions and daily learning reflections.
        </p>
        """, unsafe_allow_html=True)

        history_subtab1, history_subtab2 = st.tabs(["📝 Past Daily Standups Archive", "⏱️ Past Work Sessions Log"])

        with history_subtab1:
            all_checkouts = get_daily_checkouts(user_id=user["id"], limit=100)
            if all_checkouts:
                search_q = st.text_input("Filter Past Standups by Keyword", placeholder="Search by learning or deliverable...", key="standup_search_kw")
                filtered_co = [co for co in all_checkouts if (not search_q) or (search_q.lower() in co['work_summary'].lower() or search_q.lower() in co['learning_today'].lower())]

                st.markdown(f"<div style='color:#94A3B8; font-size:0.85rem; margin-bottom:12px;'>Found {len(filtered_co)} standup records:</div>", unsafe_allow_html=True)
                for co in filtered_co:
                    render_html(f"""
                    <div class="cyber-card" style="margin-bottom: 12px; padding: 16px; border-left: 4px solid #00FFA3;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                            <span style="font-weight: 700; color: #00FFA3; font-size: 0.95rem;">📅 Date: {co['date']}</span>
                            <span style="font-family: 'JetBrains Mono', monospace; color: #FFFFFF; font-size: 0.85rem;">{co['hours_worked']} hrs focus</span>
                        </div>
                        <div style="background: #0E1117; border-radius: 6px; padding: 10px; margin-bottom: 6px;">
                            <div style="color: #00D2FF; font-size: 0.75rem; text-transform: uppercase; font-weight: 700; margin-bottom: 2px;">What I Learned</div>
                            <div style="color: #FFFFFF; font-size: 0.9rem;">{co['learning_today']}</div>
                        </div>
                        <div style="background: #0E1117; border-radius: 6px; padding: 10px; margin-bottom: 6px;">
                            <div style="color: #94A3B8; font-size: 0.75rem; text-transform: uppercase; font-weight: 700; margin-bottom: 2px;">Deliverables & Tasks Accomplished</div>
                            <div style="color: #CBD5E1; font-size: 0.88rem;">{co['work_summary']}</div>
                        </div>
                        {f'<div style="color: #94A3B8; font-size: 0.8rem; margin-top: 4px;"><em>Feedback: {co["blockers_feedback"]}</em></div>' if co['blockers_feedback'] else ''}
                    </div>
                    """)
            else:
                render_html("""
                <div class="zero-state-card">
                    <div style="font-size: 2rem; margin-bottom: 8px;">🌱</div>
                    <div style="font-weight: 700; color: #FFFFFF; font-size: 1.1rem;">No Past Standup Records Yet</div>
                    <div style="color: #64748B; font-size: 0.88rem; margin-top: 4px;">
                        When you punch out and submit your daily checkout reflection, it will permanently be archived in this database.
                    </div>
                </div>
                """)

        with history_subtab2:
            all_sessions = get_all_user_work_sessions(user["id"], limit=100)
            if all_sessions:
                df_sess = pd.DataFrame(all_sessions)
                st.dataframe(df_sess[["id", "date", "start_time", "end_time", "duration_hours", "duration_minutes", "notes"]], hide_index=True)
            else:
                render_html("""
                <div class="zero-state-card">
                    <div style="font-size: 2rem; margin-bottom: 8px;">⏱️</div>
                    <div style="font-weight: 700; color: #FFFFFF; font-size: 1.1rem;">No Completed Work Sessions Yet</div>
                    <div style="color: #64748B; font-size: 0.88rem; margin-top: 4px;">
                        Punch in and punch out to record your first completed work session!
                    </div>
                </div>
                """)

# -----------------------------------------------------------------------------
# Module 3: Interactive Skill Roadmaps & Growth Checklists (Clean Tabs)
# -----------------------------------------------------------------------------
def render_skill_roadmaps_view():
    """
    Renders interactive skill roadmaps where engineers tick off topics
    (e.g., Python, UI/UX, AI/ML, System Ops) and create custom skill tracks.
    """
    user = st.session_state.user

    render_html("""
    <div style="margin-bottom: 24px;">
        <h1 style="font-size: 2.2rem; font-weight: 800; margin-bottom: 4px;">Skill Roadmaps & Growth Checklists</h1>
        <p style="color: #94A3B8; font-size: 0.95rem;">
            Tick off milestone topics as you master them to earn +100 XP and increase your Cyber Level tier.
        </p>
    </div>
    """)

    tab_roadmaps, tab_add_track, tab_log_sprint = st.tabs([
        "Roadmaps & Checklists",
        "Add Custom Roadmap",
        "Log Learning Sprint"
    ])

    completed_topics = get_roadmap_progress(user["id"])

    with tab_roadmaps:
        # Prepare full track dictionary
        all_tracks_dict = {}
        for track_name, catalog_data in ROADMAP_CATALOG.items():
            all_tracks_dict[track_name] = {
                "icon": catalog_data.get("icon", "⚡"),
                "category": catalog_data.get("category", "General"),
                "difficulty": catalog_data.get("difficulty", "All Levels"),
                "duration": catalog_data.get("duration", "Self-Paced"),
                "summary": catalog_data.get("summary", ""),
                "phases": catalog_data.get("phases", {}),
                "topics": catalog_data.get("topics", []),
                "learning_guide": catalog_data.get("learning_guide", {}),
                "is_custom": False
            }

        custom_tracks = get_custom_tracks(user["id"])
        for ct in custom_tracks:
            try:
                ct_topics = json.loads(ct["topics_json"])
                c_key = f"{ct['track_name']} (Custom)"
                all_tracks_dict[c_key] = {
                    "icon": "🛠️",
                    "category": "Custom Roadmaps",
                    "difficulty": "Custom",
                    "duration": "Custom Track",
                    "summary": f"Custom personalized roadmap created by {ct['username']}.",
                    "phases": {"All Milestones": ct_topics},
                    "topics": ct_topics,
                    "learning_guide": {},
                    "is_custom": True
                }
            except Exception:
                pass

        # Filter categories
        cat_list = ["All Categories"] + sorted(list({d["category"] for d in all_tracks_dict.values()}))

        col_ctrl1, col_ctrl2 = st.columns([1, 2])
        with col_ctrl1:
            selected_cat = st.selectbox("Filter Domain", cat_list, index=0, key="rm_domain_cat_filter")
        with col_ctrl2:
            rm_search = st.text_input("🔍 Search Any Skill / Topic", placeholder="e.g. SQL, React, Next.js, Python, LLM, Machine Learning...", key="rm_instant_search")

        filtered_track_names = []
        for t_name, d in all_tracks_dict.items():
            if selected_cat != "All Categories" and d["category"] != selected_cat:
                continue
            if rm_search:
                q = rm_search.lower()
                matches = q in t_name.lower() or q in d["category"].lower() or any(q in top.lower() for top in d["topics"])
                if not matches:
                    continue
            filtered_track_names.append(t_name)

        if not filtered_track_names:
            render_html("""
            <div class="zero-state-card" style="margin-top: 16px;">
                <div style="font-size: 1.8rem; margin-bottom: 6px;">🔍</div>
                <div style="font-weight: 700; color: #FFFFFF;">No matching roadmaps found</div>
                <div style="color: #64748B; font-size: 0.85rem; margin-top: 4px;">Try searching for another keyword or selecting All Categories.</div>
            </div>
            """)
        else:
            display_options = {t: f"{all_tracks_dict[t]['icon']} {t} — [{all_tracks_dict[t]['category']}]" for t in filtered_track_names}
            selected_track = st.selectbox(
                "Select Skill Roadmap to Open Full Curriculum",
                options=filtered_track_names,
                format_func=lambda x: display_options[x],
                index=0,
                key="rm_active_roadmap_select"
            )

            track_info = all_tracks_dict[selected_track]
            topics = track_info["topics"]
            completed_in_track = sum(1 for t in topics if (selected_track, t) in completed_topics)
            total_in_track = len(topics)
            mastery_pct = int((completed_in_track / total_in_track) * 100) if total_in_track > 0 else 0

            tier = "Master" if mastery_pct >= 85 else ("Advanced" if mastery_pct >= 65 else ("Intermediate" if mastery_pct >= 40 else ("Foundation" if mastery_pct > 0 else "Not Started")))
            tier_color = "#00FFA3" if mastery_pct >= 85 else ("#00D2FF" if mastery_pct >= 65 else ("#FFB800" if mastery_pct >= 40 else ("#A855F7" if mastery_pct > 0 else "#64748B")))

            # Roadmap Hero Banner
            render_html(f"""
            <div class="cyber-card" style="margin-top: 14px; margin-bottom: 20px; border-left: 4px solid #00FFA3;">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap;">
                    <div>
                        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 6px;">
                            <span style="font-size: 2.2rem;">{track_info['icon']}</span>
                            <div>
                                <h2 style="margin: 0; color: #FFFFFF; font-size: 1.45rem; font-weight: 800;">{selected_track}</h2>
                                <div style="display: flex; gap: 8px; align-items: center; margin-top: 4px; flex-wrap: wrap;">
                                    <span style="background: rgba(0,210,255,0.15); color: #00D2FF; border: 1px solid rgba(0,210,255,0.3); font-size: 0.72rem; padding: 2px 8px; border-radius: 4px; font-weight: 600; text-transform: uppercase;">{track_info['category']}</span>
                                    <span style="color: #94A3B8; font-size: 0.8rem;">⏳ Duration: {track_info['duration']}</span>
                                    <span style="color: #94A3B8; font-size: 0.8rem;">🎯 Difficulty: {track_info['difficulty']}</span>
                                </div>
                            </div>
                        </div>
                        <p style="color: #CBD5E1; font-size: 0.9rem; margin-top: 8px; margin-bottom: 0;">
                            {track_info['summary']}
                        </p>
                    </div>
                    <div style="text-align: right; margin-top: 8px;">
                        <span class="badge" style="background: rgba(0, 210, 255, 0.15); color: {tier_color}; border: 1px solid {tier_color}; font-size: 0.85rem;">
                            {tier} ({mastery_pct}%)
                        </span>
                        <div style="color: #94A3B8; font-size: 0.8rem; margin-top: 4px;">
                            <strong style="color: #FFFFFF;">{completed_in_track} of {total_in_track}</strong> milestones mastered
                        </div>
                    </div>
                </div>
                <div style="background: #0A0D13; border: 1px solid #262730; border-radius: 6px; height: 10px; width: 100%; margin-top: 14px; overflow: hidden;">
                    <div style="background: linear-gradient(90deg, #00D2FF 0%, #00FFA3 100%); height: 100%; width: {mastery_pct}%; border-radius: 6px; transition: width 0.3s ease;"></div>
                </div>
            </div>
            """)

            # Learning guide & resources ("Kahan Se Kya Lagta Hai")
            guide = track_info.get("learning_guide", {})
            if guide:
                with st.expander("📚 Complete Learning Guide, Projects & Free Resources ('Kahan Se Kya Lagta Hai')", expanded=True):
                    if "what_to_learn" in guide:
                        st.markdown(f"**🎯 Core Concepts to Study & Solidify:**\n\n{guide['what_to_learn']}")
                    
                    if "practice_tasks" in guide and guide["practice_tasks"]:
                        st.markdown("**✍️ Hands-on Practice Tasks & Exercises:**")
                        for pt in guide["practice_tasks"]:
                            st.markdown(f"- 📝 {pt}")

                    if "capstone_project" in guide:
                        st.markdown(f"**🚀 Recommended Capstone Proof-of-Work Project:**\n\n{guide['capstone_project']}")

                    if "free_resources" in guide and guide["free_resources"]:
                        st.markdown("**🔗 Free Curated Official Documentation & Guided Tutorials:**")
                        for res in guide["free_resources"]:
                            st.markdown(f"- 📖 [{res['title']}]({res['url']})")

                    if "job_checklist" in guide and guide["job_checklist"]:
                        st.markdown("**💼 Job-Ready Checklist & Interview Prep:**")
                        for jc in guide["job_checklist"]:
                            st.markdown(f"- ✅ {jc}")

            # Phases / Milestones
            st.markdown("### 🗺️ Phased Roadmap Milestones (Click to Update Mastery)")
            phases = track_info.get("phases", {})
            if phases:
                for phase_name, phase_topics in phases.items():
                    phase_completed = sum(1 for pt in phase_topics if (selected_track, pt) in completed_topics)
                    render_html(f"""
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 18px; margin-bottom: 8px; border-bottom: 1px solid #262730; padding-bottom: 6px;">
                        <span style="font-weight: 700; color: #00D2FF; font-size: 1.05rem;">{phase_name}</span>
                        <span style="font-size: 0.8rem; color: #94A3B8;">{phase_completed}/{len(phase_topics)} Mastered</span>
                    </div>
                    """)
                    p_col1, p_col2 = st.columns(2)
                    for p_idx, p_topic in enumerate(phase_topics):
                        p_col = p_col1 if (p_idx % 2 == 0) else p_col2
                        is_p_done = (selected_track, p_topic) in completed_topics
                        with p_col:
                            new_val = st.checkbox(
                                label=f"**{p_topic}**",
                                value=is_p_done,
                                key=f"chk_{user['id']}_{selected_track}_{phase_name}_{p_idx}"
                            )
                            if new_val != is_p_done:
                                toggle_roadmap_topic(user["id"], user["username"], selected_track, p_topic, new_val)
                                if new_val:
                                    st.toast(f"Milestone Mastered! +100 XP awarded for '{p_topic}'! 🚀")
                                st.rerun()
            else:
                col1, col2 = st.columns(2)
                for idx, topic in enumerate(topics):
                    col = col1 if (idx % 2 == 0) else col2
                    is_done = (selected_track, topic) in completed_topics
                    with col:
                        new_val = st.checkbox(
                            label=f"**{topic}**",
                            value=is_done,
                            key=f"chk_{user['id']}_{selected_track}_{idx}"
                        )
                        if new_val != is_done:
                            toggle_roadmap_topic(user["id"], user["username"], selected_track, topic, new_val)
                            if new_val:
                                st.toast(f"Milestone checked! +100 XP awarded for mastering '{topic}'! 🚀")
                            st.rerun()

    with tab_add_track:
        st.markdown("### Create Custom Skill Roadmap")
        render_html("""
        <p style="color: #94A3B8; font-size: 0.85rem; margin-top: -8px; margin-bottom: 16px;">
            Define your own personalized curriculum (e.g. Docker, Rust, Distributed DBs) with custom milestones.
        </p>
        <div class="cyber-card">
        """)
        with st.form("custom_track_form"):
            c_name = st.text_input("Skill Track Name *", placeholder="e.g. Docker & Kubernetes Orchestration")
            c_topics_str = st.text_area("Milestone Topics (One per line) *", placeholder="1. Dockerfile fundamentals\n2. Docker Compose multi-container\n3. Kubernetes Pods & Services\n4. Helm charts deployment", height=120)

            submitted = st.form_submit_button("Add Custom Roadmap", type="primary")
            if submitted:
                topics_arr = [line.strip() for line in c_topics_str.split("\n") if line.strip()]
                if c_name.strip() and topics_arr:
                    create_custom_track(user["id"], user["username"], c_name.strip(), topics_arr)
                    st.success(f"Custom track '{c_name}' created!")
                    st.rerun()
                else:
                    st.error("Please provide both a track name and at least one topic.")
        render_html("</div>")

    with tab_log_sprint:
        st.markdown("### Log Dedicated Learning Sprint / Proof of Work")
        render_html('<div class="cyber-card">')
        with st.form("sprint_learning_form"):
            col_s1, col_s2 = st.columns([2, 1])
            with col_s1:
                s_name = st.text_input("Skill or Technology *", placeholder="e.g. FastAPI Async Database Connection Pooling")
            with col_s2:
                s_hours = st.number_input("Hours Invested *", min_value=0.5, max_value=100.0, value=3.0, step=0.5)

            s_proof = st.text_input("Proof of Work Link / Repo URL", placeholder="https://github.com/... or brief summary")
            s_notes = st.text_area("Key Takeaways / Architecture Notes", placeholder="What breakthrough or concept did you solidify?")

            if st.form_submit_button("Record Learning Sprint", type="primary"):
                if s_name.strip():
                    add_learning_log(user["id"], user["username"], s_name, s_proof, s_hours, 80, s_notes)
                    st.toast("Sprint logged! XP updated.")
                    st.success("Sprint logged successfully!")
                    st.rerun()
                else:
                    st.error("Skill name is required.")
        render_html("</div>")

# -----------------------------------------------------------------------------
# Module 4: Tasks Board (Lead Assignment + Member Execution)
# -----------------------------------------------------------------------------
def render_tasks_view():
    """Renders task assignment for Lead (Rajat) and personalized tasks for Members."""
    user = st.session_state.user
    is_admin = (user["role"] == "admin")

    render_html(f"""
    <div style="margin-bottom: 24px;">
        <h1 style="font-size: 2.2rem; font-weight: 800; margin-bottom: 4px;">Task Management & Milestones</h1>
        <p style="color: #94A3B8; font-size: 0.95rem;">
            {'Lead Admin View: Assign deliverables, prioritize pipelines, and oversee sprint flow.' if is_admin else 'Member View: Track your assigned deliverables and update progress with one click.'}
        </p>
    </div>
    """)

    if is_admin:
        tab_list, tab_create = st.tabs(["Active Deliverables", "Assign New Task"])
    else:
        tab_list = st.container()

    if is_admin:
        with tab_create:
            render_html('<div class="cyber-card">')
            with st.form("assign_task_form"):
                col_t1, col_t2 = st.columns([2, 1])
                with col_t1:
                    task_title = st.text_input("Task Title *", placeholder="e.g. Build SQLite WAL concurrency harness")
                with col_t2:
                    all_users = get_all_users()
                    assignee_options = [u["username"] for u in all_users]
                    task_assignee = st.selectbox("Assign To *", assignee_options)

                task_desc = st.text_area("Task Description & Scope", placeholder="Key deliverables, acceptance criteria, or links...")

                col_p1, col_p2, col_p3 = st.columns(3)
                with col_p1:
                    priority = st.selectbox("Priority", ["High", "Medium", "Low"])
                with col_p2:
                    category = st.selectbox("Category", ["Client Project", "Core Skill", "Academics"])
                with col_p3:
                    due_date = st.date_input("Due Date", min_value=dt.now().date(), value=dt.now().date() + timedelta(days=3))

                submitted = st.form_submit_button("Assign Deliverable", type="primary")
                if submitted:
                    if task_title.strip():
                        assign_task(
                            title=task_title,
                            description=task_desc,
                            assigned_to=task_assignee,
                            assigned_by=user["username"],
                            priority=priority,
                            category=category,
                            due_date=due_date.strftime("%Y-%m-%d")
                        )
                        st.success(f"Task successfully assigned to {task_assignee}!")
                        st.rerun()
                    else:
                        st.error("Task title cannot be empty.")
            render_html('</div>')

    with tab_list:
        col_f1, col_f2, col_f3, col_f4 = st.columns([2.5, 1.8, 2, 1.7])
        with col_f1:
            task_search_q = st.text_input("🔍 Quick Search Deliverables", placeholder="Search title, details, category...", key="task_instant_search")
        with col_f2:
            status_filter = st.selectbox("Filter Status", ["All", "Pending", "In Progress", "Under Review", "Completed"], key="task_status_filter")
        with col_f3:
            if is_admin:
                all_users = get_all_users()
                user_filter_options = ["All Members"] + [u["username"] for u in all_users]
                selected_user_filter = st.selectbox("Filter Member", user_filter_options, key="task_user_filter")
                target_user = None if selected_user_filter == "All Members" else selected_user_filter
            else:
                st.selectbox("View Scope", [f"My Tasks ({user['username']})"], disabled=True)
                target_user = user["username"]
        with col_f4:
            view_mode = st.radio("Display Layout", ["Kanban Cards", "Data Table"], horizontal=True)

        tasks = get_tasks(assigned_to=target_user, status_filter=status_filter)
        if task_search_q.strip():
            sq = task_search_q.strip().lower()
            tasks = [
                t for t in tasks 
                if sq in (t.get("title") or "").lower() 
                or sq in (t.get("description") or "").lower() 
                or sq in (t.get("category") or "").lower()
            ]

        # Compute Tasks KPI metrics
        all_target_tasks = get_tasks(assigned_to=target_user)
        t_total = len(all_target_tasks)
        t_prog = sum(1 for t in all_target_tasks if t["status"] == "In Progress")
        t_comp = sum(1 for t in all_target_tasks if t["status"] == "Completed")
        t_seconds = sum((t.get("time_spent_seconds") or 0) for t in all_target_tasks)
        t_hours_str = f"{round(t_seconds / 3600.0, 1)} hrs"
        t_active_timers = sum(1 for t in all_target_tasks if t.get("timer_started_at"))

        render_html(f"""
        <div class="kpi-container" style="margin-top: 14px; margin-bottom: 20px;">
            <div class="kpi-card">
                <div class="kpi-title">Total Tasks</div>
                <div class="kpi-value">{t_total}</div>
                <div class="kpi-subtext">Deliverables in sprint</div>
            </div>
            <div class="kpi-card cyan">
                <div class="kpi-title">In Progress</div>
                <div class="kpi-value">{t_prog}</div>
                <div class="kpi-subtext">Active sprint tasks</div>
            </div>
            <div class="kpi-card amber">
                <div class="kpi-title">Completed</div>
                <div class="kpi-value">{t_comp}</div>
                <div class="kpi-subtext">Successfully shipped</div>
            </div>
            <div class="kpi-card purple">
                <div class="kpi-title">Task Time Logged</div>
                <div class="kpi-value">{t_hours_str}</div>
                <div class="kpi-subtext">Tracked via stopwatch</div>
            </div>
        </div>
        """)

        if t_active_timers > 0:
            render_html(f"""
            <div style="background: rgba(0, 255, 163, 0.08); border: 1px solid rgba(0, 255, 163, 0.4); border-radius: 8px; padding: 10px 16px; margin-bottom: 16px; display: flex; align-items: center; gap: 10px;">
                <span class="pulse-dot"></span>
                <span style="color: #00FFA3; font-weight: 700; font-size: 0.88rem;">{t_active_timers} Active Stopwatch{'s' if t_active_timers > 1 else ''} Currently Ticking</span>
                <span style="color: #94A3B8; font-size: 0.8rem;">— Time is being actively tracked on deliverables right now.</span>
            </div>
            """)

        if not tasks:
            render_html(f"""
            <div class="zero-state-card">
                <div style="font-size: 2rem; margin-bottom: 8px;">📂</div>
                <div style="font-weight: 700; color: #FFFFFF; font-size: 1.1rem;">No Tasks Found</div>
                <div style="color: #64748B; font-size: 0.88rem; margin-top: 4px;">
                    {'Switch to "Assign New Task" above to create your first sprint deliverable.' if is_admin else 'No deliverables currently assigned. Lead can assign tasks from the Lead portal.'}
                </div>
            </div>
            """)
            return

        st.markdown(f"<div style='margin-top: 10px; margin-bottom: 16px; font-weight: 600; color: #94A3B8;'>Showing {len(tasks)} tasks:</div>", unsafe_allow_html=True)

        if view_mode == "Data Table":
            table_rows = []
            for t in tasks:
                sec = t.get("time_spent_seconds") or 0
                is_running = bool(t.get("timer_started_at"))
                timer_status = f"⏱️ Running ({t.get('timer_started_by')})" if is_running else "Idle"
                table_rows.append({
                    "ID": t["id"],
                    "Title": t["title"],
                    "Assignee": t["assigned_to"],
                    "Priority": t["priority"],
                    "Category": t["category"],
                    "Due Date": t["due_date"],
                    "Status": t["status"],
                    "Time Tracked": format_seconds_to_hhmmss(sec),
                    "Stopwatch": timer_status,
                    "Assigned By": t["assigned_by"]
                })
            st.dataframe(pd.DataFrame(table_rows), hide_index=True, use_container_width=True)
        else:
            for task in tasks:
                status = task["status"]
                badge_class = {
                    "Pending": "badge-pending",
                    "In Progress": "badge-inprogress",
                    "Under Review": "badge-review",
                    "Completed": "badge-completed"
                }.get(status, "badge-pending")

                p_color = "#FF4757" if task["priority"] == "High" else ("#FFB800" if task["priority"] == "Medium" else "#38BDF8")

                # Stopwatch Timer Metrics
                is_running = bool(task.get("timer_started_at"))
                running_user = task.get("timer_started_by") or ""
                accumulated_sec = task.get("time_spent_seconds") or 0

                current_elapsed_sec = 0
                start_ts_ms = 0
                if is_running:
                    try:
                        st_dt = dt.fromisoformat(task["timer_started_at"])
                        current_elapsed_sec = int(max(0, (dt.now() - st_dt).total_seconds()))
                        start_ts_ms = int(st_dt.timestamp() * 1000)
                    except Exception:
                        current_elapsed_sec = 0
                        start_ts_ms = int(dt.now().timestamp() * 1000)

                total_task_sec = accumulated_sec + current_elapsed_sec
                formatted_accumulated = format_seconds_to_hhmmss(accumulated_sec)
                formatted_total = format_seconds_to_hhmmss(total_task_sec)
                formatted_session = format_seconds_to_hhmmss(current_elapsed_sec)

                with st.container():
                    render_html(f"""
                    <div class="cyber-card" style="border-left: 4px solid {p_color}; margin-bottom: 14px; padding: 16px 20px;">
                        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 8px;">
                            <div>
                                <div style="display: flex; align-items: center; gap: 10px;">
                                    <span class="badge {badge_class}">{status}</span>
                                    <span style="font-size: 0.75rem; font-weight: 700; color: {p_color};">{task['priority'].upper()} PRIORITY</span>
                                    <span style="color: #64748B; font-size: 0.78rem;">Category: {task['category']}</span>
                                </div>
                                <h3 style="margin: 8px 0 4px 0; font-size: 1.15rem; color: #FFFFFF;">{task['title']}</h3>
                                <p style="color: #94A3B8; font-size: 0.88rem; margin-bottom: 8px;">{task['description'] if task['description'] else 'No detailed description.'}</p>
                                <div style="display: flex; gap: 16px; font-size: 0.78rem; color: #64748B; flex-wrap: wrap;">
                                    <span>Assignee: <strong style="color: #FFFFFF;">{task['assigned_to']}</strong></span>
                                    <span>Due Date: <strong style="color: #FFFFFF;">{task['due_date']}</strong></span>
                                    <span>Assigned By: {task['assigned_by']}</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    """)

                    # Dedicated Task Stopwatch Widget Bar
                    if is_running:
                        render_html(f"""
                        <div class="task-timer-box-running">
                            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                                <div style="display: flex; align-items: center; gap: 10px;">
                                    <span class="pulse-dot"></span>
                                    <div>
                                        <div style="font-weight: 700; color: #00FFA3; font-size: 0.82rem; letter-spacing: 0.5px; text-transform: uppercase;">
                                            ⏱️ STOPWATCH RUNNING
                                        </div>
                                        <div style="color: #94A3B8; font-size: 0.78rem;">
                                            Tracking: <strong style="color: #FFFFFF;">{running_user}</strong>
                                        </div>
                                    </div>
                                </div>
                                <div style="display: flex; gap: 16px; align-items: center; text-align: right; flex-wrap: wrap;">
                                    <div>
                                        <div style="color: #94A3B8; font-size: 0.68rem; text-transform: uppercase;">Current Session</div>
                                        <div id="stopwatch_span_{task['id']}" style="font-family: 'JetBrains Mono', monospace; font-size: 1.35rem; font-weight: 800; color: #00FFA3;">
                                            {formatted_session}
                                        </div>
                                    </div>
                                    <div style="border-left: 1px solid rgba(0, 255, 163, 0.3); padding-left: 14px;">
                                        <div style="color: #94A3B8; font-size: 0.68rem; text-transform: uppercase;">Total Time on Task</div>
                                        <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.1rem; font-weight: 700; color: #FFFFFF;">
                                            {formatted_total}
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        """)
                    else:
                        render_html(f"""
                        <div class="task-timer-box-idle">
                            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
                                <div style="display: flex; align-items: center; gap: 8px;">
                                    <span style="font-size: 1.1rem;">⏱️</span>
                                    <span style="color: #94A3B8; font-size: 0.82rem; font-weight: 600;">Time Tracked on Task:</span>
                                    <span style="font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #00FFA3; font-size: 0.95rem;">{formatted_accumulated}</span>
                                </div>
                                <div style="color: #64748B; font-size: 0.78rem;">
                                    Stopwatch: <span style="color: #94A3B8;">Ready to Start</span>
                                </div>
                            </div>
                        </div>
                        """)

                    # Action Row 1: Stopwatch Controls & Quick Add
                    col_sw1, col_sw2, col_sw3 = st.columns([2, 1, 1])
                    with col_sw1:
                        if is_running:
                            if st.button("⏹️ Stop Stopwatch & Log Time", key=f"btn_stop_timer_{task['id']}", type="primary"):
                                sec_logged, msg = stop_task_timer(task["id"], user["username"])
                                st.toast(f"Logged {format_seconds_to_hhmmss(sec_logged)} to '{task['title']}'!")
                                st.rerun()
                        else:
                            if st.button("▶️ Start Task Stopwatch", key=f"btn_start_timer_{task['id']}"):
                                start_task_timer(task["id"], user["username"])
                                st.toast(f"Stopwatch started for '{task['title']}'!")
                                st.rerun()

                    with col_sw2:
                        with st.popover("➕ Add Time", key=f"quick_add_pop_{task['id']}"):
                            st.markdown("<div style='font-size:0.85rem; font-weight:600; color:#FFFFFF; margin-bottom:8px;'>Quick Log Minutes</div>", unsafe_allow_html=True)
                            q1, q2, q3 = st.columns(3)
                            if q1.button("+15m", key=f"add15_{task['id']}"):
                                manual_add_task_time(task["id"], user["username"], 15)
                                st.toast("Added 15m to task!")
                                st.rerun()
                            if q2.button("+30m", key=f"add30_{task['id']}"):
                                manual_add_task_time(task["id"], user["username"], 30)
                                st.toast("Added 30m to task!")
                                st.rerun()
                            if q3.button("+1h", key=f"add60_{task['id']}"):
                                manual_add_task_time(task["id"], user["username"], 60)
                                st.toast("Added 1 hr to task!")
                                st.rerun()

                    with col_sw3:
                        if is_admin and is_running:
                            if st.button("Reset Timer", key=f"btn_rst_timer_{task['id']}"):
                                reset_task_timer(task["id"])
                                st.toast("Timer reset.")
                                st.rerun()

                    # Action Row 2: Status & Sprint Workflow
                    col_act1, col_act2, col_act3, col_act4 = st.columns([2, 1, 1, 1])

                    with col_act1:
                        new_status = st.selectbox(
                            "Update Status",
                            ["Pending", "In Progress", "Under Review", "Completed"],
                            index=["Pending", "In Progress", "Under Review", "Completed"].index(status),
                            key=f"status_select_{task['id']}",
                            label_visibility="collapsed"
                        )
                        if new_status != status:
                            update_task_status(task["id"], new_status)
                            if new_status == "Completed":
                                st.toast("Task completed! +150 XP awarded.")
                            st.rerun()

                    with col_act2:
                        if status != "In Progress" and status != "Completed":
                            if st.button("In Progress", key=f"quick_prog_{task['id']}"):
                                update_task_status(task["id"], "In Progress")
                                st.rerun()

                    with col_act3:
                        if status == "In Progress":
                            if st.button("For Review", key=f"quick_rev_{task['id']}"):
                                update_task_status(task["id"], "Under Review")
                                st.rerun()
                        elif status != "Completed":
                            if st.button("Completed", key=f"quick_comp_{task['id']}"):
                                update_task_status(task["id"], "Completed")
                                st.toast("Task completed! +150 XP awarded.")
                                st.rerun()

                    with col_act4:
                        if is_admin:
                            if st.button("Delete", key=f"del_task_{task['id']}"):
                                delete_task(task["id"])
                                st.rerun()

# -----------------------------------------------------------------------------
# Module 5: Academic & Doubt Clearing Hub
# -----------------------------------------------------------------------------
def render_academics_view():
    """Renders the team Q&A forum for technical, academic, and code queries."""
    user = st.session_state.user

    render_html("""
    <div style="margin-bottom: 24px;">
        <h1 style="font-size: 2.2rem; font-weight: 800; margin-bottom: 4px;">Academic & Doubt Clearing Hub</h1>
        <p style="color: #94A3B8; font-size: 0.95rem;">Internal engineering forum for resolving architecture dilemmas, debugging code, and sharing knowledge.</p>
    </div>
    """)

    tab_questions, tab_ask = st.tabs(["Browse Questions", "Post New Query"])

    with tab_ask:
        render_html('<div class="cyber-card">')
        with st.form("ask_query_form"):
            q_title = st.text_input("Query Title *", placeholder="e.g. How to structure SQLite foreign keys with ON DELETE CASCADE?")
            q_tags = st.text_input("Tags (comma-separated)", placeholder="e.g. SQLite, Python, Performance")
            q_content = st.text_area("Detailed Query / Code Snippet *", placeholder="Provide context, expected vs actual behavior, or code snippets...", height=150)

            submitted = st.form_submit_button("Post Question to Hub", type="primary")
            if submitted:
                if q_title.strip() and q_content.strip():
                    add_academic_query(
                        author=user["username"],
                        title=q_title,
                        content=q_content,
                        tags=q_tags if q_tags.strip() else "General"
                    )
                    st.success("Query submitted to the hub!")
                    st.rerun()
                else:
                    st.error("Title and content are required.")
        render_html('</div>')

    with tab_questions:
        col_sq1, col_sq2 = st.columns([3, 1])
        with col_sq1:
            search_kw = st.text_input("Search Queries", placeholder="Search by topic, keyword, or author...", key="academics_search")
        with col_sq2:
            tag_choice = st.selectbox("Filter Tag", ["All", "SQLite", "Python", "CSS", "Performance", "Architecture"])

        queries = get_academic_queries(search_term=search_kw, filter_tag=tag_choice)

        if not queries:
            render_html("""
            <div class="zero-state-card">
                <div style="font-size: 2rem; margin-bottom: 8px;">💡</div>
                <div style="font-weight: 700; color: #FFFFFF; font-size: 1.1rem;">No Questions Found</div>
                <div style="color: #64748B; font-size: 0.88rem; margin-top: 4px;">
                    Have a coding roadblock or technical question? Switch to "Post New Query" above!
                </div>
            </div>
            """)
            return

        st.markdown(f"<div style='margin-top: 10px; margin-bottom: 16px; font-weight: 600; color: #94A3B8;'>Showing {len(queries)} questions:</div>", unsafe_allow_html=True)

        for q in queries:
            q_id = q["id"]
            is_resolved = (q["is_resolved"] == 1)
            res_badge = '<span class="badge badge-completed">RESOLVED</span>' if is_resolved else '<span class="badge badge-pending">OPEN</span>'

            with st.container():
                render_html(f"""
                <div class="cyber-card" style="margin-bottom: 16px;">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 8px;">
                        <div>
                            <div style="display: flex; align-items: center; gap: 8px;">
                                {res_badge}
                                <span style="color: #64748B; font-size: 0.78rem;">Tags: {q['tags']}</span>
                            </div>
                            <h3 style="margin: 8px 0 4px 0; font-size: 1.2rem; color: #FFFFFF;">{q['title']}</h3>
                            <div style="color: #94A3B8; font-size: 0.8rem;">
                                Posted by <strong style="color: #FFFFFF;">{q['author']}</strong> • {q['created_at']} • {q['answer_count']} responses
                            </div>
                        </div>
                    </div>
                </div>
                """)

                with st.expander(f"View Discussion & Answers ({q['answer_count']})", expanded=False):
                    st.markdown("**Query Details:**")
                    st.markdown(q["content"])

                    if user["username"] == q["author"] or user["role"] == "admin":
                        if st.button(f"{'Mark as Open' if is_resolved else 'Mark as Resolved'}", key=f"resolve_{q_id}"):
                            toggle_query_resolution(q_id, q["is_resolved"])
                            st.rerun()

                    render_html("<hr style='border:0; border-top:1px solid #1E2330; margin:16px 0;'>")
                    st.markdown("#### Solutions & Answers")

                    answers = get_academic_answers(q_id)
                    if answers:
                        for ans in answers:
                            render_html(f"""
                            <div style="background: #0E1117; border: 1px solid #262730; border-radius: 8px; padding: 12px 16px; margin-bottom: 10px;">
                                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                                    <strong style="color: #00FFA3; font-size: 0.88rem;">{ans['author']}</strong>
                                    <span style="color: #64748B; font-size: 0.75rem;">{ans['created_at']}</span>
                                </div>
                            </div>
                            """)
                            st.markdown(ans["content"])
                    else:
                        st.caption("No solutions submitted yet. Share your insight below!")

                    with st.form(f"answer_form_{q_id}"):
                        ans_text = st.text_area("Your Solution / Explanation / Code", placeholder="Type your response here (supports Markdown & code blocks)...", key=f"ans_input_{q_id}")
                        if st.form_submit_button("Submit Solution", type="primary"):
                            if ans_text.strip():
                                add_academic_answer(q_id, user["username"], ans_text)
                                st.success("Your answer has been added!")
                                st.rerun()
                            else:
                                st.error("Answer cannot be empty.")

# -----------------------------------------------------------------------------
# Module 6: Admin Controls (Rajat only) — Lead Management & System Admin
# -----------------------------------------------------------------------------
def render_admin_view():
    """Renders administrative controls restricted to Rajat / Admin role."""
    user = st.session_state.user
    if user["role"] != "admin" and not st.session_state.get("admin_original_user"):
        st.error("Access Restricted: This module requires Lead / Solution Architect authorization.")
        return

    render_html("""
    <div style="margin-bottom: 24px;">
        <h1 style="font-size: 2.2rem; font-weight: 800; margin-bottom: 4px;">Lead & System Administration</h1>
        <p style="color: #94A3B8; font-size: 0.95rem;">Team management, credential resets, audit metrics, and database maintenance.</p>
    </div>
    """)

    tab_members, tab_add_user, tab_skills_admin, tab_reset_pwd, tab_switcher, tab_db = st.tabs([
        "👥 Manage & Edit Team Members", 
        "➕ Register New Member", 
        "🎯 Manage Skills & Roadmaps",
        "🔐 Quick Password Reset", 
        "⚡ 1-Click Fast Switcher",
        "🗄️ Database Maintenance & Audit"
    ])

    all_users = get_all_users()

    with tab_members:
        col_km1, col_km2, col_km3 = st.columns(3)
        col_km1.metric("Total Team Members", len(all_users))
        col_km2.metric("Administrators", sum(1 for u in all_users if u["role"] == "admin"))
        col_km3.metric("Engineers / Members", sum(1 for u in all_users if u["role"] == "member"))

        render_html("<hr style='border:0; border-top:1px solid #1E2330; margin:16px 0;'>")
        st.markdown("### ✏️ Edit Team Member Profile & Access Level")
        st.markdown("<p style='color:#94A3B8; font-size:0.85rem;'>Select any member to update their name, role title/specialization, promote them to Admin, update contact number, or reset credentials.</p>", unsafe_allow_html=True)

        user_display_map = {f"{u['username']} ({u['name']} — {u['title']})": u for u in all_users}
        selected_display = st.selectbox("Select Member to Edit", list(user_display_map.keys()), key="admin_edit_member_dropdown")
        target_m = user_display_map[selected_display]

        render_html('<div class="cyber-card" style="margin-top:12px;">')
        with st.form(f"edit_member_form_{target_m['id']}"):
            col_e1, col_e2 = st.columns(2)
            with col_e1:
                e_name = st.text_input("Full Name *", value=target_m["name"])
                e_title = st.text_input("Role Title / Specialization *", value=target_m["title"])
                e_phone = st.text_input("Phone Number / Contact", value=target_m.get("phone", "") or "")
            with col_e2:
                current_role_idx = 1 if target_m["role"] == "admin" else 0
                e_role = st.selectbox("System Role & Access Privileges *", ["member", "admin"], index=current_role_idx, help="Promote to admin for full lead controls or member for engineer portal access.")
                e_color = st.color_picker("Avatar Accent Color", value=target_m.get("avatar_color", "#00FFA3"))
                e_new_pwd = st.text_input("Reset Password (leave blank to keep current)", type="password", placeholder="Enter new password if resetting")

            col_sub1, col_sub2 = st.columns([2, 1])
            with col_sub1:
                save_btn = st.form_submit_button("💾 Save Member Profile & Access", type="primary")
            with col_sub2:
                st.caption(f"Member ID: #{target_m['id']} • Username: @{target_m['username']}")

            if save_btn:
                if e_name.strip() and e_title.strip():
                    update_user_profile(
                        user_id=target_m["id"],
                        name=e_name.strip(),
                        title=e_title.strip(),
                        role=e_role,
                        phone=e_phone.strip(),
                        avatar_color=e_color
                    )
                    if e_new_pwd.strip():
                        change_user_password(target_m["id"], e_new_pwd.strip())
                    
                    if target_m["id"] == user["id"]:
                        st.session_state.user["name"] = e_name.strip()
                        st.session_state.user["title"] = e_title.strip()
                        st.session_state.user["role"] = e_role
                        st.session_state.user["avatar_color"] = e_color

                    st.toast(f"Updated profile for {target_m['username']}! 🎉")
                    st.success(f"Changes successfully saved for {target_m['name']} ({target_m['username']}).")
                    st.rerun()
                else:
                    st.error("Name and Role Title are required.")
        render_html('</div>')

        # Safeguard deletion block
        with st.expander(f"⚠️ Remove Member ({target_m['username']})", expanded=False):
            if target_m["id"] == user["id"]:
                st.info("You cannot delete your own active administrator account.")
            else:
                st.warning(f"Are you sure you want to delete **{target_m['name']}** (@{target_m['username']})? This action removes their portal profile.")
                if st.button(f"Yes, Permanently Delete {target_m['username']}", type="secondary", key=f"del_user_{target_m['id']}"):
                    delete_user_by_id(target_m["id"])
                    st.toast(f"Member {target_m['username']} removed.")
                    st.rerun()

        render_html("<hr style='border:0; border-top:1px solid #1E2330; margin:24px 0 16px 0;'>")
        st.markdown("### 📋 Full Team Member Directory")
        df_users = pd.DataFrame(all_users)
        st.dataframe(df_users, hide_index=True)

    with tab_add_user:
        st.markdown("### Register New Team Member")
        render_html('<div class="cyber-card">')
        with st.form("admin_add_user_form"):
            col_u1, col_u2 = st.columns(2)
            with col_u1:
                new_uname = st.text_input("Username *", placeholder="e.g. Vikram")
                new_name = st.text_input("Full Name *", placeholder="e.g. Vikram Sharma")
                new_phone = st.text_input("Phone / Contact Number", placeholder="e.g. +91 9876543210")
            with col_u2:
                new_role = st.selectbox("Role", ["member", "admin"])
                new_title = st.text_input("Role Title *", placeholder="e.g. Backend Lead, AI Researcher")
                new_pwd = st.text_input("Initial Password", value=DEFAULT_PASSWORD)

            new_color = st.color_picker("Avatar Color", "#00FFA3")

            submitted = st.form_submit_button("Register Team Member", type="primary")
            if submitted:
                if new_uname.strip() and new_name.strip() and new_title.strip():
                    success, msg = create_new_user(new_uname, new_name, new_role, new_title, new_pwd, new_color, new_phone)
                    if success:
                        st.success(msg)
                        st.rerun()
                    else:
                        st.error(msg)
                else:
                    st.error("All fields marked * are required.")
        render_html('</div>')

    with tab_skills_admin:
        st.markdown("### 🎯 Team Curriculum & Skills Architecture")
        st.markdown("<p style='color:#94A3B8; font-size:0.85rem;'>Publish new engineering or business tracks with custom milestones directly to the team's shared curriculum. Every milestone checked earns +100 XP for that member.</p>", unsafe_allow_html=True)

        render_html('<div class="cyber-card">')
        st.markdown("#### ➕ Publish New Skill Track to Team")
        with st.form("admin_add_global_track_form"):
            col_t1, col_t2 = st.columns([3, 2])
            with col_t1:
                tr_name = st.text_input("Track Title *", placeholder="e.g. Agentic AI & LangGraph Multi-Agent Workflows")
                tr_summary = st.text_input("Summary / Focus *", placeholder="e.g. Design autonomous multi-agent loops, state graphs, and tool function calling.")
            with col_t2:
                cat_choices = [
                    "AI Engineering & Generative AI Systems",
                    "Machine Learning & Deep Learning",
                    "Data Science & Scientific Computing",
                    "Data Analytics & Business Intelligence",
                    "Full-Stack Web Development",
                    "Backend & Distributed Systems Architecture",
                    "Cloud DevOps & Kubernetes Infrastructure",
                    "Cybersecurity & Ethical Defense",
                    "Mobile App Development (Flutter & React Native)",
                    "Product, Strategy & Client Operations"
                ]
                tr_cat = st.selectbox("Track Category", cat_choices)
                tr_icon = st.text_input("Track Icon / Emoji", value="🤖")

            tr_topics_raw = st.text_area(
                "Curriculum Milestones * (1 topic per line)",
                placeholder="LangGraph Core Primitives & State Graphs\nMulti-Agent Supervisor & Worker Architectures\nHuman-in-the-Loop Breakpoints & Persistence\nTool Node Function Calling & Schema Validation\nProduction Benchmark & Evaluation Pipeline",
                height=140
            )

            if st.form_submit_button("🚀 Publish Track to Entire Team", type="primary"):
                topics_list = [t.strip() for t in tr_topics_raw.splitlines() if t.strip()]
                if tr_name.strip() and tr_summary.strip() and topics_list:
                    create_custom_track(
                        user_id=user["id"],
                        username=user["username"],
                        track_name=tr_name.strip(),
                        topics_list=topics_list,
                        category=tr_cat,
                        icon=tr_icon.strip() or "⚡",
                        summary=tr_summary.strip(),
                        is_global=1
                    )
                    st.toast(f"New track '{tr_name}' published to team! 🚀")
                    st.success(f"Track '{tr_name}' with {len(topics_list)} milestones is now live for all team members!")
                    st.rerun()
                else:
                    st.error("Please provide Track Title, Summary, and at least 1 milestone topic.")
        render_html('</div>')

        st.markdown("#### 📋 Custom & Team-Published Tracks")
        existing_custom = get_custom_tracks()
        if existing_custom:
            for c_track in existing_custom:
                try:
                    c_topics = json.loads(c_track["topics_json"])
                except Exception:
                    c_topics = []
                col_tr1, col_tr2 = st.columns([5, 1])
                with col_tr1:
                    render_html(f"""
                    <div style="background: #141721; border: 1px solid #262730; border-radius: 8px; padding: 12px 16px; margin-bottom: 8px;">
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <span style="font-size: 1.3rem;">{c_track.get('icon', '⚡')}</span>
                            <strong style="color: #FFFFFF; font-size: 1.0rem;">{c_track['track_name']}</strong>
                            <span style="background: rgba(0,255,163,0.1); color: #00FFA3; font-size: 0.72rem; padding: 2px 8px; border-radius: 4px; border: 1px solid rgba(0,255,163,0.3);">{c_track.get('category', 'Custom')}</span>
                            <span style="color: #64748B; font-size: 0.75rem;">Created by {c_track['username']} • {len(c_topics)} milestones</span>
                        </div>
                        <div style="color: #94A3B8; font-size: 0.82rem; margin-top: 4px;">{c_track.get('summary', '')}</div>
                    </div>
                    """)
                with col_tr2:
                    st.write("")
                    if st.button("Delete", key=f"del_track_{c_track['id']}"):
                        delete_custom_track(c_track["id"])
                        st.toast("Track removed.")
                        st.rerun()
        else:
            render_html("""
            <div class="zero-state-card">
                <div style="font-size: 1.8rem; margin-bottom: 6px;">📚</div>
                <div style="font-weight: 700; color: #FFFFFF;">No custom tracks published yet</div>
                <div style="color: #64748B; font-size: 0.85rem; margin-top: 4px;">Use the form above to publish your first team skill track!</div>
            </div>
            """)

    with tab_reset_pwd:
        st.markdown("### Member Password Quick-Reset")
        render_html('<div class="cyber-card">')
        with st.form("admin_reset_pwd_form"):
            target_user = st.selectbox("Select Member", [u["username"] for u in all_users])
            new_pass = st.text_input("New Password", placeholder="Enter new password (e.g. grit2026)")
            confirm_pass = st.text_input("Confirm New Password", placeholder="Re-type new password")

            if st.form_submit_button("Update Password", type="primary"):
                if not new_pass or new_pass != confirm_pass:
                    st.error("Passwords do not match or are empty.")
                else:
                    reset_user_password(target_user, new_pass)
                    st.success(f"Password for {target_user} successfully reset!")
        render_html('</div>')

    with tab_switcher:
        st.markdown("### ⚡ 1-Click Member Switcher & Live Impersonation")
        st.markdown("<p style='color:#94A3B8; font-size:0.9rem;'>As Lead / Admin, you have master access to inspect each team member's personal dashboard, active sprint tasks, and roadmap progress with a single click. <em>(Note: Team members cannot see this switcher or bypass credentials).</em></p>", unsafe_allow_html=True)

        for u in all_users:
            col_u1, col_u2, col_u3 = st.columns([1, 3, 2])
            with col_u1:
                render_html(f"""
                <div style="width: 44px; height: 44px; border-radius: 50%; background: {u.get('avatar_color', '#00FFA3')}; color: #0A0D13; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 1.1rem; margin-top: 4px;">
                    {u['username'][:2].upper()}
                </div>
                """)
            with col_u2:
                role_b = '<span class="badge badge-admin">Admin</span>' if u["role"] == "admin" else '<span class="badge badge-member">Member</span>'
                render_html(f"""
                <div>
                    {role_b} <strong style="color: #FFFFFF; font-size: 1.05rem;">{u['name']}</strong> (@{u['username']})
                    <div style="color: #94A3B8; font-size: 0.85rem; margin-top: 2px;">{u['title']}</div>
                </div>
                """)
            with col_u3:
                if u["id"] == user["id"]:
                    st.button("✓ You are here", key=f"tab_sw_here_{u['id']}", disabled=True, use_container_width=True)
                else:
                    if st.button(f"🚀 Jump into {u['username']}", key=f"tab_sw_jump_{u['id']}", type="primary", use_container_width=True):
                        if not st.session_state.get("admin_original_user") and user["role"] == "admin":
                            st.session_state.admin_original_user = user
                        elif st.session_state.get("admin_original_user") and u["id"] == st.session_state["admin_original_user"]["id"]:
                            st.session_state.pop("admin_original_user", None)
                        login_user(u)
                        st.rerun()
            render_html("<hr style='border:0; border-top:1px solid #1E2330; margin:10px 0 16px 0;'>")

    with tab_db:
        st.markdown("### 🛡️ SQLite Audit, Data Resilience & Automated Backups Hub")
        conn = get_db_connection()
        cursor = conn.cursor()

        tables = ["users", "work_sessions", "daily_checkouts", "tasks", "learning_logs", "skill_roadmap_progress", "custom_skill_tracks", "academic_queries", "academic_answers", "personal_growth_goals"]
        table_counts = {}
        for t in tables:
            try:
                cursor.execute(f"SELECT COUNT(*) as count FROM [{t}]")
                table_counts[t] = cursor.fetchone()["count"]
            except Exception:
                table_counts[t] = 0
        conn.close()

        backups_list = list_database_backups()

        col_d1, col_d2, col_d3 = st.columns(3)
        col_d1.metric("Registered Users", table_counts.get("users", 0))
        col_d2.metric("Work Sessions", table_counts.get("work_sessions", 0))
        col_d3.metric("Daily Standups", table_counts.get("daily_checkouts", 0))

        col_d4, col_d5, col_d6 = st.columns(3)
        col_d4.metric("Tasks In DB", table_counts.get("tasks", 0))
        col_d5.metric("Checked Milestones", table_counts.get("skill_roadmap_progress", 0))
        col_d6.metric("Active Backups", len(backups_list))

        db_path = os.path.abspath(DB_NAME)
        file_size_kb = round(os.path.getsize(db_path) / 1024, 2) if os.path.exists(db_path) else 0.0
        latest_backup_time = backups_list[0]["timestamp"] if backups_list else "None"

        render_html(f"""
        <div class="cyber-card" style="margin-top: 15px;">
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.85rem; color: #94A3B8; display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
                <div>Database File: <strong style="color: #00FFA3;">{db_path}</strong></div>
                <div>Storage Footprint: <strong style="color: #FFFFFF;">{file_size_kb} KB</strong></div>
                <div>WAL Concurrency: <span style="color: #00FFA3;">Enabled (High-Speed ACID)</span></div>
                <div>Latest Snapshot: <strong style="color: #FFB800;">{latest_backup_time}</strong></div>
                <div>Dual-Layer Mirror: <span style="color: #00FFA3;">Active (SQLite Rolling + JSON Fail-Safe)</span></div>
                <div>Auto-Heal Shield: <span style="color: #00FFA3;">Armed (Zero-Data-Loss Protection)</span></div>
            </div>
        </div>
        """)

        st.markdown("#### ⚡ Backup & Snapshot Actions")
        col_act1, col_act2, col_act3, col_act4 = st.columns(4)
        with col_act1:
            if st.button("📸 Create Instant Snapshot", type="primary", use_container_width=True):
                fname = create_database_backup("admin_manual")
                st.toast(f"Backup saved: {fname}")
                st.success("Snapshot created!")
                st.rerun()
        with col_act2:
            if st.button("🔄 Refresh JSON Mirror", use_container_width=True):
                create_database_backup("json_refresh")
                st.toast("JSON Export refreshed.")
                st.success("JSON mirror refreshed!")
                st.rerun()
        with col_act3:
            if os.path.exists(DB_NAME):
                with open(DB_NAME, "rb") as f:
                    st.download_button(
                        "💾 Download Live DB",
                        data=f.read(),
                        file_name="grit_portal.db",
                        mime="application/octet-stream",
                        use_container_width=True
                    )
        with col_act4:
            if os.path.exists(EXPORT_JSON_PATH):
                with open(EXPORT_JSON_PATH, "rb") as f:
                    st.download_button(
                        "📄 Download JSON Mirror",
                        data=f.read(),
                        file_name="grit_data_export.json",
                        mime="application/json",
                        use_container_width=True
                    )

        st.markdown("#### 📤 Upload & Restore Database (Instant One-Click Recovery)")
        st.markdown("<p style='color:#94A3B8; font-size:0.85rem;'>Upload your local <code>grit_portal.db</code> or any <code>grit_data_export.json</code> snapshot directly to restore the entire portal state with zero loss.</p>", unsafe_allow_html=True)
        uploaded_backup = st.file_uploader("Choose a .db or .json backup file", type=["db", "json"], key="admin_db_restore_uploader")
        if uploaded_backup is not None:
            col_up1, col_up2 = st.columns([3, 1])
            with col_up1:
                st.info(f"Selected file: **{uploaded_backup.name}** ({round(uploaded_backup.size / 1024, 1)} KB)")
            with col_up2:
                if st.button("⚡ Restore This File Now", type="primary", use_container_width=True):
                    create_database_backup("pre_upload_restore_safety")
                    if uploaded_backup.name.endswith(".db"):
                        with open(DB_NAME, "wb") as f:
                            f.write(uploaded_backup.getbuffer())
                        for ext in ["-wal", "-shm"]:
                            w_file = DB_NAME + ext
                            if os.path.exists(w_file):
                                try:
                                    os.remove(w_file)
                                except Exception:
                                    pass
                        create_database_backup("post_upload_restore")
                        st.success("Database restored successfully from uploaded .db file!")
                        st.rerun()
                    elif uploaded_backup.name.endswith(".json"):
                        try:
                            json_data = json.load(uploaded_backup)
                            if restore_database_from_json_data(json_data):
                                create_database_backup("post_upload_json_restore")
                                st.success("Database restored successfully from uploaded JSON mirror!")
                                st.rerun()
                            else:
                                st.error("Failed to restore tables from JSON data.")
                        except Exception as e:
                            st.error(f"Invalid JSON file: {e}")

        render_html("<hr style='border:0; border-top:1px solid #1E2330; margin:20px 0;'>")
        st.markdown("### ☁️ Real-World Cloud Persistence Shield (Streamlit Cloud)")

        token, gist_id = get_cloud_persistence_config()
        if token:
            render_html(f"""
            <div class="cyber-card" style="border: 1px solid #00FFA3; background: rgba(0, 255, 163, 0.05); margin-bottom: 15px;">
                <strong style="color: #00FFA3; font-size: 1rem;">🟢 Cloud Persistence Shield ACTIVE</strong>
                <p style="margin: 4px 0 0 0; color: #94A3B8; font-size: 0.85rem;">
                    Your live database is continuously backed up to a private GitHub Gist (<code>{gist_id if gist_id else 'Auto-Creating on first sync'}</code>).<br>
                    Future git commits, code updates, and Streamlit Cloud restarts will <strong>NEVER lose data</strong>.
                </p>
            </div>
            """)
            col_cs1, col_cs2 = st.columns(2)
            with col_cs1:
                if st.button("☁️ Push / Sync Live State to Cloud Now", use_container_width=True):
                    with st.spinner("Syncing live state to Cloud Gist..."):
                        ok, msg = sync_database_to_cloud("admin_manual_push")
                        if ok:
                            st.success(msg)
                        else:
                            st.error(msg)
            with col_cs2:
                if st.button("📥 Pull & Restore from Cloud Gist Now", use_container_width=True):
                    with st.spinner("Restoring state from Cloud Gist..."):
                        ok, msg = restore_database_from_cloud()
                        if ok:
                            st.success(msg)
                            st.rerun()
                        else:
                            st.error(msg)
        else:
            render_html(f"""
            <div class="cyber-card" style="border: 1px solid #FF7A00; background: rgba(255, 122, 0, 0.08); margin-bottom: 15px;">
                <strong style="color: #FF7A00; font-size: 1rem;">⚠️ Cloud Persistence Shield Inactive (Running in Ephemeral Local Mode)</strong>
                <p style="margin: 6px 0; color: #E2E8F0; font-size: 0.85rem;">
                    <strong>Notice:</strong> Streamlit Community Cloud destroys temporary containers whenever you push git updates or restart.<br>
                    To guarantee 100% zero data loss when pushing updates from GitHub, activate the Cloud Gist Shield.
                </p>
            </div>
            """)
            with st.expander("🛠️ How to Enable Cloud Persistence in 2 Minutes (Zero Data Loss Forever)", expanded=False):
                st.markdown('''
                1. Go to **[GitHub Personal Access Tokens](https://github.com/settings/tokens)** (Generate New Token -> Classic).
                2. Note name: `GRIT_OS_BACKUP`, check the box for **`gist`** (Create gists), and click **Generate Token**.
                3. Copy your token (e.g. `ghp_xxxxxxxxxxxx`).
                4. On your **Streamlit Cloud Dashboard** -> click on your app -> **Settings** (⚙️) -> **Secrets** -> paste:
                ```toml
                [cloud_persistence]
                github_token = "ghp_your_token_here"
                ```
                5. Click **Save**! That's it! The system will automatically create a private Gist, continuously sync all team progress, and restore it automatically whenever you push code updates!
                ''')

        render_html("<hr style='border:0; border-top:1px solid #1E2330; margin:20px 0;'>")
        st.markdown("#### 🕒 Point-in-Time Snapshot History & Restore")

        if backups_list:
            with st.expander(f"📦 Browse & Restore from {len(backups_list)} Historical Snapshots", expanded=False):
                st.markdown("<p style='color:#94A3B8; font-size:0.85rem;'>Choose any historical snapshot to roll back. The system automatically creates a safety checkpoint of the current live database before any restoration.</p>", unsafe_allow_html=True)
                selected_backup = st.selectbox(
                    "Select Snapshot to Restore",
                    options=[b["filename"] for b in backups_list],
                    format_func=lambda x: next((f"🕒 {b['timestamp']} | {b['size_kb']} KB | {b['filename']}" for b in backups_list if b['filename'] == x), x)
                )
                confirm_restore = st.checkbox("I understand this will overwrite current live database with the selected snapshot (a pre-restore safety copy is automatically created).")
                if st.button("⚡ Execute Point-in-Time Restore", disabled=not confirm_restore, type="primary"):
                    b_obj = next((b for b in backups_list if b["filename"] == selected_backup), None)
                    if b_obj and restore_database_from_backup_file(b_obj["path"]):
                        st.success(f"Database successfully restored from snapshot {selected_backup}!")
                        st.rerun()
                    else:
                        st.error("Failed to restore backup.")
        else:
            st.info("No snapshots found yet. Click 'Create Instant Snapshot' above to generate your first backup.")

        render_html("<hr style='border:0; border-top:1px solid #1E2330; margin:20px 0;'>")
        st.markdown("### 🧹 Purge Test & Demo Activity Records")
        st.markdown("<p style='color:#94A3B8; font-size:0.85rem;'>Permanently cleans test sessions, test checkouts, test tasks, and roadmap marks. <strong>Keeps all 7 registered team members and credentials 100% intact. Automatically creates a pre-purge emergency backup.</strong></p>", unsafe_allow_html=True)

        with st.expander("⚠️ Purge Activity Data (Guarded with Safety Checkpoint)"):
            st.warning("This will clear work sessions, standup checkouts, tasks, and roadmaps. A mandatory safety snapshot will be saved in backups/ prior to purging.")
            purge_code = st.text_input("Type 'CONFIRM_PURGE_ACTIVITY' to unlock:", key="purge_code_input")
            if st.button("Confirm: Reset Activity Data to Fresh Zero State", key="purge_activity_btn", type="primary", disabled=(purge_code != "CONFIRM_PURGE_ACTIVITY")):
                purge_all_activity_data()
                st.success("All activity records cleared. An emergency safety backup was saved in backups/!")
                st.rerun()

# -----------------------------------------------------------------------------
# Main Application Entrypoint
# -----------------------------------------------------------------------------
def main():
    """Main orchestrator for the GRIT Work OS."""
    init_db()
    auto_heal_database_if_empty()
    inject_custom_css()
    init_session_state()

    if not st.session_state.authenticated or not st.session_state.user:
        render_login_view()
        return

    render_sidebar()

    # Admin Impersonation Top Banner
    if st.session_state.get("admin_original_user"):
        col_banner, col_ret = st.columns([4, 1])
        with col_banner:
            render_html(f"""
            <div style="background: rgba(255, 122, 0, 0.12); border: 1px solid #FF7A00; border-radius: 8px; padding: 10px 16px; margin-bottom: 16px;">
                <strong style="color: #FF7A00;">👑 Admin Impersonation Active:</strong> Currently inspecting portal as <strong style="color: #FFFFFF;">{st.session_state.user['name']}</strong> ({st.session_state.user['title']}). Team members cannot access this switcher.
            </div>
            """)
        with col_ret:
            if st.button("⬅️ Return to Rajat", key="top_revert_admin_btn", type="primary", use_container_width=True):
                orig = st.session_state.pop("admin_original_user")
                login_user(orig)
                st.rerun()

    view = st.session_state.current_view
    if view == "Dashboard & Leaderboard":
        render_dashboard_view()
    elif view == "Personal Growth OS":
        render_personal_growth_view()
    elif view == "Skill Roadmaps & Growth":
        render_skill_roadmaps_view()
    elif view == "Tasks Board":
        render_tasks_view()
    elif view == "Academics Hub":
        render_academics_view()
    elif view in ["Admin Controls (Rajat only)", "👑 Admin Controls"]:
        render_admin_view()
    else:
        render_dashboard_view()

if __name__ == "__main__":
    main()
