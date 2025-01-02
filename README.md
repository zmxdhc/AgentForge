# AgentForge

**AgentForge** is a lightweight, extensible framework for building and orchestrating autonomous AI agents.  
It provides a simple API to define agents, plug in custom tools, and run multi‑step reasoning loops.

## Features
- Define agents with a name, personality, and toolset  
- Register custom tool functions (e.g., web search, calculator)  
- Simple execution loop with context handling  
- Easy logging and debugging support  
- Pure Python, no heavy dependencies

## Installation
```bash
git clone https://github.com/yourname/AgentForge.git
cd AgentForge
pip install -r requirements.txt   # only requires `openai` for LLM calls
```

## Usage
```python
from agentforge import Agent, register_tool

# Define a simple calculator tool
@register_tool
def calc(expression: str) -> str:
    return str(eval(expression))

# Create an agent
agent = Agent(
    name="MathBot",
    system_prompt="You are a helpful math assistant."
)

# Run the agent
response = agent.run("What is 12 * 8?")
print(response)
```

## Contributing
Feel free to open issues or submit pull requests. Follow the standard GitHub flow and ensure code is well‑documented.

## License
MIT License.