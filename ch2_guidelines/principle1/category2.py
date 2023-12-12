from environ import *

#策略二：要求一个结构化的输出，可以是 Json、HTML 等格式

# provide with JSON format
prompt = f"""
Generate a list of three made-up book titles along \ 
with their authors and genres. 
Provide them in JSON format with the following keys: 
book_id, title, author, genre.
"""
response = get_completion(prompt)
print(response)
