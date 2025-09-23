import json
from pathlib import Path
from typing import List, Dict, Optional, Tuple

def create_complete_workadventure_map(
    output_path: str = "public/wa_map-interativo.tmj",
    width_tiles: int = 80,
    height_tiles: int = 60,
    tile_size: int = 32
) -> str:
    """Cria mapa completo do WorkAdventure com todas as camadas e salas"""
    
    # Inicializar dados do mapa
    floor_data = [0] * (width_tiles * height_tiles)
    walls_data = [0] * (width_tiles * height_tiles)
    collision_data = [0] * (width_tiles * height_tiles)
    furniture_data = [0] * (width_tiles * height_tiles)
    decoration_data = [0] * (width_tiles * height_tiles)
    
    # Definir tiles por tipo
    LOBBY_TILE = 725  # Azul vibrante
    CORRIDOR_TILE = 1  # Cinza médio
    MANAGEMENT_TILE = 2  # Cinza claro
    OPERATIONS_TILE = 3  # Cinza claro
    CONVIVENCE_TILE = 4  # Verde suave
    WALL_TILE = 100  # Paredes
    FURNITURE_TILE = 200  # Mobiliário
    DECORATION_TILE = 300  # Decoração
    
    def fill_rect(data: List[int], W: int, x: int, y: int, w: int, h: int, tile_id: int) -> None:
        """Preenche retângulo com tile específico"""
        for yy in range(h):
            for xx in range(w):
                if 0 <= x + xx < W and 0 <= y + yy < height_tiles:
                    data[(y + yy) * W + (x + xx)] = tile_id
    
    def create_walls(data: List[int], W: int, x: int, y: int, w: int, h: int) -> None:
        """Cria paredes ao redor de uma área"""
        # Paredes horizontais
        fill_rect(data, W, x, y, w, 1, WALL_TILE)  # Topo
        fill_rect(data, W, x, y + h - 1, w, 1, WALL_TILE)  # Base
        # Paredes verticais
        fill_rect(data, W, x, y, 1, h, WALL_TILE)  # Esquerda
        fill_rect(data, W, x + w - 1, y, 1, h, WALL_TILE)  # Direita
    
    def create_door(data: List[int], W: int, x: int, y: int) -> None:
        """Cria porta removendo parte da parede"""
        data[y * W + x] = 0
    
    # 1. ÁREA CENTRAL - Lobby/Recepção (azul 725)
    fill_rect(floor_data, width_tiles, 20, 30, 40, 15, LOBBY_TILE)
    create_walls(walls_data, width_tiles, 20, 30, 40, 15)
    create_door(walls_data, width_tiles, 39, 30)  # Porta superior
    create_door(walls_data, width_tiles, 39, 44)  # Porta inferior
    create_door(walls_data, width_tiles, 20, 37)  # Porta esquerda
    create_door(walls_data, width_tiles, 59, 37)  # Porta direita
    
    # 2. ALA ESQUERDA - Gestão & CEO (cinza claro)
    fill_rect(floor_data, width_tiles, 4, 26, 15, 23, MANAGEMENT_TILE)
    create_walls(walls_data, width_tiles, 4, 26, 15, 23)
    create_door(walls_data, width_tiles, 19, 26)  # Porta para lobby
    
    # 3. ALA DIREITA - Operações (cinza claro)
    fill_rect(floor_data, width_tiles, 61, 26, 15, 23, OPERATIONS_TILE)
    create_walls(walls_data, width_tiles, 61, 26, 15, 23)
    create_door(walls_data, width_tiles, 61, 26)  # Porta para lobby
    
    # 4. PARTE SUPERIOR - Convivência & Eventos (verde suave)
    fill_rect(floor_data, width_tiles, 10, 6, 61, 17, CONVIVENCE_TILE)
    create_walls(walls_data, width_tiles, 10, 6, 61, 17)
    create_door(walls_data, width_tiles, 39, 22)  # Porta para lobby
    
    # 5. CORREDORES (cinza médio)
    fill_rect(floor_data, width_tiles, 39, 22, 2, 31, CORRIDOR_TILE)
    fill_rect(floor_data, width_tiles, 38, 22, 4, 3, CORRIDOR_TILE)
    fill_rect(floor_data, width_tiles, 19, 26, 2, 2, CORRIDOR_TILE)
    fill_rect(floor_data, width_tiles, 59, 26, 2, 2, CORRIDOR_TILE)
    
    # 6. SUBDIVISÕES DETALHADAS
    
    # Ala Esquerda - Subdivisões
    # CEO (x=4..8, y=26..30)
    fill_rect(floor_data, width_tiles, 4, 26, 5, 5, MANAGEMENT_TILE)
    create_walls(walls_data, width_tiles, 4, 26, 5, 5)
    create_door(walls_data, width_tiles, 6, 30)
    
    # RH (x=9..13, y=26..30)
    fill_rect(floor_data, width_tiles, 9, 26, 5, 5, MANAGEMENT_TILE)
    create_walls(walls_data, width_tiles, 9, 26, 5, 5)
    create_door(walls_data, width_tiles, 11, 30)
    
    # Projetos (x=4..8, y=31..35)
    fill_rect(floor_data, width_tiles, 4, 31, 5, 5, MANAGEMENT_TILE)
    create_walls(walls_data, width_tiles, 4, 31, 5, 5)
    create_door(walls_data, width_tiles, 6, 35)
    
    # Processos & IA (x=9..13, y=31..35)
    fill_rect(floor_data, width_tiles, 9, 31, 5, 5, MANAGEMENT_TILE)
    create_walls(walls_data, width_tiles, 9, 31, 5, 5)
    create_door(walls_data, width_tiles, 11, 35)
    
    # Financeiro (x=4..8, y=36..40)
    fill_rect(floor_data, width_tiles, 4, 36, 5, 5, MANAGEMENT_TILE)
    create_walls(walls_data, width_tiles, 4, 36, 5, 5)
    create_door(walls_data, width_tiles, 6, 40)
    
    # Vendas (x=9..13, y=36..40)
    fill_rect(floor_data, width_tiles, 9, 36, 5, 5, MANAGEMENT_TILE)
    create_walls(walls_data, width_tiles, 9, 36, 5, 5)
    create_door(walls_data, width_tiles, 11, 40)
    
    # Ala Direita - Subdivisões
    # Marketing (x=61..65, y=26..30)
    fill_rect(floor_data, width_tiles, 61, 26, 5, 5, OPERATIONS_TILE)
    create_walls(walls_data, width_tiles, 61, 26, 5, 5)
    create_door(walls_data, width_tiles, 63, 30)
    
    # Comercial (x=66..70, y=26..30)
    fill_rect(floor_data, width_tiles, 66, 26, 5, 5, OPERATIONS_TILE)
    create_walls(walls_data, width_tiles, 66, 26, 5, 5)
    create_door(walls_data, width_tiles, 68, 30)
    
    # Desenvolvimento (x=61..65, y=31..35)
    fill_rect(floor_data, width_tiles, 61, 31, 5, 5, OPERATIONS_TILE)
    create_walls(walls_data, width_tiles, 61, 31, 5, 5)
    create_door(walls_data, width_tiles, 63, 35)
    
    # QA (x=66..70, y=31..35)
    fill_rect(floor_data, width_tiles, 66, 31, 5, 5, OPERATIONS_TILE)
    create_walls(walls_data, width_tiles, 66, 31, 5, 5)
    create_door(walls_data, width_tiles, 68, 35)
    
    # DevOps (x=61..65, y=36..40)
    fill_rect(floor_data, width_tiles, 61, 36, 5, 5, OPERATIONS_TILE)
    create_walls(walls_data, width_tiles, 61, 36, 5, 5)
    create_door(walls_data, width_tiles, 63, 40)
    
    # Suporte (x=66..70, y=36..40)
    fill_rect(floor_data, width_tiles, 66, 36, 5, 5, OPERATIONS_TILE)
    create_walls(walls_data, width_tiles, 66, 36, 5, 5)
    create_door(walls_data, width_tiles, 68, 40)
    
    # Convivência - Subdivisões
    # Auditório (x=10..25, y=6..12)
    fill_rect(floor_data, width_tiles, 10, 6, 16, 7, CONVIVENCE_TILE)
    create_walls(walls_data, width_tiles, 10, 6, 16, 7)
    create_door(walls_data, width_tiles, 18, 12)
    
    # Jardim Virtual (x=26..40, y=6..12)
    fill_rect(floor_data, width_tiles, 26, 6, 15, 7, CONVIVENCE_TILE)
    create_walls(walls_data, width_tiles, 26, 6, 15, 7)
    create_door(walls_data, width_tiles, 33, 12)
    
    # Lounge/Copa (x=41..55, y=6..12)
    fill_rect(floor_data, width_tiles, 41, 6, 15, 7, CONVIVENCE_TILE)
    create_walls(walls_data, width_tiles, 41, 6, 15, 7)
    create_door(walls_data, width_tiles, 48, 12)
    
    # Treinamento (x=56..70, y=6..12)
    fill_rect(floor_data, width_tiles, 56, 6, 15, 7, CONVIVENCE_TILE)
    create_walls(walls_data, width_tiles, 56, 6, 15, 7)
    create_door(walls_data, width_tiles, 63, 12)
    
    # Salas de Reunião A e B (x=10..25, y=13..18)
    fill_rect(floor_data, width_tiles, 10, 13, 7, 6, CONVIVENCE_TILE)
    create_walls(walls_data, width_tiles, 10, 13, 7, 6)
    create_door(walls_data, width_tiles, 13, 18)
    
    fill_rect(floor_data, width_tiles, 18, 13, 7, 6, CONVIVENCE_TILE)
    create_walls(walls_data, width_tiles, 18, 13, 7, 6)
    create_door(walls_data, width_tiles, 21, 18)
    
    # 7. MOBILIÁRIO E DECORAÇÃO
    
    # Mobiliário no lobby
    fill_rect(furniture_data, width_tiles, 25, 32, 2, 1, FURNITURE_TILE)  # Mesa recepção
    fill_rect(furniture_data, width_tiles, 35, 32, 2, 1, FURNITURE_TILE)  # Mesa central
    fill_rect(furniture_data, width_tiles, 45, 32, 2, 1, FURNITURE_TILE)  # Mesa lateral
    
    # Decoração
    fill_rect(decoration_data, width_tiles, 30, 35, 1, 1, DECORATION_TILE)  # Planta
    fill_rect(decoration_data, width_tiles, 50, 35, 1, 1, DECORATION_TILE)  # Planta
    
    # 8. COLISÕES
    # Paredes são colisões
    collision_data = walls_data.copy()
    
    # Criar estrutura do mapa
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
        "nextlayerid": 15,
        "nextobjectid": 200,
        "properties": [
            {
                "name": "mapName",
                "type": "string",
                "value": "AR Online - Escritório Virtual Completo"
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
                "tilewidth": tile_size,
                "tileheight": tile_size,
                "tilecount": 1000,
                "columns": 25,
                "image": "tilesets/WA_Room_Builder.png",
                "imagewidth": 800,
                "imageheight": 1280,
            }
        ],
        "layers": [
            # Camada de piso
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
            # Camada de paredes
            {
                "id": 2,
                "name": "walls",
                "type": "tilelayer",
                "width": width_tiles,
                "height": height_tiles,
                "opacity": 1,
                "visible": True,
                "data": walls_data
            },
            # Camada de colisões
            {
                "id": 3,
                "name": "collision",
                "type": "tilelayer",
                "width": width_tiles,
                "height": height_tiles,
                "opacity": 0,
                "visible": False,
                "data": collision_data
            },
            # Camada de mobiliário
            {
                "id": 4,
                "name": "furniture",
                "type": "tilelayer",
                "width": width_tiles,
                "height": height_tiles,
                "opacity": 1,
                "visible": True,
                "data": furniture_data
            },
            # Camada de decoração
            {
                "id": 5,
                "name": "decoration",
                "type": "tilelayer",
                "width": width_tiles,
                "height": height_tiles,
                "opacity": 1,
                "visible": True,
                "data": decoration_data
            },
            # Ponto de spawn
            {
                "id": 6,
                "name": "start",
                "type": "objectgroup",
                "opacity": 1,
                "visible": True,
                "objects": [
                    {
                        "id": 1,
                        "name": "spawn",
                        "x": 39 * tile_size,
                        "y": 37 * tile_size,
                        "width": tile_size,
                        "height": tile_size,
                        "type": "spawn",
                        "visible": True
                    }
                ]
            },
            # Zonas privadas
            {
                "id": 7,
                "name": "PrivateZones",
                "type": "objectgroup",
                "opacity": 1,
                "visible": True,
                "objects": [
                    # CEO
                    {
                        "id": 2,
                        "name": "CEO",
                        "x": 4 * tile_size,
                        "y": 26 * tile_size,
                        "width": 5 * tile_size,
                        "height": 5 * tile_size,
                        "type": "private",
                        "visible": True
                    },
                    # RH
                    {
                        "id": 3,
                        "name": "RH",
                        "x": 9 * tile_size,
                        "y": 26 * tile_size,
                        "width": 5 * tile_size,
                        "height": 5 * tile_size,
                        "type": "private",
                        "visible": True
                    },
                    # Desenvolvimento
                    {
                        "id": 4,
                        "name": "Desenvolvimento",
                        "x": 61 * tile_size,
                        "y": 31 * tile_size,
                        "width": 5 * tile_size,
                        "height": 5 * tile_size,
                        "type": "private",
                        "visible": True
                    },
                    # Marketing
                    {
                        "id": 5,
                        "name": "Marketing",
                        "x": 61 * tile_size,
                        "y": 26 * tile_size,
                        "width": 5 * tile_size,
                        "height": 5 * tile_size,
                        "type": "private",
                        "visible": True
                    }
                ]
            },
            # Zonas especiais
            {
                "id": 8,
                "name": "zones",
                "type": "objectgroup",
                "opacity": 1,
                "visible": True,
                "objects": [
                    # Lobby Central
                    {
                        "id": 6,
                        "name": "Lobby Central",
                        "x": 20 * tile_size,
                        "y": 30 * tile_size,
                        "width": 40 * tile_size,
                        "height": 15 * tile_size,
                        "type": "lobby",
                        "visible": True
                    },
                    # Auditório
                    {
                        "id": 7,
                        "name": "Auditório",
                        "x": 10 * tile_size,
                        "y": 6 * tile_size,
                        "width": 16 * tile_size,
                        "height": 7 * tile_size,
                        "type": "auditorium",
                        "visible": True
                    },
                    # Café
                    {
                        "id": 8,
                        "name": "Café",
                        "x": 41 * tile_size,
                        "y": 6 * tile_size,
                        "width": 15 * tile_size,
                        "height": 7 * tile_size,
                        "type": "cafe",
                        "visible": True
                    },
                    # Impressão
                    {
                        "id": 9,
                        "name": "Impressão",
                        "x": 56 * tile_size,
                        "y": 6 * tile_size,
                        "width": 15 * tile_size,
                        "height": 7 * tile_size,
                        "type": "printing",
                        "visible": True
                    },
                    # Arquivo
                    {
                        "id": 10,
                        "name": "Arquivo",
                        "x": 26 * tile_size,
                        "y": 6 * tile_size,
                        "width": 15 * tile_size,
                        "height": 7 * tile_size,
                        "type": "archive",
                        "visible": True
                    }
                ]
            }
        ]
    }
    
    # Salvar arquivo
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    return str(output_file)

if __name__ == "__main__":
    output_path = create_complete_workadventure_map()
    print(f"Mapa completo criado em: {output_path}")
    print("\nCamadas criadas:")
    print("- floor: Piso base")
    print("- walls: Paredes e divisórias")
    print("- collision: Colisões (invisível)")
    print("- furniture: Mobiliário")
    print("- decoration: Decoração")
    print("- start: Ponto de spawn")
    print("- PrivateZones: Zonas privadas")
    print("- zones: Zonas especiais")
    print("\nSalas criadas:")
    print("- Lobby Central")
    print("- CEO, RH, Projetos, Processos & IA, Financeiro, Vendas")
    print("- Marketing, Comercial, Desenvolvimento, QA, DevOps, Suporte")
    print("- Auditório, Jardim Virtual, Lounge/Copa, Treinamento")
    print("- Salas de Reunião A e B")
    print("- Café, Impressão, Arquivo")
