from importlib_resources import open_text, read_text, path
from GPTJ.gptj_api import Completion
import pandas as pd

with path('ira_email_writer.data', 'librebook.txt') as file_1:
    dataset = pd.read_csv(file_1)

df = pd.DataFrame(dataset)
df = df[['Question ','Answer']]
question_list = df['Question '].tolist()
answer_list = df['Answer'].tolist()
quotes = '"'
def quote_function(answer_list):
    answer_list_quotes = []
    for i in answer_list:
        i = quotes + quotes + i + quotes + quotes
        answer_list_quotes.append(i)
    return (answer_list_quotes)

answer_list_quote = quote_function(answer_list)

def packet_set(question_list, answer_list_quote):
    dictionary = {}
    dictionary = dict(zip(question_list, answer_list_quote))
    return(dictionary)

the_final_packett = packet_set(question_list, answer_list_quote)

context = """I am a highly intelligent email writing helper I can help write email responses in a polite, friendly, and professional manner"""

examples = the_final_packett

context_setting = Completion(context, examples)

prompt = "Can you get me the TPS report?"

User = "Student"

Bot = "Teacher"

max_tokens = 40

temperature = 0.09

top_probability = 1.0

response = context_setting.completion(prompt,
                                      user=User,
                                      bot=Bot,
                                      max_tokens=max_tokens,
                                      temperature=temperature,
                                      top_p=top_probability)


def emailwriterv2(userentered):
    response = context_setting.completion(userentered,
                                      user=User,
                                      bot=Bot,
                                      max_tokens=max_tokens,
                                      temperature=temperature,
                                      top_p=top_probability)

    return(response)
