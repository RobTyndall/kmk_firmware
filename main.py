print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers

LVSio = KMKKeyboard() #declaration of the input panel as an instance of a KMKKeyboard
LVSio.debug_enabled #Enables more verbose serial console output
layers = Layers()
encoder_handler = EncoderHandler()
LVSio.modules = [layers, encoder_handler] #import encoder module


LVSio.col_pins = (board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15) #declaration of hardware column pins
LVSio.row_pins = (board.GP20, board.GP19, board.GP18, board.GP17, board.GP16) #declaration of hardware row pins
LVSio.diode_orientation = DiodeOrientation.COL2ROW #declaration of hardware diode direction (current flows from the column pins to the row pins when a switch is closed.)

encoder_handler.pins = ((board.GP0, board.GP1), (board.GP2, board.GP3), (board.GP4, board.GP5),
(board.GP6, board.GP7), (board.GP8, board.GP9), (board.GP21, board.GP22), )
 #declaration of hardware encoder pins, each tuple is for one encoder (Pin A, Pin B, Buttton Pin, Inverted), so there are 6 tuples

LVSio.keymap = [
    [KC.E,  KC.W,  KC.Q,  KC.R,  KC.VOLU,    KC.NO, #E and Q unfortunately switched
     KC.RCTL(KC.R),  KC.S,  KC.A,  KC.F,  KC.VOLD,    KC.NO, #CTRL+R and A unfortunately switched
     KC.Z,  KC.X,  KC.C,  KC.V,  KC.B,       KC.N,
     KC.I,  KC.U,  KC.Y,  KC.O,  KC.P,       KC.NO, #I and Y unfortunately switched
     KC.K,  KC.J,  KC.H,  KC.L,  KC.SCOLON,  KC.NO, #H and K unfortunately switched
    ]
]

encoder_handler.map = [(
(KC.N1, KC.N2),
(KC.N3, KC.N4),
(KC.N5, KC.N6),
(KC.N7, KC.N8),
(KC.N9, KC.N0),
(KC.N1, KC.N2), ),
]
 #declaration of the output keystroke for each encoder, similar to encoder pin declaration (Left key, Right key, pushbutton key)

if __name__ == '__main__':
    LVSio.go()
