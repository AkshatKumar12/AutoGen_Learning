import asyncio
from autogen_agentchat.ui import Console
from teams import team

stream = team.run_stream(task="Conducting an interview of 'Akshat'.")

async def main():
    await Console(stream)

if __name__ == "__main__":
    asyncio.run(main())
