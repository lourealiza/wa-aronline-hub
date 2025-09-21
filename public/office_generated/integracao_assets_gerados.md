# Integração dos Assets Gerados (Tileset e Imagem de Fundo)

Para que o mapa `work_adventure_map_from_image.json` seja exibido corretamente no Work Adventure, você precisará integrar os arquivos de tileset e a imagem de fundo que foram gerados.

## 1. Arquivos Gerados

Você recebeu os seguintes arquivos:

*   `space_background.png`: A imagem de fundo espacial.
*   `tileset_colors_walls.png`: A imagem que contém todos os tiles de piso e parede.
*   `tileset_colors_walls.json`: O arquivo de definição do tileset que referencia `tileset_colors_walls.png`.

## 2. Estrutura de Diretórios no seu Projeto Work Adventure

É crucial que esses arquivos estejam nos locais corretos dentro do seu projeto Work Adventure. Uma estrutura comum seria:

```
seu-projeto-workadventure/
├── maps/
│   └── work_adventure_map_from_image.json
├── assets/
│   ├── tiles/
│   │   ├── tileset_colors_walls.png
│   │   └── tileset_colors_walls.json
│   └── backgrounds/
│       └── space_background.png
└── ... outros arquivos do projeto ...
```

**Passos:**

1.  **Mova `work_adventure_map_from_image.json`** para a pasta `maps/` do seu projeto.
2.  **Crie a pasta `assets/tiles/`** (se não existir) e **mova `tileset_colors_walls.png` e `tileset_colors_walls.json`** para lá.
3.  **Crie a pasta `assets/backgrounds/`** (se não existir) e **mova `space_background.png`** para lá.

## 3. Configurando o Tileset no `work_adventure_map_from_image.json`

O arquivo `work_adventure_map_from_image.json` já foi gerado com uma referência ao `tileset_colors_walls.json`. No entanto, você precisa garantir que o caminho (`source`) dentro do JSON do mapa esteja correto em relação à localização do seu arquivo `tileset_colors_walls.json`.

Abra `work_adventure_map_from_image.json` e localize a seção `tilesets`. Ela deve ser algo parecido com isto:

```json
"tilesets": [
    {
        "firstgid": 1,
        "source": "../assets/tiles/tileset_colors_walls.json" // Ajuste este caminho se necessário
    }
],
```

*   Se `tileset_colors_walls.json` estiver na pasta `assets/tiles/` e seu mapa em `maps/`, o caminho `"../assets/tiles/tileset_colors_walls.json"` geralmente funcionará, pois `../` sobe um nível do diretório `maps/` para o diretório raiz do projeto, e então desce para `assets/tiles/`.
*   Se você colocou o `tileset_colors_walls.json` na mesma pasta `maps/` que o mapa, o caminho seria simplesmente `"tileset_colors_walls.json"`.

## 4. Configurando a Imagem de Fundo (`space_background.png`)

O Work Adventure permite definir uma imagem de fundo para o mapa. No `work_adventure_map_from_image.json`, adicionei uma propriedade `background-image`:

```json
"properties": [
    {
        "name": "background-image",
        "type": "string",
        "value": "space_background.png" // Caminho para a imagem de fundo
    }
]
```

Você precisará ajustar o `value` para o caminho correto da sua imagem `space_background.png` em relação ao arquivo JSON do mapa. Por exemplo, se `space_background.png` estiver em `assets/backgrounds/` e seu mapa em `maps/`, o caminho seria `"../assets/backgrounds/space_background.png"`.

## 5. Visualizando no Tiled Editor

Para verificar se o tileset e a imagem de fundo estão configurados corretamente, você pode abrir o `work_adventure_map_from_image.json` no Tiled Editor:

1.  Abra o Tiled Editor.
2.  Vá em `File > Open...` e selecione `work_adventure_map_from_image.json`.
3.  O Tiled Editor deve carregar o mapa, exibir os tiles de piso e parede usando `tileset_colors_walls.png` e, se configurado corretamente, mostrar a imagem de fundo espacial.

## 6. Testando no Work Adventure

Após configurar os caminhos e verificar no Tiled Editor, inicie seu servidor Work Adventure e carregue o mapa. Você deverá ver o mapa com o layout da imagem, os pisos coloridos, as paredes e o fundo espacial. Lembre-se que este mapa é uma base e precisará de mais detalhes e objetos para se assemelhar completamente à imagem original.

