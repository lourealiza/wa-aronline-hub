#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Criar mapa super simples que funciona no WorkAdventure
"""

import json
import os

def create_simple_working_map():
    # Configurações do mapa
    width_tiles = 20
    height_tiles = 15
    tile_size = 32
    
    # Criar camada de piso base com tiles básicos
    floor_data = []
    for y in range(height_tiles):
        for x in range(width_tiles):
            # Usar diferentes tiles para criar padrões visuais
            if x < 10 and y < 8:  # Lobby
                floor_data.append(1)
            elif x >= 10 and y < 8:  # CEO
                floor_data.append(2)
            elif x < 10 and y >= 8:  # Marketing
                floor_data.append(3)
            else:  # Desenvolvimento
                floor_data.append(4)
    
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
            "id": 2,
            "name": "Lobby",
            "type": "common",
            "x": 0,   # 0 * 32
            "y": 0,   # 0 * 32
            "width": 320,  # 10 * 32
            "height": 256, # 8 * 32
            "visible": True,
            "properties": [
                {"name": "tile", "type": "int", "value": 1},
                {"name": "description", "type": "string", "value": "Área central de recepção"}
            ]
        },
        {
            "id": 3,
            "name": "CEO",
            "type": "department",
            "x": 320,  # 10 * 32
            "y": 0,    # 0 * 32
            "width": 320,  # 10 * 32
            "height": 256, # 8 * 32
            "visible": True,
            "properties": [
                {"name": "tile", "type": "int", "value": 2},
                {"name": "description", "type": "string", "value": "Gabinete executivo"}
            ]
        },
        {
            "id": 4,
            "name": "Marketing",
            "type": "department",
            "x": 0,    # 0 * 32
            "y": 256,  # 8 * 32
            "width": 320,  # 10 * 32
            "height": 224, # 7 * 32
            "visible": True,
            "properties": [
                {"name": "tile", "type": "int", "value": 3},
                {"name": "description", "type": "string", "value": "Estratégias de mercado"}
            ]
        },
        {
            "id": 5,
            "name": "Desenvolvimento",
            "type": "department",
            "x": 320,  # 10 * 32
            "y": 256,  # 8 * 32
            "width": 320,  # 10 * 32
            "height": 224, # 7 * 32
            "visible": True,
            "properties": [
                {"name": "tile", "type": "int", "value": 4},
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
        "nextlayerid": 4,
        "nextobjectid": 10,
        "properties": [
            {
                "name": "mapName",
                "type": "string",
                "value": "AR Online - Mapa Simples Funcional"
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
                "name": "start",
                "type": "objectgroup",
                "opacity": 1,
                "visible": True,
                "objects": [spawn_point]
            },
            {
                "id": 3,
                "name": "zones",
                "type": "objectgroup",
                "opacity": 1,
                "visible": True,
                "objects": zones
            }
        ]
    }
    
    # Salvar como .json
    output_path = "wa_map-simple-working.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    # Também salvar como .tmj
    output_path_tmj = "wa_map-simple-working.tmj"
    with open(output_path_tmj, 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Mapa simples funcional criado:")
    print(f"   📄 JSON: {output_path}")
    print(f"   📄 TMJ: {output_path_tmj}")
    print(f"📊 Tamanho: {width_tiles}x{height_tiles} tiles")
    print(f"🏠 Salas: 4 salas com tiles 1, 2, 3, 4")
    print(f"🎯 Spawn: Centro do lobby")
    print(f"📐 Layout: 2x2 grid de salas")
    
    return output_path, output_path_tmj

if __name__ == "__main__":
    create_simple_working_map()
