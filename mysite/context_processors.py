# https://www.google.com/url?q=https://stackoverflow.com/questions/34902707/how-can-i-pass-data-to-django-layouts-like-base-html-without-having-to-provi/34903331&sa=D&source=hangouts&ust=1587514845679000&usg=AFQjCNHKhgLwSVQe4FYZMTwpKllVTsdL4A

def add_variable_to_context(request):
    return {
        'Eliri_name': 'Eliri',
        'Mythe_name': 'Ilemythe',
        'Vogel_name': 'Vogel'
    }
