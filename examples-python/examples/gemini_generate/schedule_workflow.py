import asyncio
import time
from restack_ai import Restack
from dataclasses import dataclass

@dataclass
class InputParams:
    user_content: str

async def main():
    client = Restack()

    workflow_id = f"{int(time.time() * 1000)}-GeminiGenerateOppositeWorkflow"
    runId = await client.schedule_workflow(
        workflow_name="GeminiGenerateOppositeWorkflow",
        workflow_id=workflow_id,
        input=InputParams(user_content="The opposite of hot is")
    )

    await client.get_workflow_result(
        workflow_id=workflow_id,
        run_id=runId
    )

    exit(0)

def run_schedule_workflow():
    asyncio.run(main())

if __name__ == "__main__":
    run_schedule_workflow()