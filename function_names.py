def open_browser(browser_name):
    pass


def go_to_companyname_homepage(page_url):
    pass


def find_registration_button_on_login_page(page_url, button_text):
    pass


functions_list = (open_browser, go_to_companyname_homepage, find_registration_button_on_login_page)
for func in functions_list:
    print("Name of the function: ", func.__name__.replace("_", " ").capitalize())
    print("Names of the arguments:", str(func.__code__.co_varnames).replace("_", " ").replace("'", "").replace("(", "").replace(")", "").capitalize())
    print("--------------------------------------------------------------")