
import json

def generate_tiled_map_json():
    # Definir as dimensões do mapa (ajustado para acomodar mais salas)
    map_width = 70
    map_height = 70
    tile_size = 32 # pixels

    # Estrutura básica do JSON para o Tiled
    tiled_map = {
        "compressionlevel": -1,
        "height": map_height,
        "infinite": False,
        "layers": [],
        "nextlayerid": 1,
        "nextobjectid": 1,
        "orientation": "orthogonal",
        "renderorder": "right-down",
        "tiledversion": "1.9.2", # Versão do Tiled Editor, pode ser ajustada
        "tileheight": tile_size,
        "tilesets": [],
        "tilewidth": tile_size,
        "type": "map",
        "version": "1.9",
        "width": map_width
    }

    # Adicionar um tileset básico (exemplo, você precisaria de um tileset real)
    # Para simplificar, vamos assumir um tileset genérico. O usuário precisará ajustar isso.
    tiled_map["tilesets"].append({
        "firstgid": 1,
        "source": "tileset.json" # O usuário precisará criar este arquivo tileset.json
    })

    # Camada de tiles (fundo)
    # Preencher com um tile padrão (ex: tile 1, que seria o piso azul se o tileset for configurado)
    background_data = [1] * (map_width * map_height)
    tiled_map["layers"].append({
        "data": background_data,
        "height": map_height,
        "id": 1,
        "name": "Background",
        "opacity": 1,
        "type": "tilelayer",
        "visible": True,
        "width": map_width,
        "x": 0,
        "y": 0
    })

    # Camada de objetos (para elementos interativos e decorativos)
    object_layer = {
        "draworder": "topdown",
        "id": 2,
        "name": "Objects",
        "objects": [],
        "opacity": 1,
        "type": "objectgroup",
        "visible": True,
        "x": 0,
        "y": 0
    }

    # Adicionar objetos baseados no layout (simplificado)
    # Lobby/Recepção
    object_layer["objects"].append({"id": 1, "name": "AR Online Logo", "point": True, "x": map_width/2 * tile_size, "y": map_height/2 * tile_size, "type": "image", "properties": [{"name": "image", "type": "string", "value": "ar_online_lobby_logo.png"}, {"name": "trigger", "type": "string", "value": "onPlayerEnters"}, {"name": "script", "type": "string", "value": "displayWelcomeMessage.js"}]})
    object_layer["objects"].append({"id": 2, "name": "Telão Tecnológico", "point": True, "x": map_width/2 * tile_size, "y": (map_height/2 - 5) * tile_size, "type": "image", "properties": [{"name": "image", "type": "string", "value": "ar_online_telao_tecnologico.png"}, {"name": "openWebsite", "type": "string", "value": "https://www.ar-online.com.br/video-institucional"}]})
    object_layer["objects"].append({"id": 3, "name": "Balcão de Atendimento", "point": True, "x": (map_width/2 + 5) * tile_size, "y": map_height/2 * tile_size, "type": "image", "properties": [{"name": "image", "type": "string", "value": "ar_online_balcao_atendimento.png"}, {"name": "openWebsite", "type": "string", "value": "https://aria.ar-online.com"}]})

    # Alas Laterais - Gestão e CEO
    object_layer["objects"].append({"id": 4, "name": "Sala CEO", "point": True, "x": (map_width/4) * tile_size, "y": (map_height/4) * tile_size, "type": "area"})
    object_layer["objects"].append({"id": 5, "name": "Gestão de Projetos Board", "point": True, "x": (map_width/4 + 2) * tile_size, "y": (map_height/4 + 2) * tile_size, "type": "image", "properties": [{"name": "image", "type": "string", "value": "ar_online_project_management_board.png"}, {"name": "openWebsite", "type": "string", "value": "https://jira.ar-online.com/dashboard"}]})
    object_layer["objects"].append({"id": 10, "name": "RH Boards", "point": True, "x": (map_width/4 + 5) * tile_size, "y": (map_height/4 + 5) * tile_size, "type": "image", "properties": [{"name": "image", "type": "string", "value": "ar_online_hr_boards.png"}, {"name": "openWebsite", "type": "string", "value": "https://rh.ar-online.com/portal"}]})
    object_layer["objects"].append({"id": 11, "name": "Holographic Screens", "point": True, "x": (map_width/4 - 2) * tile_size, "y": (map_height/4 + 5) * tile_size, "type": "image", "properties": [{"name": "image", "type": "string", "value": "ar_online_holographic_screens.png"}, {"name": "openWebsite", "type": "string", "value": "https://ar-online.com/inovacao"}]})

    # Alas Laterais - Operações (4 Salas Comerciais)
    # Sala Comercial 1
    object_layer["objects"].append({"id": 18, "name": "Sala Comercial 1", "point": True, "x": (map_width * 3/4) * tile_size, "y": (map_height/4) * tile_size, "type": "area"})
    object_layer["objects"].append({"id": 19, "name": "Sales Dashboard 1", "point": True, "x": (map_width * 3/4 - 2) * tile_size, "y": (map_height/4 + 2) * tile_size, "type": "image", "properties": [{"name": "image", "type": "string", "value": "ar_online_sales_dashboard.png"}, {"name": "openWebsite", "type": "string", "value": "https://crm.ar-online.com/dashboard/sala1"}]})
    # Sala Comercial 2
    object_layer["objects"].append({"id": 20, "name": "Sala Comercial 2", "point": True, "x": (map_width * 3/4) * tile_size, "y": (map_height/4 + 8) * tile_size, "type": "area"})
    object_layer["objects"].append({"id": 21, "name": "Sales Dashboard 2", "point": True, "x": (map_width * 3/4 - 2) * tile_size, "y": (map_height/4 + 10) * tile_size, "type": "image", "properties": [{"name": "image", "type": "string", "value": "ar_online_sales_dashboard.png"}, {"name": "openWebsite", "type": "string", "value": "https://crm.ar-online.com/dashboard/sala2"}]})
    # Sala Comercial 3
    object_layer["objects"].append({"id": 22, "name": "Sala Comercial 3", "point": True, "x": (map_width * 3/4) * tile_size, "y": (map_height/4 + 16) * tile_size, "type": "area"})
    object_layer["objects"].append({"id": 23, "name": "Sales Dashboard 3", "point": True, "x": (map_width * 3/4 - 2) * tile_size, "y": (map_height/4 + 18) * tile_size, "type": "image", "properties": [{"name": "image", "type": "string", "value": "ar_online_sales_dashboard.png"}, {"name": "openWebsite", "type": "string", "value": "https://crm.ar-online.com/dashboard/sala3"}]})
    # Sala Comercial 4
    object_layer["objects"].append({"id": 24, "name": "Sala Comercial 4", "point": True, "x": (map_width * 3/4) * tile_size, "y": (map_height/4 + 24) * tile_size, "type": "area"})
    object_layer["objects"].append({"id": 25, "name": "Sales Dashboard 4", "point": True, "x": (map_width * 3/4 - 2) * tile_size, "y": (map_height/4 + 26) * tile_size, "type": "image", "properties": [{"name": "image", "type": "string", "value": "ar_online_sales_dashboard.png"}, {"name": "openWebsite", "type": "string", "value": "https://crm.ar-online.com/dashboard/sala4"}]})

    object_layer["objects"].append({"id": 6, "name": "Sala Marketing", "point": True, "x": (map_width * 3/4) * tile_size, "y": (map_height/4 - 8) * tile_size, "type": "area"})
    object_layer["objects"].append({"id": 7, "name": "Marketing Board", "point": True, "x": (map_width * 3/4 - 2) * tile_size, "y": (map_height/4 - 6) * tile_size, "type": "image", "properties": [{"name": "image", "type": "string", "value": "ar_online_marketing_board.png"}, {"name": "openWebsite", "type": "string", "value": "https://marketing.ar-online.com/dashboard"}]})
    object_layer["objects"].append({"id": 13, "name": "Dev Monitors", "point": True, "x": (map_width * 3/4 - 5) * tile_size, "y": (map_height/4 + 32) * tile_size, "type": "image", "properties": [{"name": "image", "type": "string", "value": "ar_online_dev_monitors.png"}, {"name": "openWebsite", "type": "string", "value": "https://github.com/ar-online-dev"}]})
    object_layer["objects"].append({"id": 14, "name": "Support Dashboard", "point": True, "x": (map_width * 3/4 - 5) * tile_size, "y": (map_height/4 + 35) * tile_size, "type": "image", "properties": [{"name": "image", "type": "string", "value": "ar_online_support_dashboard.png"}, {"name": "openWebsite", "type": "string", "value": "https://support.ar-online.com/dashboard"}]})

    # Área de Convivência e Eventos
    object_layer["objects"].append({"id": 8, "name": "Jardim Virtual", "point": True, "x": map_width/2 * tile_size, "y": (map_height/4 - 10) * tile_size, "type": "image", "properties": [{"name": "image", "type": "string", "value": "ar_online_virtual_garden.png"}, {"name": "openWebsite", "type": "string", "value": "https://ar-online.com/sustentabilidade"}]})
    object_layer["objects"].append({"id": 15, "name": "Auditorio", "point": True, "x": (map_width/2 - 10) * tile_size, "y": (map_height/4 - 15) * tile_size, "type": "area"})
    object_layer["objects"].append({"id": 16, "name": "Lounge Sofa", "point": True, "x": (map_width/2 + 10) * tile_size, "y": (map_height/4 - 15) * tile_size, "type": "image", "properties": [{"name": "image", "type": "string", "value": "WA_Seats.png"}, {"name": "openWebsite", "type": "string", "value": "https://ar-online.com/playlist-lounge"}]})

    tiled_map["layers"].append(object_layer)

    # Camada de Colisão (exemplo)
    collision_data = [0] * (map_width * map_height) # 0 = sem colisão, 1 = colisão
    # Adicionar algumas colisões de exemplo (paredes ao redor do lobby)
    for i in range(map_width):
        collision_data[i] = 1 # Top wall
        collision_data[(map_height - 1) * map_width + i] = 1 # Bottom wall
    for i in range(map_height):
        collision_data[i * map_width] = 1 # Left wall
        collision_data[i * map_width + (map_width - 1)] = 1 # Right wall

    tiled_map["layers"].append({
        "data": collision_data,
        "height": map_height,
        "id": 3,
        "name": "Collisions",
        "opacity": 1,
        "type": "tilelayer",
        "visible": False, # Camada de colisão geralmente invisível
        "width": map_width,
        "x": 0,
        "y": 0
    })

    # Camada de Zonas Privadas (exemplo)
    private_zone_layer = {
        "draworder": "topdown",
        "id": 4,
        "name": "PrivateZones",
        "objects": [],
        "opacity": 1,
        "type": "objectgroup",
        "visible": True,
        "x": 0,
        "y": 0
    }
    # Exemplo de zona privada na sala do CEO
    private_zone_layer["objects"].append({"id": 9, "name": "CEO_Private_Zone", "rectangle": True, "x": (map_width/4 - 3) * tile_size, "y": (map_height/4 - 3) * tile_size, "width": 6 * tile_size, "height": 6 * tile_size, "type": "zone", "properties": [{"name": "private", "type": "bool", "value": True}]})
    # Zonas privadas para as 4 salas comerciais
    private_zone_layer["objects"].append({"id": 26, "name": "Comercial_Zone_1", "rectangle": True, "x": (map_width * 3/4 - 4) * tile_size, "y": (map_height/4 - 2) * tile_size, "width": 8 * tile_size, "height": 6 * tile_size, "type": "zone", "properties": [{"name": "private", "type": "bool", "value": True}]})
    private_zone_layer["objects"].append({"id": 27, "name": "Comercial_Zone_2", "rectangle": True, "x": (map_width * 3/4 - 4) * tile_size, "y": (map_height/4 + 6) * tile_size, "width": 8 * tile_size, "height": 6 * tile_size, "type": "zone", "properties": [{"name": "private", "type": "bool", "value": True}]})
    private_zone_layer["objects"].append({"id": 28, "name": "Comercial_Zone_3", "rectangle": True, "x": (map_width * 3/4 - 4) * tile_size, "y": (map_height/4 + 14) * tile_size, "width": 8 * tile_size, "height": 6 * tile_size, "type": "zone", "properties": [{"name": "private", "type": "bool", "value": True}]})
    private_zone_layer["objects"].append({"id": 29, "name": "Comercial_Zone_4", "rectangle": True, "x": (map_width * 3/4 - 4) * tile_size, "y": (map_height/4 + 22) * tile_size, "width": 8 * tile_size, "height": 6 * tile_size, "type": "zone", "properties": [{"name": "private", "type": "bool", "value": True}]})

    tiled_map["layers"].append(private_zone_layer)

    # Camada de Teleportes (exemplo)
    teleport_layer = {
        "draworder": "topdown",
        "id": 5,
        "name": "Teleports",
        "objects": [],
        "opacity": 1,
        "type": "objectgroup",
        "visible": True,
        "x": 0,
        "y": 0
    }
    # Exemplo de teleporte do lobby para o auditório
    teleport_layer["objects"].append({"id": 17, "name": "LobbyToAuditorio", "rectangle": True, "x": (map_width/2 - 1) * tile_size, "y": (map_height/2 - 10) * tile_size, "width": 2 * tile_size, "height": 2 * tile_size, "type": "teleport", "properties": [{"name": "teleportToMap", "type": "string", "value": "nome_do_mapa_auditorio.json"}, {"name": "teleportToX", "type": "int", "value": 10}, {"name": "teleportToY", "type": "int", "value": 20}]})
    tiled_map["layers"].append(teleport_layer)

    with open("work_adventure_map_v2.json", "w") as f:
        json.dump(tiled_map, f, indent=4)

if __name__ == "__main__":
    generate_tiled_map_json()


