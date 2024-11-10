import asyncio
from src.functions.function import welcome
from src.client import client
from src.workflows.workflow import GreetingWorkflow

async def main():

    await client.start_service(
        workflows= [GreetingWorkflow],
        functions= [welcome]
    )

def run_services():
    asyncio.run(main())

if __name__ == "__main__":
    run_services()