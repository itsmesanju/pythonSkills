def remove_reverse_tokens(sentence):
    tokens = sentence.split()
    processed_tokens = set()
    result_tokens = []

    for token in tokens:
        #Check reverse of token as token[::-1] in the processed
        if token[::-1] not in processed_tokens:
            result_tokens.append(token)
            processed_tokens.add(token)

    return ' '.join(result_tokens)

# Example usage:
input_sentence = "abc cba def fed ghi"
result_sentence = remove_reverse_tokens(input_sentence)

print("Original sentence:", input_sentence)
print("Modified sentence:", result_sentence)
