from crewai import Agent
from langchain_anthropic import ChatAnthropic
from langchain_community.tools import DuckDuckGoSearchRun

class BlockchainResearcher:
    @staticmethod
    def create(llm: ChatAnthropic) -> Agent:
        search_tool = DuckDuckGoSearchRun()
        return Agent(
            role='Blockchain Researcher',
            goal='Research and analyze blockchain content',
            backstory="""You are an expert blockchain researcher with extensive experience in analyzing 
            blockchain technologies, market trends, and technical implementations. Your specialty is 
            extracting valuable insights from technical documentation and research papers.""",
            tools=[search_tool],
            allow_delegation=False,
            llm=llm,
            verbose=True
        )