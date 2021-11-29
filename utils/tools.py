import pygame
from os import path

def load_asset(asset_path): 
    asset = pygame.image.load(path.join(path.dirname(__file__), '../assets', asset_path))
    asset.set_colorkey((0, 0, 0))
    return asset

def load_assets(assets:list):
    assets = [ load_asset(i) for i in assets ]
    return assets

def scale_asset(asset, scale:tuple): 
    scaled_asset = pygame.transform.scale(asset, scale)
    return scaled_asset