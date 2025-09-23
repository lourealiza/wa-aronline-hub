#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Criar mapa WorkAdventure simples com divisões visuais básicas
"""

import json
import os

def create_simple_visual_map():
    # Configurações do mapa
    width_tiles = 40
    height_tiles = 30
    tile_size = 32
    
    # Dados das salas com tiles básicos (1-10)
    rooms = {
        "Lobby Central": {"x": 10, "y": 15, "w": 20, "h": 8, "tile": 1},
        "CEO": {"x": 2, "y": 13, "w": 3, "h": 3, "tile": 2},
        "RH": {"x": 5, "y": 13, "w": 3, "h": 3, "tile": 3},
        "Marketing": {"x": 30, "y": 13, "w": 3, "h": 3, "tile": 4},
        "Desenvolvimento": {"x": 30, "y": 16, "w": 3, "h": 3, "tile": 5},
        "Auditório": {"x": 5, "y": 3, "w": 8, "h": 4, "tile": 6},
        "Café": {"x": 20, "y": 3, "w": 8, "h": 4, "tile": 7},
        "Impressão": {"x": 28, "y": 3, "w": 4, "h": 4, "tile": 8},
        "Arquivo": {"x": 13, "y": 3, "w": 4, "h": 4, "tile": 9},
    }
    
    # Criar camada de piso base
    floor_data = [1] * (width_tiles * height_tiles)  # Tile 1 = piso padrão
    
    # Criar camada de salas com diferentes tiles
    rooms_data = [0] * (width_tiles * height_tiles)  # 0 = vazio
    
    # Preencher salas com tiles diferentes
    for room_name, room in rooms.items():
        for y in range(room["y"], room["y"] + room["h"]):
            for x in range(room["x"], room["x"] + room["w"]):
                if 0 <= x < width_tiles and 0 <= y < height_tiles:
                    index = y * width_tiles + x
                    rooms_data[index] = room["tile"]
    
    # Criar camada de paredes/bordas
    walls_data = [0] * (width_tiles * height_tiles)
    
    # Adicionar bordas das salas
    for room_name, room in rooms.items():
        # Bordas horizontais
        for x in range(room["x"], room["x"] + room["w"]):
            if 0 <= x < width_tiles:
                # Borda superior
                if room["y"] > 0:
                    walls_data[(room["y"] - 1) * width_tiles + x] = 10
                # Borda inferior
                if room["y"] + room["h"] < height_tiles:
                    walls_data[(room["y"] + room["h"]) * width_tiles + x] = 10
        
        # Bordas verticais
        for y in range(room["y"], room["y"] + room["h"]):
            if 0 <= y < height_tiles:
                # Borda esquerda
                if room["x"] > 0:
                    walls_data[y * width_tiles + (room["x"] - 1)] = 10
                # Borda direita
                if room["x"] + room["w"] < width_tiles:
                    walls_data[y * width_tiles + (room["x"] + room["w"])] = 10
    
    # Criar objetos para as salas
    private_zones = []
    zones = []
    
    for room_name, room in rooms.items():
        # Converter coordenadas para pixels
        x_px = room["x"] * tile_size
        y_px = room["y"] * tile_size
        w_px = room["w"] * tile_size
        h_px = room["h"] * tile_size
        
        room_obj = {
            "id": len(private_zones) + 1,
            "name": room_name,
            "type": "department" if room_name in ["CEO", "RH", "Marketing", "Desenvolvimento"] else "common",
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
        
        if room_name in ["CEO", "RH", "Marketing", "Desenvolvimento"]:
            private_zones.append(room_obj)
        else:
            zones.append(room_obj)
    
    # Criar spawn point
    spawn_point = {
        "id": 1,
        "name": "spawn",
        "type": "spawn",
        "x": 320,  # Centro do lobby
        "y": 480,
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
        "nextlayerid": 8,
        "nextobjectid": 50,
        "properties": [
            {
                "name": "mapName",
                "type": "string",
                "value": "AR Online - Escritório Simples com Divisões"
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
                "name": "walls",
                "type": "tilelayer",
                "width": width_tiles,
                "height": height_tiles,
                "opacity": 1,
                "visible": True,
                "data": walls_data
            },
            {
                "id": 4,
                "name": "collision",
                "type": "tilelayer",
                "width": width_tiles,
                "height": height_tiles,
                "opacity": 1,
                "visible": False,
                "data": walls_data
            },
            {
                "id": 5,
                "name": "start",
                "type": "objectgroup",
                "opacity": 1,
                "visible": True,
                "objects": [spawn_point]
            },
            {
                "id": 6,
                "name": "PrivateZones",
                "type": "objectgroup",
                "opacity": 1,
                "visible": True,
                "objects": private_zones
            },
            {
                "id": 7,
                "name": "zones",
                "type": "objectgroup",
                "opacity": 1,
                "visible": True,
                "objects": zones
            }
        ]
    }
    
    # Salvar arquivo
    output_path = "public/wa_map-simple-visual.tmj"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Mapa simples com divisões visuais criado: {output_path}")
    print(f"📊 Salas criadas: {len(rooms)}")
    print(f"🎨 Usando tiles básicos (1-10)")
    
    return output_path

if __name__ == "__main__":
    create_simple_visual_map()
