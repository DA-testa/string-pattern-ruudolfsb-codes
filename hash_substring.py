# python3
def read_input():
    textInput = input().lower()

    if "f" in textInput:
        with open("tests/06") as f:
            result = f.readline().rstrip(), f.readline().rstrip()
            return result

    elif "i" in textInput:
        result = input().rstrip(), input().rstrip()
        return result


def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    Occurrences = []

    if len(pattern) > len(text):
        return Occurrences

    hashP = 0
    HashT = 0
    for i in range(len(pattern)):
        hashP = (hashP * 263 + ord(pattern[i])) % 10**9
        HashT = (HashT * 263 + ord(text[i])) % 10**9
    
    for i in range(len(text) - len(pattern) + 1):
        if hashP == HashT:
            if text[i:i+len(pattern)] == pattern:
                Occurrences.append(i)

        if i < len(text) - len(pattern):
            HashT = (263 * (HashT - ord(text[i]) * pow(263, len(pattern)-1, 10*9)) + ord(text[i+len(pattern)])) % 10*9
            HashT = (HashT + 10*9) % 10*9
    return Occurrences


if _name_ == '_main_':
    print_occurrences(get_occurrences(*read_input()))
