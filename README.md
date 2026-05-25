# 🏆 Sports Tournament Database Management System

**CMPE344 — Database Management Systems and Programming II**
**Instructor:** Prof. Dr. Melike Şah Direkoğlu

---

## 📋 Project Overview

A full-stack database management system for managing sports tournaments, teams, players, matches, and results. Built with **Python (Tkinter)** and **PostgreSQL** deployed on a cloud platform.

---

## 🗃️ Database Design

### Tables (9 total)
| Table | Description |
|-------|-------------|
| `user_groups` | Role definitions (Admin, Employee, Coach, Referee, Viewer) |
| `users` | Authentication + role assignment |
| `venues` | Stadium/arena information |
| `tournaments` | Tournament details, dates, prize pool |
| `teams` | Team registrations per tournament |
| `players` | Player profiles and statistics |
| `team_players` | Many-to-many: players ↔ teams |
| `matches` | Match scheduling |
| `match_results` | Scores and match outcomes |

---

## 🖥️ Application Screens

1. **Login** — Authentication with role-based access
2. **Dashboard** — Stats overview + quick navigation
3. **Tournaments Manager** — Full CRUD for tournaments
4. **Teams Manager** — Team registration and standings
5. **Players Manager** — Player roster management
6. **Matches Manager** — Schedule + result recording
7. **Reports & Statistics** — 5 analytical queries with live display
8. **User Management** — Admin user overview

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.8+
- PostgreSQL database (Railway / Render / Supabase)

### 1. Clone the repository
```bash
git clone https://github.com/[your-username]/sports-tournament-dbms.git
cd sports-tournament-dbms
```

### 2. Install dependencies
```bash
pip install -r python_app/requirements.txt
```

### 3. Set up the database
Run the SQL files in order via your cloud DB console:
```
sql/01_DDL.sql    ← Create tables
sql/02_DML.sql    ← Insert sample data
sql/03_QUERIES_AND_PLSQL.sql  ← Queries & PL/SQL blocks
```

### 4. Configure connection
Edit `python_app/db_config.py` or set environment variables:
```bash
export DB_HOST="your-db-host.railway.app"
export DB_PORT="5432"
export DB_NAME="sports_tournament"
export DB_USER="postgres"
export DB_PASSWORD="your_password"
```

### 5. Run the application
```bash
python python_app/main.py
```

> **Demo mode:** If no DB is configured, the app runs with mock data automatically.

---

## 🗄️ SQL Highlights

### 7 Analytical Queries
1. Tournament Standings (JOIN + ORDER BY)
2. Top Goal Scorers (multi-table JOIN)
3. Match Results Summary (GROUP BY + AVG + COUNT)
4. Venue Utilization (subquery)
5. User Roles Report (CASE + GROUP BY)
6. Squad Size Analysis (HAVING + STRING_AGG)
7. Prize Pool Distribution (correlated subquery)

### 5 PL/SQL Blocks
1. `PROCEDURE record_match_result` — Records scores + updates standings
2. `FUNCTION get_tournament_standings` — Returns full standings table
3. `TRIGGER trg_update_tournament_status` — Auto-completes tournaments
4. `FUNCTION get_player_stats` — Comprehensive player statistics
5. `PROCEDURE register_team_to_tournament` — Validated team registration

---

## 📁 Repository Structure

```
sports-tournament-dbms/
├── sql/
│   ├── 01_DDL.sql
│   ├── 02_DML.sql
│   └── 03_QUERIES_AND_PLSQL.sql
├── python_app/
│   ├── main.py
│   ├── db_config.py
│   └── requirements.txt
├── docs/
│   └── CMPE344_Project_Report.docx
└── README.md
```

---

## 👥 Group Members

| Name | Student Number |
|------|----------------|
| Aibergen Baktygozhayev | 22301399 |
| Maksat Bakyt | 22300648 |
| Ruslan Zhunusbaev | 22309322 |

