from pytohtml.page import Page
from pytohtml.components import elements, stylesheet
from .styles.form_style import REGISTER_STYLE

class RootScreen:
    
    def __init__(self) -> None:
        self.input.inputs_list.clear()

    class MetaPage : 
        title = 'Register'
        output_path = 'register.html'

    class h1 : 
        text = 'register'
        stylesheet={
            'text-align' : 'center',
            'color' : "#fff",
            'font-family' : 'sans-serif',
        }

    class input : 
        inputs_list = []
        stylesheet = {}

        @classmethod
        def append_child (cls, placeholder, name, type_, index=None) :
            if index is None :
                index = len(cls.inputs_list) - 1
            
            cls.inputs_list.insert(
                index,
                {
                    'placeholder' : placeholder,
                    'name' : name,
                    'type' : type_,
                }
            )

    
    class hyperlink :
        text = "Login ?"
        href = 'https://www.google.com'
        stylesheet = {}

    class submit_button :
        text = 'Submit'
        stylesheet = {}

    class bg_img:
        src = 'images/bg.png'
        stylesheet = {}

    class form:
        method = "POST"
        enctype = 'multipart/form-data'
        stylesheet = {}
    
    class style:
        attr = REGISTER_STYLE

    def page (self) : 
        page = Page(self.MetaPage.title)
        root = page.body

        childs = [
    
            elements.H1(
                text=self.h1.text,
                stylesheet=self.h1.stylesheet

            )

        ]
        

        for i in self.input.inputs_list : 
            childs.append(
                elements.Input(
                    tags={
                        'type' : i['type'],
                        'placeholder' : i['placeholder'],
                        'name' : i['name'],
                    },
                    stylesheet=self.input.stylesheet
                ) 
            )

        childs.append(
            elements.Div(
                    class_name='btns',
                ).append_child([

                    elements.Hyperlink(
                        text=self.hyperlink.text,
                        tags={
                            'href' : self.hyperlink.href,
                        },
                        stylesheet=self.hyperlink.stylesheet
                    ),

                    elements.Button(
                        text=self.submit_button.text,
                        tags={
                            'type' : 'submit'
                        },
                        stylesheet=self.submit_button.stylesheet
                    )

                ])
        )


        root.childs = [

            stylesheet.Style(
                attr=self.style.attr
            ),

            elements.Img(
                class_name='bg',
                tags={
                    'src' : self.bg_img.src
                },
                stylesheet=self.bg_img.stylesheet
            ),

            elements.Form(
                class_name='container',
                tags={
                    'method' : self.form.method,
                    'enctype' : self.form.enctype
                },
                stylesheet=self.form.stylesheet
            ).append_child(childs)

        ]


        return page
