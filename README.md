# wa-aronline-hub: Hub Interativo da AR Online no Work Adventure

Este repositório contém os arquivos necessários para configurar e personalizar o hub interativo da AR Online no Work Adventure. Aqui você encontrará o mapa base, assets visuais e scripts para criar uma experiência imersiva e funcional para os usuários.

## Estrutura do Repositório

```
wa-aronline-hub/
├── assets/                 # Imagens e outros assets visuais
├── maps/                   # Arquivos de mapa do Tiled (.json, .tmj)
├── scripts/                # Scripts JavaScript para interatividade
├── tilesets/               # Imagens de tilesets e objetos para o Tiled
├── README.md               # Este arquivo
└── ... (outros arquivos do projeto)
```

## Como Usar

### 1. Configuração Inicial

Certifique-se de ter o [Tiled Map Editor](https://www.mapeditor.org/) instalado para editar os arquivos de mapa.

### 2. Arquivos Gerados

Os seguintes arquivos foram gerados e são essenciais para a configuração do seu mapa:

*   `work_adventure_map.json`: O arquivo JSON do mapa Tiled, contendo a estrutura do mapa, camadas e objetos interativos.
*   `sugestoes_interativas_work_adventure.md`: Um documento detalhando as sugestões de elementos interativos que podem ser implementados no mapa.
*   `integracao_tileset_imagens.md`: Um guia explicando como integrar corretamente os tilesets e as imagens no Tiled Editor.

### 3. Integração do Mapa

1.  **Mova o arquivo `work_adventure_map.json`** para a pasta `maps/` do seu repositório. Se a pasta `maps/` não existir, crie-a.
2.  **Organize seus assets:** O arquivo `integracao_tileset_imagens.md` detalha a estrutura de pastas recomendada para seus tilesets e imagens. Certifique-se de que as imagens referenciadas no `work_adventure_map.json` (como `ar_online_lobby_logo.png`, `ar_online_telao_tecnologico.png`, etc.) estejam na pasta `tilesets/` ou em uma subpasta `assets/images/` dentro do seu repositório, conforme a estrutura que você preferir.
    *   **Ajuste os caminhos:** Abra o `work_adventure_map.json` no Tiled Editor. Para cada objeto que usa uma imagem, verifique e ajuste o caminho da propriedade `image` para que aponte corretamente para o local da imagem dentro do seu repositório (ex: `../tilesets/ar_online_lobby_logo.png` ou `../assets/images/ar_online_lobby_logo.png`).
3.  **Configure os Tilesets:** O `work_adventure_map.json` faz referência a um `tileset.json`. Você precisará criar este arquivo ou configurar os tilesets diretamente no Tiled Editor, apontando para as imagens de tilesets localizadas na pasta `tilesets/` (ex: `WA_Room_Builder.png`, `WA_Decoration.png`). Consulte `integracao_tileset_imagens.md` para instruções detalhadas.

### 4. Implementação da Interatividade

O `work_adventure_map.json` já inclui propriedades para elementos interativos como `openWebsite`, `trigger` e `script`.

*   **Links (`openWebsite`):** Para objetos com a propriedade `openWebsite`, o Work Adventure abrirá automaticamente o URL especificado quando o jogador interagir com o objeto.
*   **Scripts (`script`):** Para interações mais complexas que utilizam a propriedade `script` (ex: `displayWelcomeMessage.js`), você precisará criar os arquivos JavaScript correspondentes na pasta `scripts/` do seu repositório. Estes scripts conterão a lógica para as ações desejadas (ex: exibir uma mensagem, iniciar um diálogo, etc.).

### 5. Testando o Mapa

Após configurar o mapa e os assets no Tiled Editor, você pode testá-lo localmente ou implantá-lo no seu ambiente Work Adventure para verificar se tudo está funcionando como esperado.

## Contribuição

Sinta-se à vontade para contribuir com melhorias, novos assets ou funcionalidades para este hub. Para isso, siga os passos:

1.  Faça um fork deste repositório.
2.  Crie uma nova branch para suas alterações (`git checkout -b minha-nova-feature`).
3.  Faça suas alterações e commit-as (`git commit -am 'Adiciona nova feature'`).
4.  Envie para a branch (`git push origin minha-nova-feature`).
5.  Abra um Pull Request.

---

## Referências

- Guia: [Integração e Uso de Scripts Dinâmicos](integracao-uso-scripts-dinamicos.md)

**Gerado por Manus AI**

