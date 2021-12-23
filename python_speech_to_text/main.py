import serial.tools.list_ports
import time
import speech_recognition as sr

# Get all the ports
def get_ports():
    ports = serial.tools.list_ports.comports()
    return ports


# find arduino's port
def findArduino(portsFound):
    commPort = 'None'
    numConnection = len(portsFound)
    for i in range(0,numConnection):
        port = portsFound[i]
        strPort = str(port)
        if 'Arduino' in strPort: 
            splitPort = strPort.split(' ')
            commPort = (splitPort[0])
    return commPort

                  
foundPorts = get_ports()        
connectPort = findArduino(foundPorts)

#If arduino's port was successfully found
if connectPort != 'None':
    #Establish communication with the arduino
    arduino = serial.Serial(connectPort, baudrate = 9600, timeout=1)
    arduino.timeout = 1

    while True:
        time.sleep(0.05)
        r = sr.Recognizer() #Initialize speech recognizer
        with sr.Microphone() as source:
            print("Please talk....")
            audio_text = r.listen(source)
            print("Caught audio....")
            try:
                audio_text = r.recognize_google(audio_text) #Put this inside try to avoid multiple instances error
                if audio_text == "close":
                    arduino.write(audio_text.encode())
                    print('Exiting the program')
                    break
                arduino.write(audio_text.encode())
                print(arduino.readline().decode('ascii'))
                print('-------------------------------------------------------------------------')
            except:
                print("Sorry, I did not get that")
    arduino.close()   

#If arduino's port wasn't successfully found 
else:
    print('Couldn\'t connect to the arduino. Please try again!')

