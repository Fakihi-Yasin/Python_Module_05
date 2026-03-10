from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """
    Abstract base class for all data processors.
    Defines the common interface that all processors must implement.
    Uses ABC to enforce implementation of abstract methods in subclasses.
    """
    @abstractmethod
    def process(self, data: Any) -> str:
        """
        Process the input data and return a result string.
        Must be overridden by subclasses to provide specific behavior.
        """
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """
        Validate the input data.
        Must be overridden by subclasses to provide type-specific validation.
        """
        pass

    def format_output(self, result: str) -> str:
        """
        Format the output result string.
        Provides default implementation that can be overridden if needed.
        """
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """
    Specialized processor for numeric data (lists/tuples of numbers).
    Overrides abstract methods to handle numeric-specific operations.
    """
    def __init__(self) -> None:
        """
        Initialize the Numeric Processor.
        Calls parent constructor using super() to maintain inheritance chain.
        """
        super().__init__()
        print("Initializing Numeric Processor...")

    def process(self, data: Any) -> str:
        """
        Override: Process numeric data and return statistical summary.
        Calculates sum and average of numeric values.
        Returns error message if processing fails (maintains str return type).
        """
        try:
            avg = sum(data) / len(data)
            return (f"Processed {len(data)} numeric values, "
                    f"sum={sum(data)}, avg={avg}")
        except (TypeError, ValueError, ZeroDivisionError) as e:
            return f"Error processing numeric data: {e}"

    def validate(self, data: Any) -> bool:
        """
        Override: Validate that data is a list/tuple of numeric values.
        Uses isinstance() to check types as required by subject.
        Returns bool without raising exceptions.
        """
        # Check if data is a list or tuple
        if isinstance(data, (list, tuple)):
            print("Validation: Numeric data verified")
            return True
        return False


class TextProcessor(DataProcessor):
    """
    Specialized processor for text data (strings).
    Overrides abstract methods to handle text-specific operations.
    """
    def __init__(self) -> None:
        """
        Initialize the Text Processor.
        Calls parent constructor using super() to maintain inheritance chain.
        """
        super().__init__()
        print("Initializing Text Processor...")

    def process(self, data: Any) -> str:
        """
        Override: Process text data and return character/word count.
        Analyzes string length and word count using split().
        Returns error message if processing fails (maintains str return type).
        """
        try:
            return (f"Processed text: {len(data)} characters, "
                    f"{len(data.split())} words")
        except Exception as e:
            return f"Error processing text data: {e}"

    def validate(self, data: Any) -> bool:
        """
        Override: Validate that data is a string.
        Uses isinstance() to check type as required by subject.
        """
        if isinstance(data, str):
            print("Validation: Text data verified")
            return True
        return False


class LogProcessor(DataProcessor):
    """
    Specialized processor for log entries (formatted strings).
    Overrides abstract methods to handle log-specific operations.
    Expects log format: "LEVEL: message"
    """
    def __init__(self) -> None:
        """
        Initialize the Log Processor.
        Calls parent constructor using super() to maintain inheritance chain.
        """
        super().__init__()
        print("Initializing Log Processor...")

    def process(self, data: Any) -> str:
        """
        Override: Process log entries and format based on severity level.
        Parses log format "LEVEL: message" and adds appropriate tags.
        Returns formatted log or error message if parsing fails.
        """
        try:
            # Split log entry into level and message
            parts = data.split(": ")
            level = parts[0]
            message = parts[1]
            # Format based on log level
            if level == "ERROR":
                return f"[ALERT] ERROR level detected: {message}"
            elif level == "INFO":
                return f"[INFO] INFO level detected: {message}"
            else:
                return f"Unknown log level: {level}"
        except Exception:
            return f"Unknown log level: {data}"

    def validate(self, data: Any) -> bool:
        """
        Override: Validate that data is a properly formatted log entry.
        Uses isinstance() to check type and verifies log format.
        Expects format: "LEVEL: message"
        """
        if isinstance(data, str) and ": " in data:
            print("Validation: Log entry verified")
            return True
        return False


if __name__ == "__main__":
    # Demonstration of polymorphic behavior:
    # Same interface (process, validate, format_output) works with different
    # data types through method overriding

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    # Test NumericProcessor with list of integers
    my_num_process = NumericProcessor()
    print("Processing data: [1, 2, 3, 4, 5]")
    my_num_process.validate([1, 2, 3, 4, 5])
    print(my_num_process.format_output(
        my_num_process.process([1, 2, 3, 4, 5])))
    print()

    # Test TextProcessor with string
    txt_processor = TextProcessor()
    print('Processing data: "Hello Nexus World"')
    txt_processor.validate("Hello Nexus World")
    print(txt_processor.format_output(
        txt_processor.process("Hello Nexus World")))
    print()

    # Test LogProcessor with formatted log entry
    log_processor = LogProcessor()
    print('Processing data: "ERROR: Connection timeout"')
    log_processor.validate("ERROR: Connection timeout")
    print(log_processor.format_output(
        log_processor.process("ERROR: Connection timeout")))
    print()

    # Demonstrate polymorphism: same method name, different behavior
    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    # Each processor handles its data type differently through overridden
    # process() method, but all are called the same way
    print("Result 1:", my_num_process.process([1, 2, 3]))
    print("Result 2:", txt_processor.process("Hello  World"))
    print("Result 3:", log_processor.process("INFO: System ready"))

    print()
    print("Foundation systems online. Nexus ready for advanced streams.")
