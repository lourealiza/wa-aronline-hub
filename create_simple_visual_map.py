#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Criar mapa super simples com divisões visuais que realmente funcionam
"""

import json
import os

def create_simple_visual_map():
    # Configurações do mapa - bem pequeno para garantir que funcione
    width_tiles = 8
    height_tiles = 6
    tile_size = 32
    
    # Criar camada de piso base (tile 1 = chão)
    floor_data = [1] * (width_tiles * height_tiles)
    
    # Criar camada de salas com tiles diferentes para cada área
    rooms_data = [0] * (width_tiles * height_tiles)
    
    # Sala 1 - Lobby (tile 2) - canto superior esquerdo
    for y in range(0, 3):
        for x in range(0, 4):
            index = y * width_tiles + x
            rooms_data[index] = 2
    
    # Sala 2 - CEO (tile 3) - canto superior direito
    for y in range(0, 3):
        for x in range(4, 8):
            index = y * width_tiles + x
            rooms_data[index] = 3
    
    # Sala 3 - Marketing (tile 4) - canto inferior esquerdo
    for y in range(3, 6):
        for x in range(0, 4):
            index = y * width_tiles + x
            rooms_data[index] = 4
    
    # Sala 4 - Desenvolvimento (tile 5) - canto inferior direito
    for y in range(3, 6):
        for x in range(4, 8):
            index = y * width_tiles + x
            rooms_data[index] = 5
    
    # Criar spawn point no centro do lobby
    spawn_point = {
        "id": 1,
        "name": "spawn",
        "type": "spawn",
        "x": 48,  # Centro do lobby (1.5 * 32)
        "y": 48,  # Centro do lobby (1.5 * 32)
        "width": 32,
        "height": 32,
        "visible": True
    }
    
    # Criar objetos de zona para cada sala
    zones = [
        {
            "id": 2,
            "name": "Lobby",
            "type": "common",
            "x": 0,    # 0 * 32
            "y": 0,    # 0 * 32
            "width": 128,  # 4 * 32
            "height": 96,  # 3 * 32
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
            "x": 128,  # 4 * 32
            "y": 0,    # 0 * 32
            "width": 128,  # 4 * 32
            "height": 96,  # 3 * 32
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
            "x": 0,    # 0 * 32
            "y": 96,   # 3 * 32
            "width": 128,  # 4 * 32
            "height": 96,  # 3 * 32
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
            "x": 128,  # 4 * 32
            "y": 96,   # 3 * 32
            "width": 128,  # 4 * 32
            "height": 96,  # 3 * 32
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
                "value": "AR Online - Mapa Simples com Divisões"
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
    output_path = "wa_map-simple-working.tmj"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    # Copiar para public também
    with open(f"public/{output_path}", 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Mapa simples com divisões criado:")
    print(f"   📄 TMJ: {output_path} (raiz e public)")
    print(f"📊 Tamanho: {width_tiles}x{height_tiles} tiles (pequeno e funcional)")
    print(f"🏠 Salas: 4 salas em grid 2x2")
    print(f"🎯 Spawn: Centro do lobby")
    print(f"🎨 Tiles: 2=Lobby, 3=CEO, 4=Marketing, 5=Desenvolvimento")
    print(f"📐 Layout: Quadrantes bem definidos")
    
    return output_path

if __name__ == "__main__":
    create_simple_visual_map()