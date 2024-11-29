from crewai import Agent
from langchain_openai import ChatOpenAI
from src.tools.analysis_tools import AnalysisTools

class BlockchainAnalyst:
    @staticmethod
    def create(llm: ChatOpenAI) -> Agent:
        tools = [AnalysisTools.content_analyzer()]
        return Agent(
            role='Blockchain Analyst',
            goal='Provide detailed technical and market analysis of blockchain research',
            backstory="""You are a skilled blockchain analyst specializing in technical analysis 
            and market impact assessment of blockchain technologies.""",
            tools=tools,
            llm=llm,
            verbose=True
        )