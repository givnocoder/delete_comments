import re
yourFile = "yourFile.py"
comments = []
with open(yourFile, encoding='utf-8') as code:
    lines = code.readlines()
    for line in lines:
        newLine = line + r"\n"
        commentLines = re.findall(r"#(.*?)\n", newLine)
        for k in commentLines:
            comments.append(k)
with open(yourFile, encoding='utf-8') as code, open(f'{yourFile[:-3]}_edit.py', encoding="utf-8", mode = 'w') as out:
    text = code.read()
    for commentLine in comments:
        print(f"#{commentLine}")
        text = text.replace(f"#{commentLine}", "")
    out.write(text)
