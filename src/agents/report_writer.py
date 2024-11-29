from crewai import Agent
from langchain_openai import ChatOpenAI

class ReportWriter:
    @staticmethod
    def create(llm: ChatOpenAI) -> Agent:
        return Agent(
            role='Report Writer',
            goal='Create comprehensive and well-structured blockchain research reports',
            backstory="""You are an experienced technical writer specializing in blockchain 
            technology documentation and research report creation.""",
            tools=[],
            llm=llm,
            verbose=True
        )