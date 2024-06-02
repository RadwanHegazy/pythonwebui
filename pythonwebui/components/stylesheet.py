from .base import BaseComponent



class Style (BaseComponent) :
    namespace = 'style'
    replaced = '</style>'
    main = """
    * {
        padding:0;
        margin:0;
        box-sizing:border-box;
    }\n
"""

    def __init__(self, attr:dict={}) -> None:
        super().__init__(stylesheet=None, class_name='', id_name='', tags=None)
        self.str_build = super().build()
    
        self.attr = attr
        for key,val in self.attr.items() :
            key:str = key
            val:dict = val
            style = "\n\t" + key +"{\n"

            for css_k, css_v in val.items() : 
                style += f'\t\t{css_k}:{css_v};\n'

            style += '}\n'
            self.main += style

        self.new =self.str_build.replace(
            self.replaced, f'{self.main}\n{self.replaced}'
        )

        self.main = self.new



    def build(self) -> str:
        return self.main
    

