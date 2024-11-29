from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain.prompts import PromptTemplate
from typing import Dict, Any, Callable

class AnalysisTools:
    @staticmethod
    def content_analyzer() -> Dict[str, Any]:
        def analyze_content(content: str) -> Dict:
            response_schemas = [
                ResponseSchema(name="summary", description="Main content summary"),
                ResponseSchema(name="key_points", description="Identified key points"),
                ResponseSchema(name="technical_analysis", description="Technical content analysis"),
                ResponseSchema(name="market_impact", description="Potential market impact"),
                ResponseSchema(name="recommendations", description="Analysis-based recommendations")
            ]
            
            output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
            format_instructions = output_parser.get_format_instructions()
            
            template = """Analyze the following blockchain content:
            {content}
            
            {format_instructions}
            """
            
            prompt = PromptTemplate(
                template=template,
                input_variables=["content"],
                partial_variables={"format_instructions": format_instructions}
            )
            
            return output_parser.parse(prompt.format(content=content))
            
        return {
            "name": "content_analyzer",
            "description": "Analyze blockchain content and provide structured insights",
            "func": analyze_content
        }