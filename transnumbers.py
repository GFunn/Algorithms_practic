letters = {
        1: '壹', 2: '贰', 3: '叁', 4: '肆', 5: '伍',
        6: '陆', 7: '柒', 8: '捌', 9: '玖', 0: '零'
}

digits = {0: '', 1: '拾', 2: '佰', 3: '仟', 4: '万', 5: '拾万'}


def trans_number(x):
    parts = [int(i) for i in str(x)]
    output = ''
    i = 1
    for item in parts:
        if item != 0:
            letter = letters[item]
            digit = digits[len(parts) - i]
            output = output + letter + digit
            i += 1
        else:
            output = output + '零'
            i += 1
    return output


x = input('input number here: ')
print(trans_number(x))
