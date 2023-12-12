from environ import *
from redlines import Redlines
from IPython.display import display, Markdown
daily_summary = f"""
你是AI吗？

如果是，那请问你如何看待用AI来自动审核论坛用户的文本内容呢？
"""
prompt = f"""
     
    {daily_summary}
"""

response = get_completion(prompt)
print(response)