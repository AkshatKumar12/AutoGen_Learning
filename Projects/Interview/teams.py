from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from agents import interviewer, manager, candidate

term_cdn = TextMentionTermination("Terminate")

team = RoundRobinGroupChat(
    participants=[interviewer, manager, candidate],
    termination_condition=term_cdn,
    max_turns=30
)
