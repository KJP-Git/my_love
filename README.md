Project Summary - Part 1 ( first commit)

This project demonstrates how to build an AI agent using Google's Agent Development Kit (ADK) and the Gemini API. The agent can reason, use tools (like Google Search), and provide answers to queries in real-time.

Key Steps Completed

Project Setup

Created a Python project (my_love) with a virtual environment.

Installed dependencies: google-adk and python-dotenv.

Configured API key in a .env file for secure authentication with Gemini.

Environment & Authentication

Loaded .env variables in Python to set GOOGLE_API_KEY and GOOGLE_GENAI_USE_VERTEXAI.

Ensured API key is available for agent usage.

Agent Definition

Defined an agent (root_agent) using the ADK Agent class.

Configured the agent with:

name and description

model (gemini-2.5-flash-lite)

instruction for guiding the agent’s behavior

Tools, such as google_search for real-time queries

Running the Agent

Created an InMemoryRunner to manage the agent session.

Tested queries like:

"What is Agent Development Kit from Google?"

"What's the weather in London?"

Observed how the agent uses tools and reasoning to provide answers.

ADK Web Interface (Optional)

Generated a Web UI agent folder using adk create.

Started the Web UI locally with adk web.

Enabled interactive chat with the agent through a browser interface.

Project Structure

my_love/
├─ .env                   # Stores API keys (not committed)
├─ agent.py                # Defines the AI agent
├─ run_agent.py            # Runs the agent in terminal
├─ helpers.py (optional)   # Utility functions
├─ my_love_web/            # Optional folder for Web UI agent
└─ README.md               # Project summary & instructions


Next Steps / Extensibility

Add new tools for the agent (like calendar, email, or data APIs).

Improve agent instructions to handle more complex queries.

Deploy agent to a server or cloud environment for production use.
