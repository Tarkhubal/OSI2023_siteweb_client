class Communication():
    def __init__(self) -> None:
        pass
    
    def start(self, nb_personnes: int):
        print("START", nb_personnes, "personnes")
    
    def stop(self):
        print("STOP")
    
    def get_data(self):
        """L'image doit être le chemin relatif à partir d'un dossier "static" (en minuscule)"""
        return [ [5, "happy", "./logo.png"], [3, "sad", "./5c9a1917-450f-4402-9866-97d87f368e23-0_cuted.png"] ]