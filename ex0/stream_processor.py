from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """
    Docstring for DataProcessor
    Base class for data processors.
    """
    @abstractmethod
    def process(self, data: Any) -> str:
        """
        Process the input data and return a result string.
        """
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """
        Validate the input data.
        """
        pass

    def format_output(self, result: str) -> str:
        """
        Format the output result string.
        """
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """
    Docstring for NumericProcessor
    Processor for numeric data.
    """
    def __init__(self) -> None:
        """
        Initialize the Numeric Processor.
        """
        print("Initializing Numeric Processor...")

    def process(self, data: Any) -> str:
        """
        Process numeric data and return a summary string.
        """
        try:
            avg = sum(data) / len(data)
            return (f"Processed {len(data)} numeric values, "
                    f"sum={sum(data)}, avg={avg}")
        except (TypeError, ValueError, ZeroDivisionError) as e:
            return f"Error processing numeric data: {e}"

    def validate(self, data: Any) -> bool:
        """
        Validate that the data is numeric.
        """
        try:
            [int(item) for item in data]
            print("Validation: Numeric data verified")
            return True
        except (TypeError, ValueError, AttributeError):
            return False


class TextProcessor(DataProcessor):
    """
    Docstring for TextProcessor
    Processor for text data.
    """
    def __init__(self) -> None:
        """
        Initialize the Text Processor.
        """
        print("Initializing Text Processor...")

    def process(self, data: Any) -> str:
        """
        Process text data and return a summary string.
        """
        try:
            return (f"Processed text: {len(data)} characters, "
                    f"{len(data.split())} words")
        except Exception as e:
            return f"Error processing text data: {e}"

    def validate(self, data: Any) -> bool:
        """
        Validate that the data is text.
        """
        try:
            if "" + data == data:
                print("Validation: Text data verified")
                return True
        except Exception:
            pass
        return False


class LogProcessor(DataProcessor):
    """
    Docstring for LogProcessor
    Processor for log data.
    """
    def __init__(self) -> None:
        """
        Initialize the Log Processor.
        """
        print("Initializing Log Processor...")

    def process(self, data: Any) -> str:
        """
        Process log data and return a summary string.
        """
        try:
            parts = data.split(": ")
            level = parts[0]
            message = parts[1]
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
        Validate that the data is a str.
        """
        try:
            if "" + data == data and ": " in data:
                print("Validation: Log entry verified")
                return True
        except TypeError:
            pass
        return False


if __name__ == "__main__":

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    my_num_process = NumericProcessor()
    print("Processing data: [1, 2, 3, 4, 5]")
    my_num_process.validate([1, 2, 3, 4, 5])
    print(my_num_process.format_output(
        my_num_process.process([1, 2, 3, 4, 5])))
    print()

    txt_processor = TextProcessor()
    print('Processing data: "Hello Nexus World"')
    txt_processor.validate("Hello Nexus World")
    print(txt_processor.format_output(
        txt_processor.process("Hello Nexus World")))
    print()

    log_processor = LogProcessor()
    print('Processing data: "ERROR: Connection timeout"')
    log_processor.validate("ERROR: Connection timeout")
    print(log_processor.format_output(
        log_processor.process("ERROR: Connection timeout")))
    print()

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    print("Result 1:", my_num_process.process([1, 2, 3]))
    print("Result 2:", txt_processor.process("Hello  World"))
    print("Result 3:", log_processor.process("INFO: System ready"))

    print()
    print("Foundation systems online. Nexus ready for advanced streams.")
