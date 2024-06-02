

class BaseComponent :
    
    namespace = None
    has_end = True

    def __init__(self, stylesheet:dict={}, class_name:str='', id_name:str='', tags:dict={}, text:str='') -> None:
        self.class_name = class_name
        self.id_name = id_name
        self.stylesheet = stylesheet
        self.childs = []
        self.tags = tags
        self.text = text

    def getStyleSheetCode (self):
        style = 'style="'
        for key, val in self.stylesheet.items() : 
            style += f'{key}:{val};'
        style += '"'
        return style
    
    def build (self) ->str:
        
        element = f"\n\t<{self.namespace} "
        if self.class_name != "" : 
            element += f"class='{self.class_name}' "
        
        if self.id_name != "" :
            element += f"id='{self.id_name}' "

        if self.stylesheet:
            element += f"{self.getStyleSheetCode()}"
        
        if self.tags:
            for key, val in self.tags.items() : 
                element += f'{key}="{val}" '
        
        element += ">\n\t\t\t"

        if self.has_end == False and self.text != "" :
            raise Exception("you can set a text for this element")

        if self.text != "" :
            element += self.text

        if self.has_end : 
            element += self.build_childs() + '\n\t'
            element += f'</{self.namespace}>\n'

        return element
    

    def build_childs (self) -> str:
        childs_body = ""
        for child in self.childs:
            childs_body += f'{child.build()}\n'
        return childs_body


    def append_child(self, sub_childs=[]) :
        if self.has_end == False:
            raise Exception(f'can not append childs for this element : {self.__class__.__name__}')
        
        for i in sub_childs:
            self.childs.append(i)
            
        return self