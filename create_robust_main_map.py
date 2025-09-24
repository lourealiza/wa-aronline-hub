#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Criar mapa principal robusto com divisões visuais claras
"""

import json
import os

def create_robust_main_map():
    # Configurações do mapa
    width_tiles = 40
    height_tiles = 30
    tile_size = 32
    
    # Criar camada de piso base
    floor_data = [1] * (width_tiles * height_tiles)  # Tile 1 = piso padrão
    
    # Criar camada de salas com divisões visuais claras
    rooms_data = [0] * (width_tiles * height_tiles)  # 0 = vazio
    
    # Definir salas com coordenadas e tiles
    rooms = [
        {"name": "Lobby Central", "x": 15, "y": 15, "w": 20, "h": 10, "tile": 2},
        {"name": "CEO", "x": 2, "y": 12, "w": 6, "h": 6, "tile": 3},
        {"name": "RH", "x": 8, "y": 12, "w": 6, "h": 6, "tile": 4},
        {"name": "Marketing", "x": 32, "y": 12, "w": 6, "h": 6, "tile": 5},
        {"name": "Desenvolvimento", "x": 32, "y": 18, "w": 6, "h": 6, "tile": 6},
        {"name": "Auditório", "x": 5, "y": 2, "w": 12, "h": 8, "tile": 7},
        {"name": "Café", "x": 20, "y": 2, "w": 10, "h": 8, "tile": 8},
        {"name": "Impressão", "x": 30, "y": 2, "w": 6, "h": 8, "tile": 9},
        {"name": "Arquivo", "x": 15, "y": 2, "w": 6, "h": 8, "tile": 10},
    ]
    
    # Preencher salas com tiles diferentes
    for room in rooms:
        for y in range(room["y"], room["y"] + room["h"]):
            for x in range(room["x"], room["x"] + room["w"]):
                if 0 <= x < width_tiles and 0 <= y < height_tiles:
                    index = y * width_tiles + x
                    rooms_data[index] = room["tile"]
    
    # Criar spawn point
    spawn_point = {
        "id": 1,
        "name": "spawn",
        "type": "spawn",
        "x": 480,  # Centro do lobby
        "y": 480,
        "width": 32,
        "height": 32,
        "visible": True
    }
    
    # Criar objetos de zona
    zones = []
    private_zones = []
    
    for room in rooms:
        x_px = room["x"] * tile_size
        y_px = room["y"] * tile_size
        w_px = room["w"] * tile_size
        h_px = room["h"] * tile_size
        
        room_obj = {
            "id": len(zones) + len(private_zones) + 1,
            "name": room["name"],
            "type": "department" if room["name"] in ["CEO", "RH", "Marketing", "Desenvolvimento"] else "common",
            "x": x_px,
            "y": y_px,
            "width": w_px,
            "height": h_px,
            "visible": True,
            "properties": [
                {
                    "name": "tile",
                    "type": "int",
                    "value": room["tile"]
                }
            ]
        }
        
        if room["name"] in ["CEO", "RH", "Marketing", "Desenvolvimento"]:
            private_zones.append(room_obj)
        else:
            zones.append(room_obj)
    
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
        "nextlayerid": 6,
        "nextobjectid": 20,
        "properties": [
            {
                "name": "mapName",
                "type": "string",
                "value": "AR Online - Escritório Virtual com Divisões Visuais"
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
            },
            {
                "id": 5,
                "name": "PrivateZones",
                "type": "objectgroup",
                "opacity": 1,
                "visible": True,
                "objects": private_zones
            }
        ]
    }
    
    # Salvar como .json (funciona melhor no GitHub Pages)
    output_path = "wa_map-interativo.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    # Também salvar como .tmj
    output_path_tmj = "wa_map-interativo.tmj"
    with open(output_path_tmj, 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Mapa principal robusto criado:")
    print(f"   📄 JSON: {output_path}")
    print(f"   📄 TMJ: {output_path_tmj}")
    print(f"📊 Tamanho: {width_tiles}x{height_tiles} tiles")
    print(f"🏠 Salas: {len(rooms)} salas com tiles diferentes (2-10)")
    print(f"🎯 Spawn: Centro do lobby")
    print(f"🔒 Zonas privadas: {len(private_zones)}")
    print(f"🌐 Zonas comuns: {len(zones)}")
    
    return output_path, output_path_tmj

if __name__ == "__main__":
    create_robust_main_map()
