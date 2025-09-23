# wa-aronline-hub: Hub Interativo da AR Online no WorkAdventure

Este repositório contém os arquivos necessários para configurar e publicar o hub interativo da AR Online no WorkAdventure. Aqui você encontra o mapa base, tilesets, página inicial e script do mapa para interações dinâmicas.

## Estrutura do Repositório

`
wa-aronline-hub/

- public/
  - images/                 # Ícones e imagens públicas
  - wa_map-interativo.tmj   # Mapa padrão (Tiled JSON - TMJ)
  - mapScript.js            # Script do mapa (map-scripting)
- tilesets/                 # Tilesets e imagens usadas pelo mapa
- src/                      # Código Vite (mínimo)
- index.html                # Homepage com links para testar/publicar
- vite.config.ts            # Configuração Vite + otimizador de mapas
- tsconfig.json             # TypeScript config
- package.json              # Scripts NPM
- README.md                 # Este arquivo
`

## Como Rodar Localmente

- Desenvolvimento:
pm run start → abre em <http://localhost:5173/>
- Preview de produção:
pm run build e
pm run prod → <http://localhost:4173/>

## Publicação (GitHub Pages)

O projeto está configurado para deploy automático no GitHub Pages:

- **Página principal**: <https://lourealiza.github.io/wa-aronline-hub/>
- **Mapa direto**: <https://lourealiza.github.io/wa-aronline-hub/wa_map-interativo.tmj>
- **WorkAdventure (global)**: <https://play.workadventu.re/_/global/lourealiza.github.io/wa-aronline-hub/wa_map-interativo.tmj>

### Deploy Automático

- Push para branch `master` → Deploy automático via GitHub Actions
- Build otimizado com Vite
- Arquivos estáticos servidos diretamente

## Mapa Padrão e Scripts Dinâmicos

- O mapa padrão é public/wa_map-interativo.tmj.
- O script do mapa está em public/mapScript.js e é referenciado pela propriedade raiz script dentro do TMJ.
- Guia detalhado: [Integração e Uso de Scripts Dinâmicos](integracao-uso-scripts-dinamicos.md)

## Otimização de Mapas (build)

O projeto usa wa-map-optimizer-vite durante o build:

- Otimiza tilesets e gera versões empacotadas dos mapas para o diretório dist/.
- Para que a otimização funcione, o TMJ deve referenciar corretamente o tileset (ex.: ../tilesets/WA_Room_Builder.png).

## Contribuição

Contribuições são bem-vindas! Passos sugeridos:

- Fork do repositório
- Nova branch: git checkout -b minha-nova-feature
- Commits claros e objetivos
- Pull Request explicando a motivação e o escopo

---
