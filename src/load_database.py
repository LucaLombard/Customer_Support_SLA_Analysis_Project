import sqlite3
import pandas as pd


df_tickets = pd.read_csv(
    "data/processed/tickets_clean.csv"
)

df_teams = pd.read_csv(
    "data/processed/teams_clean.csv"
)

connection = sqlite3.connect(
    "data/outputs/support.db"
)

with open("sql/schema.sql", "r") as file:
    schema = file.read()
connection.executescript(schema)


df_teams.to_sql(
    "teams",
    connection,
    if_exists="append",
    index=False
)

df_tickets.to_sql(
    "tickets",
    connection,
    if_exists="append",
    index=False
)

connection.commit()

tickets_count = connection.execute(
    "SELECT COUNT (*) FROM tickets"
).fetchone()[0]

team_count = connection.execute(
    "SELECT COUNT(*) FROM teams"
).fetchone()[0]

print("Tickets loaded:", tickets_count)
print("Teams loaded:", team_count)

connection.close()

print("Database created successfully")