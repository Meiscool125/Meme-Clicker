import pygame
pygame.init()
SceneSwitcherButtonHitbox = pygame.Rect(0, 400, 200, 100)
SceneSwitcherButtonFont = pygame.font.Font(None, 20)
SceneSwitcherButtonTextOnClicker = "Click to view upgrades"
SceneSwitcherButtonTextOnUpgrades = "Click to go back"
def SwitchScenes(GameState):
    if GameState == "Main Clicker Scene":
        GameState = "Upgrades Scene"
    elif GameState == "Upgrades Scene":
        GameState = "Main Clicker Scene"
    return GameState

