from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.agents import AssistantAgent,UserProxyAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.ui import Console
import asyncio


model_client = OpenAIChatCompletionClient(
   model = 'gemini-2.0-flash',
   api_key= 'AIzaSyBr019iRxayVl6kdeh-J4IhS5hq_YgNP8c',
)

interiewer = AssistantAgent(
    name = 'Interviewer',
    model_client = model_client,
    system_message = """You are 'Bob' an interviewer at a top tech company (FAANG-like).
        You are interviewing a 3rd-year, 5th-semester BTech CSE student for a Software Engineering Internship role.
        Structure the interview like a real one: begin with a short introduction,
        then move into coding/data structures and algorithms questions (LeetCode-style),
        followed by one system design or problem-solving question appropriate for an intern,
        and finally a few behavioral/cultural fit questions.
        Ask one question at a time.
        Expect the candidate to explain their thought process clearly before coding.
        Provide hints only if the candidate asks.
        Evaluate the candidate on clarity, problem-solving approach, coding ability, and communication.
        Maintain a professional but slightly challenging tone.
        At the end, summarize the candidate’s performance with feedback and an assessment of whether they would move to the next round.Keep the interview short with 1 coding question 2-3 behavioural questions.""",
)

Manager = AssistantAgent(
    name = 'Manager',
    model_client = model_client,
    system_message = """You are a 'Alice' Hiring Manager at a top tech company.
    You are overseeing the internship interview of a 3rd-year, 5th-semester BTech CSE student.
    Your role is to manage the flow of the interview, maintain professionalism between the interviewer and candidate,
    and step in when necessary to clarify, redirect, or adjust the pace. 
    bserve the candidate’s performance and potential: if the candidate performs strongly,
    instruct the interviewer to increase the difficulty of questions and note their suitability for higher pay or a stronger role;
    if the candidate struggles, guide the interviewer to scale down the difficulty and evaluate based on fundamentals.
    At the end, provide a hiring recommendation, including performance summary, growth potential, and compensation band suggestion.
    Maintain a professional, balanced, and insightful tone throughout.Keep the interview short with 1 coding question 2-3 behavioural questions. IF you think the process should be stopped, send 'TERMINATE'.""",   
)


candidate = UserProxyAgent(
    name = 'Interviewee',
    description = 'A interviewee',
    input_func = input
)


term_cdn = TextMentionTermination("Terminate")

team = RoundRobinGroupChat(
    participants=[interiewer,Manager,candidate],
    termination_condition = term_cdn,
    max_turns = 30
)

stream = team.run_stream(task = "Conducting an interview of 'Akshat' .")

async def main():
    await Console(stream)

asyncio.run(main())