def atom(variable=None):

    def get_val():
        return variable

    def set_val(value):
        nonlocal variable
        variable = value
        return variable

    def process_val(*func):
        nonlocal variable
        for i in func:
            variable = i(variable)
        return variable

    def delete_val():
        nonlocal variable
        del variable

    return get_val(), set_val(6), process_val(range, list), delete_val()


print(atom(4))
