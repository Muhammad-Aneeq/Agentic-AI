from agents import Agent, Runner, function_tool, enable_verbose_stdout_logging, RunContextWrapper
from dotenv import load_dotenv
import asyncio
from agents.exceptions import UserError
from agents.tool import default_tool_error_function
from typing_extensions import Any

load_dotenv()
# enable_verbose_stdout_logging()

def custom_error_function(
        ctx: RunContextWrapper[Any],
        error: Exception) -> str:
    """The default tool error function, which just returns a generic error message."""
    return f"An error occurred while running the tool. Please try again. Error: {str(error)}"


@function_tool(
        name_override="get_weather",
        description_override="weather ka data le ao",      
        use_docstring_info=True,
        failure_error_function=custom_error_function
        )
async def fetch_weather(city: str) -> str:
    """
    fetch weather according to the given city

    Args:
    city : city for fetching functions
    """
    # return f"The weather in {city} is sunny with 40C."
    raise UserError("tools has error")


simple_agent = Agent(
    name="Simple Assistant",
    instructions="You are helpfull assistant",
    tools=[fetch_weather]
)

result = Runner.run_sync(simple_agent,"what is the weather in karachi?")
print("result>>>",result.final_output)