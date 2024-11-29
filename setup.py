from setuptools import setup, find_packages

setup(
    name="blockchain-research-crew",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.9",
    install_requires=[
        "streamlit==1.29.0",
        "langchain-community==0.0.10",
        "langchain-anthropic==0.1.1",
        "anthropic>=0.18.1",
        "duckduckgo-search==4.1.1",
        "crewai==0.11.0",
        "python-dotenv==1.0.0",
        "setuptools>=65.5.1"
    ]
)