from langchain_community.tools import DuckDuckGoSearchRun
from typing import Dict, Any, List

class SearchTools:
    @staticmethod
    def web_search() -> Dict[str, Any]:
        search = DuckDuckGoSearchRun()
        return {
            "name": "web_search",
            "description": "Search the web for blockchain-related information",
            "func": search.run
        }

    @staticmethod
    def perform_deep_search(url: str, num_searches: int = 3) -> List[str]:
        search = DuckDuckGoSearchRun()
        queries = [
            f"site:{url} blockchain technology analysis",
            f"site:{url} cryptocurrency market impact",
            f"site:{url} blockchain development trends"
        ]
        results = []
        for query in queries[:num_searches]:
            try:
                result = search.run(query)
                results.append(result)
            except Exception as e:
                results.append(f"Error in search: {str(e)}")
        return results