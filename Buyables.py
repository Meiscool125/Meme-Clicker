import pygame
pygame.init()
BuyablesFont = pygame.font.Font(None, 20)
# Augustus Gloop
AugustusGloopUnscaled = pygame.image.load('assets/augustus_gloop.jpg')
AugustusGloopImage = pygame.transform.scale(AugustusGloopUnscaled, (150, 100))
# Augustus Gloop Upgrades
AugustusGloopUpgrade1Bought = False
# Fortnite Kid
FortniteKidUnscaled = pygame.image.load('assets/fortnite_kid.jpg')
FortniteKidImage = pygame.transform.scale(FortniteKidUnscaled, (150, 200))
# Heavenly Dingle
HeavenlyDingleUnscaled = pygame.image.load('assets/heavenly_dingle.JPG')
HeavenlyDingleImage = pygame.transform.scale(HeavenlyDingleUnscaled, (150, 100))
# Joe Bartlozzi
JoeBartlozziUnscaled = pygame.image.load('assets/joe_bartlozzi.PNG')
JoeBartlozziImage = pygame.transform.scale(JoeBartlozziUnscaled, (150, 100))
# top screen upgrade changing text
TopScreenUpgradeText = None
TopScreenUpgradeCostText = None
# Groups
BuyablesGroup = pygame.sprite.Group()
UpgradesGroup = pygame.sprite.Group()
TopScreenUpgradeTextList = []
def CheckUpgradeCollision(TopScreenUpgradeTextList, position):
    global TopScreenUpgradeText, TopScreenUpgradeCostText
    for i in range(len(UpgradesGroup.sprites())):
        if UpgradesGroup.sprites()[i].rect.collidepoint(position):
            TopScreenUpgradeText = UpgradesGroup.sprites()[i].text
            TopScreenUpgradeCostText = UpgradesGroup.sprites()[i].costtext
    TopScreenUpgradeTextList = [TopScreenUpgradeText, TopScreenUpgradeCostText]
    return TopScreenUpgradeTextList
class Buyables(pygame.sprite.Sprite):
    def __init__(self, image, MemesPerSecond, Price, X, Y, text, type, isbought = False, item = None, costtext = None):
        super().__init__()
        if type == "item":
            self.image = image
            self.rect = self.image.get_rect()
            self.MemesPerSecond  = MemesPerSecond
            self.Price = Price
            self.rect.x = X
            self.rect.y = Y
            self.count = 0
            self.text = text
            self.type = type
            self.level = 1
        elif type == "upgrade":
            self.image = pygame.Surface([30, 30])
            self.image.fill((255, 255, 255))
            self.rect = self.image.get_rect()
            self.Price = Price
            self.rect.x = X
            self.rect.y = Y
            self.count = 0
            self.text = text
            self.type = type
            self.level = 1
            self.isbought = isbought
            self.item = item
            self.costtext = costtext
    def WriteText(self, screen):
        if self.type == "item":
            # making self.text X and Y
            self.textX = self.rect.x - (self.image.get_width())
            self.textY = self.rect.y + (self.image.get_height()/2)
            # putting text next to the images
            self.renderedtext = BuyablesFont.render(self.text, True, (0, 0, 0))
            screen.blit(self.renderedtext,(self.textX, self.textY -15))
            self.renderedtext = BuyablesFont.render(str(self.MemesPerSecond) + " memes per second", True, (0, 0, 0))
            screen.blit(self.renderedtext, (self.textX, self.textY))
            self.renderedtext = BuyablesFont.render("Cost: " + str(self.Price), True, (0, 0, 0))
            screen.blit(self.renderedtext,(self.textX, self.textY + 15))
            self.renderedtext = BuyablesFont.render("Amount owned: " +str(self.count), True, (0, 0, 0))
            screen.blit(self.renderedtext,(self.textX, self.textY + 30))
        if self.type == "upgrade":
            self.textX = 1000 - (len(self.text)/2)
            self.textY = 20
            self.renderedtext = BuyablesFont.render(self.text, True, (255, 255, 255))
            screen.blit(self.renderedtext,(self.textX, self.textY))



    def clicked(self, currentMemes, item = None):
        if currentMemes >= self.Price:
            if self.type == "item":
                self.count += 1
                currentMemes -= self.Price
                self.Price = round(self.Price *1.15)
            if self.type == "upgrade":
                if self.isbought == False:
                    self.isbought = True
                    self.ItemUpgrade1(item)
                    currentMemes -= self.Price
                    self.image.fill((128, 128, 128))
        return (currentMemes)
    def ItemUpgrade1(self, item):
        item.MemesPerSecond = (item.MemesPerSecond *2)
AugustusGloopText = "Augustus Gloop: "
AugustusGloopItem = Buyables(AugustusGloopImage, 0.1, 10, 850, 0, AugustusGloopText, "item")
FortniteKidText = "Fortnite Kid: "
FortniteKidItem = Buyables(FortniteKidImage, 1, 50, 850, 100, FortniteKidText, "item")
HeavenlyDingleText = "Heavenly Dingle: "
HeavenlyDingleItem = Buyables(HeavenlyDingleImage, 10, 200, 850, 300, HeavenlyDingleText, "item")
JoeBartlozziText = "Joe Bartlozzi: "
JoeBartlozziItem = Buyables(JoeBartlozziImage, 300, 10000, 850, 400, JoeBartlozziText, "item")

AugustusGloopUpgrade = Buyables("None", 0, 1000, 200, 200, "Augustus Gloop Efficiency 100% -> 200%", "upgrade", item = AugustusGloopItem, costtext= "Cost = 1000 Memes")
FortniteKidUpgrade = Buyables("None", 0, 5000, 300, 200, "Fortnite Kid Efficiency 100% -> 200%", "upgrade", item = FortniteKidItem, costtext= "Cost = 5000 Memes")
HeavenlyDingleUpgrade = Buyables("None", 0, 10000, 400, 200, "Heavenly Dingle Efficiency 100% -> 200%", "upgrade", item = HeavenlyDingleItem, costtext= "Cost = 10000 Memes")
JoeBartlozziUpgrade = Buyables("None", 0, 30000, 500, 200, "Joe Bartlozzi Efficiency 100% -> 200%", "upgrade", item = JoeBartlozziItem, costtext= "Cost = 30000 Memes")
#image, MemesPerSecond, Price, X, Y, text, type, isbought = False, item = None, costtext = None