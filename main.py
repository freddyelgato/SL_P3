from fasthtml.common import *

app,rt = fast_app()

@rt('/change')
def get(): return P('Nice to be here!')

@rt('/')
def get(): return Div(P('Hello World My name is Freddy!'), hx_get="/change")

serve()