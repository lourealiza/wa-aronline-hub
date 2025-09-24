#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Criar mapa funcional usando extensão .tmj que funciona no GitHub Pages
"""

import json
import os

def create_working_tmj_map():
    # Configurações do mapa
    width_tiles = 12
    height_tiles = 8
    tile_size = 32
    
    # Criar camada de piso base
    floor_data = [1] * (width_tiles * height_tiles)
    
    # Criar spawn point
    spawn_point = {
        "id": 1,
        "name": "spawn",
        "type": "spawn",
        "x": 128,  # Centro do mapa
        "y": 96,
        "width": 32,
        "height": 32,
        "visible": True
    }
    
    # Criar zonas simples
    zones = [
        {
            "id": 2,
            "name": "Lobby",
            "type": "common",
            "x": 0,    # 0 * 32
            "y": 0,    # 0 * 32
            "width": 192,  # 6 * 32
            "height": 128, # 4 * 32
            "visible": True,
            "properties": [
                {"name": "description", "type": "string", "value": "Área central de recepção"}
            ]
        },
        {
            "id": 3,
            "name": "CEO",
            "type": "department",
            "x": 192,  # 6 * 32
            "y": 0,    # 0 * 32
            "width": 192,  # 6 * 32
            "height": 128, # 4 * 32
            "visible": True,
            "properties": [
                {"name": "description", "type": "string", "value": "Gabinete executivo"}
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
                "value": "AR Online - Mapa Funcional"
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
    
    # Salvar apenas como .tmj (que funciona)
    output_path = "wa_map-working.tmj"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    # Copiar para public também
    with open(f"public/{output_path}", 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Mapa funcional criado:")
    print(f"   📄 TMJ: {output_path} (raiz e public)")
    print(f"📊 Tamanho: {width_tiles}x{height_tiles} tiles")
    print(f"🏠 Salas: 2 salas (Lobby, CEO)")
    print(f"🎯 Spawn: Centro do mapa")
    print(f"📐 Layout: 2 salas lado a lado")
    print(f"✅ Usando extensão .tmj que funciona no GitHub Pages")
    
    return output_path

if __name__ == "__main__":
    create_working_tmj_map()
