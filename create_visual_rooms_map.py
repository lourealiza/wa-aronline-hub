#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Criar mapa WorkAdventure com divisões visuais de salas
"""

import json
import os

def create_visual_rooms_map():
    # Configurações do mapa
    width_tiles = 80
    height_tiles = 60
    tile_size = 32
    
    # Dados das salas com cores específicas
    rooms = {
        "Lobby Central": {"x": 20, "y": 30, "w": 40, "h": 15, "color": 725},  # Azul
        "CEO": {"x": 4, "y": 26, "w": 5, "h": 5, "color": 2},  # Cinza claro
        "RH": {"x": 9, "y": 26, "w": 5, "h": 5, "color": 2},   # Cinza claro
        "Marketing": {"x": 61, "y": 26, "w": 5, "h": 5, "color": 3},  # Cinza claro
        "Desenvolvimento": {"x": 61, "y": 31, "w": 5, "h": 5, "color": 3},  # Cinza claro
        "Auditório": {"x": 10, "y": 6, "w": 16, "h": 7, "color": 4},  # Verde
        "Café": {"x": 41, "y": 6, "w": 15, "h": 7, "color": 4},  # Verde
        "Impressão": {"x": 56, "y": 6, "w": 8, "h": 7, "color": 4},  # Verde
        "Arquivo": {"x": 26, "y": 6, "w": 8, "h": 7, "color": 4},  # Verde
    }
    
    # Criar camada de piso base
    floor_data = [1] * (width_tiles * height_tiles)  # Tile 1 = piso cinza
    
    # Criar camada de salas com cores
    rooms_data = [0] * (width_tiles * height_tiles)  # 0 = vazio
    
    # Preencher salas com cores
    for room_name, room in rooms.items():
        for y in range(room["y"], room["y"] + room["h"]):
            for x in range(room["x"], room["x"] + room["w"]):
                if 0 <= x < width_tiles and 0 <= y < height_tiles:
                    index = y * width_tiles + x
                    rooms_data[index] = room["color"]
    
    # Criar camada de paredes/bordas
    walls_data = [0] * (width_tiles * height_tiles)
    
    # Adicionar bordas das salas
    for room_name, room in rooms.items():
        # Bordas horizontais
        for x in range(room["x"], room["x"] + room["w"]):
            if 0 <= x < width_tiles:
                # Borda superior
                if room["y"] > 0:
                    walls_data[(room["y"] - 1) * width_tiles + x] = 1
                # Borda inferior
                if room["y"] + room["h"] < height_tiles:
                    walls_data[(room["y"] + room["h"]) * width_tiles + x] = 1
        
        # Bordas verticais
        for y in range(room["y"], room["y"] + room["h"]):
            if 0 <= y < height_tiles:
                # Borda esquerda
                if room["x"] > 0:
                    walls_data[y * width_tiles + (room["x"] - 1)] = 1
                # Borda direita
                if room["x"] + room["w"] < width_tiles:
                    walls_data[y * width_tiles + (room["x"] + room["w"])] = 1
    
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
                    "name": "color",
                    "type": "string",
                    "value": str(room["color"])
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
        "x": 640,  # Centro do lobby
        "y": 960,
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
                "opacity": 0.7,
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
    output_path = "public/wa_map-visual-rooms.tmj"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Mapa com divisões visuais criado: {output_path}")
    print(f"📊 Salas criadas: {len(rooms)}")
    print(f"🎨 Cores utilizadas: Azul (Lobby), Cinza (Departamentos), Verde (Comum)")
    
    return output_path

if __name__ == "__main__":
    create_visual_rooms_map()
