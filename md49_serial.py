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

def SET_SPEED_1(speed):
        strSpeed = struct.pack("B",speed)
        writeBytes("\x00\x31" + strSpeed)

def SET_SPEED_2(speed):
        strSpeed = struct.pack("B",speed)
        writeBytes("\x00\x32" + strSpeed)

def GET_ENCODER_1():
        writeBytes("\x00\x23")
        encByte = struct.unpack("B",port.read())
        encByte += struct.unpack("B",port.read())
        encByte += struct.unpack("B",port.read())
        encByte += struct.unpack("B",port.read())
        encoder = (encByte[0] << 24) + (encByte[1] << 16) + (encByte[2] << 8) + encByte[3]
        return encoder

def GET_ENCODER_2():
        writeBytes("\x00\x24")
        encByte = struct.unpack("B",port.read())
        encByte += struct.unpack("B",port.read())
        encByte += struct.unpack("B",port.read())
        encByte += struct.unpack("B",port.read())
        encoder = (encByte[0] << 24) + (encByte[1] << 16) + (encByte[2] << 8) + encByte[3]
        return encoder

SET_MODE(0)
SET_SPEED_1(190)
SET_SPEED_2(190)
print GET_ENCODER_1()

