#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Criar mapa definitivo que funciona com tiles que existem
"""

import json
import os

def create_definitive_working_map():
    """Cria mapa que definitivamente funciona"""
    
    width_tiles = 16
    height_tiles = 12
    tile_size = 32
    
    # Usar apenas tiles 1, 2, 3 que sabemos que existem
    floor_data = []
    
    # Criar padrão de xadrez com tiles 1 e 2
    for y in range(height_tiles):
        for x in range(width_tiles):
            if (x + y) % 2 == 0:
                floor_data.append(1)
            else:
                floor_data.append(2)
    
    # Adicionar algumas bordas com tile 3
    for y in range(height_tiles):
        for x in range(width_tiles):
            if x == 0 or x == width_tiles - 1 or y == 0 or y == height_tiles - 1:
                floor_data[y * width_tiles + x] = 3
    
    # Criar spawn point
    spawn_point = {
        "id": 1,
        "name": "spawn",
        "type": "spawn",
        "x": 128,
        "y": 96,
        "width": 32,
        "height": 32,
        "visible": True
    }
    
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
        "nextlayerid": 3,
        "nextobjectid": 10,
        "properties": [
            {
                "name": "mapName",
                "type": "string",
                "value": "AR Online - Mapa Definitivo Funcional"
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
            }
        ]
    }
    
    # Salvar mapa
    output_path = "wa_map-definitive.tmj"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    # Copiar para public
    with open(f"public/{output_path}", 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Mapa definitivo criado:")
    print(f"   📄 TMJ: {output_path}")
    print(f"📊 Tamanho: {width_tiles}x{height_tiles} tiles")
    print(f"🎨 Padrão: Xadrez com tiles 1 e 2, bordas com tile 3")
    
    return output_path

def create_alternating_stripes_map():
    """Cria mapa com listras alternadas"""
    
    width_tiles = 20
    height_tiles = 10
    tile_size = 32
    
    floor_data = []
    
    # Listras horizontais alternadas
    for y in range(height_tiles):
        for x in range(width_tiles):
            if y % 2 == 0:
                floor_data.append(1)
            else:
                floor_data.append(2)
    
    # Criar spawn point
    spawn_point = {
        "id": 1,
        "name": "spawn",
        "type": "spawn",
        "x": 160,
        "y": 80,
        "width": 32,
        "height": 32,
        "visible": True
    }
    
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
        "nextlayerid": 3,
        "nextobjectid": 10,
        "properties": [
            {
                "name": "mapName",
                "type": "string",
                "value": "AR Online - Mapa com Listras"
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
            }
        ]
    }
    
    # Salvar mapa
    output_path = "wa_map-stripes.tmj"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    # Copiar para public
    with open(f"public/{output_path}", 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Mapa com listras criado:")
    print(f"   📄 TMJ: {output_path}")
    print(f"📊 Tamanho: {width_tiles}x{height_tiles} tiles")
    print(f"🎨 Padrão: Listras horizontais alternadas")
    
    return output_path

if __name__ == "__main__":
    print("🔧 Criando mapas definitivos que funcionam...")
    print()
    
    # Criar mapa definitivo
    create_definitive_working_map()
    print()
    
    # Criar mapa com listras
    create_alternating_stripes_map()
    print()
    
    print("✅ Mapas definitivos criados!")
    print("🎯 Teste estes mapas - eles DEVEM mostrar diferenças visuais!")
