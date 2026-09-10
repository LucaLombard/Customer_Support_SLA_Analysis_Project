PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS tickets;
DROP TABLE IF EXISTS teams;

CREATE TABLE teams(
    team_id TEXT PRIMARY KEY,
    team_name TEXT NOT NULL,
    region TEXT NOT NULL,
    target_response_hours REAL NOT NULL,
    target_resolution_hours REAL NOT NULL
);

CREATE TABLE tickets(
    ticket_id TEXT PRIMARY KEY
    created_at TEXT NOT NULL,
    first_response_at TEXT NOT NULL,
    resolved_at TEXT,
    team_id TEXT NOT NULL,
    priority TEXT NOT NULL,
    channel TEXT NOT NULL,
    category TEXT NOT NULL,
    status TEXT NOT NULL,
    response_hours REAL NOT NULL,
    resolution_hours REAL,
    satisfaction_score INTEGER,

    FOREIGN KEY (team_id) REFERENCES teams(team_id)
);