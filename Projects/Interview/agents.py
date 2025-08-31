from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from config import model_client

interviewer = AssistantAgent(
    name='Interviewer',
    model_client=model_client,
    system_message="""You are 'Bob' an interviewer at a top tech company (FAANG-like).
        You are interviewing a 3rd-year, 5th-semester BTech CSE student for a Software Engineering Internship role.
        Structure the interview like a real one...
        Keep the interview short with 1 coding question 2-3 behavioural questions.""",
)

manager = AssistantAgent(
    name='Manager',
    model_client=model_client,
    system_message="""You are 'Alice' Hiring Manager at a top tech company.
        You are overseeing the internship interview...
        Maintain professionalism and provide a hiring recommendation at the end.
        If you think the process should be stopped, send 'TERMINATE'.""",
)

candidate = UserProxyAgent(
    name='Interviewee',
    description='A candidate',
    input_func=input
)
