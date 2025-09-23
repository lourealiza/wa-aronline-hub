import json
from pathlib import Path
from typing import List, Dict, Optional, Tuple

def create_sector_map(
    output_path: str = "public/wa_map-interativo.tmj",
    width_tiles: int = 80,
    height_tiles: int = 60,
    tile_size: int = 32
) -> str:
    """Cria mapa com divisão de setores conforme especificação"""
    
    # Inicializar dados do mapa
    data = [0] * (width_tiles * height_tiles)
    
    # Definir tiles por cor
    LOBBY_TILE = 725  # Azul vibrante
    CORRIDOR_TILE = 1  # Cinza médio
    MANAGEMENT_TILE = 2  # Cinza claro
    OPERATIONS_TILE = 3  # Cinza claro
    CONVIVENCE_TILE = 4  # Verde suave
    
    def fill_rect(data: List[int], W: int, x: int, y: int, w: int, h: int, tile_id: int) -> None:
        """Preenche retângulo com tile específico"""
        for yy in range(h):
            for xx in range(w):
                if 0 <= x + xx < W and 0 <= y + yy < height_tiles:
                    data[(y + yy) * W + (x + xx)] = tile_id
    
    # 1. ÁREA CENTRAL - Lobby/Recepção (azul 725)
    # Retângulo: x=20..59, y=30..44 (largura 40, altura 15)
    fill_rect(data, width_tiles, 20, 30, 40, 15, LOBBY_TILE)
    
    # 2. ALA ESQUERDA - Gestão & CEO (cinza claro)
    # Retângulo: x=4..18, y=26..48 (largura 15, altura 23)
    fill_rect(data, width_tiles, 4, 26, 15, 23, MANAGEMENT_TILE)
    
    # 3. ALA DIREITA - Operações (cinza claro)
    # Retângulo: x=61..75, y=26..48 (largura 15, altura 23)
    fill_rect(data, width_tiles, 61, 26, 15, 23, OPERATIONS_TILE)
    
    # 4. PARTE SUPERIOR - Convivência & Eventos (verde suave)
    # Retângulo: x=10..70, y=6..22 (largura 61, altura 17)
    fill_rect(data, width_tiles, 10, 6, 61, 17, CONVIVENCE_TILE)
    
    # 5. CORREDORES (cinza médio)
    
    # Espinha vertical central: x=39..40, y=22..52 (2 tiles de largura)
    fill_rect(data, width_tiles, 39, 22, 2, 31, CORRIDOR_TILE)
    
    # Conector superior (Convivência ↔ Lobby): y=22..24, x=38..41
    fill_rect(data, width_tiles, 38, 22, 4, 3, CORRIDOR_TILE)
    
    # Conector lateral esquerdo (Lobby ↔ Gestão): y=26..27, x=19..20
    fill_rect(data, width_tiles, 19, 26, 2, 2, CORRIDOR_TILE)
    
    # Conector lateral direito (Lobby ↔ Operações): y=26..27, x=59..60
    fill_rect(data, width_tiles, 59, 26, 2, 2, CORRIDOR_TILE)
    
    # Anel de circulação do lobby: 1-2 tiles de borda interna
    # Borda superior
    fill_rect(data, width_tiles, 20, 29, 40, 1, CORRIDOR_TILE)
    # Borda inferior
    fill_rect(data, width_tiles, 20, 45, 40, 1, CORRIDOR_TILE)
    # Borda esquerda
    fill_rect(data, width_tiles, 19, 30, 1, 15, CORRIDOR_TILE)
    # Borda direita
    fill_rect(data, width_tiles, 60, 30, 1, 15, CORRIDOR_TILE)
    
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
        "nextlayerid": 8,
        "nextobjectid": 100,
        "properties": [
            {
                "name": "mapName",
                "type": "string",
                "value": "AR Online - Escritório Virtual com Divisão de Setores"
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
            {
                "id": 1,
                "name": "floor",
                "type": "tilelayer",
                "width": width_tiles,
                "height": height_tiles,
                "opacity": 1,
                "visible": True,
                "data": data
            },
            {
                "id": 2,
                "name": "Lobby Central",
                "type": "objectgroup",
                "opacity": 1,
                "visible": True,
                "objects": [
                    {
                        "id": 1,
                        "name": "Lobby Central",
                        "rectangle": True,
                        "x": 20 * tile_size,
                        "y": 30 * tile_size,
                        "width": 40 * tile_size,
                        "height": 15 * tile_size,
                        "type": "lobby",
                        "visible": True
                    }
                ]
            },
            {
                "id": 3,
                "name": "Gestão & CEO",
                "type": "objectgroup",
                "opacity": 1,
                "visible": True,
                "objects": [
                    {
                        "id": 2,
                        "name": "Gestão & CEO",
                        "rectangle": True,
                        "x": 4 * tile_size,
                        "y": 26 * tile_size,
                        "width": 15 * tile_size,
                        "height": 23 * tile_size,
                        "type": "management",
                        "visible": True
                    }
                ]
            },
            {
                "id": 4,
                "name": "Operações",
                "type": "objectgroup",
                "opacity": 1,
                "visible": True,
                "objects": [
                    {
                        "id": 3,
                        "name": "Operações",
                        "rectangle": True,
                        "x": 61 * tile_size,
                        "y": 26 * tile_size,
                        "width": 15 * tile_size,
                        "height": 23 * tile_size,
                        "type": "operations",
                        "visible": True
                    }
                ]
            },
            {
                "id": 5,
                "name": "Convivência & Eventos",
                "type": "objectgroup",
                "opacity": 1,
                "visible": True,
                "objects": [
                    {
                        "id": 4,
                        "name": "Convivência & Eventos",
                        "rectangle": True,
                        "x": 10 * tile_size,
                        "y": 6 * tile_size,
                        "width": 61 * tile_size,
                        "height": 17 * tile_size,
                        "type": "convivence",
                        "visible": True
                    }
                ]
            },
            {
                "id": 6,
                "name": "Corredores",
                "type": "objectgroup",
                "opacity": 1,
                "visible": True,
                "objects": [
                    {
                        "id": 5,
                        "name": "Espinha Central",
                        "rectangle": True,
                        "x": 39 * tile_size,
                        "y": 22 * tile_size,
                        "width": 2 * tile_size,
                        "height": 31 * tile_size,
                        "type": "corridor",
                        "visible": True
                    },
                    {
                        "id": 6,
                        "name": "Conector Superior",
                        "rectangle": True,
                        "x": 38 * tile_size,
                        "y": 22 * tile_size,
                        "width": 4 * tile_size,
                        "height": 3 * tile_size,
                        "type": "corridor",
                        "visible": True
                    },
                    {
                        "id": 7,
                        "name": "Conector Esquerdo",
                        "rectangle": True,
                        "x": 19 * tile_size,
                        "y": 26 * tile_size,
                        "width": 2 * tile_size,
                        "height": 2 * tile_size,
                        "type": "corridor",
                        "visible": True
                    },
                    {
                        "id": 8,
                        "name": "Conector Direito",
                        "rectangle": True,
                        "x": 59 * tile_size,
                        "y": 26 * tile_size,
                        "width": 2 * tile_size,
                        "height": 2 * tile_size,
                        "type": "corridor",
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
    output_path = create_sector_map()
    print(f"Mapa com divisão de setores criado em: {output_path}")
    print("\nSetores criados:")
    print("- Lobby Central (azul 725): x=20..59, y=30..44")
    print("- Gestão & CEO (cinza claro): x=4..18, y=26..48")
    print("- Operações (cinza claro): x=61..75, y=26..48")
    print("- Convivência & Eventos (verde suave): x=10..70, y=6..22")
    print("- Corredores (cinza médio): espinha central e conectores")
