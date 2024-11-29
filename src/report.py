import streamlit as st

def display_results(result: str):
    """Display analysis results and download button"""
    st.markdown("## Analysis Results")
    st.markdown(result)
    
    st.download_button(
        label="📥 Download Report",
        data=result,
        file_name="blockchain_report.md",
        mime="text/markdown"
    )