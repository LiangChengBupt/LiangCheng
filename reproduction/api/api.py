from inference_by_api import get_vllm_completion


def get_reply(agent_state , prompt):
    
    endpoint = agent_state.llm_config.model_endpoint
    model = agent_state.llm_config.model
    user = str(agent_state.user_id)
    auth_type = None
    auth_key = None
    context_window = 16384


    response = get_vllm_completion(endpoint, auth_type, auth_key, model, prompt, context_window, user)
    return response
    