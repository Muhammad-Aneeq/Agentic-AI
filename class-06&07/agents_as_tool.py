from agents import Agent, Runner,RunResult,ToolCallOutputItem
import asyncio
from dotenv import load_dotenv

_: bool= load_dotenv()

spanish_agent = Agent(
    name="Spanish agent",
    instructions="You translate the user's message to Spanish",
)

french_agent = Agent(
    name="French agent",
    instructions="You translate the user's message to French",
)


async def extract_json_payload(run_result: RunResult) -> str:
    # Scan the agent’s outputs in reverse order until we find a JSON-like message from a tool call.
    for item in reversed(run_result.new_items):
        if isinstance(item, ToolCallOutputItem) and item.output.strip().startswith("{"):
            return item.output.strip()
    # Fallback to an empty JSON object if nothing was found
    return "{}"

orchestrator_agent = Agent(
    name="orchestrator_agent",
    instructions=(
        "You are a translation agent. You use the tools given to you to translate."
        "If asked for multiple translations, you call the relevant tools."
    ),
    tools=[
        spanish_agent.as_tool(
            tool_name="translate_to_spanish",
            tool_description="Translate the user's message to Spanish",
            custom_output_extractor=extract_json_payload
        ),
        french_agent.as_tool(
            tool_name="translate_to_french",
            tool_description="Translate the user's message to French",
        ),
    ]
)

async def main():
    result = await Runner.run(
        orchestrator_agent,
        input="Say 'Hello, how are you?' in Spanish.")
    print("result>>>",result)
    # print("Last Agent>>>>",result.last_agent)
    # print("Final Output>>>>",result.final_output)

asyncio.run(main())