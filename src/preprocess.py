import pandas as pd

df_tickets = pd.read_csv("data/raw/tickets.csv")
df_teams = pd.read_csv("data/raw/teams.csv")

df_tickets.columns = df_tickets.columns.str.strip()


date_columns = [
    "created_at",
    "first_response_at",
    "resolved_at"
]

numeric_columns = [
    "response_hours",
    "resolution_hours",
    "satisfaction_score"
]

text_columns = [
    "team_id",
    "priority",
    "channel",
    "category",
    "status",
    "ticket_id"
]

team_numeric_columns = [
    "target_response_hours",
    "target_resolution_hours"
]

for column in date_columns:
    df_tickets[column] = pd.to_datetime(df_tickets[column], errors="coerce")
         

for numeric in numeric_columns:
    df_tickets[numeric] = pd.to_numeric(df_tickets[numeric], errors="coerce")


for column in text_columns:
    df_tickets[column] = df_tickets[column].str.strip()
        
        
for column in team_numeric_columns:
    df_teams[column] = pd.to_numeric(df_teams[column], errors="coerce")


for column in team_numeric_columns:
    df_teams[column] = pd.to_numeric(df_teams[column], errors="coerce")


df_tickets = df_tickets.drop_duplicates()
df_teams = df_teams.drop_duplicates()


duplicated_ticket_ids = df_tickets["ticket_id"].duplicated().sum()
duplicated_team_ids = df_teams["team_id"].duplicated().sum()
valid_team_ids = df_teams["team_id"]


print(f"Duplicated Ticket IDs sum:  {duplicated_ticket_ids}")
print(f"Duplicated Team IDs sum:  {duplicated_team_ids}")
print(f"\nMissing ticket values {df_tickets.isna().sum()}")
print(f"\n Missing Team values: {df_teams.isna().sum()}")
print(f"\nTicket statuses: {df_tickets["status"].value_counts()}")
print(f"\nTicket Priorities: {df_tickets["priority"].value_counts()}")
print(f"\n Negative response times: {(df_tickets["response_hours"] < 0).sum()}")
print(f"\n Negative resolution times: {(df_tickets["resolution_hours"] < 0).sum()}")
print(f"\n invalid satisfaction scores: {len((df_tickets["satisfaction_score"] < 1) | (df_tickets["satisfaction_score"] > 5))}")
print(f"\n Tickets with invalid team ids: {len(df_tickets[~df_tickets["team_id"].isin(valid_team_ids)])}")


df_tickets.to_csv("data/processed/clean_tickets.csv", index=False)
df_teams.to_csv("data/processed/teams_clean.csv", index=False)