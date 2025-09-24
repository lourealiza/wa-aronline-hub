#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Criar mapa de teste simples para WorkAdventure
"""

import json
import os

def create_test_map():
    # Configurações do mapa
    width_tiles = 20
    height_tiles = 15
    tile_size = 32
    
    # Criar camada de piso base
    floor_data = [1] * (width_tiles * height_tiles)  # Tile 1 = piso padrão
    
    # Criar camada de salas simples
    rooms_data = [0] * (width_tiles * height_tiles)  # 0 = vazio
    
    # Adicionar algumas salas básicas
    # Sala 1 (tile 2)
    for y in range(2, 8):
        for x in range(2, 8):
            index = y * width_tiles + x
            rooms_data[index] = 2
    
    # Sala 2 (tile 3)
    for y in range(2, 8):
        for x in range(10, 16):
            index = y * width_tiles + x
            rooms_data[index] = 3
    
    # Sala 3 (tile 4)
    for y in range(9, 13):
        for x in range(6, 12):
            index = y * width_tiles + x
            rooms_data[index] = 4
    
    # Criar spawn point
    spawn_point = {
        "id": 1,
        "name": "spawn",
        "type": "spawn",
        "x": 160,  # Centro do mapa
        "y": 240,
        "width": 32,
        "height": 32,
        "visible": True
    }
    
    # Criar objetos de zona
    zones = [
        {
            "id": 1,
            "name": "Sala 1",
            "type": "common",
            "x": 64,  # 2 * 32
            "y": 64,  # 2 * 32
            "width": 192,  # 6 * 32
            "height": 192,  # 6 * 32
            "visible": True
        },
        {
            "id": 2,
            "name": "Sala 2",
            "type": "common",
            "x": 320,  # 10 * 32
            "y": 64,  # 2 * 32
            "width": 192,  # 6 * 32
            "height": 192,  # 6 * 32
            "visible": True
        },
        {
            "id": 3,
            "name": "Sala 3",
            "type": "common",
            "x": 192,  # 6 * 32
            "y": 288,  # 9 * 32
            "width": 192,  # 6 * 32
            "height": 128,  # 4 * 32
            "visible": True
        }
    ]
    
    # Estrutura do mapa
    map_data = {
        "type": "map",
        "version": "1.10",
        "tiledversion": "1.10.2",
        "orientation": "orthogonal",
        "renderorder": "right-down",
        "infinite": False,
        "width": width_tiles,
        "height": height_tiles,
        "tilewidth": tile_size,
        "tileheight": tile_size,
        "compressionlevel": -1,
        "nextlayerid": 5,
        "nextobjectid": 10,
        "properties": [
            {
                "name": "mapName",
                "type": "string",
                "value": "AR Online - Mapa de Teste"
            },
            {
                "name": "script",
                "type": "string",
                "value": "mapScript.js"
            }
        ],
        "tilesets": [
            {
                "firstgid": 1,
                "name": "WA_Room_Builder",
                "tilewidth": 32,
                "tileheight": 32,
                "tilecount": 1000,
                "columns": 25,
                "image": "tilesets/WA_Room_Builder.png",
                "imagewidth": 800,
                "imageheight": 1280
            }
        ],
        "layers": [
            {
                "id": 1,
                "name": "floor",
                "type": "tilelayer",
                "width": width_tiles,
                "height": height_tiles,
                "opacity": 1,
                "visible": True,
                "data": floor_data
            },
            {
                "id": 2,
                "name": "rooms",
                "type": "tilelayer",
                "width": width_tiles,
                "height": height_tiles,
                "opacity": 1,
                "visible": True,
                "data": rooms_data
            },
            {
                "id": 3,
                "name": "start",
                "type": "objectgroup",
                "opacity": 1,
                "visible": True,
                "objects": [spawn_point]
            },
            {
                "id": 4,
                "name": "zones",
                "type": "objectgroup",
                "opacity": 1,
                "visible": True,
                "objects": zones
            }
        ]
    }
    
    # Salvar arquivo
    output_path = "wa_map-teste.tmj"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Mapa de teste criado: {output_path}")
    print(f"📊 Tamanho: {width_tiles}x{height_tiles} tiles")
    print(f"🏠 Salas: 3 salas com tiles diferentes (2, 3, 4)")
    
    return output_path

if __name__ == "__main__":
    create_test_map()
