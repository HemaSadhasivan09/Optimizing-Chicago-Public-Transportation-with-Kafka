"""Contains functionality related to Weather"""
import logging


logger = logging.getLogger(__name__)


class Weather:
    """Defines the Weather model"""

    def __init__(self):
        """Creates the weather model"""
        self.temperature = 70.0
        self.status = "sunny"

    def process_message(self, message):
        """Handles incoming weather data"""
        logger.info("weather process_message is in progress")
        #
        #
        # TODO: Process incoming weather messages. Set the temperature and status.
        #
        #
        if message.topic() == "com.udacity.cta.weather.v1":
            weather = message.value()
            self.temperature = weather['temperature']
            self.status = weather['status']
        else:
            logger.error("Expected weather topic but received %s", message.topic)