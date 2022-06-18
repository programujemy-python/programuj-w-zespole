# Definiowanie funkcji w Python a34


def function_name():
    some_value = 20
    print("This is a sample function printing some text.")
    value = 4 * some_value
    print(f"And printing some value = {value}.")


def function_test_type(first_param, second_param):
    if type(first_param) is int or type(second_param) is int:
        return "One parameter is a number"
    if type(second_param) is str:
        return "Second is string"
    if type(first_param) is float:
        return first_param * 5

    # jeśli żaden z powyższych nie zadziała
    return "Hmm... I don't know, what to do."


def function_returns_tuple(param):
    if type(param) is not int:
        return None

    some_value = 4.5
    value_1 = some_value * param
    some_value = "TEXT "
    value_2 = some_value * param
    return value_1, value_2


# wywołanie funkcji kontra nazwa funkcji
function_name()
function_name
print(function_name)
print("----------------------------------------------")

function_name()
# poniższe wywołania nie wypiszą nic na ekranie
function_test_type(1, 2)
function_returns_tuple(3)
print("----------------------------------------------")
# wywołanie z przypisaniem zwracanej wartości,
# nawet gdy funkcja nie zwraca jawnie 'return'
ret_value = function_name()
print(f"Funkcja bez return zwraca: {ret_value}")
print("----------------------------------------------")

ret_value = function_test_type(1, 2.0)
print(ret_value)
ret_value = function_test_type("Adam", "Beata")
print(ret_value)
ret_value = function_test_type(1, "Beata")
print(ret_value)
ret_value = function_test_type(1.0, None)
print(ret_value)
ret_value = function_test_type("Nic", None)
print(ret_value)
ret_value = function_returns_tuple(3)
print(ret_value)
ret_value = function_returns_tuple("Python")
print(ret_value)
