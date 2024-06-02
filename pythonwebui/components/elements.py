from .base import BaseComponent



class Div (BaseComponent) :
    namespace = 'div'

class Section (BaseComponent) : 
    namespace = 'section'

class Form (BaseComponent) : 
    namespace = 'form'

class Img (BaseComponent) :
    namespace = 'img'
    has_end = False

class Hyperlink (BaseComponent) :
    namespace = 'a'

class Button (BaseComponent) : 
    namespace = 'button'

class Input (BaseComponent) : 
    namespace = 'input'
    has_end = False

class Video (BaseComponent) : 
    namespace = 'video'

class H1 (BaseComponent) : 
    namespace = 'h1'

class H2 (BaseComponent) : 
    namespace = 'h2'

class H3 (BaseComponent) : 
    namespace = 'h3'

class P (BaseComponent) : 
    namespace = 'p'