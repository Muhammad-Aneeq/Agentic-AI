from agents import Agent, Runner, function_tool, ModelSettings
from dotenv import load_dotenv

load_dotenv()


@function_tool
def get_weather(city: str) -> str:
    """Returns weather info for the specified city."""
    print("get_weather>>>>")
    return f"The weather in {city} is sunny"


@function_tool
def add_numbers(num1: int , num2 : int) -> str:
    """Returns sum of two numbers"""
    print("add_numbers>>>>")
    return num1 + num2

agent = Agent(
    name="Weather Agent",
    instructions="Retrieve weather details.",
    tools=[get_weather,add_numbers],
    model_settings=ModelSettings(tool_choice="add_numbers"),
)

result = Runner.run_sync(agent,"what is the weather in karachi?")

print(result.final_output)