from abc import ABC, abstractmethod
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)

class Module(ABC):
    """
    Abstract base class for modules within the Autonomous Modular Evolution Engine (AMEE).
    
    Modules are self-contained components that can operate independently or integrate with other modules in an ecosystem.
    """

    @abstractmethod
    def initialize(self, config: Dict[str, Any]) -> None:
        """
        Initialize the module with the given configuration.

        Args:
            config: The configuration parameters for the module.
        """
        pass

    @abstractmethod
    def process(self, input_data: Any) -> Any:
        """
        Process input data and return output.

        Args:
            input_data: The input data to be processed.

        Returns:
            The processed output data.
        """
        pass

    @abstractmethod
    def adapt(self, feedback: Dict[str, Any]) -> None:
        """
        Adapt the module based on received feedback.

        Args:
            feedback: The feedback data used for adaptation.
        """
        pass

    @abstractmethod
    def terminate(self) -> None:
        """
        Cleanly terminate the module's operations.
        """
        pass

    def __init__(self):
        self.initialized = False
        self.feedback_buffer = []
        logger.info(f"Initialized module.")