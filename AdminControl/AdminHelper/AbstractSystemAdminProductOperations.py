from abc import ABC, abstractmethod

class AbstractSystemAdminProductInformation(ABC):
    @abstractmethod
    def add_product(self):
        pass

    @abstractmethod
    def list_product_with_quantity(self):
        pass