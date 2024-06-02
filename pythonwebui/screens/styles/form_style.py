from pytohtml.style import components as style_compo

REGISTER_STYLE = {
    
    'body' : {
        **style_compo.FlexColumn.attrs,
        'position' : 'relative',
        'width' : '100%',
        'height' : '100vh',
        'font-family' : 'sans-serif',
    },


    'img.bg': {
        'position' : 'absolute',
        'width' : '100%',
        'height' : '100vh',
        'z-index' : -1,
    },


    '.container' : {
        **style_compo.FormStyle.attrs,
        'width' : '400px',
        'height' : 'auto',
        'padding' : '1.3rem 1.9rem',
        'backdrop-filter' : 'blur(30px)',
        'border-radius' : '20px',
        
    },


    '.container input' : {
        **style_compo.InputStyle.attrs,
        'color' : '#fff'
    },

    '.container .btns' : {
        **style_compo.FlexRow.attrs,
        'width' : '100%',
        'justify-content' : 'space-between',
    },

    '.btns a' : {
        'color' : '#0082ff'
    },

    '.btns button' : {
        'width' : '120px',
        'height' : "45px",
        
        'border' : 'none',
        'outline' : 'none',
        'background-color' : "#fcaf3c",
        'color' : '#fff',
        'border-radius' : '12px',
        'cursor' : 'pointer',
    }

}