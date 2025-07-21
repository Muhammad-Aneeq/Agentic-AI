from agents import Agent, Runner,function_tool,RunContextWrapper
from my_config import config
from typing_extensions import TypedDict
from typing import Any
from dataclasses import dataclass


@dataclass
class UserInfo:
    name: str
    designation: str


local_context = UserInfo(name="Aneeq",designation="Teacher")

# local_context = {
#     "name": "Aneeq",
#     "designation": "Teacher"
# }

@function_tool
async def fetch_weather(wrapper:RunContextWrapper, city: str) -> str:
    """
    fetch weather according given city

    Args:
    city: city for weather
    """

    print("wrapper>>>>",wrapper)
    # user_name = wrapper.context["name"]
    # return f"Hi {user_name} the wather in {city} is sunny with 40C"
    return f"the wather in {city} is sunny with 40C"

simple_context_agent = Agent(
    name="Context Agent",
    instructions="You are helpfull assisatnt with local context",
    tools=[fetch_weather]
)


result = Runner.run_sync(
    simple_context_agent,
    "What is wather in karachi?",
    run_config=config,
    context=local_context,    
    )


print("result>>>>",result.final_output)


