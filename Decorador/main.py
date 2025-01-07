class Text:
    def render(self):
        return "Hola, Mundo!"

class TextDecorator:
    def __init__(self, text: Text ):
        self._text = text

    def render(self):
        return self._text.render()

class UpperCaseDecorator(TextDecorator):
    def render(self):
        return self._text.render().upper()

class BorderDecorator(TextDecorator):
    def render(self):
        return f"*** {self._text.render()} ***"

# Texto base
simple_text = Text()

# Decoramos el texto
uppercase_text = UpperCaseDecorator(simple_text)
bordered_text = BorderDecorator(uppercase_text)

# Renderizamos
print(simple_text.render())       # Output: Hola, Mundo!
print(uppercase_text.render())    # Output: HOLA, MUNDO!
print(bordered_text.render())     # Output: *** HOLA, MUNDO! ***
