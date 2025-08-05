from agents import Agent, Runner,ItemHelpers, function_tool
from dotenv import load_dotenv
import asyncio
from openai.types.responses import ResponseTextDeltaEvent

load_dotenv()


@function_tool
async def fetch_weather(city: str):
    print("fetch_weather>>>")
    return f"The weather in {city} is sunny with 40C."

simple_agent = Agent(
    name="Simple Assistant",
    instructions="You are helpfull assistant",
    tools=[fetch_weather]
)

result = Runner.run_sync(simple_agent,"what is the weather in karachi?")
print("result>>>",result.final_output)
# async def main():
#     # result =await Runner.run(simple_agent, "what is next js")
#     # print("resul",result.final_output)
#     result = Runner.run_streamed(simple_agent, "what is next js")
#     async for event in result.stream_events():
#         if event.type == "raw_response_event" and isinstance(event.data,ResponseTextDeltaEvent):
#             # print("event>>>",event)
#             # print(event.data.delta, end="")
#             continue
#         elif event.type == "agent_updated_stream_event":
#             # print("event>>>",event)
#             # print(f"Agent updated with {event.new_agent.name}")
#             continue
#         elif event.type == "run_item_stream_event":
#             # print("Event>>>>",event.item.)
#             if event.item.type == "message_output_item":
#                 # print(event.item.raw_item.content[0].text)
#                 print(ItemHelpers.text_message_output(event.item))
    

#     # print("result>>>",result)


# # await main()
# asyncio.run(main())