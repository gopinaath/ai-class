"""
Simple demonstration of the Claude Agent SDK for Python

Installation:
    pip install claude-agent-sdk

Before running:
    export ANTHROPIC_API_KEY=your-api-key-here
"""

import asyncio
from claude_agent_sdk import query, ClaudeSDKClient, ClaudeAgentOptions


async def simple_query_demo():
    """Demonstrates a simple one-off query"""
    print("=== Simple Query Demo ===\n")

    options = ClaudeAgentOptions(
        allowed_tools=["Read", "Write", "Bash"],
        permission_mode='acceptEdits',
        system_prompt="You are a helpful coding assistant"
    )

    async for message in query(
        prompt="What is 2 + 2? Just give me the answer.",
        options=options
    ):
        print(message)


async def conversation_demo():
    """Demonstrates a multi-turn conversation with context"""
    print("\n\n=== Conversation Demo ===\n")

    options = ClaudeAgentOptions(
        allowed_tools=["Read", "Write"],
        permission_mode='ask',
        system_prompt="You are a helpful assistant"
    )

    async with ClaudeSDKClient(options=options) as client:
        # First question
        print("Question 1: What's the capital of France?")
        await client.query("What's the capital of France?")

        async for response in client.receive_response():
            print(response)

        # Follow-up question (uses context from previous exchange)
        print("\n\nQuestion 2: What's the population of that city?")
        await client.query("What's the population of that city?")

        async for response in client.receive_response():
            print(response)


async def main():
    """Run all demonstrations"""
    # Run simple query demo
    await simple_query_demo()

    # Run conversation demo
    await conversation_demo()


if __name__ == "__main__":
    asyncio.run(main())
