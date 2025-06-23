def format_name(f_name, l_name):
    print(f_name.title())
    print(l_name.title())

format_name("pranav", "KUMBHAR")

#docstrings in Python
#They give some info about the functions we create

#example 

def name_combined(f_name, l_name):
    """combines first and lastname, formats it and returns a combined name.""" #first indented line is for docstrings.
    formatname = f_name.title()
    formatlname = l_name.title()
    return f"{formatname} {formatlname}"

print(name_combined("pRanav", "kumbhar"))

