def highlight_text(text, start, length):
    return text[:start] + "**" + text[start:start+length] + "**" + text[start+length:]
