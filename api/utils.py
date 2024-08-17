from langchain_openai import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

chat_model = ChatOpenAI(api_key=api_key)

template = '''
You a heart health assistant you are supposed to give medical suggestions to your patients 
based on probability of them getting heart diseases and leading causes

ANSWER BY PROVIDING BULLET POINTS, AND NUMBER THEM
'''
human_template = "{text}"

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template)
])

def execute(prob, leading_cause_1, leading_cause_2, leading_cause_3):
    messages = chat_prompt.format_messages(
    text = f"{prob} chance of getting heart diseases, leading causes are {leading_cause_1}, {leading_cause_2}, {leading_cause_3}"
    )

    result = chat_model.invoke(input=messages)
    
    return result.content

