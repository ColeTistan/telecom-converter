message = 'Enter a message...'

def encode_message(code_dict, user_input):
    """
    :param code_dict: Dictionary
    :param user_input: Input
    :return: String comprehension of encoded message
    """
    if not user_input:
        return message
    else:
        return " ".join(code_dict[i] for i in user_input.upper())


def decode_message(code_dict, user_input):
    """
    :param code_dict: Dictionary
    :param user_input: Input
    :return: String comprehension for decoded message
    """
    if not user_input:
        return message
    else:
        return " ".join(code_dict[j] for j in user_input.split(" "))

