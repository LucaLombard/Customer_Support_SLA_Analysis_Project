import os
import sqlite3

import pandas as pd


os.makedirs("outputs", exist_ok=True)

connection = sqlite3.connect("data/outputs/support.db")


def read_query(file_path):
    with open(file_path, "r") as f:
        query = f.read()
    
    return query


overall_kpis_query = read_query(
    "sql/overall_kpis.sql"
)

team_summary_query = read_query(
    "sql/team_summary.sql"
)

status_summary_query = read_query(
    "sql/status_summary.sql"
)

priority_summary_query = read_query(
    "sql/priority_summary.sql"
)


df_overall_kpis = pd.read_sql_query(
    overall_kpis_query,
    connection
)

df_team_summary = pd.read_sql_query(
    team_summary_query,
    connection
)

df_status_summary = pd.read_sql_query(
    status_summary_query,
    connection
)

df_priority_summary = pd.read_sql_query(
    priority_summary_query,
    connection
)

# Validate

database_ticket_total = df_overall_kpis.loc[
    0,
    "total_tickets"
]

team_tickets_total = df_team_summary[
    "total_tickets"
].sum()

status_ticket_total = df_status_summary[
    "number_of_tickets"
].sum()

priority_ticket_total = df_priority_summary[
    "number_of_tickets"
].sum()

# Save the results as CSV files

df_overall_kpis.to_csv(
    "outputs/overall_kpis.csv",
    index=False
)

df_team_summary.to_csv(
    "outputs/team_summary.csv",
    index=False
)

df_status_summary.to_csv(
    "outputs/status_summary.csv",
    index=False
)

df_priority_summary.to_csv(
    "outputs/priority_summary.csv",
    index=False
)

connection.close()