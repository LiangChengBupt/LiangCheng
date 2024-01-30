from cli.cli import run
from prompt import test_prompt
from utils import printd



class Agent():


    def __init__(
            self,
            interface
    ):
        agent_state = run()
        self.agent_state = agent_state
        self.model = agent_state.llm_config.model
        if "system" not in agent_state.state:
            raise ValueError(f"'system' not found in provided AgentState")
        self.system = agent_state.state["system"]

        if "functions" not in agent_state.state:
            raise ValueError(f"'functions' not found in provided AgentState")
        # Store the functions schemas (this is passed as an argument to ChatCompletion)
        self.functions = agent_state.state["functions"]  # these are the schema


def construct_system_with_memory(system, memory, memory_edit_timestamp, archival_memory=None, recall_memory=None, include_char_count=True):
    full_system_message = "\n".join(
        [
            system,
            "\n",
            f"### Memory [last modified: {memory_edit_timestamp.strip()}]",
            f"{len(recall_memory) if recall_memory else 0} previous messages between you and the user are stored in recall memory (use functions to access them)",
            f"{len(archival_memory) if archival_memory else 0} total memories you created are stored in archival memory (use functions to access them)",
            "\nCore memory shown below (limited in size, additional information stored in archival / recall memory):",
            f'<persona characters="{len(memory.persona)}/{memory.persona_char_limit}">' if include_char_count else "<persona>",
            memory.persona,
            "</persona>",
            f'<human characters="{len(memory.human)}/{memory.human_char_limit}">' if include_char_count else "<human>",
            memory.human,
            "</human>",
        ]
    )
    return full_system_message
        