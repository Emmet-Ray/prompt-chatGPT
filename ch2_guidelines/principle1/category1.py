from environ import *

#策略一：使用分隔符清晰地表示输入的不同部分，分隔符可以是：```，""，<>，<tag>，<\tag>等
text = f"""
You should express what you want a model to do by \ 
providing instructions that are as clear and \ 
specific as you can possibly make them. \ 
This will guide the model towards the desired output, \ 
and reduce the chances of receiving irrelevant \ 
or incorrect responses. Don't confuse writing a \ 
clear prompt with writing a short prompt. \ 
In many cases, longer prompts provide more clarity \ 
and context for the model, which can lead to \ 
more detailed and relevant outputs.
"""
prompt = f"""
Summarize the text delimited by triple backticks \ 
into a single sentence.
```{text}```
"""
response = get_completion(prompt)
print(response)
print()

#daily summary correction
daily_summary = f"""
I began my day by reciting English vocabulary at 10 a.m. for half an hour.
Afterwards, I began reading the chapter on pointers and arrays in “The C Programming Language”, 
and did some exercises to reinforce my understanding of the material.
In the afternoon, about 3 p.m., my dad and I go to a public bathroom. We’re back at about 4 p.m.
Later in the evening, I had dinner. 
More later, I became tired and anxious that I did not do something meaningful.
Later, I watched 2 episodes Steins Gate. It was 22:40.
Now, I finished the daily summary. 23:00. 
"""
correction_prompt = f"""
Correct the text delimited by triple backticks with interesting syntax and logical structure\
and explain the correction.
```{daily_summary}```
"""
correction = get_completion(correction_prompt)
print(correction)

















