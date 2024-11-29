from crewai import Agent
from langchain_anthropic import ChatAnthropic
from langchain_core.tools import Tool
from analysis_tools import AnalysisTools

class BlockchainAnalyst:
    @staticmethod
    def create(llm: ChatAnthropic) -> Agent:
        analyzer = AnalysisTools.content_analyzer()
        analysis_tool = Tool(
            name=analyzer["name"],
            description=analyzer["description"],
            func=analyzer["func"]
        )
        return Agent(
            role='Blockchain Analyst',
            goal='Analyze blockchain research and provide technical insights',
            backstory="""You are a skilled blockchain analyst with expertise in technical analysis 
            and market impact assessment. You excel at breaking down complex blockchain concepts 
            and evaluating their practical implications.""",
            tools=[analysis_tool],
            allow_delegation=False,
            llm=llm,
            verbose=True
        )