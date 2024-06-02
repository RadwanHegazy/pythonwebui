
class BaseStyle :
    attrs:dict = {}

    def build (self) : 
        elements = "{\n"
        for ele in [f'\t{k}:{v};\n' for k,v in self.attrs.items()] :
            elements += ele
        elements += "}\n"
        return  elements  
