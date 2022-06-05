import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
    """Klasa przeznaczona do przedstawiania informacji o punktacji."""

    def __init__(self, ai_game):
        """Inicjalizacja atrybutów dotyczących punktacji."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #Ustawienia czcionki dla informacji dotyczących punktacji.
        self.text_colour = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #Przygotowanie początkowych obrazów z punktacją.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Przekształcenie punktacji na wygenerowany obraz."""
        score_str = str(self.stats.score)
        self.score_image = self.font.render("Wynik: "+score_str, True, 
            self.text_colour, self.settings.bg_color)

        #Wyświetlanie punktacji w prawym górnym rogu ekranu.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Konwersja najlepszego wyniku w grze na wygerenowany obraz."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render("Najlepszy wynik: "+high_score_str, True,
            self.text_colour, self.settings.bg_color)

        #Wyświetlanie najlepszego wyniku w grze na środku ekranu,
        #przy górnej krawędzi.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top
        

    def show_score(self):
        """Wyświetlanie punktacji na ekranie."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
        
    def check_high_score(self):
        """Sprawdzenie czy mamy najlepszy osiągnięty dotąd wynik w grze."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
            
    def prep_level(self):
        """Konwersja numeru poziomu na wygenerowany obraz."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render("Poziom: "+level_str, True,
                                            self.text_colour,
                                            self.settings.bg_color)
        
        #Numer poziomu jest wyświetlany pod aktualną punktacją.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
        
    def prep_ships(self):
        """Wyświetla liczbę statków jaka pozostała graczowi."""
        self.ships = Group()
        for ship_number in  range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
            