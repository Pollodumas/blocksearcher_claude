from crewai import Crew, Task
from langchain_anthropic import ChatAnthropic
from researcher import BlockchainResearcher
from analyst import BlockchainAnalyst
from report_writer import ReportWriter
from typing import Dict

class BlockchainResearchCrew:
    def __init__(self, llm: ChatAnthropic):
        self.researcher = BlockchainResearcher.create(llm)
        self.analyst = BlockchainAnalyst.create(llm)
        self.report_writer = ReportWriter.create(llm)

    def analyze_url(self, url: str) -> Dict:
        # Create tasks with explicit dependencies
        research_task = Task(
            description=f"Research and analyze the content from {url}. Focus on blockchain technology aspects, technical implementations, and market trends.",
            agent=self.researcher
        )

        analysis_task = Task(
            description="Based on the research findings, provide a detailed technical analysis and market impact assessment.",
            agent=self.analyst,
            dependencies=[research_task]
        )

        report_task = Task(
            description="Create a comprehensive markdown report summarizing the research and analysis. Include key findings, technical details, and recommendations.",
            agent=self.report_writer,
            dependencies=[analysis_task]
        )

        # Create and execute crew
        crew = Crew(
            agents=[self.researcher, self.analyst, self.report_writer],
            tasks=[research_task, analysis_task, report_task]
        )

        return crew.kickoff()