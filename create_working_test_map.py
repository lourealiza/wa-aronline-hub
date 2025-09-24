#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Criar mapa de teste funcional para WorkAdventure
"""

import json
import os

def create_working_test_map():
    # Configurações do mapa
    width_tiles = 20
    height_tiles = 15
    tile_size = 32
    
    # Criar camada de piso base
    floor_data = [1] * (width_tiles * height_tiles)  # Tile 1 = piso padrão
    
    # Criar camada de salas com divisões visuais
    rooms_data = [0] * (width_tiles * height_tiles)  # 0 = vazio
    
    # Sala 1 - Lobby (tile 2)
    for y in range(1, 8):
        for x in range(1, 10):
            index = y * width_tiles + x
            rooms_data[index] = 2
    
    # Sala 2 - CEO (tile 3)
    for y in range(1, 5):
        for x in range(12, 18):
            index = y * width_tiles + x
            rooms_data[index] = 3
    
    # Sala 3 - Desenvolvimento (tile 4)
    for y in range(6, 12):
        for x in range(12, 18):
            index = y * width_tiles + x
            rooms_data[index] = 4
    
    # Sala 4 - Marketing (tile 5)
    for y in range(9, 13):
        for x in range(1, 8):
            index = y * width_tiles + x
            rooms_data[index] = 5
    
    # Criar spawn point
    spawn_point = {
        "id": 1,
        "name": "spawn",
        "type": "spawn",
        "x": 160,  # Centro do lobby
        "y": 128,
        "width": 32,
        "height": 32,
        "visible": True
    }
    
    # Criar objetos de zona
    zones = [
        {
            "id": 1,
            "name": "Lobby",
            "type": "common",
            "x": 32,  # 1 * 32
            "y": 32,  # 1 * 32
            "width": 288,  # 9 * 32
            "height": 224,  # 7 * 32
            "visible": True,
            "properties": [
                {
                    "name": "tile",
                    "type": "int",
                    "value": 2
                }
            ]
        },
        {
            "id": 2,
            "name": "CEO",
            "type": "department",
            "x": 384,  # 12 * 32
            "y": 32,  # 1 * 32
            "width": 192,  # 6 * 32
            "height": 128,  # 4 * 32
            "visible": True,
            "properties": [
                {
                    "name": "tile",
                    "type": "int",
                    "value": 3
                }
            ]
        },
        {
            "id": 3,
            "name": "Desenvolvimento",
            "type": "department",
            "x": 384,  # 12 * 32
            "y": 192,  # 6 * 32
            "width": 192,  # 6 * 32
            "height": 192,  # 6 * 32
            "visible": True,
            "properties": [
                {
                    "name": "tile",
                    "type": "int",
                    "value": 4
                }
            ]
        },
        {
            "id": 4,
            "name": "Marketing",
            "type": "department",
            "x": 32,  # 1 * 32
            "y": 288,  # 9 * 32
            "width": 224,  # 7 * 32
            "height": 128,  # 4 * 32
            "visible": True,
            "properties": [
                {
                    "name": "tile",
                    "type": "int",
                    "value": 5
                }
            ]
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
                "value": "AR Online - Mapa de Teste Funcional"
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
    
    # Salvar como .json (funciona melhor no GitHub Pages)
    output_path = "wa_map-teste.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    # Também salvar como .tmj
    output_path_tmj = "wa_map-teste.tmj"
    with open(output_path_tmj, 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Mapa de teste funcional criado:")
    print(f"   📄 JSON: {output_path}")
    print(f"   📄 TMJ: {output_path_tmj}")
    print(f"📊 Tamanho: {width_tiles}x{height_tiles} tiles")
    print(f"🏠 Salas: 4 salas com tiles diferentes (2, 3, 4, 5)")
    print(f"🎯 Spawn: Centro do lobby")
    
    return output_path, output_path_tmj

if __name__ == "__main__":
    create_working_test_map()
