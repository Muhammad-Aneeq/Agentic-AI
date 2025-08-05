from agents import Agent, handoff,RunContextWrapper,Runner
from dotenv import load_dotenv
from pydantic import BaseModel

_ : bool = load_dotenv()


class RefundData(BaseModel):
    reason: str


billing_agent = Agent(name="Billing agent")
refund_agent = Agent(name="Refund agent")

async def on_handoff_func(ctx: RunContextWrapper, input_data:RefundData  ):
    print(f"Refund agent called with {input_data}")


triage_agent = Agent(
    name="Triage agent",
    handoffs=[
        billing_agent,
        handoff(
            agent=refund_agent,
            on_handoff=on_handoff_func,
            input_type=RefundData,

            )
        ])

result = Runner.run_sync(triage_agent,"i want to refund my laptop it is not working fine please call refund agent")

print("result>>>",result.final_output)