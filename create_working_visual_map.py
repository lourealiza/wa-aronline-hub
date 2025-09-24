#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Criar mapa funcional com divisões visuais que funciona no WorkAdventure
"""

import json
import os

def create_working_visual_map():
    # Configurações do mapa
    width_tiles = 16
    height_tiles = 12
    tile_size = 32
    
    # Criar camada de piso base
    floor_data = [1] * (width_tiles * height_tiles)
    
    # Criar camada de salas com diferentes tiles
    rooms_data = [0] * (width_tiles * height_tiles)
    
    # Sala 1 - Lobby (tile 2)
    for y in range(2, 8):
        for x in range(2, 8):
            index = y * width_tiles + x
            rooms_data[index] = 2
    
    # Sala 2 - CEO (tile 3)
    for y in range(2, 8):
        for x in range(10, 14):
            index = y * width_tiles + x
            rooms_data[index] = 3
    
    # Sala 3 - Marketing (tile 4)
    for y in range(8, 12):
        for x in range(2, 8):
            index = y * width_tiles + x
            rooms_data[index] = 4
    
    # Sala 4 - Desenvolvimento (tile 5)
    for y in range(8, 12):
        for x in range(10, 14):
            index = y * width_tiles + x
            rooms_data[index] = 5
    
    # Criar spawn point
    spawn_point = {
        "id": 1,
        "name": "spawn",
        "type": "spawn",
        "x": 128,  # Centro do lobby
        "y": 128,
        "width": 32,
        "height": 32,
        "visible": True
    }
    
    # Criar objetos de zona
    zones = [
        {
            "id": 2,
            "name": "Lobby",
            "type": "common",
            "x": 64,   # 2 * 32
            "y": 64,   # 2 * 32
            "width": 192,  # 6 * 32
            "height": 192, # 6 * 32
            "visible": True,
            "properties": [
                {"name": "tile", "type": "int", "value": 2},
                {"name": "description", "type": "string", "value": "Área central de recepção"}
            ]
        },
        {
            "id": 3,
            "name": "CEO",
            "type": "department",
            "x": 320,  # 10 * 32
            "y": 64,   # 2 * 32
            "width": 128,  # 4 * 32
            "height": 192, # 6 * 32
            "visible": True,
            "properties": [
                {"name": "tile", "type": "int", "value": 3},
                {"name": "description", "type": "string", "value": "Gabinete executivo"}
            ]
        },
        {
            "id": 4,
            "name": "Marketing",
            "type": "department",
            "x": 64,   # 2 * 32
            "y": 256,  # 8 * 32
            "width": 192,  # 6 * 32
            "height": 128, # 4 * 32
            "visible": True,
            "properties": [
                {"name": "tile", "type": "int", "value": 4},
                {"name": "description", "type": "string", "value": "Estratégias de mercado"}
            ]
        },
        {
            "id": 5,
            "name": "Desenvolvimento",
            "type": "department",
            "x": 320,  # 10 * 32
            "y": 256,  # 8 * 32
            "width": 128,  # 4 * 32
            "height": 128, # 4 * 32
            "visible": True,
            "properties": [
                {"name": "tile", "type": "int", "value": 5},
                {"name": "description", "type": "string", "value": "Equipe de programação"}
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
                "value": "AR Online - Mapa com Divisões Visuais"
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
    
    # Salvar como .tmj
    output_path = "wa_map-visual-working.tmj"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    # Copiar para public também
    with open(f"public/{output_path}", 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Mapa com divisões visuais criado:")
    print(f"   📄 TMJ: {output_path} (raiz e public)")
    print(f"📊 Tamanho: {width_tiles}x{height_tiles} tiles")
    print(f"🏠 Salas: 4 salas com tiles 2, 3, 4, 5")
    print(f"🎯 Spawn: Centro do lobby")
    print(f"📐 Layout: 2x2 grid de salas")
    print(f"🎨 Divisões visuais com tiles diferentes")
    
    return output_path

if __name__ == "__main__":
    create_working_visual_map()