def trim(phrase, size):
    if len(phrase) <= size:
        return phrase
    elif len(phrase) <= 3 or len(phrase[:size]) <= 3:
        return phrase[:size] + '...'
    else:
        return phrase[:size - 3] + '...'


def mango(quantity, price):
    return (quantity - quantity // 3) * price


def unique_in_order(sequence):
    output = []
    if len(sequence) == 0:
        return output
    elif len(sequence) == 1:
        output.append(sequence[0])
        return output
    else:
        for i in range(len(sequence)):
            if i == 0:
                output.append(sequence[i])
            elif i == len(sequence) - 1:
                if sequence[i] != sequence[i - 1]:
                    output.append(sequence[i])
            else:
                if sequence[i - 1] != sequence[i] and sequence[i + 1]:
                    output.append(sequence[i])
        return output

# print(trim("Hello, world!", 8))
# print(mango(9, 5))
# print(unique_in_order("ABBCcA"))
