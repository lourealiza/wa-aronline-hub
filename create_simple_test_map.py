import json
from pathlib import Path

def create_simple_test_map():
    """Cria um mapa simples para teste"""
    
    # Mapa 10x10 simples
    width, height = 10, 10
    floor_data = [1] * (width * height)  # Tile 1 para todo o piso
    
    map_data = {
        "type": "map",
        "version": "1.10",
        "tiledversion": "1.10.2",
        "orientation": "orthogonal",
        "renderorder": "right-down",
        "infinite": False,
        "width": width,
        "height": height,
        "tilewidth": 32,
        "tileheight": 32,
        "compressionlevel": -1,
        "nextlayerid": 3,
        "nextobjectid": 10,
        "properties": [
            {
                "name": "mapName",
                "type": "string",
                "value": "AR Online - Teste Simples"
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
                "imageheight": 1280,
            }
        ],
        "layers": [
            {
                "id": 1,
                "name": "floor",
                "type": "tilelayer",
                "width": width,
                "height": height,
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
                "objects": [
                    {
                        "id": 1,
                        "name": "spawn",
                        "x": 5 * 32,
                        "y": 5 * 32,
                        "width": 32,
                        "height": 32,
                        "type": "spawn",
                        "visible": True
                    }
                ]
            }
        ]
    }
    
    # Salvar arquivo
    output_file = Path("public/wa_map-teste.tmj")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(map_data, f, indent=2, ensure_ascii=False)
    
    return str(output_file)

if __name__ == "__main__":
    output_path = create_simple_test_map()
    print(f"Mapa de teste criado em: {output_path}")
