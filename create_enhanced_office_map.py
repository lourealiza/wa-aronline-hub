import json
from pathlib import Path
from typing import List, Dict, Optional, Tuple

def create_office_room(x: int, y: int, width: int, height: int, name: str, room_type: str = "office") -> Dict:
    """Cria uma sala de escritório com mobiliário básico"""
    objects = []
    
    # Adicionar mesas e cadeiras baseado no tipo de sala
    if room_type == "meeting":
        # Sala de reunião - mesa central
        objects.append({
            "id": len(objects) + 1,
            "name": f"{name}_table",
            "rectangle": True,
            "x": float(x * 32 + 8),
            "y": float(y * 32 + 8),
            "width": float((width - 2) * 32),
            "height": float((height - 2) * 32),
            "type": "table",
            "visible": True
        })
    elif room_type == "open_office":
        # Escritório aberto - múltiplas mesas
        for i in range(max(1, width // 3)):
            for j in range(max(1, height // 3)):
                table_x = x + 1 + i * 3
                table_y = y + 1 + j * 3
                if table_x < x + width - 1 and table_y < y + height - 1:
                    objects.append({
                        "id": len(objects) + 1,
                        "name": f"{name}_desk_{i}_{j}",
                        "rectangle": True,
                        "x": float(table_x * 32),
                        "y": float(table_y * 32),
                        "width": 64.0,
                        "height": 32.0,
                        "type": "desk",
                        "visible": True
                    })
    else:
        # Sala padrão - mesa simples
        objects.append({
            "id": len(objects) + 1,
            "name": f"{name}_desk",
            "rectangle": True,
            "x": float((x + 1) * 32),
            "y": float((y + 1) * 32),
            "width": 64.0,
            "height": 32.0,
            "type": "desk",
            "visible": True
        })
    
    return {
        "id": len(objects) + 1,
        "name": name,
        "rectangle": True,
        "x": float(x * 32),
        "y": float(y * 32),
        "width": float(width * 32),
        "height": float(height * 32),
        "type": "room",
        "visible": True,
        "properties": [
            {"name": "roomType", "type": "string", "value": room_type},
            {"name": "roomName", "type": "string", "value": name}
        ]
    }

def create_enhanced_office_map(
    output_path: str = "wa_map-interativo.tmj",
    width_tiles: int = 100,
    height_tiles: int = 80,
    tile_size: int = 32
) -> str:
    """Cria um mapa de escritório aprimorado baseado no layout da imagem"""
    
    W, H = width_tiles, height_tiles
    
    # Dados do piso (todos os tiles são piso por padrão)
    floor_data = [1] * (W * H)  # GID 1 = piso padrão
    
    # Dados das paredes (inicialmente vazios)
    wall_data = [0] * (W * H)
    
    # Definir layout das salas baseado na imagem
    rooms = [
        # Área central (lobby principal)
        {"x": 40, "y": 30, "w": 20, "h": 20, "name": "Lobby Central", "type": "lobby"},
        
        # Ala superior esquerda
        {"x": 5, "y": 5, "w": 25, "h": 15, "name": "Desenvolvimento", "type": "open_office"},
        {"x": 5, "y": 25, "w": 15, "h": 10, "name": "QA", "type": "office"},
        {"x": 25, "y": 25, "w": 15, "h": 10, "name": "DevOps", "type": "office"},
        
        # Ala superior direita
        {"x": 70, "y": 5, "w": 25, "h": 15, "name": "Marketing", "type": "open_office"},
        {"x": 70, "y": 25, "w": 15, "h": 10, "name": "Design", "type": "office"},
        {"x": 90, "y": 25, "w": 10, "h": 10, "name": "Criativo", "type": "office"},
        
        # Ala inferior esquerda
        {"x": 5, "y": 50, "w": 20, "h": 15, "name": "RH", "type": "office"},
        {"x": 30, "y": 50, "w": 15, "h": 15, "name": "Financeiro", "type": "office"},
        {"x": 5, "y": 70, "w": 25, "h": 10, "name": "Atendimento", "type": "open_office"},
        
        # Ala inferior direita
        {"x": 70, "y": 50, "w": 20, "h": 15, "name": "Vendas", "type": "open_office"},
        {"x": 95, "y": 50, "w": 5, "h": 15, "name": "Diretoria", "type": "office"},
        {"x": 70, "y": 70, "w": 25, "h": 10, "name": "Suporte", "type": "open_office"},
        
        # Salas de reunião
        {"x": 35, "y": 5, "w": 10, "h": 8, "name": "Sala de Reunião A", "type": "meeting"},
        {"x": 50, "y": 5, "w": 10, "h": 8, "name": "Sala de Reunião B", "type": "meeting"},
        {"x": 35, "y": 70, "w": 10, "h": 8, "name": "Auditório", "type": "meeting"},
        {"x": 50, "y": 70, "w": 10, "h": 8, "name": "Treinamento", "type": "meeting"},
    ]
    
    # Criar paredes ao redor das salas
    for room in rooms:
        x, y, w, h = room["x"], room["y"], room["w"], room["h"]
        
        # Paredes horizontais (superior e inferior)
        for i in range(w):
            if x + i < W:
                if y > 0:
                    wall_data[(y - 1) * W + (x + i)] = 2  # GID 2 = parede horizontal
                if y + h < H:
                    wall_data[(y + h) * W + (x + i)] = 2
        
        # Paredes verticais (esquerda e direita)
        for i in range(h):
            if y + i < H:
                if x > 0:
                    wall_data[(y + i) * W + (x - 1)] = 3  # GID 3 = parede vertical
                if x + w < W:
                    wall_data[(y + i) * W + (x + w)] = 3
    
    # Adicionar corredores principais
    # Corredor horizontal central
    for i in range(W):
        for j in range(25, 35):
            if j < H:
                floor_data[j * W + i] = 4  # GID 4 = corredor
    
    # Corredor vertical central
    for i in range(35, 65):
        for j in range(H):
            if i < W:
                floor_data[j * W + i] = 4
    
    # Tileset
    tileset = {
        "firstgid": 1,
        "name": "WA_Room_Builder",
        "tilewidth": tile_size,
        "tileheight": tile_size,
        "tilecount": 1000,
        "columns": 25,
        "image": "tilesets/WA_Room_Builder.png",
        "imagewidth": 800,
        "imageheight": 1280,
    }
    
    # Spawn no lobby central
    spawn_x = float((40 + 20 // 2) * tile_size)
    spawn_y = float((30 + 20 // 2) * tile_size)
    
    # Criar objetos das salas
    room_objects = []
    for room in rooms:
        room_obj = create_office_room(
            room["x"], room["y"], room["w"], room["h"], 
            room["name"], room["type"]
        )
        room_objects.append(room_obj)
    
    # Hotspots interativos
    hotspots = [
        {
            "id": 1,
            "name": "AR Online Logo",
            "rectangle": True,
            "x": spawn_x - 32,
            "y": spawn_y - 32,
            "width": 64.0,
            "height": 64.0,
            "type": "hotspot",
            "visible": True,
            "properties": [
                {"name": "openWebsite", "type": "string", "value": "https://www.ar-online.com.br"}
            ]
        },
        {
            "id": 2,
            "name": "Telão Tecnológico",
            "rectangle": True,
            "x": spawn_x + 100,
            "y": spawn_y - 50,
            "width": 64.0,
            "height": 64.0,
            "type": "hotspot",
            "visible": True,
            "properties": [
                {"name": "openWebsite", "type": "string", "value": "https://www.ar-online.com.br/video-institucional"}
            ]
        },
        {
            "id": 3,
            "name": "Balcão Atendimento",
            "rectangle": True,
            "x": spawn_x - 100,
            "y": spawn_y + 50,
            "width": 64.0,
            "height": 64.0,
            "type": "hotspot",
            "visible": True,
            "properties": [
                {"name": "openWebsite", "type": "string", "value": "https://aria.ar-online.com"}
            ]
        }
    ]
    
    # Camadas
    layers = [
        # Camada de piso
        {
            "id": 1,
            "name": "floor",
            "type": "tilelayer",
            "width": W,
            "height": H,
            "data": floor_data,
            "opacity": 1,
            "visible": True,
            "x": 0,
            "y": 0,
        },
        # Camada de paredes
        {
            "id": 2,
            "name": "walls",
            "type": "tilelayer",
            "width": W,
            "height": H,
            "data": wall_data,
            "opacity": 1,
            "visible": True,
            "x": 0,
            "y": 0,
        },
        # Camada de spawn
        {
            "draworder": "topdown",
            "id": 3,
            "name": "start",
            "objects": [
                {
                    "id": 1,
                    "name": "spawn",
                    "point": True,
                    "x": spawn_x,
                    "y": spawn_y,
                    "type": "spawn",
                    "visible": True,
                }
            ],
            "opacity": 1,
            "type": "objectgroup",
            "visible": True,
            "x": 0,
            "y": 0,
        },
        # Camada de piso (objeto)
        {
            "draworder": "topdown",
            "id": 4,
            "name": "floorLayer",
            "objects": [
                {
                    "id": 2,
                    "name": "floor",
                    "rectangle": True,
                    "x": 0.0,
                    "y": 0.0,
                    "width": float(W * tile_size),
                    "height": float(H * tile_size),
                    "type": "floor",
                    "visible": True,
                }
            ],
            "opacity": 1,
            "type": "objectgroup",
            "visible": True,
            "x": 0,
            "y": 0,
        },
        # Camada de salas
        {
            "draworder": "topdown",
            "id": 5,
            "name": "rooms",
            "objects": room_objects,
            "opacity": 1,
            "type": "objectgroup",
            "visible": True,
            "x": 0,
            "y": 0,
        },
        # Camada de hotspots
        {
            "draworder": "topdown",
            "id": 6,
            "name": "hotspots",
            "objects": hotspots,
            "opacity": 1,
            "type": "objectgroup",
            "visible": True,
            "x": 0,
            "y": 0,
        },
        # Zonas privadas
        {
            "draworder": "topdown",
            "id": 7,
            "name": "PrivateZones",
            "objects": [
                {
                    "id": 4,
                    "name": "Diretoria_Private_Zone",
                    "rectangle": True,
                    "x": float(95 * tile_size),
                    "y": float(50 * tile_size),
                    "width": float(5 * tile_size),
                    "height": float(15 * tile_size),
                    "type": "zone",
                    "visible": True,
                    "properties": [
                        {"name": "private", "type": "bool", "value": True}
                    ],
                }
            ],
            "opacity": 1,
            "type": "objectgroup",
            "visible": True,
            "x": 0,
            "y": 0,
        },
    ]
    
    # Estrutura do mapa
    data = {
        "type": "map",
        "version": "1.10",
        "tiledversion": "1.10.2",
        "orientation": "orthogonal",
        "renderorder": "right-down",
        "infinite": False,
        "width": W,
        "height": H,
        "tilewidth": tile_size,
        "tileheight": tile_size,
        "compressionlevel": -1,
        "nextlayerid": len(layers) + 1,
        "nextobjectid": 100,
        "properties": [
            {"name": "mapName", "type": "string", "value": "AR Online - Escritório Virtual Aprimorado"},
            {"name": "script", "type": "string", "value": "public/mapScript.js"}
        ],
        "tilesets": [tileset],
        "layers": layers,
    }
    
    # Salvar arquivo
    out = Path(output_path)
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return str(out)

if __name__ == "__main__":
    path = create_enhanced_office_map()
    print(f"Mapa aprimorado gerado em: {path}")
    print("Salas criadas:")
    print("- Lobby Central")
    print("- Desenvolvimento (escritório aberto)")
    print("- QA, DevOps, Design, Criativo")
    print("- RH, Financeiro, Atendimento")
    print("- Vendas, Diretoria, Suporte")
    print("- Salas de Reunião A e B")
    print("- Auditório e Treinamento")
