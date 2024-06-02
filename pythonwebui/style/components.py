from .base import BaseStyle

class Overlay (BaseStyle) : 
    attrs = {
        'position' : "fixed",
        'top': 0,
        'left' : 0,
        'width' : '100%',
        'height' : '100vh',
        'z-index' : 2,
    }


class FlexColumn (BaseStyle) : 
    attrs = {
        'display': 'flex',
        'flex-direction': 'column',
        'align-items': 'center',
        'justify-content': 'center',
    }


class FlexRow (BaseStyle) : 
    attrs = {
        'display': 'flex',
        'flex-direction': 'row',
        'align-items': 'center',
        'justify-content': 'space-between',
    }

class FormStyle (BaseStyle) :
    attrs = {
        'width' : '300px',
        'height' : 'auto',
        'padding' : '1.2rem 1.9rem',
        'gap' : '10px',
        'border-radius' : '12px',
        **FlexColumn.attrs,
        'justify-content': 'flex-start',
    }


class InputStyle (BaseStyle) : 
    attrs = {
        'width' : '100%',
        'height' : '45px',
        'padding' : "6px 12px",
        'background-color' : '#ffffff10',
        'border-radius' : '12px',
        'border' : 'none',
        'outline' : 'none',
    }