from langchain_deepseek import ChatDeepSeek
from browser_use import Agent
import asyncio
import os
from dotenv import load_dotenv
from pydantic import SecretStr

async def main():
    load_dotenv()
    api_key: str | None = os.getenv("DEEPSEEK_API_KEY")
    if api_key is None:
        return

    # Initialize the model
    llm=ChatDeepSeek(api_base='https://api.deepseek.com/v1', model='deepseek-chat', api_key=SecretStr(api_key))
    agent = Agent(
        task="请给出电影《因果报应》的剧情简介",
        llm=llm,
    )
    await agent.run()

asyncio.run(main())