""" extracting company name """
def extract_name(name):
    """ will convert name into list """
    information = name
    information = information.split('@')
    company_name = information[1]
    company_name = company_name.split('.')
    return company_name[0]

EMAIL = input("Enter Email Address: ")
extract_name(EMAIL)
print(extract_name(EMAIL))