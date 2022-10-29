import pygame
from mainClicker import *
from Buyables import *
from SceneSwitcher import *
from sound import *
import time
from pygame.locals import *
#load background
ShrekTheTankEngine = pygame.image.load('assets/shrek_the_tank_engine.png')
ShrekTheTankEngine = pygame.transform.scale(ShrekTheTankEngine, (1000, 500))
# pygame.init starts the code
pygame.init()
# create time
clock = pygame.time.Clock()
# making fonts
mainfont = pygame.font.Font(None, 50)
secondaryfont = pygame.font.Font(None, 30)
# make screen
screen = pygame.display.set_mode((1000, 500))
CurrentlyRunning = True
# Game/Scene State
GameState = "Main Clicker Scene"
# Saul Goodman Group
SaulGoodmanGroup = pygame.sprite.Group()
MainSaul = SaulGoodmanObject()
SaulGoodmanGroup.add(MainSaul)
# position of something
position = (0, 0)
#add buyables to buyables group
BuyablesGroup.add(AugustusGloopItem)
BuyablesGroup.add(FortniteKidItem)
BuyablesGroup.add(HeavenlyDingleItem)
BuyablesGroup.add(JoeBartlozziItem)
#add upgrades to upgrades group
UpgradesGroup.add(AugustusGloopUpgrade)
UpgradesGroup.add(FortniteKidUpgrade)
UpgradesGroup.add(HeavenlyDingleUpgrade)
UpgradesGroup.add(JoeBartlozziUpgrade)
# meme variables
currentMemes = 0
MemesPerClick = 1
MemesPerSecond = 0.0
def updateMemes():
    global currentMemes
    currentMemes += MemesPerSecond/60
def calculateMemesPerSecond():
    global MemesPerSecond
    MemesPerSecond = 0.0
    for Buyable in BuyablesGroup:
        for count in range(Buyable.count):
            MemesPerSecond += Buyable.MemesPerSecond
while CurrentlyRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if MainSaul.rect.collidepoint(event.pos):
                currentMemes = MainSaul.clicked(currentMemes, MemesPerClick)
            if SceneSwitcherButtonHitbox.collidepoint(event.pos):
                GameState = SwitchScenes(GameState)
            for i in range (len(BuyablesGroup.sprites())):
                if BuyablesGroup.sprites()[i].rect.collidepoint(event.pos):
                    currentMemes = BuyablesGroup.sprites()[i].clicked(currentMemes)
                    calculateMemesPerSecond()
            for i in range (len(UpgradesGroup.sprites())):
                if UpgradesGroup.sprites()[i].rect.collidepoint(event.pos):
                    currentMemes = UpgradesGroup.sprites()[i].clicked(currentMemes, UpgradesGroup.sprites()[i].item)
                    calculateMemesPerSecond()
        if event.type == pygame.MOUSEMOTION:
            TopScreenUpgradeTextList = CheckUpgradeCollision(TopScreenUpgradeTextList, event.pos)
            TopScreenUpgradeText = TopScreenUpgradeTextList[0]
            TopScreenUpgradeCostText = TopScreenUpgradeTextList[1]
    if GameState == "Main Clicker Scene":
        screen.fill((0,0,0))
        screen.blit(ShrekTheTankEngine, (0, 0))
        currentMemesText = mainfont.render("Current Memes: " + str(round(currentMemes, 2)), True, (0, 0, 0))
        screen.blit(currentMemesText, (300, 20))
        currentMemesPerSecond = secondaryfont.render("Current memes per second" + str(round(MemesPerSecond, 2)), True, (0, 0, 0))
        screen.blit(currentMemesPerSecond, (315, 50))
        ClickSaulToGetMemeText = secondaryfont.render("Click this image to get " + str(MemesPerClick) + " meme(s)", True, (0, 0, 0))
        screen.blit(ClickSaulToGetMemeText, (0, 200))
        SaulGoodmanGroup.draw(screen)
        BuyablesGroup.draw(screen)
        for i in range(len(BuyablesGroup.sprites())):
            BuyablesGroup.sprites()[i].WriteText(screen)
        pygame.draw.rect(screen, (255, 127, 80), SceneSwitcherButtonHitbox)
        text = secondaryfont.render("Click to view", True, (0, 0, 0))
        screen.blit(text, (30, 430))
        text = secondaryfont.render("upgrades", True, (0, 0, 0))
        screen.blit(text, (50, 450))
    if GameState == "Upgrades Scene":
        screen.fill((0,0,0))
        UpgradesGroup.draw(screen)
        pygame.draw.rect(screen, (255,127,80), SceneSwitcherButtonHitbox)
        text = secondaryfont.render("Click to view", True, (0, 0, 0))
        screen.blit(text, (30, 430))
        text = secondaryfont.render("main clicker", True, (0, 0, 0))
        screen.blit(text, (32, 450))
        text = secondaryfont.render(TopScreenUpgradeText, True, (255, 255, 255))
        screen.blit(text, (300, 20))
        text = secondaryfont.render(TopScreenUpgradeCostText, True, (255, 255, 255))
        screen.blit(text, (400, 40))
    updateMemes()
    clock.tick(60)
    pygame.display.flip()