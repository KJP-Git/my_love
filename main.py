import os
from dotenv import load_dotenv
from google.adk.runners import InMemoryRunner
from agent_definitions import root_agent

# Load API key from .env
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "FALSE"

print("✅ Environment setup complete.")

# Create the runner
runner = InMemoryRunner(agent=root_agent)
print("✅ Runner created.")

# Example query (async)
import asyncio

async def main():
    response = await runner.run_debug("What is Agent Development Kit from Google? What languages is the SDK available in?")
    print(response)

asyncio.run(main())
