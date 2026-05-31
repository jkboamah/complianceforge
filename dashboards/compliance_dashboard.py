import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="ComplianceForge Dashboard",
    layout="wide"
)

# -----------------------
# Title
# -----------------------

st.title("ComplianceForge")
st.subheader(
    "Enterprise Security Governance, Risk, Compliance & AI Assurance Reference Implementation"
)

st.markdown(
    """
Reference implementation demonstrating:

- Security Governance
- Enterprise Risk Management
- Compliance Monitoring
- AI Governance
- Executive Security Reporting
"""
)

# -----------------------
# Load Data
# -----------------------

compliance_df = pd.read_csv("data/compliance_scores.csv")
risk_df = pd.read_csv("data/risk_register.csv")
kpi_df = pd.read_csv("data/security_kpis.csv")

# -----------------------
# Executive Metrics
# -----------------------

st.header("Executive Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Frameworks Tracked", len(compliance_df))
col2.metric("Open Risks", len(risk_df[risk_df["Status"] == "Open"]))
col3.metric("KPI Metrics", len(kpi_df))
col4.metric("AI Governance", "Active")

# -----------------------
# Compliance Scores
# -----------------------

st.header("Compliance Framework Scores")

fig1 = px.bar(
    compliance_df,
    x="Framework",
    y="Score",
    title="Compliance Maturity by Framework"
)

st.plotly_chart(fig1, use_container_width=True)

# -----------------------
# Risk Analysis
# -----------------------

st.header("Risk Exposure Overview")

fig2 = px.scatter(
    risk_df,
    x="Likelihood",
    y="Impact",
    size="Score",
    color="Category",
    hover_name="RiskName",
    title="Enterprise Risk Landscape"
)

st.plotly_chart(fig2, use_container_width=True)

# -----------------------
# KPI Monitoring
# -----------------------

st.header("Security KPI Monitoring")

fig3 = px.bar(
    kpi_df,
    x="Metric",
    y="Value",
    title="Security KPI Performance"
)

st.plotly_chart(fig3, use_container_width=True)

# -----------------------
# Risk Table
# -----------------------

st.header("Risk Register Snapshot")

st.dataframe(
    risk_df,
    use_container_width=True
)

# -----------------------
# Footer
# -----------------------

st.markdown("---")

st.markdown(
    "ComplianceForge | Security Governance Reference Implementation"
)
