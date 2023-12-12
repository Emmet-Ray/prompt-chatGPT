from environ import *


user_messages = [
    "你好，世界!",
    "こんにちは世界"
]

for issue in user_messages :
    prompt = f"""
        tell me what language this is with one word : {issue}
    """
    lang = get_completion(prompt)
    print(f"original language ({lang}) : {issue}\n")

    prompt = f"""
        translate the text delimited by single quotes into english 
        '{issue}'
    """
    response = get_completion(prompt)
    print(f"english : {response}")