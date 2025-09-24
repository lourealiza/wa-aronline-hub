#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Criar mapa com divisões visuais usando objetos coloridos
"""

import json
import os

def create_visual_objects_map():
    # Configurações do mapa
    width_tiles = 16
    height_tiles = 12
    tile_size = 32
    
    # Criar camada de piso base
    floor_data = [1] * (width_tiles * height_tiles)
    
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
    
    # Criar objetos coloridos para divisões visuais
    visual_objects = [
        # Lobby Central (azul)
        {
            "id": 2,
            "name": "Lobby",
            "type": "rectangle",
            "x": 64,   # 2 * 32
            "y": 64,   # 2 * 32
            "width": 192,  # 6 * 32
            "height": 192, # 6 * 32
            "visible": True,
            "properties": [
                {"name": "color", "type": "string", "value": "#3498db"},
                {"name": "opacity", "type": "float", "value": 0.3},
                {"name": "description", "type": "string", "value": "Lobby Central"}
            ]
        },
        # CEO (vermelho)
        {
            "id": 3,
            "name": "CEO",
            "type": "rectangle",
            "x": 320,  # 10 * 32
            "y": 64,   # 2 * 32
            "width": 128,  # 4 * 32
            "height": 192, # 6 * 32
            "visible": True,
            "properties": [
                {"name": "color", "type": "string", "value": "#e74c3c"},
                {"name": "opacity", "type": "float", "value": 0.3},
                {"name": "description", "type": "string", "value": "Gabinete Executivo"}
            ]
        },
        # Marketing (verde)
        {
            "id": 4,
            "name": "Marketing",
            "type": "rectangle",
            "x": 64,   # 2 * 32
            "y": 256,  # 8 * 32
            "width": 192,  # 6 * 32
            "height": 128, # 4 * 32
            "visible": True,
            "properties": [
                {"name": "color", "type": "string", "value": "#2ecc71"},
                {"name": "opacity", "type": "float", "value": 0.3},
                {"name": "description", "type": "string", "value": "Marketing"}
            ]
        },
        # Desenvolvimento (roxo)
        {
            "id": 5,
            "name": "Desenvolvimento",
            "type": "rectangle",
            "x": 320,  # 10 * 32
            "y": 256,  # 8 * 32
            "width": 128,  # 4 * 32
            "height": 128, # 4 * 32
            "visible": True,
            "properties": [
                {"name": "color", "type": "string", "value": "#9b59b6"},
                {"name": "opacity", "type": "float", "value": 0.3},
                {"name": "description", "type": "string", "value": "Desenvolvimento"}
            ]
        }
    ]
    
    # Criar zonas para interação
    zones = [
        {
            "id": 6,
            "name": "Lobby",
            "type": "common",
            "x": 64,
            "y": 64,
            "width": 192,
            "height": 192,
            "visible": True,
            "properties": [
                {"name": "description", "type": "string", "value": "Área central de recepção"}
            ]
        },
        {
            "id": 7,
            "name": "CEO",
            "type": "department",
            "x": 320,
            "y": 64,
            "width": 128,
            "height": 192,
            "visible": True,
            "properties": [
                {"name": "description", "type": "string", "value": "Gabinete executivo"}
            ]
        },
        {
            "id": 8,
            "name": "Marketing",
            "type": "department",
            "x": 64,
            "y": 256,
            "width": 192,
            "height": 128,
            "visible": True,
            "properties": [
                {"name": "description", "type": "string", "value": "Estratégias de mercado"}
            ]
        },
        {
            "id": 9,
            "name": "Desenvolvimento",
            "type": "department",
            "x": 320,
            "y": 256,
            "width": 128,
            "height": 128,
            "visible": True,
            "properties": [
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
        "nextlayerid": 6,
        "nextobjectid": 15,
        "properties": [
            {
                "name": "mapName",
                "type": "string",
                "value": "AR Online - Mapa com Objetos Visuais"
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
                "name": "visual_objects",
                "type": "objectgroup",
                "opacity": 1,
                "visible": True,
                "objects": visual_objects
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
    output_path = "wa_map-visual-objects-working.tmj"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    # Copiar para public também
    with open(f"public/{output_path}", 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Mapa com objetos visuais criado:")
    print(f"   📄 TMJ: {output_path} (raiz e public)")
    print(f"📊 Tamanho: {width_tiles}x{height_tiles} tiles")
    print(f"🎨 Objetos coloridos: 4 retângulos com cores diferentes")
    print(f"   - Lobby: Azul (#3498db)")
    print(f"   - CEO: Vermelho (#e74c3c)")
    print(f"   - Marketing: Verde (#2ecc71)")
    print(f"   - Desenvolvimento: Roxo (#9b59b6)")
    print(f"🎯 Spawn: Centro do lobby")
    print(f"📐 Layout: 2x2 grid com objetos visuais")
    
    return output_path

if __name__ == "__main__":
    create_visual_objects_map()
