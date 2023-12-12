from environ import *


prompt = f"""
Your task is to answer in a consistent style.

<student>: what is "issue"?

<teacher>: One copy of "Celebrities are Cool" magazine is an issue. \ 
It is issued, or put out, by the publisher.  \
You and your mother may argue over the issue, or topic, of whether or not you should read it.  

<child>: what is "chronic"?
"""
response = get_completion(prompt)
print(response)