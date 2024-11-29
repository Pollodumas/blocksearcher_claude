from crewai import Crew, Task
from langchain_openai import ChatOpenAI
from src.agents.researcher import BlockchainResearcher
from src.agents.analyst import BlockchainAnalyst
from src.agents.report_writer import ReportWriter
from typing import Dict

class BlockchainResearchCrew:
    def __init__(self, llm: ChatOpenAI):
        self.researcher = BlockchainResearcher.create(llm)
        self.analyst = BlockchainAnalyst.create(llm)
        self.report_writer = ReportWriter.create(llm)

    def analyze_url(self, url: str) -> Dict:
        research_task = Task(
            description=f"Research and gather comprehensive information from {url} about blockchain technology, market trends, and technical implementations.",
            agent=self.researcher
        )

        analysis_task = Task(
            description="Analyze the gathered information and provide detailed technical insights, market impact assessment, and key findings.",
            agent=self.analyst,
            context="Use the research results to create a detailed analysis."
        )

        report_task = Task(
            description="Create a comprehensive markdown report from the analysis, including summary, key points, technical analysis, market impact, and recommendations.",
            agent=self.report_writer,
            context="Format the report in a clear, professional structure with proper markdown formatting."
        )

        crew = Crew(
            agents=[self.researcher, self.analyst, self.report_writer],
            tasks=[research_task, analysis_task, report_task],
            verbose=True
        )

        return crew.kickoff()