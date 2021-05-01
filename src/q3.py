def sortlist():
    STRING_LIST=[12,24,35,24,88,120,155,88,120,155]

    # convert each element into individual integers
    INTEGER_LIST = []

    for number in STRING_LIST:
        INTEGER_LIST.append(int(number))
    print("list (Integer_List) : ", INTEGER_LIST)

    DISTINCT_ELEMENT = []
    DISTINCT_ELEMENT = set(INTEGER_LIST)
    print(DISTINCT_ELEMENT)
    print(type(DISTINCT_ELEMENT))

    RESULT = []
    for element in INTEGER_LIST:
        if element in DISTINCT_ELEMENT:
            RESULT.append(element)
            DISTINCT_ELEMENT.remove(element)

    return RESULT