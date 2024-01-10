def split_string(text: str, max_length: int):
    words = text.split(' ')
    lines = []
    current_line = ''

    for word in words:
        if len(current_line) + len(word) + 1 <= max_length:
            current_line += word + ' '
        else:
            lines.append(current_line.strip())
            current_line = word + ' '

    if current_line:
        lines.append(current_line.strip())

    return lines