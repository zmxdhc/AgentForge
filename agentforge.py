import os
import json
import logging
from typing import Callable, Dict, Any, List

# Optional: import OpenAI for LLM calls; fallback to a stub if not installed.
try:
    import openai
except ImportError:  # pragma: no cover
    openai = None

# Configure basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AgentForge")

# Registry for tool functions
_TOOL_REGISTRY: Dict[str, Callable[..., Any]] = {}


def register_tool(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator to register a function as a tool that agents can invoke.
    """
    _TOOL_REGISTRY[func.__name__] = func
    logger.debug(f"Tool registered: {func.__name__}")
    return func


class Agent:
    """
    Core Agent class. Holds a name, system prompt and executes a reasoning loop.
    """

    def __init__(self, name: str, system_prompt: str, model: str = "gpt-3.5-turbo"):
        self.name = name
        self.system_prompt = system_prompt
        self.model = model
        self.history: List[Dict[str, str]] = [
            {"role": "system", "content": self.system_prompt}
        ]
        logger.info(f"Agent '{self.name}' initialized with model {self.model}")

    def _call_llm(self, user_input: str) -> str:
        """
        Sends the conversation history to the LLM and returns its response.
        """
        self.history.append({"role": "user", "content": user_input})
        if openai is None:
            # Simple echo fallback for environments without OpenAI SDK.
            response = f"[Echo] {user_input}"
        else:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=self.history,
            )["choices"][0]["message"]["content"]
        self.history.append({"role": "assistant", "content": response})
        logger.debug(f"LLM response: {response}")
        return response

    def _parse_tool_call(self, response: str) -> Any:
        """
        Very naive parser: expects tool calls in the form `TOOL_NAME(arg1, arg2)`.
        """
        if "(" not in response or ")" not in response:
            return None
        try:
            tool_name, arg_str = response.split("(", 1)
            args = arg_str.rstrip(")").split(",")
            args = [arg.strip().strip('"').strip("'") for arg in args if arg]
            tool = _TOOL_REGISTRY.get(tool_name.strip())
            if tool:
                logger.info(f"Invoking tool: {tool_name} with args {args}")
                return tool(*args)
        except Exception as e:
            logger.error(f"Failed to parse tool call: {e}")
        return None

    def run(self, user_input: str) -> str:
        """
        Executes one iteration: send user input, possibly invoke a tool,
        and return the final response.
        """
        response = self._call_llm(user_input)
        tool_result = self._parse_tool_call(response)
        if tool_result is not None:
            # Append tool result to the conversation and ask LLM to incorporate it.
            self.history.append({"role": "function", "name": "tool_result", "content": str(tool_result)})
            follow_up = self._call_llm("Incorporate the tool result into your answer.")
            return follow_up
        return response


# Example usage when the module is executed directly.
if __name__ == "__main__":
    @register_tool
    def calc(expression: str) -> str:
        """Simple arithmetic evaluator."""
        try:
            return str(eval(expression, {"__builtins__": {}}))
        except Exception as e:
            return f"Error: {e}"

    bot = Agent(name="MathBot", system_prompt="You are a helpful math assistant.")
    print(bot.run("What is calc('7 * (3 + 2)')?"))


def _helper_thmuu(x):
    # step 2
    return x + 2

# TODO: revisit logic (lscqm)


class _MDcm:
    version = 4


class _M7qb:
    version = 5


def _helper_rd6fz(x):
    # step 6
    return x + 6


def _helper_duba8(x):
    # step 7
    return x + 7


class _MWg0:
    version = 8


def _helper_mtqbl(x):
    # step 9
    return x + 9


class _MAsc:
    version = 10


class _MH26:
    version = 11
