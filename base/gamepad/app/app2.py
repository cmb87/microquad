"""Simple example showing how to get gamepad events."""
from __future__ import print_function
from inputs import get_gamepad
import time
import logging
import socketio
import config


# =============================================
# Set logging formats
logging.basicConfig(
    level=config.server["logginglevel"],
    format=("[%(filename)8s] [%(levelname)4s] :  %(funcName)s - %(message)s"),
)

# standard Python
sio = socketio.Client()


class Gamepad:

    # =================================
    QUADCONT = {
        "ABS_Z": {"lb":127, "ub":-128, "iv":0, "lbm":1000, "ubm":1350, "description":"throttle", "invert": False},
        "ABS_X": {"lb":-128, "ub":127, "iv":0, "lbm":1000, "ubm":2000, "description":"roll", "invert": False},
        "ABS_Y": {"lb":-128, "ub":127, "iv":0, "lbm":1000, "ubm":2000, "description":"pitch", "invert": True},
        "ABS_HAT0X": {"lb":-1, "ub":1, "iv":0, "lbm":1100, "ubm":1900, "description":"yaw", "invert": False},

        "BTN_THUMB": {"lb":0, "ub":1, "iv":0, "lbm":1100, "ubm":1800, "description":"aux1", "activated": False},
        "BTN_TOP": {"lb":0, "ub":1, "iv":0, "lbm":1100, "ubm":1800, "description":"aux2", "activated": False},
    }

    # =================================
    def __init__(self):

        self.state = {
            "throttle":Gamepad.QUADCONT["ABS_Z"]["lbm"],
            "pitch":1500,
            "roll":1500,
            "yaw":1500,
            "aux1": 1000,
            "aux2": 1000,
        }

    # =================================
    def start(self):
        """Just print out some event infomation when the gamepad is used."""

        while True:


            events = get_gamepad()

            for event in events:


                print(event.ev_type, event.code, event.state)

                if event.code in ["ABS_X", "ABS_Y", "ABS_Z", "ABS_HAT0X"]:
                    
                    if Gamepad.QUADCONT[event.code]['invert']:
                        val = 1.0 -(event.state-Gamepad.QUADCONT[event.code]['lb'])/(Gamepad.QUADCONT[event.code]['ub']-Gamepad.QUADCONT[event.code]['lb'])
                    else:
                        val = (event.state-Gamepad.QUADCONT[event.code]['lb'])/(Gamepad.QUADCONT[event.code]['ub']-Gamepad.QUADCONT[event.code]['lb'])

                    val = int(Gamepad.QUADCONT[event.code]['lbm'] + val*(Gamepad.QUADCONT[event.code]['ubm']-Gamepad.QUADCONT[event.code]['lbm']))
                    self.state[Gamepad.QUADCONT[event.code]['description']] = val
 
               
                if event.code in ["BTN_THUMB", "BTN_TOP"]:
                    # Deactivate Button from activated state
                    if Gamepad.QUADCONT[event.code]['activated'] and event.state == 1:
                        self.state[Gamepad.QUADCONT[event.code]['description']] = Gamepad.QUADCONT[event.code]['lbm']
                        Gamepad.QUADCONT[event.code]['activated'] = False
                    
                    # Activate Button
                    elif not Gamepad.QUADCONT[event.code]['activated'] and event.state == 1:
                        self.state[Gamepad.QUADCONT[event.code]['description']] = Gamepad.QUADCONT[event.code]['ubm']
                        Gamepad.QUADCONT[event.code]['activated'] = True


            sio.emit('gamepad', [self.state[k] for k in ["pitch", "roll", "throttle", "yaw", "aux1", "aux2" ]])


def main():
    while True:
        try:
            sio.connect(f"ws://{config.server['hostname']}:{config.server['port']}", namespaces=[config.server['namespace']])
            logging.info("Connected!")
            break
        except:
            logging.warning(f"Could not connect to server ws://{config.server['hostname']}:{config.server['port']}")
            time.sleep(4)

    print("starting gamepad")
    g = Gamepad()
    g.start()

if __name__ == "__main__":
    main()
