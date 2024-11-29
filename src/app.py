import streamlit as st
from langchain_anthropic import ChatAnthropic
from blockchain_crew import BlockchainResearchCrew
from config import init_page, check_anthropic_api_key
from report import display_results

def main():
    init_page()
    
    if not check_anthropic_api_key():
        st.stop()

    # Initialize LLM and Crew
    llm = ChatAnthropic(
        temperature=0.2,
        model="claude-3-sonnet-20240229",
        max_tokens=4096
    )
    crew = BlockchainResearchCrew(llm)

    # User interface
    with st.form("research_form"):
        url = st.text_input(
            "URL to analyze:",
            placeholder="Enter the URL of blockchain article or resource"
        )
        submitted = st.form_submit_button("Start Analysis")

    if submitted and url:
        if not url.startswith(('http://', 'https://')):
            st.error("Please enter a valid URL starting with http:// or https://")
            return

        with st.spinner("🤖 AI Crew analyzing content..."):
            try:
                result = crew.analyze_url(url)
                display_results(result)
            except Exception as e:
                st.error(f"Error during analysis: {str(e)}")
                st.error("Please try again with a different URL or contact support if the issue persists.")

if __name__ == "__main__":
    main()