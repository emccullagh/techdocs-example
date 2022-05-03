def define_env(env):
    """Functions for formatting link text, etc"""

    @env.macro
    def rfc(id, section='', text=''):
        text = text if text != '' else 'RFC {id}'.format(id=id)
        return '[{text}](https://tools.ietf.org/html/rfc{id}#{section})'.format(text=text, id=id, section=section)

