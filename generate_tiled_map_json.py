import json
from pathlib import Path
from typing import List, Dict, Optional


def _fill_rect(data: List[int], W: int, x: int, y: int, w: int, h: int, gid: int) -> None:
    for yy in range(max(0, y), y + h):
        if yy < 0 or yy >= len(data) // W:
            continue
        row_start = yy * W
        for xx in range(max(0, x), x + w):
            if xx < 0 or xx >= W:
                continue
            data[row_start + xx] = gid


def generate_tiled_map_json(
    output_path: str = "public/office_generated/ar_office_layout.tmj",
    width_tiles: int = 70,
    height_tiles: int = 50,
    tile_size: int = 32,
    tileset_image: str = "../tilesets/WA_Room_Builder.png",
    floor_gid: int = 725,
    zones: Optional[List[Dict]] = None,
    map_name: str = "AR Online HQ",
) -> str:
    """Gera um TMJ compatível com WorkAdventure (Tiled 1.10.x) com:
    - tileset embutido (sem TSX externo)
    - camadas obrigatórias: 'start' e 'floorLayer'
    - layout base (lobby + alas) com piso (GID configurável)
    - camada 'zones' para objetos interativos (se fornecidos)
    """

    W, H = width_tiles, height_tiles
    floor_data = [0] * (W * H)

    # Lobby central (aprox. 40% x 30%)
    lobby_w = max(10, round(W * 0.4))
    lobby_h = max(8, round(H * 0.3))
    lobby_x = (W - lobby_w) // 2
    lobby_y = (H - lobby_h) // 2
    _fill_rect(floor_data, W, lobby_x, lobby_y, lobby_w, lobby_h, floor_gid)

    # Corredor superior até área de eventos
    _fill_rect(floor_data, W, lobby_x, max(0, lobby_y - 6), lobby_w, 6, floor_gid)

    # Alas laterais esquerda/direita
    _fill_rect(floor_data, W, max(0, lobby_x - lobby_w), lobby_y, lobby_w, lobby_h, floor_gid)
    _fill_rect(floor_data, W, min(W - lobby_w, lobby_x + lobby_w), lobby_y, lobby_w, lobby_h, floor_gid)

    # Spawn no centro do lobby (em pixels)
    spawn_x = float((lobby_x + lobby_w // 2) * tile_size)
    spawn_y = float((lobby_y + lobby_h // 2) * tile_size)

    # Tileset embutido (evita TSX externo)
    tileset = {
        "firstgid": 1,
        "name": "WA_Room_Builder",
        "tilewidth": tile_size,
        "tileheight": tile_size,
        "tilecount": 1000,
        "columns": 25,
        "image": tileset_image,
        "imagewidth": 800,
        "imageheight": 1280,
    }

    # Hotspots base (podem ser expandidos via 'zones')
    def hotspot_layer(name: str, cx_px: float, cy_px: float, url: str) -> Dict:
        return {
            "draworder": "topdown",
            "id": 0,  # placeholder; Tiled cuidará disso
            "name": name,
            "objects": [
                {
                    "id": 1,
                    "name": name,
                    "rectangle": True,
                    "x": cx_px - tile_size,
                    "y": cy_px - tile_size,
                    "width": tile_size * 2,
                    "height": tile_size * 2,
                    "type": "hotspot",
                    "visible": True,
                    "properties": [
                        {"name": "openWebsite", "type": "string", "value": url}
                    ],
                }
            ],
            "opacity": 1,
            "type": "objectgroup",
            "visible": True,
            "x": 0,
            "y": 0,
        }

    layers: List[Dict] = [
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
        {
            "draworder": "topdown",
            "id": 2,
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
        {
            "draworder": "topdown",
            "id": 3,
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
        hotspot_layer("AR Online Logo", spawn_x, spawn_y, "https://www.ar-online.com.br/sobre"),
        hotspot_layer("Telão Tecnológico", spawn_x, max(0.0, spawn_y - tile_size * 3), "https://www.ar-online.com.br/video-institucional"),
        hotspot_layer("Balcão Atendimento", spawn_x + tile_size * 6, spawn_y, "https://aria.ar-online.com"),
        {
            "draworder": "topdown",
            "id": 4,
            "name": "PrivateZones",
            "objects": [
                {
                    "id": 3,
                    "name": "CEO_Private_Zone",
                    "rectangle": True,
                    "x": float(max(0, lobby_x - lobby_w + 2) * tile_size),
                    "y": float(lobby_y * tile_size),
                    "width": float(tile_size * 6),
                    "height": float(tile_size * 6),
                    "type": "zone",
                    "visible": True,
                    "properties": [{"name": "private", "type": "bool", "value": True}],
                }
            ],
            "opacity": 1,
            "type": "objectgroup",
            "visible": True,
            "x": 0,
            "y": 0,
        },
    ]

    # Camada "zones" opcional (objetos adicionais)
    if zones:
        layers.append({
            "id": len(layers) + 1,
            "name": "zones",
            "type": "objectgroup",
            "objects": zones,
            "opacity": 1,
            "visible": True,
            "x": 0,
            "y": 0,
        })

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
            {"name": "mapName", "type": "string", "value": map_name},
        ],
        "tilesets": [tileset],
        "layers": layers,
    }

    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return str(out)


if __name__ == "__main__":
    path = generate_tiled_map_json()
    print(f"Mapa gerado em: {path}")

