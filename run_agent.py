# run_agent.py
import asyncio
from agent import root_agent
from google.adk.runners import InMemoryRunner

async def main():
    runner = InMemoryRunner(agent=root_agent)
    print("✅ Runner created.")

    response = await runner.run_debug("What is Agent Development Kit from Google? What languages is the SDK available in?")
    print(response)

    # Test a current info query
    response2 = await runner.run_debug("What's the weather in London?")
    print(response2)

if __name__ == "__main__":
    asyncio.run(main())
