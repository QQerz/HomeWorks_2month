class Car:
    def __init__(self, title, model, color, engine):
        self.title = title
        self.model = model
        self.color = color
        self.engine = engine

    def start_engine():
        return  f"ENGINE Started"

    def stop_engine():
        return f"ENGINE Stopped"

    def __str__(self):
        return (f'Title: {self.title}\n'
                f'Model: {self.model}\n'
                f'Engine: {self.engine}\n'
                f'Color: {self.color}')
