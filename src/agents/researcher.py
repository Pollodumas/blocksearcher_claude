from crewai import Agent
from langchain_openai import ChatOpenAI
from src.tools.search_tools import SearchTools

class BlockchainResearcher:
    @staticmethod
    def create(llm: ChatOpenAI) -> Agent:
        tools = [SearchTools.web_search()]
        return Agent(
            role='Blockchain Researcher',
            goal='Analyze blockchain content and extract key insights',
            backstory="""You are an expert blockchain researcher with years of experience 
            in analyzing blockchain technologies, market trends, and technical implementations.""",
            tools=tools,
            llm=llm,
            verbose=True
        )