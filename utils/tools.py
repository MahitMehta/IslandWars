import pygame
import os, sys, inspect

def base():
   if getattr(sys,"frozen",False):
       return os.path.dirname(os.path.abspath(sys.executable))
   else:
       thisdir = os.path.dirname(inspect.getfile(inspect.currentframe()))
       return os.path.abspath(os.path.join(thisdir, os.pardir))

def load_asset(asset_path): 
    asset = pygame.image.load(os.path.join(base(), 'assets', asset_path))
    asset.set_colorkey((0, 0, 0))
    return asset

def load_assets(assets:list):
    assets = [ load_asset(i) for i in assets ]
    return assets

def scale_asset(asset, scale:tuple): 
    scaled_asset = pygame.transform.scale(asset, scale)
    return scaled_asset