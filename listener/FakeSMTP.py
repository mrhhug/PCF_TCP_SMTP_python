import asyncio
import logging

#from smtplib import SMTP
from aiosmtpd.controller import Controller
from aiosmtpd.handlers import Sink
from aiosmtpd.handlers import Mailbox
from aiosmtpd.handlers import Debugging

#to get the port
from os import getenv

myPort = int(getenv("PORT"))

async def amain(mainEventLoop):
    cont = Controller(Debugging(), hostname='0.0.0.0', port=myPort)
    cont.start()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    eventLoop = asyncio.get_event_loop()
    eventLoop.create_task(amain(mainEventLoop=eventLoop))
    try:
        eventLoop.run_forever()
    except KeyboardInterrupt:
        pass
