from abc import ABC, abstractmethod
from typing import List, Optional

class BaseCollector(ABC):
    """
    Abstract contract for all link collectors.
    """

    def __init__(self, site_name: str, base_url: Optional[str] = None) -> None:
        self.site_name = site_name
        self.base_url = base_url

    @abstractmethod
    def collect_links(self, url: str) -> List[str]:
        """Extract all download links from the given page URL."""
        pass

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(site_name='{self.site_name}')"
