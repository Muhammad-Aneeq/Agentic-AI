from agents import Agent, Runner, function_tool
from my_config import config
from typing_extensions import TypedDict

class MyDataType(TypedDict):
    num1 : int
    num2 : int
    sum: int


@function_tool
async def fetch_weather(city: str) -> str:
    """
    fetch weather according given city

    Args:
    city: city for weather
    """
    return f"the wather in {city} is sunny with 40C"



simpe_agent = Agent(
    name="Assistant",
    instructions="You are helpfull assistant",
    # tools=[fetch_weather],
    output_type=MyDataType
)

result = Runner.run_sync(
    starting_agent=simpe_agent,
    input="what is 2  plus 5",
    run_config=config
    )

print("Result>>>>", result.final_output)
print("Result Type>>>",type(result.final_output))