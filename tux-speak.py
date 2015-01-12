#! /usr/bin/python
""" simple TTS script for TuxDroid """

from tuxisalive.api.TuxAPI import *
import argparse
import sys

# parse parameters and options
parser = argparse.ArgumentParser(description='TuxDroid text-to-speech')

parser.add_argument('-t',
                    dest='tts',
                    help='text to speak',
                    required='True')

args = parser.parse_args()

tts = args.tts


# connect to the Tux API
tux = TuxAPI('127.0.0.1', 54321)
tux.server.autoConnect(CLIENT_LEVEL_RESTRICTED, 'TuxPyFoo', 'NONE')
tux.server.waitConnected(2.0)
tux.dongle.waitConnected(2.0)
tux.radio.waitConnected(2.0)

# open our mouth and let the words flow
tux.mouth.open()
tux.tts.speak(tts)
tux.mouth.close()

# clean up our API connection
tux.server.disconnect()
tux.destroy()

# drop back to the shell
sys.exit(0)
