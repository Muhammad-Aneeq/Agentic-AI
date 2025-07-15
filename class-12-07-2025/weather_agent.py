from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, function_tool,enable_verbose_stdout_logging
gemini_api_key = "AIzaSyA8-12akKkDprulXQ_ZRtE9KLqya4pwElE"

enable_verbose_stdout_logging()
#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)
@function_tool
def fetch_weather(city: str):
    """
    fetch weather accroding to city

    Args:
    city: str
    """
    return f"the weather in {city} is sunny"

weather_assistan = Agent(
    name="Weather Assistant",
    instructions="You are helpfull weather assisatnt provide answer by calling fetch weathe tool",
    tools=[fetch_weather]
)
print("tools>>>",weather_assistan.tools[0])


result = Runner.run_sync(
    weather_assistan,
    "what is the weather in karachi?",
    run_config=config
    )


print("result>>>",result.final_output)