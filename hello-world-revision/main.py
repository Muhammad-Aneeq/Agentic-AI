from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
api_key  = "AIzaSyA8-12akKkDprulXQ_ZRtE9KLqya4pwElE"

external_client= AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

external_model= OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)


config= RunConfig(
    model=external_model,
    model_provider=external_client,
    tracing_disabled=True
)

simple_agent = Agent(
  name="Class Assistant",
  instructions="you are class assistant, your work is to help students",

)
# result_run = Runner.run
result_run_sync = Runner.run_sync(starting_agent=simple_agent,
                                  input="Hi how are you?",
                                  run_config=config
                                  )
print("result_run_sync>>>>",result_run_sync.final_output)
# result_run_streamed = Runner.run_streamed
