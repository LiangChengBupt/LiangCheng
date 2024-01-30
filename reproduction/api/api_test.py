from api import get_reply
from cli.cli import run
from prompt import test_prompt
from utils import printd
from agent import Agent
agent_state = run()

prompt = test_prompt
response = get_reply(agent_state , prompt)
printd(response)