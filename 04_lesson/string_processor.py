
class StringProcessor:
    @staticmethod
    def process(text):
        if not isinstance(text, str):
            return '.'
        if text is None:
            return '.'
        processed_text = text[0].upper() + text[1:]
        if not processed_text.endswith('.'):
            processed_text += '.'
        return processed_text

print(type(None))