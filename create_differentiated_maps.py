#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Criar mapas com diferenças visuais reais para resolver o problema de mapas iguais
"""

import json
import os

def create_visual_differences_map():
    """Cria mapa com diferenças visuais claras no piso"""
    
    # Mapa 20x15 com diferentes tiles no piso
    width_tiles = 20
    height_tiles = 15
    tile_size = 32
    
    # Criar camada de piso com diferentes tiles para cada área
    floor_data = []
    
    # Área 1: Tiles 1 (cinza) - Lobby
    for y in range(0, 5):
        for x in range(0, 10):
            floor_data.append(1)
        for x in range(10, 20):
            floor_data.append(1)
    
    # Área 2: Tiles 2 (azul) - CEO
    for y in range(5, 10):
        for x in range(0, 10):
            floor_data.append(2)
        for x in range(10, 20):
            floor_data.append(2)
    
    # Área 3: Tiles 3 (verde) - Operações
    for y in range(10, 15):
        for x in range(0, 10):
            floor_data.append(3)
        for x in range(10, 20):
            floor_data.append(3)
    
    # Criar spawn point
    spawn_point = {
        "id": 1,
        "name": "spawn",
        "type": "spawn",
        "x": 160,  # Centro
        "y": 96,
        "width": 32,
        "height": 32,
        "visible": True
    }
    
    # Criar zonas
    zones = [
        {
            "id": 2,
            "name": "Lobby",
            "type": "common",
            "x": 0,
            "y": 0,
            "width": 640,  # 20 * 32
            "height": 160, # 5 * 32
            "visible": True,
            "properties": [
                {"name": "tile", "type": "int", "value": 1},
                {"name": "description", "type": "string", "value": "Área de recepção"}
            ]
        },
        {
            "id": 3,
            "name": "CEO",
            "type": "department",
            "x": 0,
            "y": 160,
            "width": 640,
            "height": 160,
            "visible": True,
            "properties": [
                {"name": "tile", "type": "int", "value": 2},
                {"name": "description", "type": "string", "value": "Gabinete executivo"}
            ]
        },
        {
            "id": 4,
            "name": "Operações",
            "type": "department",
            "x": 0,
            "y": 320,
            "width": 640,
            "height": 160,
            "visible": True,
            "properties": [
                {"name": "tile", "type": "int", "value": 3},
                {"name": "description", "type": "string", "value": "Equipe de operações"}
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
                "value": "AR Online - Mapa com Diferenças Visuais"
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
    
    # Salvar mapa
    output_path = "wa_map-visual-differences.tmj"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    # Copiar para public
    with open(f"public/{output_path}", 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Mapa com diferenças visuais criado:")
    print(f"   📄 TMJ: {output_path}")
    print(f"📊 Tamanho: {width_tiles}x{height_tiles} tiles")
    print(f"🎨 Tiles: 1=Lobby, 2=CEO, 3=Operações")
    print(f"👁️ Diferenças visuais no piso!")
    
    return output_path

def create_professional_map_fixed():
    """Cria mapa profissional com diferenças visuais reais"""
    
    width_tiles = 24
    height_tiles = 20
    tile_size = 32
    
    # Criar camada de piso com diferentes tiles
    floor_data = []
    
    # Área Superior - Convivência (tile 3)
    for y in range(0, 7):
        for x in range(0, 24):
            floor_data.append(3)
    
    # Ala Esquerda - Gestão (tile 4)
    for y in range(7, 20):
        for x in range(0, 12):
            floor_data.append(4)
    
    # Ala Direita - Operações (tile 5)
    for y in range(7, 20):
        for x in range(12, 24):
            floor_data.append(5)
    
    # Centro - Lobby (tile 6) - sobrepor nas áreas de gestão/operações
    for y in range(7, 13):
        for x in range(8, 16):
            index = y * width_tiles + x
            floor_data[index] = 6
    
    # Criar spawn point
    spawn_point = {
        "id": 1,
        "name": "spawn",
        "type": "spawn",
        "x": 192,
        "y": 160,
        "width": 32,
        "height": 32,
        "visible": True
    }
    
    # Criar zonas
    zones = [
        {
            "id": 2,
            "name": "Lobby AR ONLINE",
            "type": "common",
            "x": 256,
            "y": 224,
            "width": 256,
            "height": 192,
            "visible": True,
            "properties": [
                {"name": "tile", "type": "int", "value": 6},
                {"name": "description", "type": "string", "value": "Área central da AR Online"},
                {"name": "color", "type": "string", "value": "azul"}
            ]
        },
        {
            "id": 3,
            "name": "Convivência & Eventos",
            "type": "common",
            "x": 0,
            "y": 0,
            "width": 768,
            "height": 224,
            "visible": True,
            "properties": [
                {"name": "tile", "type": "int", "value": 3},
                {"name": "description", "type": "string", "value": "Área de convivência e eventos"},
                {"name": "color", "type": "string", "value": "verde"}
            ]
        },
        {
            "id": 4,
            "name": "Gestão & Liderança",
            "type": "department",
            "x": 0,
            "y": 224,
            "width": 384,
            "height": 416,
            "visible": True,
            "properties": [
                {"name": "tile", "type": "int", "value": 4},
                {"name": "description", "type": "string", "value": "Gestão e liderança"},
                {"name": "color", "type": "string", "value": "cinza"}
            ]
        },
        {
            "id": 5,
            "name": "Operações",
            "type": "department",
            "x": 384,
            "y": 224,
            "width": 384,
            "height": 416,
            "visible": True,
            "properties": [
                {"name": "tile", "type": "int", "value": 5},
                {"name": "description", "type": "string", "value": "Operações e desenvolvimento"},
                {"name": "color", "type": "string", "value": "azul"}
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
                "value": "AR Online - Escritório Profissional (CORRIGIDO)"
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
    
    # Salvar mapa
    output_path = "wa_map-professional-fixed.tmj"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    # Copiar para public
    with open(f"public/{output_path}", 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Mapa profissional CORRIGIDO criado:")
    print(f"   📄 TMJ: {output_path}")
    print(f"📊 Tamanho: {width_tiles}x{height_tiles} tiles")
    print(f"🎨 Tiles: 3=Convivência, 4=Gestão, 5=Operações, 6=Lobby")
    print(f"👁️ DIFERENÇAS VISUAIS REAIS NO PISO!")
    
    return output_path

if __name__ == "__main__":
    print("🔧 Corrigindo mapas com diferenças visuais...")
    print()
    
    # Criar mapa com diferenças visuais
    create_visual_differences_map()
    print()
    
    # Criar mapa profissional corrigido
    create_professional_map_fixed()
    print()
    
    print("✅ Todos os mapas corrigidos com diferenças visuais!")
    print("🎯 Agora os mapas terão aparências diferentes no WorkAdventure!")

