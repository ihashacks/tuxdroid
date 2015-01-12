#! /usr/bin/python
""" simple TTS script for TuxDroid """

from tuxisalive.api.TuxAPI import *
import argparse
import sys

# parse parameters and options
parser = argparse.ArgumentParser(description='TuxDroid text-to-speech')

parser.add_argument('-H',
                    dest='host',
                    help='TuxDroid API server to connect to',
                    default='127.0.0.1',
                    required=False)
parser.add_argument('-p',
                    dest='port',
                    help='TuxDroid API port to connect to',
                    default='54321',
                    required=False,
                    type=int)
parser.add_argument('-t',
                    dest='tts',
                    help='text to speak',
                    required=True)

args = parser.parse_args()

host = args.host
port = args.port
tts = args.tts

# connect to the Tux API
tux = TuxAPI(host, port)
tux.server.autoConnect(CLIENT_LEVEL_RESTRICTED, 'TuxSpeakPy', 'NONE')
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
