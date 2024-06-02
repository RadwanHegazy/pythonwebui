from dataclasses import dataclass
from .components.base import BaseComponent


class Head (BaseComponent) :
    title = ""
    def build(self) -> str:
        return f"""
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.title}</title>
</head>
        """ 


class Body (BaseComponent):
    def build(self) -> str:
        return f"""
<body>
    {self.build_childs()}
</body>        
"""
    

class Html (BaseComponent) : 
    def build(self) -> str:
        return f"""
<!DOCTYPE html>
<html lang="en">
{self.build_childs()}
</html>
"""

class Page :
    
    def __init__(self, title:str) -> None:
        self.title = title
        self.head = Head()
        self.head.title = title
        self.body = Body()


    def save (self, name:str) : 
        name = name if name.endswith('.html') else name + '.html'
        html_file = open(name, 'w', encoding='utf-8')
        text = self.get_html_text
        html_file.write(text)
        html_file.close()


    @property
    def get_html_text(self) : 
        self.html = Html()
        self.html.childs = [self.head, self.body] # important arrangement
        return self.html.build()