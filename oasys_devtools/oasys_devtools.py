import cv2
import argparse
import sys
import uuid
import requests

"""
some text
"""

parser = argparse.ArgumentParser()

sp = parser.add_subparsers(dest='videomode')

rstp = sp.add_parser('rstp')
rstp.set_defaults(vid=lambda: cv2.VideoCapture(f"rstp"))

webcam = sp.add_parser('webcam')
webcam.set_defaults(vid=lambda: cv2.VideoCapture(-1))

media = sp.add_parser('media')
media.set_defaults(vid=lambda: cv2.VideoCapture(f"path"))

parser.add_argument('--cam', metavar='user:pass@ipaddress', type=str,
                    help='Cam access information')

parser.add_argument('--area', metavar='N', type=int, nargs=4,
                    help='Area restriction')

parser.add_argument('--id', metavar='uuid4', type=str,
                    help='Instance UUID')

parser.add_argument('--token', metavar='token', type=str,
                    help='Instance token')

parser.add_argument('--reporturl', metavar='url', type=str,
                    help='Report url endpoint')

args = parser.parse_args()

class Oasys:
    def __init__(self, debug: bool = False, report_url: str = False):
        self.id = args.id
        self.token = args.token
        self.args = args

        self.debug = debug
        self.reporturl = report_url if report_url else args.reporturl

    def video(self) -> cv2:
        """
            Get video instance
        """
        return self.args.vid()

    def report(self, endpoint: str = '', data: object = {}): 
        """
            Send data to the report server
        """
        data['instance_id'] = self.id
        data['instance_token'] = self.token


        url = self.reporturl + endpoint
        return requests.post(url, data=data)


def hello():
    print("Hello")