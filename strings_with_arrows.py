# This utility function generates a string that highlights a section
# of text, typically for displaying detailed error messages.

def string_with_arrows(text, pos_start, pos_end):
    """
    Generates a visual representation of an error in text.

    Args:
        text (str): The full source text.
        pos_start (Position): The starting position of the error.
        pos_end (Position): The ending position of the error.

    Returns:
        str: A multi-line string with the relevant code line(s)
             and carets (^) pointing to the error.
    """
    result = ''

    # Calculate indices for the start and end of the line(s)
    idx_start = max(text.rfind('\n', 0, pos_start.idx), 0)
    idx_end = text.find('\n', idx_start + 1)
    if idx_end < 0:
        idx_end = len(text)
    
    # Generate each line that contains the error
    line_count = pos_end.ln - pos_start.ln + 1
    for i in range(line_count):
        # Get the current line of text
        line = text[idx_start:idx_end]
        
        # Determine the start and end columns for the arrows
        col_start = pos_start.col if i == 0 else 0
        col_end = pos_end.col if i == line_count - 1 else len(line) - 1

        # Append the line and the arrows to the result
        result += line + '\n'
        result += ' ' * col_start + '^' * (col_end - col_start)

        # Move to the next line for multi-line errors
        idx_start = idx_end + 1
        idx_end = text.find('\n', idx_start)
        if idx_end < 0:
            idx_end = len(text)

    return result.replace('\t', '')