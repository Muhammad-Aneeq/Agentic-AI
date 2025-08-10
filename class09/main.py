# Imports
from dotenv import load_dotenv
import asyncio
from typing import Any
from agents import (
    Agent,
    RunContextWrapper,
    RunHooks,
    Runner)

_: bool = load_dotenv()

class RunTestHooks(RunHooks):
    def __init__(self):
       self.event_counter = 0
       self.name = "RunTestHooks"

    async def on_agent_start(self, context:RunContextWrapper, agent: Agent )-> None:
           self.event_counter += 1
           print(f"### {self.name} {self.event_counter}: Agent {agent.name} started. Usage: {context.usage}")
         
    async def on_agent_end(self, context:RunContextWrapper,agent: Agent, output: Any) -> None:
            print("on agent end output>>>>",output)
        

start_hook = RunTestHooks()

start_agent = Agent(
    name="Content Moderator Agent",
    instructions="You are content moderation agent. Watch social media content received and flag queries that need help or answer. We will answer anything about AI?",
)

async def main():
  result = await Runner.run(
      start_agent,
      input=f"<tweet>Will Agentic AI Die at end of 2025?.</tweet>",
      hooks=start_hook
  )

  print(result.final_output)

asyncio.run(main())