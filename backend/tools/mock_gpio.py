"""
This file contains code sourced from the Mock.GPIO project:
https://github.com/codenio/Mock.GPIO

All credit for the original implementation goes to the original authors of that repository.
This code is included here for reference, testing, or educational
purposes and has not been written by me.

License and ownership details remain with the original creators.
"""

from backend.tools.logger import Logger

logger = Logger.get_logger(__name__)


BCM = 11
BOARD = 10
BOTH = 33
FALLING = 32
HARD_PWM = 43
HIGH = 1
I2C = 42
IN = 1
LOW = 0
OUT = 0
PUD_DOWN = 21
PUD_OFF = 20
PUD_UP = 22
RISING = 31

RPI_INFO = {
    "MANUFACTURER": "Sony",
    "P1_REVISION": 3,
    "PROCESSOR": "BCM2837",
    "RAM": "1G",
    "REVISION": "a020d3",
    "TYPE": "Pi 3 Model B+",
}
RPI_REVISION = 3
SERIAL = 40
SPI = 41
UNKNOWN = -1
VERSION = "0.7.0"

_MODE = 0
channel_config = {}

# Flags
SET_MODE_DONE = False


class Channel:
    """Represents a GPIO channel configuration."""

    def __init__(self, channel, direction, initial=0, pull_up_down=PUD_OFF):
        self.channel_number = channel
        self.direction = direction
        self.initial = initial
        self.pull_up_down = pull_up_down

    def __repr__(self):
        return (
            f"Channel(channel={self.channel_number}, direction={self.direction}, "
            f"initial={self.initial}, pull_up_down={self.pull_up_down})"
        )

    def __str__(self):
        return f"Channel {self.channel_number} configured as {self.direction}"


# GPIO LIBRARY Functions
def setmode(mode):
    """
    Set up numbering mode to use for channels.
    BOARD - Use Raspberry Pi board numbers
    BCM   - Use Broadcom GPIO 00..nn numbers
    """
    global SET_MODE_DONE, _MODE
    if mode == BCM:
        SET_MODE_DONE = True
        _MODE = mode
    elif mode == BOARD:
        SET_MODE_DONE = True
    else:
        SET_MODE_DONE = False


def getmode():
    """
    Get numbering mode used for channel numbers.
    Returns BOARD, BCM or None
    """
    return _MODE


def setwarnings(flag):
    """
    Enable or disable warning messages.
    """
    logger.info("Set warnings as %s", flag)


def setup(channels, direction, initial=0, pull_up_down=PUD_OFF):
    """
    Set up a GPIO channel or list of channels with a direction and (optional) pull up/down control.
    """
    if isinstance(channels, (list, tuple)):
        for channel in channels:
            logger.info(
                "Setup channel: %s as %s with initial: %s and pull_up_down: %s",
                channel,
                direction,
                initial,
                pull_up_down,
            )
            channel_config[channel] = Channel(channel, direction, initial, pull_up_down)
    else:
        logger.info(
            "Setup channel: %s as %s with initial: %s and pull_up_down: %s",
            channels,
            direction,
            initial,
            pull_up_down,
        )
        channel_config[channels] = Channel(channels, direction, initial, pull_up_down)


def output(channel: int, values: int):
    """
    Output to a GPIO channel

    channel - either board pin or BCM number depending on which mode is set.
    values   - 0/1 or False/True or LOW/HIGH

    """
    logger.info("Output channel : %s with value : %s", channel, values)


def gpio_input(channel):
    """
    Input from a GPIO channel.  Returns HIGH=1=True or LOW=0=False
    channel - either board pin or BCM number depending on which mode is set.
    """
    logger.info("Reading from channel %s", channel)


def wait_for_edge(channel, edge, bouncetime, timeout):
    """
    Wait for an edge.  Returns the channel number or None on timeout.
    channel      - either board pin number or BCM number depending on which mode is set.
    edge         - RISING, FALLING or BOTH
    [bouncetime] - time allowed between calls to allow for switchbounce
    [timeout]    - timeout in ms
    """
    logger.info(
        "Waiting for edge : %s on channel : %s with bounce time : %s and Timeout :%s",
        edge,
        channel,
        bouncetime,
        timeout,
    )


def add_event_detect(channel, edge, callback=None, bouncetime=None):
    """
    Enable edge detection events for a particular GPIO channel.
    channel      - either board pin or BCM number depending on which mode is set.
    edge         - RISING, FALLING or BOTH
    [callback]   - A callback function for the event (optional)
    [bouncetime] - Switch bounce timeout in ms for callback
    """
    logger.info(
        "Event detect added for edge : %s on channel : %s with bounce time : %s and callback %s",
        edge,
        channel,
        bouncetime,
        callback,
    )


def event_detected(channel):
    """
    Returns True if an edge has occurred on a given GPIO.
    You need to enable edge detection using add_event_detect() first.
    channel - either board pin or BCM number depending on which mode is set.
    """
    logger.info("Waiting for even detection on channel :%s", channel)


def add_event_callback(channel, callback):
    """
    Add a callback for an event already defined using add_event_detect()
    channel      - either board pin or BCM number depending on which mode is set.
    callback     - a callback function
    """
    logger.info("Event callback : %s added for channel : %s", callback, channel)


def remove_event_detect(channel):
    """
    Remove edge detection for a particular GPIO channel

    channel - either board pin or BCM number depending on which mode is set.
    """
    logger.info("Event detect removed for channel : %s", channel)


def gpio_function(channel):
    """
    Return the current GPIO function (IN, OUT, PWM, SERIAL, I2C, SPI)
    channel - either board pin or BCM number depending on which mode is set.
    """
    logger.info(
        "GPIO function of channel : %s is %s",
        channel,
        channel_config[channel].direction,
    )


class PWM:
    """Represents a PWM channel."""

    def __init__(self, channel, frequency):
        """
        Initialize PWM channel.
        """
        self.channel = channel
        self.frequency = frequency
        self.dutycycle = 0
        channel_config[channel] = Channel(channel, HARD_PWM)
        logger.info(
            "Initialized PWM for channel: %s at frequency: %s", channel, frequency
        )

    def start(self, dutycycle):
        """
        Start software PWM.
        """
        self.dutycycle = dutycycle
        logger.info(
            "Start PWM on channel: %s with duty cycle: %s", self.channel, dutycycle
        )

    def change_frequency(self, frequency):
        """
        Change the frequency.
        """
        logger.info(
            "Frequency changed for channel: %s from: %s -> to: %s",
            self.channel,
            self.frequency,
            frequency,
        )
        self.frequency = frequency

    def change_duty_cycle(self, dutycycle):
        """
        Change the duty cycle.
        """
        self.dutycycle = dutycycle
        logger.info(
            "Duty cycle changed for channel: %s from: %s -> to: %s",
            self.channel,
            self.dutycycle,
            dutycycle,
        )

    def stop(self):
        """
        Stop PWM generation.
        """
        logger.info(
            "Stop PWM on channel: %s with duty cycle: %s", self.channel, self.dutycycle
        )


def cleanup(channels=None):
    """
    Clean up by resetting all GPIO channels that have been used by this program to
    INPUT with no pullup/pulldown and no event detection

    [channels] - individual channel or list/tuple of channels to clean up.
    Default - clean every channel that has been used.
    """
    if channels is not None:
        if isinstance(channels, (list, tuple)):
            for channel in channels:
                logger.info("Cleaning up channel : %s", channel)
        else:
            logger.info("Cleaning up channel : %s", channels)
    else:
        logger.info("Cleaning up all channels")
