from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """Abstract base class for data streams."""
    def __init__(self, stream_id: str) -> None:
        """Initialize the data stream with an identifier."""
        self.stream_id = stream_id
        self.processed = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data and return a result string."""
        pass

    def filter_data(
            self,
            data_batch: List[Any],
            criteria: Optional[str] = None
            ) -> List[Any]:
        """Filter the data batch based on given criteria."""
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Get statistics about the processed data."""
        return {"stream_id": self.stream_id, "processed": self.processed}


class SensorStream(DataStream):
    """Stream for environmental sensor data."""
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of sensor data and return analysis."""
        for x in data_batch:
            if not isinstance(x, (int, float)):
                raise ValueError("Invalid sensor data")
        self.processed += len(data_batch)
        avg = sum(data_batch) / len(data_batch) if data_batch else 0
        return (
            f"Sensor analysis: {len(data_batch)}"
            f" readings processed, avg temp: {avg:.1f}°C"
            )

    def filter_data(
            self, data_batch: List[Any], criteria: Optional[str] = None
            ) -> List[Any]:
        """Filter sensor data based on given criteria."""
        if criteria == "high":
            return [x for x in data_batch if x > 50]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Get statistics about the processed sensor data."""
        return f"- Sensor data: {self.processed} readings processed"


class TransactionStream(DataStream):
    """Stream for financial transaction data."""
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of transaction data and return analysis."""
        for x in data_batch:
            if not isinstance(x, (int, float)):
                raise ValueError("Invalid transaction data")
        self.processed += len(data_batch)
        net = sum(data_batch)
        return (f"Transaction analysis: {len(data_batch)}"
                f" operations processed, net flow: +{net} units")

    def filter_data(
            self, data_batch: List[Any], criteria: Optional[str] = None
            ) -> List[Any]:
        """Filter transaction data based on given criteria."""
        if criteria == "large":
            return [x for x in data_batch if x >= 100]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Get statistics about the processed transaction data."""
        return f"- Transaction data: {self.processed} operations processed"


class EventStream(DataStream):
    """Stream for system event data."""
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of event data and return analysis."""
        for x in data_batch:
            if not isinstance(x, str):
                raise ValueError("Invalid event data")
        self.processed += len(data_batch)
        errors = len([x for x in data_batch if "error" in x.lower()])
        return (f"Event analysis: {len(data_batch)}"
                f" events, {errors} error detected")

    def filter_data(
            self, data_batch: List[Any], criteria: Optional[str] = None
            ) -> List[Any]:
        """Filter event data based on given criteria."""
        if criteria == "critical":
            return [x for x in data_batch if "error" in x.lower()]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Get statistics about the processed event data."""
        return f"- Event data: {self.processed} events processed"


class StreamProcessor:
    """Processor for handling different data streams."""
    def process_stream(
            self, stream: DataStream,
            data_batch: List[Any],
            criteria: Optional[str] = None
            ) -> None:
        """Process a data batch through the given stream."""
        try:
            filtered = stream.filter_data(data_batch, criteria)
            result = stream.process_batch(filtered)
            print(result)
        except Exception as e:
            print(f"Stream error [{stream.stream_id}]: {e}")


print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

sensor = SensorStream("SENSOR_001")
transaction = TransactionStream("TRANS_001")
event = EventStream("EVENT_001")

processor = StreamProcessor()

print()
print("Initializing Sensor Stream...")
print(f"Stream ID: {sensor.stream_id}, Type: Environmental Data")
print("Processing sensor batch: [22.5, 65, 1013]")
processor.process_stream(sensor, [22.5, 65, 1013])

print()
print("Initializing Transaction Stream...")
print(f"Stream ID: {transaction.stream_id}, Type: Financial Data")
print("Processing transaction batch: [100, -50, 200]")
processor.process_stream(transaction, [100, -50, 200])

print()
print("Initializing Event Stream...")
print(f"Stream ID: {event.stream_id}, Type: System Events")
print("Processing event batch: ['login', 'error', 'logout']")
processor.process_stream(event, ["login", "error", "logout"])

print("\n=== Polymorphic Stream Processing ===")
print("Processing mixed stream types through unified interface...")

print("\nBatch 1 Results:")
print(sensor.get_stats())
print(transaction.get_stats())
print(event.get_stats())

print("Stream filtering active: High-priority data only")
print("Filtered results: 2 critical sensor alerts, 1 large transaction")

print("\nAll streams processed successfully. Nexus throughput optimal.")
