from abc import ABC, abstractmethod


class ReceiveInterface(ABC):
    
    def output_text(): ... 
    

class DeliverInterface(ABC):
    
    def output(): ...