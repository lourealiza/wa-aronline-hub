#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Criar mapa com objetos visuais para mostrar divisões de salas
"""

import json
import os

def create_visual_map_with_objects():
    # Configurações do mapa
    width_tiles = 30
    height_tiles = 20
    tile_size = 32
    
    # Criar camada de piso base
    floor_data = [1] * (width_tiles * height_tiles)  # Tile 1 = piso padrão
    
    # Criar spawn point
    spawn_point = {
        "id": 1,
        "name": "spawn",
        "type": "spawn",
        "x": 240,  # Centro do mapa
        "y": 160,
        "width": 32,
        "height": 32,
        "visible": True
    }
    
    # Criar objetos visuais para as salas (retângulos coloridos)
    room_objects = [
        # Lobby Central
        {
            "id": 2,
            "name": "Lobby Central",
            "type": "common",
            "x": 80,   # 2.5 * 32
            "y": 80,   # 2.5 * 32
            "width": 320,  # 10 * 32
            "height": 160, # 5 * 32
            "visible": True,
            "properties": [
                {"name": "color", "type": "string", "value": "#3498db"},
                {"name": "description", "type": "string", "value": "Área central de recepção"}
            ]
        },
        # CEO
        {
            "id": 3,
            "name": "CEO",
            "type": "department",
            "x": 32,   # 1 * 32
            "y": 32,   # 1 * 32
            "width": 128,  # 4 * 32
            "height": 96,  # 3 * 32
            "visible": True,
            "properties": [
                {"name": "color", "type": "string", "value": "#e74c3c"},
                {"name": "description", "type": "string", "value": "Gabinete executivo"}
            ]
        },
        # RH
        {
            "id": 4,
            "name": "RH",
            "type": "department",
            "x": 160,  # 5 * 32
            "y": 32,   # 1 * 32
            "width": 128,  # 4 * 32
            "height": 96,  # 3 * 32
            "visible": True,
            "properties": [
                {"name": "color", "type": "string", "value": "#f39c12"},
                {"name": "description", "type": "string", "value": "Recursos Humanos"}
            ]
        },
        # Marketing
        {
            "id": 5,
            "name": "Marketing",
            "type": "department",
            "x": 480,  # 15 * 32
            "y": 32,   # 1 * 32
            "width": 128,  # 4 * 32
            "height": 96,  # 3 * 32
            "visible": True,
            "properties": [
                {"name": "color", "type": "string", "value": "#9b59b6"},
                {"name": "description", "type": "string", "value": "Estratégias de mercado"}
            ]
        },
        # Desenvolvimento
        {
            "id": 6,
            "name": "Desenvolvimento",
            "type": "department",
            "x": 480,  # 15 * 32
            "y": 160,  # 5 * 32
            "width": 128,  # 4 * 32
            "height": 96,  # 3 * 32
            "visible": True,
            "properties": [
                {"name": "color", "type": "string", "value": "#27ae60"},
                {"name": "description", "type": "string", "value": "Equipe de programação"}
            ]
        },
        # Auditório
        {
            "id": 7,
            "name": "Auditório",
            "type": "common",
            "x": 32,   # 1 * 32
            "y": 256,  # 8 * 32
            "width": 192,  # 6 * 32
            "height": 128, # 4 * 32
            "visible": True,
            "properties": [
                {"name": "color", "type": "string", "value": "#16a085"},
                {"name": "description", "type": "string", "value": "Eventos e apresentações"}
            ]
        },
        # Café
        {
            "id": 8,
            "name": "Café",
            "type": "common",
            "x": 240,  # 7.5 * 32
            "y": 256,  # 8 * 32
            "width": 160,  # 5 * 32
            "height": 128, # 4 * 32
            "visible": True,
            "properties": [
                {"name": "color", "type": "string", "value": "#d35400"},
                {"name": "description", "type": "string", "value": "Área de convivência"}
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
                "value": "AR Online - Escritório com Divisões Visuais"
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
                "name": "rooms",
                "type": "objectgroup",
                "opacity": 1,
                "visible": True,
                "objects": room_objects
            }
        ]
    }
    
    # Salvar como .json
    output_path = "wa_map-visual-objects.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    # Também salvar como .tmj
    output_path_tmj = "wa_map-visual-objects.tmj"
    with open(output_path_tmj, 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Mapa com objetos visuais criado:")
    print(f"   📄 JSON: {output_path}")
    print(f"   📄 TMJ: {output_path_tmj}")
    print(f"📊 Tamanho: {width_tiles}x{height_tiles} tiles")
    print(f"🏠 Salas: {len(room_objects)} salas como objetos visuais")
    print(f"🎨 Cores: Azul, Vermelho, Laranja, Roxo, Verde, Turquesa, Marrom")
    print(f"🎯 Spawn: Centro do mapa")
    
    return output_path, output_path_tmj

if __name__ == "__main__":
    create_visual_map_with_objects()
