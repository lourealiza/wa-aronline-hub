#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Criar mapa de debug para testar tiles específicos
"""

import json
import os

def create_debug_map():
    # Configurações do mapa - bem pequeno
    width_tiles = 4
    height_tiles = 4
    tile_size = 32
    
    # Criar camada de piso com tiles que sabemos que existem
    # Tile 1 = chão padrão, Tile 2 = parede, etc.
    floor_data = [1] * (width_tiles * height_tiles)
    
    # Criar floorLayer com tiles diferentes
    floor_layer_data = [0] * (width_tiles * height_tiles)
    
    # Quadrante 1 - tile 1
    floor_layer_data[0] = 1
    floor_layer_data[1] = 1
    floor_layer_data[4] = 1
    floor_layer_data[5] = 1
    
    # Quadrante 2 - tile 2
    floor_layer_data[2] = 2
    floor_layer_data[3] = 2
    floor_layer_data[6] = 2
    floor_layer_data[7] = 2
    
    # Quadrante 3 - tile 3
    floor_layer_data[8] = 3
    floor_layer_data[9] = 3
    floor_layer_data[12] = 3
    floor_layer_data[13] = 3
    
    # Quadrante 4 - tile 4
    floor_layer_data[10] = 4
    floor_layer_data[11] = 4
    floor_layer_data[14] = 4
    floor_layer_data[15] = 4
    
    # Criar spawn point
    spawn_point = {
        "id": 1,
        "name": "spawn",
        "type": "spawn",
        "x": 32,  # Centro
        "y": 32,
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
        "nextlayerid": 4,
        "nextobjectid": 5,
        "properties": [
            {
                "name": "mapName",
                "type": "string",
                "value": "Debug Map - Teste de Tiles"
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
                "name": "floorLayer",
                "type": "tilelayer",
                "width": width_tiles,
                "height": height_tiles,
                "opacity": 1,
                "visible": True,
                "data": floor_layer_data
            },
            {
                "id": 3,
                "name": "start",
                "type": "objectgroup",
                "opacity": 1,
                "visible": True,
                "objects": [spawn_point]
            }
        ]
    }
    
    # Salvar como .tmj
    output_path = "wa_map-debug.tmj"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    # Copiar para public também
    with open(f"public/{output_path}", 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Mapa de debug criado:")
    print(f"   📄 TMJ: {output_path} (raiz e public)")
    print(f"📊 Tamanho: {width_tiles}x{height_tiles} tiles")
    print(f"🎯 Spawn: Centro")
    print(f"🎨 Tiles: 1, 2, 3, 4 em quadrantes")
    print(f"📐 Layout: 2x2 grid de teste")
    
    return output_path

if __name__ == "__main__":
    create_debug_map()
