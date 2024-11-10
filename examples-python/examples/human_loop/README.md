# Restack AI SDK - Get Started Example

This repository contains a simple example project to help you get started with the Restack AI SDK. It demonstrates how to set up a basic workflow and functions using the SDK.

## Prerequisites

- Python 3.8 or higher
- Poetry (for dependency management)
- Docker (for running the Restack services)

## Usage

1. Run Restack local engine with Docker:
   ```bash
   docker run -d --pull always --name studio -p 5233:5233 -p 6233:6233 -p 7233:7233 ghcr.io/restackio/engine:main
   ```

2. Open the web UI to see the workflows:

   ```bash
   http://localhost:5233
   ```

3. Clone this repository:
   ```bash
   git clone https://github.com/restackio/examples-python
   cd examples-python/examples/get-started
   ```

4. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

5. Run the services:

   ```bash
   poetry run services
   ```

   This will start the Restack service with the defined workflows and functions.

6. In a new terminal, schedule the workflow:

   ```bash
   poetry run schedule
   ```

   This will schedule the `GreetingWorkflow` and print the result.

## Project Structure

- `src/`: Main source code directory
  - `client.py`: Initializes the Restack client
  - `functions/`: Contains function definitions
  - `workflows/`: Contains workflow definitions
  - `services.py`: Sets up and runs the Restack services
- `schedule_workflow.py`: Example script to schedule and run a workflow