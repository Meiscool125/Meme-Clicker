import pygame
SaulGoodmanUnscaled = pygame.image.load('assets/better_call_saul.JPG')
SaulGoodman = pygame.transform.scale(SaulGoodmanUnscaled, (200, 200))
class SaulGoodmanObject(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = SaulGoodman
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
    def clicked(self, currentMemes, MemesPerClick):
        return (currentMemes + MemesPerClick)
