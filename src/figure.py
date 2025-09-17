from abc import ABC, abstractmethod


class Figure(ABC):

    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimetr(self):
        pass

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.area + figure.area
        raise ValueError('argument figure must be Figure or child class')