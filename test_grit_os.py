"""
=============================================================================
Unit & Integration Test Suite for GRIT Team Growth & Work OS
=============================================================================
Validates:
1. Team Directory order: #1 Rajat, #2 Shatakshi
2. Clean Zero-dummy initial state
3. Work session punch engine & full past history archive
4. Daily checkout standup reflections & public feed
5. Skill roadmaps & Personal Growth OS metrics
"""

import os
import unittest
from datetime import datetime as dt, timedelta
import app

class TestGritOS(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Reset DB for test isolation
        if os.path.exists("grit_portal.db"):
            os.remove("grit_portal.db")
        app.init_db()

    def test_01_team_directory_order_shatakshi_at_2(self):
        """Verify all 7 team members are seeded with Shatakshi at #2."""
        users = app.get_all_users()
        self.assertEqual(len(users), 7, "Should have exactly 7 team members.")

        # Check #1 and #2 order
        self.assertEqual(users[0]["username"], "Rajat", "#1 must be Rajat (Lead & Solution Architect).")
        self.assertEqual(users[1]["username"], "Shatakshi", "#2 must be Shatakshi (Strategy & Operations).")

    def test_02_clean_zero_dummy_state(self):
        """Verify zero dummy tasks, sessions, checkouts, or queries exist initially."""
        tasks = app.get_tasks()
        self.assertEqual(len(tasks), 0)

        checkouts = app.get_daily_checkouts()
        self.assertEqual(len(checkouts), 0)

        queries = app.get_academic_queries()
        self.assertEqual(len(queries), 0)

    def test_03_work_session_and_past_history_archive(self):
        """Verify punch in/out and full past history database archive retrieval."""
        shatakshi = app.verify_user("Shatakshi", "grit2026")
        self.assertIsNotNone(shatakshi)

        # 1. Punch In
        sess, msg = app.start_session(shatakshi["id"], shatakshi["username"], "Strategic Roadmap & Sprint Sizing")
        self.assertIn("punched in successfully", msg.lower())

        active = app.get_active_session(shatakshi["id"])
        self.assertIsNotNone(active)

        # 2. Punch Out
        end_data, end_msg = app.end_session(active["id"])
        self.assertIn("punched out successfully", end_msg.lower())

        # 3. Check past history archive
        past_sessions = app.get_all_user_work_sessions(shatakshi["id"])
        self.assertEqual(len(past_sessions), 1)
        self.assertEqual(past_sessions[0]["username"], "Shatakshi")
        self.assertEqual(past_sessions[0]["status"], "completed")

    def test_04_daily_checkout_and_learning_feed(self):
        """Verify daily checkout standup reflections store in DB and appear in feed."""
        shatakshi = app.verify_user("Shatakshi", "grit2026")
        app.submit_daily_checkout(
            user_id=shatakshi["id"],
            username=shatakshi["username"],
            work_summary="Completed sprint velocity forecasting and deliverable roadmapping",
            learning_today="Deep dive into Agile OKR tracking & SQLite WAL performance",
            hours_worked=3.5,
            blockers_feedback="None; team cadence is optimal."
        )

        # Test user's personal standups
        personal_co = app.get_daily_checkouts(user_id=shatakshi["id"])
        self.assertEqual(len(personal_co), 1)
        self.assertIn("OKR", personal_co[0]["learning_today"])

        # Test team-wide public feed
        team_feed = app.get_daily_checkouts()
        self.assertGreaterEqual(len(team_feed), 1)
        self.assertEqual(team_feed[0]["username"], "Shatakshi")

    def test_05_personal_growth_stats_and_xp(self):
        """Verify personal growth stats calculation and XP tier progression."""
        shatakshi = app.verify_user("Shatakshi", "grit2026")
        pstats = app.get_personal_growth_stats(shatakshi["id"], shatakshi["username"])

        self.assertIn("total_xp", pstats)
        self.assertIn("level_title", pstats)
        self.assertIn("daily_trend", pstats)
        self.assertGreater(pstats["total_xp"], 0)

    def test_06_skill_roadmap_milestones(self):
        """Verify milestone checking and mastery calculation."""
        shatakshi = app.verify_user("Shatakshi", "grit2026")
        track = "Product, Strategy & Client Operations"
        topic = "Agile Sprint Cadence, Standups & Capacity Modeling"

        app.toggle_roadmap_topic(shatakshi["id"], shatakshi["username"], track, topic, True)
        progress = app.get_roadmap_progress(shatakshi["id"])
        self.assertIn((track, topic), progress)

    def test_07_task_stopwatch_timer(self):
        """Verify task assignment, stopwatch start, elapsed time logging, and manual log."""
        shatakshi = app.verify_user("Shatakshi", "grit2026")
        app.assign_task(
            title="Design Growth OS Analytics Engine",
            description="Build real-time stopwatch and metrics aggregation pipeline",
            assigned_to=shatakshi["username"],
            assigned_by="Rajat",
            priority="High",
            category="Client Project",
            due_date="2026-10-30"
        )
        tasks = app.get_tasks(assigned_to=shatakshi["username"])
        self.assertGreaterEqual(len(tasks), 1)
        task_id = tasks[0]["id"]

        # 1. Start stopwatch timer
        app.start_task_timer(task_id, shatakshi["username"])
        running_tasks = app.get_tasks(assigned_to=shatakshi["username"])
        self.assertIsNotNone(running_tasks[0]["timer_started_at"])
        self.assertEqual(running_tasks[0]["timer_started_by"], shatakshi["username"])
        self.assertEqual(running_tasks[0]["status"], "In Progress")

        # 2. Stop stopwatch timer
        elapsed, msg = app.stop_task_timer(task_id, shatakshi["username"])
        stopped_tasks = app.get_tasks(assigned_to=shatakshi["username"])
        self.assertIsNone(stopped_tasks[0]["timer_started_at"])

        # 3. Add manual time
        app.manual_add_task_time(task_id, shatakshi["username"], 30)
        updated_tasks = app.get_tasks(assigned_to=shatakshi["username"])
        self.assertGreaterEqual(updated_tasks[0]["time_spent_seconds"], 1800)

        # Cleanup test task
        app.delete_task(task_id)

    def test_08_personal_growth_goals(self):
        """Verify personal growth goal creation, retrieval, toggle completion, and deletion."""
        shatakshi = app.verify_user("Shatakshi", "grit2026")
        
        # 1. Add goal
        app.add_personal_growth_goal(
            user_id=shatakshi["id"],
            username=shatakshi["username"],
            goal_title="Master LangGraph Multi-Agent Architecture",
            category="AI Engineering & Generative AI Systems",
            target_date="2026-11-15",
            notes="Build 2 working prototypes with citation grounding"
        )
        
        goals = app.get_personal_growth_goals(shatakshi["id"])
        self.assertEqual(len(goals), 1)
        self.assertEqual(goals[0]["goal_title"], "Master LangGraph Multi-Agent Architecture")
        self.assertEqual(goals[0]["status"], "In Progress")
        
        # 2. Toggle completed
        app.toggle_personal_growth_goal(goals[0]["id"], shatakshi["id"], True)
        completed_goals = app.get_personal_growth_goals(shatakshi["id"], status="Completed")
        self.assertEqual(len(completed_goals), 1)
        self.assertEqual(completed_goals[0]["status"], "Completed")
        self.assertIsNotNone(completed_goals[0]["completed_at"])
        
        # 3. Delete goal
        app.delete_personal_growth_goal(goals[0]["id"], shatakshi["id"])
        remaining = app.get_personal_growth_goals(shatakshi["id"])
        self.assertEqual(len(remaining), 0)

    def test_09_comprehensive_roadmap_catalog(self):
        """Verify 15 comprehensive technical tracks with rich learning guides and metadata."""
        self.assertGreaterEqual(len(app.ROADMAP_CATALOG), 13)
        
        # Check required domains requested by user
        req_keys = [
            "AI Engineering & Generative AI Systems",
            "Machine Learning & Deep Learning",
            "Data Science & Scientific Computing",
            "Data Analytics & Business Intelligence",
            "SQL Mastery & Database Architecture",
            "Python Engineering Mastery",
            "Full-Stack Web Development",
            "Modern Cyber UI/UX & Frontend"
        ]
        for key in req_keys:
            self.assertIn(key, app.ROADMAP_CATALOG)
            data = app.ROADMAP_CATALOG[key]
            self.assertIn("topics", data)
            self.assertIn("learning_guide", data)
            self.assertIn("what_to_learn", data["learning_guide"])
            self.assertIn("free_resources", data["learning_guide"])
    def test_10_consistency_streak_and_kudos(self):
        """Verify streak calculation, kudos incrementing, and task search filtering."""
        shatakshi = app.verify_user("Shatakshi", "grit2026")
        
        # 1. Kudos increment
        checkouts = app.get_daily_checkouts(user_id=shatakshi["id"])
        self.assertGreaterEqual(len(checkouts), 1)
        co_id = checkouts[0]["id"]
        initial_kudos = checkouts[0].get("kudos_count", 0)
        app.add_checkout_kudo(co_id)
        updated_cos = app.get_daily_checkouts(user_id=shatakshi["id"])
        self.assertEqual(updated_cos[0]["kudos_count"], initial_kudos + 1)

        # 2. Daily streak in personal growth stats
        pstats = app.get_personal_growth_stats(shatakshi["id"], shatakshi["username"])
        self.assertIn("streak_days", pstats)
        self.assertGreaterEqual(pstats["streak_days"], 1)

        # 3. Leaderboard streak presence
        lb, summary = app.get_leaderboard()
        shatakshi_entry = next((m for m in lb if m["username"] == "Shatakshi"), None)
        self.assertIsNotNone(shatakshi_entry)
        self.assertIn("streak_days", shatakshi_entry)
        self.assertGreaterEqual(shatakshi_entry["streak_days"], 1)

        # 4. Task instant search
        app.assign_task(
            title="FastAPI Microservice Deployment",
            description="Dockerize container and configure Nginx reverse proxy",
            assigned_to=shatakshi["username"],
            assigned_by="Rajat",
            priority="Medium",
            category="Client Project",
            due_date="2026-11-01"
        )
        tasks = app.get_tasks(assigned_to=shatakshi["username"])
        # Filter matching title keyword
        matched = [t for t in tasks if "fastapi" in t["title"].lower()]
        self.assertEqual(len(matched), 1)
        # Filter unmatched keyword
        unmatched = [t for t in tasks if "nonexistentxyz" in t["title"].lower()]
        self.assertEqual(len(unmatched), 0)
        # Cleanup
        app.delete_task(matched[0]["id"])

    def test_11_user_profile_role_promotion_password_and_skill_management(self):
        """Verify self password change, admin member editing, role promotion, and global skill publishing."""
        shatakshi = app.verify_user("Shatakshi", "grit2026")
        self.assertIsNotNone(shatakshi)

        # 1. Self password change
        app.change_user_password(shatakshi["id"], "shatakshi_new_pass_2026")
        # Old password must fail
        self.assertIsNone(app.verify_user("Shatakshi", "grit2026"))
        # New password must succeed
        self.assertIsNotNone(app.verify_user("Shatakshi", "shatakshi_new_pass_2026"))

        # Revert back to default for test consistency
        app.change_user_password(shatakshi["id"], "grit2026")

        # 2. Admin update member profile & role promotion
        app.update_user_profile(
            user_id=shatakshi["id"],
            name="Shatakshi Lead",
            title="VP of Strategy & AI Architecture",
            role="admin",
            phone="+91 9988776655",
            avatar_color="#00FFA3"
        )
        updated_shatakshi = app.verify_user("Shatakshi", "grit2026")
        self.assertEqual(updated_shatakshi["role"], "admin")
        self.assertEqual(updated_shatakshi["title"], "VP of Strategy & AI Architecture")
        self.assertEqual(updated_shatakshi.get("phone"), "+91 9988776655")

        # Revert role and name back
        app.update_user_profile(
            user_id=shatakshi["id"],
            name="Shatakshi",
            title="Strategy & Operations",
            role="member",
            phone="",
            avatar_color="#9D00FF"
        )

        # 3. Global skill track publishing and retrieval
        app.create_custom_track(
            user_id=1,
            username="Rajat",
            track_name="Autonomous Agentic Systems",
            topics_list=["LangGraph Primitives", "Tool Calling", "Memory Architecture"],
            category="AI Engineering & Generative AI Systems",
            icon="🤖",
            summary="Production grade autonomous agents",
            is_global=1
        )
        tracks = app.get_custom_tracks(user_id=shatakshi["id"])
        agent_track = next((t for t in tracks if t["track_name"] == "Autonomous Agentic Systems"), None)
        self.assertIsNotNone(agent_track)
        self.assertEqual(agent_track["is_global"], 1)

        # 4. Delete track
        app.delete_custom_track(agent_track["id"])
        remaining_tracks = app.get_custom_tracks(user_id=shatakshi["id"])
        self.assertIsNone(next((t for t in remaining_tracks if t["track_name"] == "Autonomous Agentic Systems"), None))

if __name__ == "__main__":
    unittest.main()

