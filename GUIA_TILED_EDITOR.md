# 🗺️ Guia do Tiled Map Editor - AR Online

## 📋 **Configuração Inicial**

### **1. Instalar Tiled Map Editor**

- **Download**: https://www.mapeditor.org/download.html
- **Versão**: 1.10.2 (recomendada)
- **Sistema**: Windows, Mac, Linux

### **2. Abrir Projeto**

1. Abra o Tiled Map Editor
2. Vá em **File** → **Open Project**
3. Selecione o arquivo `AR-Online.tiled-project`
4. O projeto será carregado com todos os mapas

## 🎯 **Estrutura do Projeto**

### **Arquivos Principais**

- **`wa_map-interativo.tmj`** - Mapa principal completo
- **`wa_map-teste.tmj`** - Mapa simples para testes
- **`mapScript.js`** - Script de interações

### **Tilesets**

- **`tilesets/WA_Room_Builder.png`** - Tileset principal
- **Localização**: `public/tilesets/`

## 🏗️ **Editando o Mapa**

### **Camadas Disponíveis**

#### **1. floor (Piso)**

- **Função**: Base do mapa com cores por setor
- **Cores**:
  - Azul (725): Lobby Central
  - Cinza (1): Corredores
  - Cinza Claro (2): Gestão & CEO
  - Cinza Claro (3): Operações
  - Verde (4): Convivência & Eventos

#### **2. walls (Paredes)**

- **Função**: Paredes e divisórias
- **Tile**: 100
- **Uso**: Separar salas e criar estrutura

#### **3. collision (Colisões)**

- **Função**: Bloqueios de movimento (invisível)
- **Uso**: Impedir que avatares passem por paredes

#### **4. furniture (Mobiliário)**

- **Função**: Mesas, cadeiras, equipamentos
- **Tile**: 200
- **Uso**: Decorar salas específicas

#### **5. decoration (Decoração)**

- **Função**: Plantas, quadros, elementos visuais
- **Tile**: 300
- **Uso**: Tornar o ambiente mais atrativo

### **Objetos e Zonas**

#### **1. start (Spawn)**

- **Função**: Ponto de entrada dos jogadores
- **Localização**: Centro do lobby
- **Propriedades**: `type: spawn`

#### **2. PrivateZones (Zonas Privadas)**

- **Função**: Áreas restritas por departamento
- **Exemplos**: CEO, RH, Desenvolvimento, Marketing
- **Propriedades**: `type: private`

#### **3. zones (Zonas Especiais)**

- **Função**: Áreas com interações específicas
- **Exemplos**: Café, Impressão, Arquivo, Auditório
- **Propriedades**: `type: [cafe|printing|archive|auditorium]`

## 🎨 **Dicas de Edição**

### **Adicionando Salas**

1. **Selecione a camada `floor`**
2. **Escolha a cor apropriada** (azul, cinza, verde)
3. **Desenhe a área da sala** com o pincel
4. **Adicione paredes** na camada `walls`
5. **Crie a zona** na camada `PrivateZones` ou `zones`

### **Adicionando Mobiliário**

1. **Selecione a camada `furniture`**
2. **Escolha o tile 200**
3. **Posicione mesas, cadeiras, equipamentos**
4. **Use a camada `decoration`** para plantas e quadros

### **Configurando Interações**

1. **Selecione a camada de objetos** (PrivateZones ou zones)
2. **Clique com botão direito** no objeto
3. **Vá em Properties**
4. **Adicione propriedades**:
   - `name`: Nome da sala
   - `type`: Tipo da zona
   - `script`: Script de interação

## 🔄 **Fluxo de Trabalho**

### **1. Editar no Tiled**

1. Abra o Tiled Map Editor
2. Edite o mapa `wa_map-interativo.tmj`
3. Salve as mudanças (Ctrl+S)

### **2. Sincronizar com GitHub**

1. Execute o script de sincronização:

   ```powershell
   .\sync-tiled-changes.ps1
   ```

2. Aguarde o deploy automático (2-3 minutos)
3. Teste no WorkAdventure

### **3. Testar Mudanças**

1. Acesse: https://play.workadventu.re/_/global/lourealiza.github.io/wa-aronline-hub/wa_map-interativo.tmj
2. Verifique se as mudanças apareceram
3. Teste as interações

## 🎯 **Salas e Coordenadas**

### **Departamentos (Ala Esquerda)**

- **CEO**: x=4..8, y=26..30
- **RH**: x=9..13, y=26..30
- **Projetos**: x=4..8, y=31..35
- **Processos & IA**: x=9..13, y=31..35
- **Financeiro**: x=4..8, y=36..40
- **Vendas**: x=9..13, y=36..40

### **Operações (Ala Direita)**

- **Marketing**: x=61..65, y=26..30
- **Comercial**: x=66..70, y=26..30
- **Desenvolvimento**: x=61..65, y=31..35
- **QA**: x=66..70, y=31..35
- **DevOps**: x=61..65, y=36..40
- **Suporte**: x=66..70, y=36..40

### **Convivência (Parte Superior)**

- **Auditório**: x=10..25, y=6..12
- **Jardim Virtual**: x=26..40, y=6..12
- **Lounge/Copa**: x=41..55, y=6..12
- **Treinamento**: x=56..70, y=6..12

## 🔧 **Comandos Úteis**

### **Atalhos do Tiled**

- **Ctrl+Z**: Desfazer
- **Ctrl+Y**: Refazer
- **Ctrl+S**: Salvar
- **Ctrl+A**: Selecionar tudo
- **Ctrl+C**: Copiar
- **Ctrl+V**: Colar
- **Delete**: Apagar seleção

### **Ferramentas**

- **Pincel**: Desenhar tiles
- **Eraser**: Apagar tiles
- **Seleção**: Selecionar área
- **Preenchimento**: Preencher área
- **Texto**: Adicionar texto

## 🚨 **Problemas Comuns**

### **Mapa não atualiza no WorkAdventure**

1. Verifique se salvou o arquivo (Ctrl+S)
2. Execute o script de sincronização
3. Aguarde 2-3 minutos para o deploy
4. Limpe o cache do navegador

### **Tileset não carrega**

1. Verifique se o arquivo está em `public/tilesets/`
2. Confirme o caminho no tileset
3. Reimporte o tileset no Tiled

### **Interações não funcionam**

1. Verifique se o `mapScript.js` está atualizado
2. Confirme os nomes das camadas
3. Teste localmente primeiro

## 📊 **Melhores Práticas**

### **Organização**

- Use nomes descritivos para camadas
- Mantenha objetos organizados por tipo
- Documente mudanças importantes

### **Performance**

- Evite mapas muito grandes
- Use tilesets otimizados
- Mantenha colisões simples

### **Colaboração**

- Faça commits frequentes
- Documente mudanças
- Teste antes de enviar

## 🎉 **Resultado Final**

Com o Tiled Map Editor, você pode:

- ✅ **Editar visualmente** o mapa
- ✅ **Adicionar salas** facilmente
- ✅ **Configurar interações** por área
- ✅ **Sincronizar automaticamente** com GitHub
- ✅ **Testar em tempo real** no WorkAdventure

**Agora você tem controle total sobre o mapa da AR Online!** 🚀
