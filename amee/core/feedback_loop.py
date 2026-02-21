from typing import Dict, Any
import logging
from .Module import Module

logger = logging.getLogger(__name__)

class FeedbackLoop:
    """
    The feedback loop component responsible for monitoring and adapting modules based on real-time data.
    """

    def __init__(self):
        self.architect = None
        self.sensors = []
        self.effectors = []

    def initialize(self, architect: 'Architect') -> None:
        """
        Initialize the feedback loop with an architect instance.

        Args:
            architect: The Architect instance to manage modules.
        """
        if not isinstance(architect, Architect):
            raise ValueError("Architect must be an instance of Architect.")
        self.architect = architect
        logger.info("Feedback loop initialized.")

    def add_sensor(self, sensor) -> None:
        """
        Add a sensor to the feedback loop.

        Args:
            sensor: The sensor instance to be added.
        """
        if not hasattr(sensor, 'sense'):
            raise ValueError("Sensor must have a 'sense' method.")
        self.sensors.append(sensor)
        logger.info(f"Added sensor '{sensor}'.")

    def add_effector(self, effector) -> None:
        """
        Add an effector to the feedback loop.

        Args:
            effector: The effector instance to be added.
        """
        if not hasattr(effector, 'act'):
        raise ValueError("Effector must have an 'act' method.")
        self.effectors.append(effector)
        logger.info(f"Added effector '{effector}'.")

    def monitor(self) -> Dict[str, Any]:
        """
        Monitor the environment and return sensory data.
        """
        data = {}
        for sensor in self.sensors:
            try:
                reading = sensor.sense()
                data[sensor.__class__.__name__] = reading
            except Exception as e:
                logger.error(f"Sensor {sensor} failed to sense: {str(e)}")
        return data

    def adapt(self, feedback: Dict[str, Any]) -> None:
        """
        Adapt the system based on received feedback.

        Args:
            feedback: The feedback data used for adaptation.
        """
        if not self.architect:
            raise RuntimeError("Feedback loop is not initialized with an architect.")
        logger.info("Adapting system based on feedback.")
        # Implementation would involve using feedback to optimize module interactions