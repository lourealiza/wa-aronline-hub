#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Corrigir mapas existentes para ter diferenças visuais
"""

import json
import os

def fix_map_floor_data(map_path, new_floor_data):
    """Corrige a camada floor de um mapa"""
    with open(map_path, 'r', encoding='utf-8') as f:
        map_data = json.load(f)
    
    # Encontrar e atualizar a camada floor
    for layer in map_data['layers']:
        if layer['name'] == 'floor':
            layer['data'] = new_floor_data
            break
    
    # Salvar arquivo corrigido
    with open(map_path, 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    # Copiar para public
    public_path = f"public/{map_path}"
    with open(public_path, 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Corrigido: {map_path}")

def create_professional_floor_data():
    """Cria dados de piso para mapa profissional"""
    width_tiles = 24
    height_tiles = 20
    floor_data = []
    
    # Área Superior - Convivência (tile 3)
    for y in range(0, 7):
        for x in range(0, 24):
            floor_data.append(3)
    
    # Ala Esquerda - Gestão (tile 4)
    for y in range(7, 20):
        for x in range(0, 12):
            floor_data.append(4)
    
    # Ala Direita - Operações (tile 5)
    for y in range(7, 20):
        for x in range(12, 24):
            floor_data.append(5)
    
    # Centro - Lobby (tile 6) - sobrepor
    for y in range(7, 13):
        for x in range(8, 16):
            index = y * width_tiles + x
            floor_data[index] = 6
    
    return floor_data

def create_interactive_floor_data():
    """Cria dados de piso para mapa interativo"""
    width_tiles = 40
    height_tiles = 30
    floor_data = []
    
    # Padrão de xadrez com diferentes tiles
    for y in range(height_tiles):
        for x in range(width_tiles):
            if (x + y) % 3 == 0:
                floor_data.append(2)  # Azul
            elif (x + y) % 3 == 1:
                floor_data.append(3)  # Verde
            else:
                floor_data.append(4)  # Amarelo
    
    return floor_data

def create_simple_floor_data():
    """Cria dados de piso para mapa simples"""
    width_tiles = 8
    height_tiles = 6
    floor_data = []
    
    # Metade esquerda: tile 2, metade direita: tile 3
    for y in range(height_tiles):
        for x in range(width_tiles):
            if x < width_tiles // 2:
                floor_data.append(2)
            else:
                floor_data.append(3)
    
    return floor_data

def main():
    print("🔧 Corrigindo mapas existentes...")
    
    # Corrigir mapa profissional
    professional_floor = create_professional_floor_data()
    fix_map_floor_data("wa_map-ar-online-professional.tmj", professional_floor)
    
    # Corrigir mapa interativo
    interactive_floor = create_interactive_floor_data()
    fix_map_floor_data("wa_map-interativo.tmj", interactive_floor)
    
    # Corrigir mapa simples
    simple_floor = create_simple_floor_data()
    fix_map_floor_data("wa_map-simple-working.tmj", simple_floor)
    
    print("\n✅ Todos os mapas corrigidos!")
    print("🎯 Agora os mapas terão diferenças visuais reais!")

if __name__ == "__main__":
    main()
