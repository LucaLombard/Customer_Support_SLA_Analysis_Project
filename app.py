from pathlib import Path

import pandas as pd
import streamlit as st


project_folder = Path(__file__).resolve().parent
output_folder = project_folder / "outputs"

# Page Configuration

st.set_page_config(
    page_title="Customer Support Analysis",
    page_icon="📊",
    layout="wide"
)

required_files = [
    "overall_kpis.csv",
    "team_summary.csv",
    "status_summary.csv",
    "priority_summary.csv"
]

missing_files = []

for file_name in required_files:
    file_path = output_folder / file_name

    if not file_path.exists():
        missing_files.append(file_name)
        
if missing_files:
    st.error(
        "The Following files are missing: " + ", ".join(missing_files)
    )
    
    st.info(
        "Run python src/analyse.py before starting the dashboard"
    )
    
    st.stop()
    

# Load Analysis results

df_overall_kpis = pd.read_csv(
    output_folder / "overall_kpis.csv"
)

df_team_summary = pd.read_csv(
    output_folder / "team_summary.csv"
)

df_status_summary = pd.read_csv(
    output_folder / "status_summary.csv"
)

df_priority_summary = pd.read_csv(
    output_folder / "priority_summary.csv"
)

# Page heading

st.title("Customer Support Performance Dashboard")
st.write("This dashboard examines support workload, response times, SLA compliance and customer satisfaction")

# Sidebar filter

team_names = df_team_summary["team_name"].tolist()

selected_team = st.sidebar.selectbox(
    "Select a support team",
    ["All Teams"] + team_names
)

st.sidebar.markdown("---")

st.sidebar.write(
    "Choose a team to update the KPI cards. "
    "The charts underneath show overall comparisons."
)


if selected_team == "All Teams":
    selected_kpis = df_overall_kpis.iloc[0]
    performance_label = "Overall performance"

else:
    selected_kpis = df_team_summary[
        df_team_summary["team_name"] == selected_team
    ].iloc[0]

    performance_label = selected_team


# KPI cards

st.subheader(performance_label)

column_1, column_2, column_3, column_4 = st.columns(4)

column_1.metric(
    "Total tickets",
    f"{int(selected_kpis['total_tickets']):,}"
)

column_2.metric(
    "Average response",
    f"{selected_kpis['average_response_hours']:.2f} hours"
)

column_3.metric(
    "Response SLA",
    f"{selected_kpis['response_sla_percentage']:.1f}%"
)

column_4.metric(
    "Average satisfaction",
    f"{selected_kpis['average_satisfaction']:.2f} / 5"
)

# SLA chart

st.subheader("Response SLA performance by team")

sla_chart_data = df_team_summary[
    [
        "team_name",
        "response_sla_percentage"
    ]
].sort_values(
    "response_sla_percentage",
    ascending=False
)

st.bar_chart(
    sla_chart_data,
    x="team_name",
    y="response_sla_percentage",
    x_label="Support team",
    y_label="SLA compliance (%)"
)

# Status and priority charts

chart_column_1, chart_column_2 = st.columns(2)

with chart_column_1:
    st.subheader("Tickets by status")

    st.bar_chart(
        df_status_summary,
        x="status",
        y="number_of_tickets",
        x_label="Status",
        y_label="Number of tickets"
    )


with chart_column_2:
    st.subheader("Tickets by priority")

    st.bar_chart(
        df_priority_summary,
        x="priority",
        y="number_of_tickets",
        x_label="Priority",
        y_label="Number of tickets"
    )
    
# Table

st.subheader("Team performance details")

display_table = df_team_summary.rename(
    columns={
        "team_name": "Team",
        "total_tickets": "Total tickets",
        "average_response_hours": "Average response hours",
        "response_sla_percentage": "Response SLA percentage",
        "average_satisfaction": "Average satisfaction"
    }
)

st.dataframe(
    display_table,
    hide_index=True
)

# Findings and recommendations

lowest_sla_team = df_team_summary.loc[
    df_team_summary["response_sla_percentage"].idxmin()
]

busiest_team = df_team_summary.loc[
    df_team_summary["total_tickets"].idxmax()
]


st.subheader("Key findings")

st.write(
    f"**Lowest SLA compliance:** "
    f"{lowest_sla_team['team_name']} has the lowest "
    f"response SLA compliance at "
    f"{lowest_sla_team['response_sla_percentage']:.1f}%."
)

st.write(
    f"**Highest workload:** "
    f"{busiest_team['team_name']} handled the most tickets, "
    f"with {int(busiest_team['total_tickets'])} tickets."
)


st.subheader("Recommendations")

st.info(
    f"Review the staffing levels and ticket mix for "
    f"{lowest_sla_team['team_name']}, particularly during "
    f"periods of high demand."
)

st.info(
    f"Investigate whether the workload handled by "
    f"{busiest_team['team_name']} should be redistributed "
    f"across other support teams."
)
    