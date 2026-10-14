from dataclasses import dataclass
from pathlib import Path

@dataclass
class fileinfo: 
    path: Path
    name: str
    size: int
    extention: str
    