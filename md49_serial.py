import serial
import struct

port  = serial.Serial("/dev/ttyS0", baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)

def writeBytes(bytes):
        port.write(bytes)


def RESET_ENCODERS():
        writeBytes("\x00\x35")

def SET_MODE(mode):
        strMode = struct.pack("B",mode)
        writeBytes("\x00\x34" + strMode)

def GET_ENCODER_1():
        writeBytes("\x00\x23")
        bytes = port.read(4)
        encoderValue = struct.unpack('L',bytes)
        print(str(encoderValue))

def SET_SPEED_1(speed):
        strSpeed = struct.pack("B",speed)
        writeBytes("\x00\x31" + strSpeed)


def SET_SPEED_2(speed):
        strSpeed = struct.pack("B",speed)
        writeBytes("\x00\x32" + strSpeed)


SET_MODE(0)
RESET_ENCODERS()
SET_SPEED_1(190)
GET_ENCODER_1()
